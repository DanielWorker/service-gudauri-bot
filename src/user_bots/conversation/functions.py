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
            'hire_instructor_confirmation_request': self.hire_instructor_confirmation_request,
            # Food & Coffee
            'food_order_info_request': self.handle_food_order_info_request,
            'food_order_confirmation_request': self.handle_food_order_confirmation_request,
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
        first_text = tmp.rent_equipment_info_text(lang)
        await self.respond(first_text)

        second_text = tmp.rent_equipment_questions_text(lang)
        await self.respond(second_text)

    async def handle_rent_equipment_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.extract_rental_equipment_details(self.text)
        lang = user.lead.lang

        if response['is_request_canceled']:
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
            state_data={'date_time': 'None', 'lesson_preference': 'None', 'equipment': 'None'}
        )

        user = self.users_repo.find_user(self.user_id)
        lang = user.lead.lang
        first_text = tmp.hire_instructor_info_text(lang)
        await self.respond(first_text)

        second_text = tmp.hire_instructor_questions_text(lang)
        await self.respond(second_text)

    async def handle_hire_instructor_info_request(self):
        user = self.users_repo.find_user(self.user_id)
        details = api.extract_mentor_booking_details(self.text)

        # if details['is_request_canceled']:  fixme
        #     return await self.all_services_menu()

        for key, value in details.items():
            if value != 'None' and value:
                user.state_data[key] = details[key]

        self.users_repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            return

        self.users_repo.update_user(self.user_id, state='hire_instructor_confirmation_request')

        date_time = user.state_data.get('date_time')
        lesson_preference = user.state_data.get('lesson_preference')
        equipment = user.state_data.get('equipment')
        text = tmp.instructor_booking_confirmation_text(user.lead.lang, date_time, lesson_preference, equipment)
        return await self.respond(text)

    async def hire_instructor_confirmation_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response['is_request_canceled']:
            return await self.handle_instructor_service()

        if answer:
            date_time = user.state_data.get('date_time')
            lesson_preference = user.state_data.get('lesson_preference')
            equipment = user.state_data.get('equipment')
            first_text = tmp.new_instructor_booking_text(user, date_time, lesson_preference, equipment)
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
        total_price = order_details.get('total_price')
        selected_items = order_details.get('selected_items')

        if order_details.get('is_request_canceled'):
            return await self.all_services_menu()

        if not selected_items:
            return await self.respond(tmp.no_food_selected_error(lang))

        self.users_repo.update_user(
            self.user_id,
            state_data=order_details
        )

        text = tmp.food_order_text(lang, selected_items, total_price)
        self.users_repo.update_user(self.user_id, state='food_order_confirmation_request')
        return await self.respond(text)

    async def handle_food_order_confirmation_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response['is_request_canceled']:
            return await self.handle_food_coffee_service()

        if answer:
            selected_items = user.state_data.get('selected_items')
            total_price = user.state_data.get('total_price')
            food_order = self.users_repo.add_food_order(selected_items, total_price)

            first_text = tmp.new_food_order_text(user, selected_items, total_price)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            second_text = tmp.food_order_confirmed_text(user.lead.lang, food_order.id)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_rent_equipment_service()
