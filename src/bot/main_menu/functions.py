import re

from telethon.errors import PhoneMigrateError, PhoneCodeExpiredError, SendCodeUnavailableError, PhoneCodeInvalidError, \
    SessionPasswordNeededError, PasswordHashInvalidError

from src.bot.objects import TGObject
from src import settings as stg
from src.bot.main_menu import buttons as kb
from src.bot.main_menu import templates as tmp


class MainMenuFunctions(TGObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def start_command(self):
        user = self.users_repo.find_user(self.user_id)
        if not user:
            self.users_repo.add_user(
                self.user_id,
                self.event.sender.first_name,
                self.event.sender.last_name,
                self.event.sender.username
            )
            user = self.users_repo.find_user(self.user_id)
        else:
            self.users_repo.update_user(self.user_id, state=None, state_data=None)

        if not (user.root or user.bot):
            return await self.respond(tmp.access_denied_text())

        bots = self.users_repo.find_all_bots()
        text = tmp.main_menu_text(user, bots)
        buttons = kb.main_menu_btn()
        return await self.respond(text, buttons=buttons)

    async def _get_provided_user_data(self):
        user_id, first_name, last_name, username = None, None, None, None

        if self.text:
            try:
                entity = await self.bot.get_entity(self.text)
                user_id, first_name, last_name, username = entity.id, entity.first_name, entity.last_name, entity.username
            except ValueError:
                return await self.respond(tmp.invalid_user_text())

        elif self.event.contact:
            contact = self.event.message.contact
            user_id, first_name, last_name = contact.user_id, contact.first_name, contact.last_name

        return user_id, first_name, last_name, username
