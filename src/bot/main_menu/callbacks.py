from src.bot.objects import CObject
from src.bot.utils import execute_callback
from src.bot.main_menu import buttons as kb
from src.bot.main_menu import templates as tmp
from src.user_bots.user_bots import session_manager


class MainMenuCallback(CObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def callback_handler(self):
        callback_functions = {
            'main_menu': self.main_menu,

            'bots_menu': self.bots_menu,
            'bot_menu': self.bot_menu,
            'add_bot': self.add_bot_menu,
            'leads_menu': self.leads_menu,
            'lead_menu': self.lead_menu,

        }

        return await execute_callback(self.callback, callback_functions)

    async def main_menu(self):
        user = self.users_repo.find_user(self.user_id)
        bots = self.users_repo.find_all_bots()
        text = tmp.main_menu_text(user, bots)
        buttons = kb.main_menu_btn()
        return await self.event.edit(text, buttons=buttons)

    async def bots_menu(self):
        bots = self.users_repo.find_all_bots()
        text = tmp.bots_menu_text(bots)
        buttons = kb.bots_menu_btn(bots)
        return await self.event.edit(text, buttons=buttons)

    async def bot_menu(self, bot_id):
        bot = self.users_repo.find_bot(bot_id=bot_id)
        client = session_manager.find_session(bot.phone_number)

        is_auth = False
        if client and client.is_connected():
            is_auth = await client.is_user_authorized()

        text = tmp.bot_menu_text(bot, is_auth)
        buttons = kb.bot_menu_btn(is_auth)
        return await self.event.edit(text, buttons=buttons)

    async def add_bot_menu(self):
        await self.delete()

        self.users_repo.update_user(self.user_id, state='phone_number_request')
        text = tmp.add_bot_menu_text()
        buttons = kb.cancel_btn()
        return await self.respond(text, buttons=buttons)

    async def leads_menu(self):
        leads = self.users_repo.find_all_leads()
        text = tmp.leads_menu_text()
        buttons = kb.leads_menu_btn(leads)
        return await self.event.edit(text, buttons=buttons)

    async def lead_menu(self, lead_id):
        lead = self.users_repo.find_lead(id=lead_id)
        lead_message = self.users_repo.find_lead_message(lead_id=lead_id)
        text = tmp.lead_menu_text(lead, lead_message)
        buttons = kb.lead_menu_btn()
        return await self.event.edit(text, buttons=buttons)
