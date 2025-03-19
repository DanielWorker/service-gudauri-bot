from datetime import timedelta

from src import utils
from src.bot.objects import TGObject
from src.user_bots.conversation import templates as tmp
from src.api import openai_api as api
import src.settings as stg


class ConversationService(TGObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def handle_message(self):
        user = self.repo.find_user(self.user_id)
        if user.root:
            return
        if not user.lead:
            self.repo.add_lead(self.user_id)
            self.repo.update_user(self.user_id, state='new_user')
        elif not user.state and user.lead.lang:
            self.repo.update_user(self.user_id, state='service_request')
            return await self.all_services_menu()
        elif not user.state and not user.lead.lang:
            self.repo.update_user(self.user_id, state='new_user')

        state_functions = {
            'new_user': self.handle_new_user,
            'language_request': self.handle_language_request,
            'service_request': self.handle_service_request,

            # Rent equipment
            'rent_equipment_info_request': self.handle_rent_equipment_info_request,
            # Hire instructor
            'hire_instructor_info_request': self.handle_hire_instructor_info_request,
            'hire_instructor_personal_info_request': self.hire_instructor_personal_info_request,
            # Food & Coffee
            'food_order_info_request': self.handle_food_order_info_request,
            'food_order_delivery_details_request': self.handle_food_order_delivery_details_request,
            'food_order_confirmation_request': self.handle_food_order_confirmation_request,
            # Massage
            'massage_date_info_request': self.handle_massage_date_info_request,
            'massage_type_info_request': self.handle_massage_type_info_request,
            # Paragliding
            'paragliding_plan_info_request': self.handle_paragliding_plan_info_request,
            'paragliding_booking_info_request': self.handle_paragliding_booking_info_request,
            'paragliding_booking_confirmation_request': self.handle_paragliding_booking_confirmation_request,
            # Snowbike
            'snowbike_tour_info_request': self.handle_snowbike_tour_info_request,
            'snowbike_booking_info_request': self.handle_snowbike_booking_info_request,
            'snowbike_booking_confirmation_request': self.handle_snowbike_booking_confirmation_request,
            # Exchange
            'exchange_info_request': self.handle_exchange_info_request,
            'exchange_booking_confirmation_request': self.handle_exchange_booking_confirmation_request,
            # Ski Service
            'ski_service_info_request': self.handle_ski_service_info_request,
            'ski_booking_info_request': self.handle_ski_booking_info_request,
            'ski_booking_confirmation_request': self.handle_ski_booking_confirmation_request,
            # Cleaning
            'cleaning_info_request': self.handle_cleaning_info_request,
            'cleaning_booking_info_request': self.handle_cleaning_booking_info_request,
            'cleaning_booking_confirmation_request': self.handle_cleaning_booking_confirmation_request,
            # Rent Flat
            'rent_flat_info_request': self.handle_rent_flat_info_request,
            'rent_flat_booking_confirmation_request': self.handle_rent_flat_booking_confirmation_request,
            # Transfer
            'transfer_info_request': self.handle_transfer_info_request,
        }

        if user.state in state_functions:
            await self.event.client.send_read_acknowledge(self.user_id, self.event.message)
            return await state_functions[user.state]()

    async def handle_new_user(self):
        detected_language = api.detect_input_language(self.text)
        if detected_language == 'undefined':
            self.repo.update_user(self.user_id, state='language_request')

            text = tmp.select_language_text()
            await self.respond(text)
        else:
            self.repo.update_lead(self.user_id, lang=detected_language)
            return await self.all_services_menu()

    async def handle_language_request(self):
        response = api.get_selected_language(self.text)
        lang = response["language"]

        if lang != "undefined":
            self.repo.update_lead(self.user_id, lang=lang)
            return await self.all_services_menu()
        else:
            text = tmp.select_language_error()
            return await self.respond(text)

    async def all_services_menu(self):
        self.repo.update_user(self.user_id, state='service_request', state_data=None)
        lead = self.repo.find_lead(user_id=self.user_id)
        text = tmp.all_services_text(lead.lang)
        return await self.respond(text)

    async def handle_service_request(self):
        user = self.repo.find_user(self.user_id)

        service_shortcuts = {
            '1': self.handle_rent_equipment_service,
            '2': self.handle_instructor_service,
            '3': self.handle_food_coffee_service,
            '4': self.handle_massage_service,
            '5': self.handle_transfer_service,
            '6': self.handle_paragliding_service,
            '7': self.handle_snowbike_service,
            '8': self.handle_exchange_service,
            '9': self.handle_ski_service,
            '11': self.handle_cleaning_service,
            '12': self.handle_rent_flat_service,
        }

        if self.text in service_shortcuts:
            return await service_shortcuts[self.text]()

        response = api.determine_service(self.text)
        service = response["service"]

        service_handlers = {
            'rent_equipment': self.handle_rent_equipment_service,
            'instructor': self.handle_instructor_service,
            'food_coffee': self.handle_food_coffee_service,
            'massage': self.handle_massage_service,
            'transfer': self.handle_transfer_service,
            'paragliding': self.handle_paragliding_service,
            'snowbike_tour': self.handle_snowbike_service,
            'exchange': self.handle_exchange_service,
            'ski_service': self.handle_ski_service,
            'cleaning': self.handle_cleaning_service,
            'rent_flat': self.handle_rent_flat_service,
        }

        if service not in service_handlers:
            text = tmp.service_unavailable_error(user.lead.lang)
            return await self.respond(text)

        return await service_handlers[service]()

    async def handle_rent_equipment_service(self):
        self.repo.update_user(
            self.user_id,
            state='rent_equipment_info_request',
            state_data={'rental_period': 'None', 'selected_items': []}
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        file_path = utils.get_path_to_asset('new_gudauri_map.png')
        first_text = tmp.rent_equipment_info_text(lang)
        await self.respond(first_text, file=file_path)

        second_text = tmp.rent_equipment_questions_text(lang)
        await self.respond(second_text)

    async def handle_rent_equipment_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_rental_equipment_details(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)
        selected_items = response.get("selected_items")
        rental_period = response.get("rental_period")

        check_answer_response = api.analyze_answer_yes_no(self.text)
        answer = check_answer_response['answer']
        if answer and answer != 'None' and user.state_data['selected_items'] and user.state_data['rental_period'] != 'None':
            return await self.rent_equipment_confirmation_request()

        # Проверка выбран ли товар
        elif not selected_items and not user.state_data['selected_items']:
            return await self.respond(tmp.no_food_selected_error(lang))

        # Проверка наличия недоступных товаров
        elif tmp.has_invalid_items(selected_items, tmp.equipment_dict):
            return await self.respond(tmp.food_order_invalid_error(lang))

        elif selected_items:
            user.state_data['selected_items'].extend(selected_items)

        if rental_period != 'None':
            user.state_data['rental_period'] = rental_period

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        text = tmp.rent_equipment_confirmation_text(lang, user.state_data['selected_items'], user.state_data['rental_period'])
        return await self.respond(text)

    async def rent_equipment_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if answer:
            selected_items = user.state_data['selected_items']
            rental_period = user.state_data['rental_period']
            first_text = tmp.new_equipment_booking_text(user, selected_items, rental_period)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            file_path = utils.get_path_to_asset('parking.mp4')
            second_text = tmp.equipment_booking_confirmed_text(user.lead.lang)
            await self.respond(second_text, file=file_path)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_rent_equipment_service()

    async def handle_instructor_service(self):
        self.repo.update_user(
            self.user_id,
            state='hire_instructor_info_request',
            state_data={'dates': 'None', 'time': 'None', 'equipment': 'None', 'participants_count': 'None', 'participants_type': 'None', 'age': 'None'}
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        first_text = tmp.hire_instructor_info_text(lang)
        await self.respond(first_text)

        second_text = tmp.hire_instructor_questions_text(lang)
        await self.respond(second_text)

    async def handle_hire_instructor_info_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        details = api.extract_mentor_booking_details(self.text)

        if details.get('is_request_canceled', False):
            return await self.all_services_menu()

        details.pop("is_request_canceled", None)

        for key, value in details.items():
            if value != 'None' and value:
                user.state_data[key] = details[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            text = tmp.instructor_booking_error(lang, user.state_data)
            return await self.respond(text)

        user.state_data.update({'name': 'None', 'phone_number': 'None', 'place': 'None'})
        self.repo.update_user(self.user_id, state_data=user.state_data, state='hire_instructor_personal_info_request')

        first_text = tmp.tracks_info_text(lang)
        file_path = utils.get_path_to_asset('tracks.png')
        await self.respond(first_text, file=file_path)

        second_text = tmp.instructor_booking_user_data_request_text(lang)
        return await self.respond(second_text)

    async def hire_instructor_personal_info_request(self):
        user = self.repo.find_user(self.user_id)
        personal_info = api.extract_user_details(self.text)

        if personal_info.get('is_request_canceled', False):
            return await self.handle_instructor_service()

        personal_info.pop("is_request_canceled", None)

        for key, value in personal_info.items():
            if value != 'None' and value:
                user.state_data[key] = personal_info[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        dates = user.state_data.get('dates')
        time = user.state_data.get('time')
        equipment = user.state_data.get('equipment')
        participants_count = user.state_data.get('participants_count')
        participants_type = user.state_data.get('participants_type')
        age = user.state_data.get('age')
        name = user.state_data.get('name')
        phone_number = user.state_data.get('phone_number')
        place = user.state_data.get('place')

        if 'None' in user.state_data.values():
            text = tmp.instructor_booking_user_data_request_error(user.lead.lang, user.state_data)
            return await self.respond(text)

        first_text = tmp.new_instructor_booking_text(user, dates, time, equipment, participants_count, participants_type, age, name, phone_number, place)
        await stg.bot.send_message(stg.notification_box_chat_id, first_text)

        second_text = tmp.instructor_booking_confirmed_text(user.lead.lang)
        await self.respond(second_text)

        return await self.all_services_menu()

    async def handle_food_coffee_service(self):
        self.repo.update_user(
            self.user_id,
            state='food_order_info_request',
            state_data={"selected_items": [], 'order_type': 'delivery', 'house_name': 'None', 'apartment': 'None', 'phone_number': 'None'}
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.food_order_info_text(lang)
        await self.respond(text)

    async def handle_food_order_info_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang

        order_details = api.extract_food_order_details(self.text)
        selected_items = order_details.get('selected_items')

        # Отмена заказа
        if order_details.get('is_request_canceled'):
            return await self.all_services_menu()

        order_details.pop("is_request_canceled", None)

        # Подтверждение заказа
        check_answer_response = api.analyze_answer_yes_no(self.text)
        answer = check_answer_response['answer']
        if answer and answer != 'None' and user.state_data['selected_items']:
            return await self.check_food_order_details()

        # Выбор типа заказа
        # order_type = api.detect_delivery_or_pickup(self.text)
        # if order_type != 'None':
        #     user.state_data['order_type'] = order_type

        # Проверка выбран ли товар
        elif not selected_items and not user.state_data['selected_items']:
            return await self.respond(tmp.no_food_selected_error(lang))

        # Проверка наличия недоступных товаров
        elif tmp.has_invalid_items(selected_items, tmp.food_coffee_dict):
            return await self.respond(tmp.food_order_invalid_error(lang))

        else:
            user.state_data['selected_items'].extend(selected_items)

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        return await self.send_food_order_message()

    async def send_food_order_message(self):
        self.repo.update_user(self.user_id, state='food_order_info_request')
        user = self.repo.find_user(self.user_id)
        text = tmp.food_order_text(user.lead.lang, user.state_data['selected_items'], user.state_data['order_type'])
        return await self.respond(text)

    async def check_food_order_details(self):
        user = self.repo.find_user(self.user_id)
        order_type = user.state_data['order_type']

        if order_type == 'delivery':
            text = tmp.food_order_delivery_details_text(user.lead.lang)
            await self.respond(text)
            self.repo.update_user(self.user_id, state='food_order_delivery_details_request')

        else:
            return await self.handle_food_order_confirmation_request()

    async def handle_food_order_delivery_details_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        details = api.extract_user_details_for_food_order(self.text)

        if details.get('is_request_canceled', False):
            return await self.send_food_order_message()

        details.pop("is_request_canceled", None)

        for key, value in details.items():
            if value != 'None' and value:
                user.state_data[key] = details[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            text = tmp.food_order_delivery_details_request_error(lang, user.state_data)
            return await self.respond(text)

        self.repo.update_user(self.user_id, state='food_order_confirmation_request')
        text = tmp.food_order_delivery_details_confirmation_text(user.lead.lang, user.state_data)
        await self.respond(text)

    async def handle_food_order_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if answer:
            selected_items = user.state_data.get('selected_items')
            order_type = user.state_data.get('order_type')
            total_price = tmp.calculate_total_price(selected_items)
            food_order = self.repo.add_food_order(selected_items, order_type, total_price)

            if order_type == 'delivery':
                delivery_details = {**user.state_data}
            else:
                delivery_details = None

            first_text = tmp.new_food_order_text(user, selected_items, order_type, delivery_details)
            await stg.bot.send_message(stg.food_orders_chat_id, first_text)

            file_path = utils.get_path_to_asset('new_gudauri_map.png')
            second_text = tmp.food_order_confirmed_text(user.lead.lang, food_order.id, order_type)
            await self.respond(second_text, file=file_path)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_food_coffee_service()

    async def handle_massage_service(self):
        self.repo.update_user(
            self.user_id,
            state='massage_type_info_request',
            state_data=None,
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.massage_service_info_text(lang)
        await self.respond(text)

    async def handle_massage_type_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_massage_details(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        user.state_data = response
        self.repo.update_user(
            self.user_id,
            state='massage_date_info_request',
            state_data=user.state_data
        )

        text = tmp.massage_type_request_text(lang)
        return await self.respond(text)

    async def handle_massage_date_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_booking_details_for_massage(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.handle_massage_service()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        date = response.get('date')
        time = response.get('time')
        massage_type = user.state_data.get('massage_type')
        duration = user.state_data.get('duration')

        try:
            due_date = utils.combine_and_localize_datetime(date, time)
        except ValueError:
            return await self.respond(tmp.booking_error(lang))

        if not (9 <= due_date.hour < 20):
            return await self.respond(tmp.invalid_massage_booking_time_error(lang))

        utc_dt = utils.convert_time_to_utc(due_date)
        if not self.repo.is_massage_booking_time_available(utc_dt, duration):
            return await self.respond(tmp.unavailable_time_error(lang))

        due_date = utils.combine_and_localize_datetime(date, time, utc=True)
        self.repo.add_massage_booking(self.user_id, due_date, massage_type, duration)

        first_text = tmp.massage_booking_text(user, date, time, massage_type, duration)
        await stg.bot.send_message(stg.massage_chat_id, first_text)

        file_path = utils.get_path_to_asset('new_gudauri_map.png')
        second_text = tmp.massage_booking_confirmed_text(lang)
        await self.respond(second_text, file=file_path)

        return await self.all_services_menu()

    async def handle_paragliding_service(self):
        self.repo.update_user(
            self.user_id,
            state='paragliding_plan_info_request',
            state_data=None,
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.paragliding_plan_info_text(lang)
        await self.respond(text)

    async def handle_paragliding_plan_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_selected_paragliding_plan(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        user.state_data = response
        user.state_data.update({'date': 'None', 'time': 'None', 'name': 'None', 'phone_number': 'None', })

        self.repo.update_user(
            self.user_id,
            state='paragliding_booking_info_request',
            state_data=user.state_data
        )

        text = tmp.user_details_collecting_text(lang)
        return await self.respond(text)

    async def handle_paragliding_booking_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_user_info(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.handle_paragliding_service()

        response.pop("is_request_canceled", None)

        for key, value in response.items():
            if value != 'None' and value:
                user.state_data[key] = response[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            return await self.respond(tmp.user_details_collecting_error(lang, user.state_data))

        date = user.state_data.get('date')
        time = user.state_data.get('time')

        try:
            due_date = utils.combine_and_localize_datetime(date, time)
        except ValueError:
            return await self.respond(tmp.booking_error(lang))

        if not (10 <= due_date.hour < 17):
            return await self.respond(tmp.invalid_paragliding_booking_time_error(lang))

        self.repo.update_user(self.user_id, state='paragliding_booking_confirmation_request')

        text = tmp.booking_confirmation_request_text(lang)
        return await self.respond(text)

    async def handle_paragliding_booking_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_paragliding_service()

        if answer:
            date = user.state_data.get('date')
            time = user.state_data.get('time')
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')
            selected_plan = user.state_data.get('selected_plan')

            first_text = tmp.paragliding_booking_text(user, date, time, name, phone_number, selected_plan)
            await stg.bot.send_message(stg.paragliding_chat_id, first_text)

            second_text = tmp.paragliding_booking_confirmed_text(lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_paragliding_service()

    async def handle_snowbike_service(self):
        self.repo.update_user(
            self.user_id,
            state='snowbike_tour_info_request',
            state_data=None,
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.snowbike_tour_info_text(lang)
        await self.respond(text)

    async def handle_snowbike_tour_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_selected_snowmobile_tour(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        user.state_data = response
        user.state_data.update({'date': 'None', 'time': 'None', 'name': 'None', 'phone_number': 'None', })

        self.repo.update_user(
            self.user_id,
            state='snowbike_booking_info_request',
            state_data=user.state_data
        )

        text = tmp.user_details_collecting_text(lang)
        return await self.respond(text)

    async def handle_snowbike_booking_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_user_info(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.handle_snowbike_service()

        response.pop("is_request_canceled", None)

        for key, value in response.items():
            if value != 'None' and value:
                user.state_data[key] = response[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            return await self.respond(tmp.user_details_collecting_error(lang, user.state_data))

        date = user.state_data.get('date')
        time = user.state_data.get('time')

        try:
            due_date = utils.combine_and_localize_datetime(date, time)
        except ValueError:
            return await self.respond(tmp.booking_error(lang))

        self.repo.update_user(self.user_id, state='snowbike_booking_confirmation_request')

        text = tmp.booking_confirmation_request_text(lang)
        return await self.respond(text)

    async def handle_snowbike_booking_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_snowbike_service()

        if answer:
            date = user.state_data.get('date')
            time = user.state_data.get('time')
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')
            selected_tour = user.state_data.get('selected_tour')

            first_text = tmp.snowbike_booking_text(user, date, time, name, phone_number, selected_tour)
            await stg.bot.send_message(stg.paragliding_chat_id, first_text)

            second_text = tmp.snowbike_booking_confirmed_text(lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_snowbike_service()

    async def handle_exchange_service(self):
        self.repo.update_user(
            self.user_id,
            state='exchange_info_request',
            state_data={'amount': 'None', 'date': 'None', 'time': 'None', 'name': 'None', 'phone_number': 'None', },
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.currency_exchange_info_text(lang)
        await self.respond(text, link_preview=False)

    async def handle_exchange_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_exchange_info(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        for key, value in response.items():
            if value != 'None' and value:
                user.state_data[key] = response[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in response.values():
            return await self.respond(tmp.exchange_booking_error(lang, user.state_data))

        date = response.get('date')
        time = response.get('time')

        try:
            due_date = utils.combine_and_localize_datetime(date, time)
        except ValueError:
            return await self.respond(tmp.booking_error(lang))

        self.repo.update_user(self.user_id, state='exchange_booking_confirmation_request')

        text = tmp.booking_confirmation_request_text(lang)
        return await self.respond(text)

    async def handle_exchange_booking_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_exchange_service()

        if answer:
            amount = user.state_data.get('amount')
            date = user.state_data.get('date')
            time = user.state_data.get('time')
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')

            first_text = tmp.exchange_booking_text(user, amount, date, time, name, phone_number)
            await stg.bot.send_message(stg.notification_box_chat_id, first_text)

            second_text = tmp.exchange_booking_confirmed_text(lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_exchange_service()

    async def handle_ski_service(self):
        self.repo.update_user(
            self.user_id,
            state='ski_service_info_request',
            state_data=None,
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.ski_service_info_text(lang)
        await self.respond(text)

    async def handle_ski_service_info_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.extract_selected_ski_service(self.text, lang)

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        user.state_data = response
        user.state_data.update({'date': 'None', 'time': 'None', 'name': 'None', 'phone_number': 'None', })

        self.repo.update_user(
            self.user_id,
            state='ski_booking_info_request',
            state_data=user.state_data
        )

        text = tmp.user_details_collecting_text(lang)
        return await self.respond(text)

    async def handle_ski_booking_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_user_info(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.handle_ski_service()

        response.pop("is_request_canceled", None)

        for key, value in response.items():
            if value != 'None' and value:
                user.state_data[key] = response[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            return await self.respond(tmp.user_details_collecting_error(lang, user.state_data))

        date = user.state_data.get('date')
        time = user.state_data.get('time')

        try:
            due_date = utils.combine_and_localize_datetime(date, time)
        except ValueError:
            return await self.respond(tmp.booking_error(lang))

        if not (9 <= due_date.hour <= 18):
            return await self.respond(tmp.invalid_ski_service_booking_time_error(lang))

        self.repo.update_user(self.user_id, state='ski_booking_confirmation_request')

        text = tmp.booking_confirmation_request_text(lang)
        return await self.respond(text)

    async def handle_ski_booking_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_ski_service()

        if answer:
            date = user.state_data.get('date')
            time = user.state_data.get('time')
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')
            selected_service = user.state_data.get('selected_service')

            first_text = tmp.ski_booking_text(user, date, time, name, phone_number, selected_service)
            await stg.bot.send_message(stg.paragliding_chat_id, first_text)

            second_text = tmp.ski_booking_confirmed_text(lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_ski_service()

    # Cleaning Service
    async def handle_cleaning_service(self):
        self.repo.update_user(
            self.user_id,
            state='cleaning_info_request',
            state_data=None,
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.cleaning_service_info_text(lang)
        await self.respond(text)

    async def handle_cleaning_info_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.extract_selected_cleaning_service(self.text, lang)

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        user.state_data = response
        user.state_data.update({'date': 'None', 'building': 'None', 'apartment': 'None', 'name': 'None', 'phone_number': 'None', })

        self.repo.update_user(
            self.user_id,
            state='cleaning_booking_info_request',
            state_data=user.state_data
        )

        text = tmp.cleaning_details_collecting_text(lang)
        return await self.respond(text)

    async def handle_cleaning_booking_info_request(self):
        user = self.repo.find_user(self.user_id)
        response = api.extract_cleaning_appointment_info(self.text)
        lang = user.lead.lang

        if response.get('is_request_canceled'):
            return await self.handle_cleaning_service()

        response.pop("is_request_canceled", None)

        for key, value in response.items():
            if value != 'None' and value:
                user.state_data[key] = response[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            return await self.respond(tmp.cleaning_details_collecting_error(lang, user.state_data))

        date = user.state_data.get('date')

        try:
            due_date = utils.combine_and_localize_datetime(date)
        except ValueError:
            return await self.respond(tmp.booking_error(lang))

        self.repo.update_user(self.user_id, state='cleaning_booking_confirmation_request')

        text = tmp.booking_confirmation_request_text(lang)
        return await self.respond(text)

    async def handle_cleaning_booking_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_cleaning_service()

        if answer:
            date = user.state_data.get('date')
            building = user.state_data.get('building')
            apartment = user.state_data.get('apartment')
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')
            selected_service = user.state_data.get('selected_service')

            first_text = tmp.cleaning_booking_text(user, date, building, apartment, name, phone_number, selected_service)
            await stg.bot.send_message(stg.paragliding_chat_id, first_text)

            second_text = tmp.cleaning_booking_confirmed_text(lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_cleaning_service()

    async def handle_rent_flat_service(self):
        self.repo.update_user(
            self.user_id,
            state='rent_flat_info_request',
            state_data=None,
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.rent_flat_service_info_text(lang)
        await self.respond(text)

    async def handle_rent_flat_info_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.extract_user_info(self.text)

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)
        response.pop("date", None)
        response.pop("time", None)

        if 'None' in response.values():
            return await self.respond(tmp.booking_error(lang))

        self.repo.update_user(
            self.user_id,
            state='rent_flat_booking_confirmation_request',
            state_data=response
        )

        text = tmp.booking_confirmation_request_text(lang)
        return await self.respond(text)

    async def handle_rent_flat_booking_confirmation_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.analyze_answer_yes_no(self.text)
        answer = response['answer']

        if response.get('is_request_canceled'):
            return await self.handle_rent_flat_service()

        if answer:
            name = user.state_data.get('name')
            phone_number = user.state_data.get('phone_number')

            first_text = tmp.rent_flat_booking_text(user, name, phone_number)
            await stg.bot.send_message(stg.rent_flat_chat_id, first_text)

            second_text = tmp.rent_flat_booking_confirmed_text(lang)
            await self.respond(second_text)

            return await self.all_services_menu()
        elif answer is None:
            pass
        else:
            return await self.handle_rent_flat_service()

    async def handle_transfer_service(self):
        self.repo.update_user(
            self.user_id,
            state='transfer_info_request',
            state_data={
                'route_number': 'None',
                'people_count': 'None',
                'equipment_bags': 'None',
                'luggage_bags': 'None',
                'car_ready_time': 'None',
                'phone_number': 'None'
            }
        )

        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        text = tmp.transfer_service_info_text(lang)
        await self.respond(text)

    async def handle_transfer_info_request(self):
        user = self.repo.find_user(self.user_id)
        lang = user.lead.lang
        response = api.extract_transportation_booking_details(self.text)

        if response.get('is_request_canceled'):
            return await self.all_services_menu()

        response.pop("is_request_canceled", None)

        for key, value in response.items():
            if value != 'None' and value:
                user.state_data[key] = response[key]

        self.repo.update_user(
            self.user_id,
            state_data=user.state_data
        )

        if 'None' in user.state_data.values():
            return await self.respond(tmp.transfer_details_collecting_error(lang, user.state_data))

        route_number = user.state_data.get('route_number')
        people_count = user.state_data.get('people_count')
        equipment_bags = user.state_data.get('equipment_bags')
        luggage_bags = user.state_data.get('luggage_bags')
        car_ready_time = user.state_data.get('car_ready_time')
        phone_number = user.state_data.get('phone_number')

        first_text = tmp.transfer_booking_text(user, route_number, people_count, equipment_bags, luggage_bags, car_ready_time, phone_number)
        await stg.bot.send_message(stg.transfer_chat_id, first_text)

        second_text = tmp.transfer_booking_confirmed_text(lang)
        await self.respond(second_text)

        return await self.all_services_menu()
