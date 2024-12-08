from src.bot import utils
from src.bot.objects import TGObject
from src.user_bots.conversation import templates as tmp
from src.api import openai_api as api
import src.settings as stg


class ConversationService(TGObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def handle_message(self):
        user = self.users_repo.find_user(self.user_id)
        if user.root:
            return
        elif not user.lead:
            self.users_repo.add_lead(self.user_id)
            self.users_repo.update_user(self.user_id, state='new_user')

        state_functions = {
            'new_user': self.handle_new_user,
            'language_request': self.handle_language_request,
            'service_request': self.handle_service_request,

            # Rent equipment
            'rent_equipment_info_request': self.handle_rent_equipment_info_request,
            # Hire instructor
            'hire_instructor_info_request': self.handle_hire_instructor_info_request,
            'hire_instructor_personal_info_request': self.hire_instructor_personal_info_request,
            'hire_instructor_confirmation_request': self.hire_instructor_confirmation_request,
            # Food & Coffee
            'food_order_info_request': self.handle_food_order_info_request,
            'food_order_confirmation_request': self.handle_food_order_confirmation_request,
            # Massage
            'massage_date_info_request': self.handle_massage_date_info_request,
            'massage_type_info_request': self.handle_massage_type_info_request,
            'massage_booking_confirmation_request': self.handle_massage_booking_confirmation_request,
        }

        if user.state in state_functions:
            await self.event.client.send_read_acknowledge(self.user_id, self.event.message)
            return await state_functions[user.state]()

    async def handle_new_user(self):
        self.users_repo.update_user(self.user_id, state='language_request')

        text = tmp.select_language_text()
        await self.respond(text)

    async def handle_language_request(self):
        response = api.determine_language(self.text)
        lang = response["language"]

        if lang != "undefined":
            self.users_repo.update_lead(self.user_id, lang=lang)
            return await self.all_services_menu()
        else:
            text = tmp.select_language_error()
            return await self.respond(text)

    async def all_services_menu(self):
        self.users_repo.update_user(self.user_id, state='service_request', state_data=None)
        user = self.users_repo.find_user(self.user_id)
        text = tmp.all_services_text(user.lead.lang)
        return await self.respond(text)

    async def handle_service_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.determine_service(self.text)
        service = response["service"]

        service_handlers = {
            'rent_equipment': self.handle_rent_equipment_service,
            'instructor': self.handle_instructor_service,
            'food_coffee': self.handle_food_coffee_service,
            'massage': self.handle_massage_service,
        }

        if service not in service_handlers:
            text = tmp.service_unavailable_error(user.lead.lang)
            return await self.respond(text)

        return await service_handlers[service]()

    async def handle_rent_equipment_service(self):
        self.users_repo.update_user(
            self.user_id,
            state='rent_equipment_info_request',
            state_data={'user_answers': []}
        )

        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        file_path = utils.get_path_to_asset('new_gudauri_map.png')
        first_text = tmp.rent_equipment_info_text(lang)
        await self.respond(first_text, file=file_path)

        second_text = tmp.rent_equipment_questions_text(lang)
        await self.respond(second_text)

    async def handle_rent_equipment_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.extract_rental_equipment_details(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        check_answer_response = api.analyze_answer_yes_no(self.text)
        answer = check_answer_response['answer']
        if answer and answer != 'None' and user.state_data['user_answers']:
            return await self.rent_equipment_confirmation_request()

        rental_equipment = response['rental_equipment']
        if rental_equipment == 'None':
            return await self.respond(tmp.rent_equipment_error(lang))

        user.state_data['user_answers'].append(rental_equipment)
        self.users_repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        text = tmp.rent_equipment_confirmation_text(lang, user.state_data['user_answers'])
        return await self.respond(text)

    async def rent_equipment_confirmation_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if answer:
            user_answers = user.state_data['user_answers']
            first_text = tmp.new_equipment_booking_text(user, user_answers)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            second_text = tmp.equipment_booking_confirmed_text(user.lead.lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_rent_equipment_service()

    async def handle_instructor_service(self):
        self.users_repo.update_user(
            self.user_id,
            state='hire_instructor_info_request',
            state_data={'dates': 'None', 'time': 'None', 'equipment': 'None', 'participants': 'None', 'age': 'None'}
        )

        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        first_text = tmp.hire_instructor_info_text(lang)
        await self.respond(first_text)

        second_text = tmp.hire_instructor_questions_text(lang)
        await self.respond(second_text)

    async def handle_hire_instructor_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        details = api.extract_mentor_booking_details(self.text)

        if details.get('is_request_canceled', False):
            return await self.all_services_menu()

        details.pop("is_request_canceled", None)

        for key, value in details.items():
            if value != 'None' and value:
                user.state_data[key] = details[key]

        self.users_repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            text = tmp.instructor_booking_error(lang, user.state_data)
            return await self.respond(text)

        user.state_data.update({'name': 'None', 'phone_number': 'None', 'place': 'None'})
        self.users_repo.update_user(self.user_id, state_data=user.state_data, state='hire_instructor_personal_info_request')

        first_text = tmp.tracks_info_text(lang)
        file_path = utils.get_path_to_asset('tracks.png')
        await self.respond(first_text, file=file_path)

        second_text = tmp.instructor_booking_user_data_request_text(lang)
        return await self.respond(second_text)

    async def hire_instructor_personal_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        personal_info = api.extract_user_details(self.text)

        if personal_info.get('is_request_canceled', False):
            return await self.handle_instructor_service()

        personal_info.pop("is_request_canceled", None)

        for key, value in personal_info.items():
            if value != 'None' and value:
                user.state_data[key] = personal_info[key]

        self.users_repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        dates = user.state_data.get('dates')
        time = user.state_data.get('time')
        equipment = user.state_data.get('equipment')
        participants = user.state_data.get('participants')
        age = user.state_data.get('age')
        name = user.state_data.get('name')
        phone_number = user.state_data.get('phone_number')
        place = user.state_data.get('place')

        if 'None' in user.state_data.values():
            text = tmp.instructor_booking_user_data_request_error(user.lead.lang, user.state_data)
            return await self.respond(text)

        self.users_repo.update_user(self.user_id, state='hire_instructor_confirmation_request')

        text = tmp.instructor_booking_confirmation_text(user.lead.lang, dates, time, equipment, participants, age, name, phone_number, place)
        return await self.respond(text)

    async def hire_instructor_confirmation_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_instructor_service()

        if answer:
            dates = user.state_data.get('dates')
            time = user.state_data.get('time')
            equipment = user.state_data.get('equipment')
            participants = user.state_data.get('participants')
            age = user.state_data.get('age')
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')
            place = user.state_data.get('place')
            first_text = tmp.new_instructor_booking_text(user, dates, time, equipment, participants, age, name, phone_number, place)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            second_text = tmp.instructor_booking_confirmed_text(user.lead.lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_rent_equipment_service()

    async def handle_food_coffee_service(self):
        self.users_repo.update_user(
            self.user_id,
            state='food_order_info_request'
        )

        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.food_order_info_text(lang)
        await self.respond(text)

    async def handle_food_order_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang

        order_details = api.extract_food_order_details(self.text)
        selected_items = order_details.get('selected_items')

        if order_details.get('is_request_canceled'):
            return await self.all_services_menu()

        if not selected_items:
            return await self.respond(tmp.no_food_selected_error(lang))

        self.users_repo.update_user(
            self.user_id,
            state_data=order_details
        )

        text = tmp.food_order_text(lang, selected_items)
        self.users_repo.update_user(self.user_id, state='food_order_confirmation_request')
        return await self.respond(text)

    async def handle_food_order_confirmation_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_food_coffee_service()

        if answer:
            selected_items = user.state_data.get('selected_items')
            total_price = tmp.calculate_total_price(selected_items)
            food_order = self.users_repo.add_food_order(selected_items, total_price)

            first_text = tmp.new_food_order_text(user, selected_items)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            file_path = utils.get_path_to_asset('new_gudauri_map.png')
            second_text = tmp.food_order_confirmed_text(user.lead.lang, food_order.id)
            await self.respond(second_text, file=file_path)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_rent_equipment_service()

    async def handle_massage_service(self):
        self.users_repo.update_user(
            self.user_id,
            state='massage_type_info_request',
            state_data=None,
        )

        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.massage_service_info_text(lang)
        await self.respond(text)

    async def handle_massage_type_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.extract_massage_details(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.massage_booking_error(lang))

        user.state_data = response
        self.users_repo.update_user(
            self.user_id,
            state='massage_date_info_request',
            state_data=user.state_data
        )

        text = tmp.massage_type_request_text(lang)
        return await self.respond(text)

    async def handle_massage_date_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.extract_booking_details_for_massage(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.handle_massage_service()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.massage_booking_error(lang))

        user.state_data.update(response)
        self.users_repo.update_user(
            self.user_id,
            state='massage_booking_confirmation_request',
            state_data=user.state_data
        )

        dates = user.state_data.get('dates')
        time = user.state_data.get('time')
        massage_type = user.state_data.get('massage_type')
        duration = user.state_data.get('duration')

        text = tmp.massage_booking_confirmation_request_text(lang, dates, time, massage_type, duration)
        return await self.respond(text)

    async def handle_massage_booking_confirmation_request(self):
        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_massage_service()

        if answer:
            dates = user.state_data.get('dates')
            time = user.state_data.get('time')
            massage_type = user.state_data.get('massage_type')
            duration = user.state_data.get('duration')

            first_text = tmp.massage_booking_text(user, dates, time, massage_type, duration)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            file_path = utils.get_path_to_asset('new_gudauri_map.png')
            second_text = tmp.massage_booking_confirmed_text(lang)
            await self.respond(second_text, file=file_path)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_massage_service()
