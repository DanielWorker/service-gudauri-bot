from src.bot.objects import TGObject
from src.user_bots.conversation import templates as tmp
from src.api import openai_api as api


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
        }

        if user.state in state_functions:
            return await state_functions[user.state]()

    async def handle_new_user(self):
        self.users_repo.update_user(self.user_id, state='language_request')

        text = tmp.select_language_text()
        await self.respond(text)

    async def handle_language_request(self):
        response = api.determine_language(self.text)
        lang = response["language"]

        if lang != "undefined":
            self.users_repo.update_lead(self.user_id, language=lang)
            self.users_repo.update_user(self.user_id, state='service_request')
            text = tmp.all_services_text(lang)
        else:
            text = tmp.select_language_error()

        return await self.respond(text)

    async def handle_service_request(self):
        user = self.users_repo.find_user(self.user_id)
        response = api.determine_service(self.text)
        service = response["service"]

        service_handlers = {
            'rent_sky_board': self.handle_sky_board_service,
            'instructor': self.handle_instructor_service,
            '': self,
        }

        if service not in service_handlers:
            text = tmp.service_unavailable_error(user.lead.language)
            return await self.respond(text)

        return await service_handlers[service]()

    async def handle_sky_board_service(self):
        pass

    async def handle_instructor_service(self):
        pass
