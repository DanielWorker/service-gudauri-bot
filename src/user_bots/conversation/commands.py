from src.bot.objects import TGObject
from src.user_bots.conversation.functions import ConversationService


class ConversationCommands(TGObject):
    MENU_COMMANDS = ['меню', 'menu']
    BACK_COMMANDS = ['назад', 'отмена', 'нет', 'cancel', 'back', 'no']
    ALL_COMMANDS = [*MENU_COMMANDS, *BACK_COMMANDS]

    def __init__(self, event, session):
        super().__init__(event, session)
        self.l_text = self.text.lower()
        self.functions = ConversationService(event, session)

    async def text_router(self):
        user = self.repo.find_user(self.user_id)

        if self.l_text in self.ALL_COMMANDS:
            if user.state in ['new_user', 'language_request']:
                await self.functions.handle_new_user()
                return True
            elif self.l_text in self.MENU_COMMANDS:
                await self.functions.all_services_menu()
                return True
            elif self.l_text in self.BACK_COMMANDS:
                await self.handle_back_command()
                return True

        return False

    async def handle_back_command(self):
        user = self.repo.find_user(self.user_id)

        state_routes = {
            # Rent equipment
            'rent_equipment_info_request': self.functions.all_services_menu,
            # Hire instructor
            'hire_instructor_info_request': self.functions.all_services_menu,
            'hire_instructor_personal_info_request': self.functions.handle_instructor_service,
            'hire_instructor_confirmation_request': self.functions.handle_instructor_service,
            # Food & Coffee
            'food_order_info_request': self.functions.all_services_menu,
            'food_order_delivery_details_request': self.functions.send_food_order_message,
            'food_order_confirmation_request': self.functions.handle_food_coffee_service,
            # Massage
            'massage_type_info_request': self.functions.all_services_menu,
            'massage_date_info_request': self.functions.handle_massage_service,
            'massage_booking_confirmation_request': self.functions.handle_massage_service,
            # Paragliding
            'paragliding_plan_info_request': self.functions.all_services_menu,
            'paragliding_booking_info_request': self.functions.handle_paragliding_service,
            'paragliding_booking_confirmation_request': self.functions.handle_paragliding_service,
            # Snowbike
            'snowbike_tour_info_request': self.functions.all_services_menu,
            'snowbike_booking_info_request': self.functions.handle_snowbike_service,
            'snowbike_booking_confirmation_request': self.functions.handle_snowbike_service,
            # Exchange
            'exchange_info_request': self.functions.all_services_menu,
            'exchange_booking_confirmation_request': self.functions.handle_exchange_service,

        }

        handler = state_routes.get(user.state, self.functions.all_services_menu)
        return await handler()
