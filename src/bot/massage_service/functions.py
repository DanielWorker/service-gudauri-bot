from src.bot.objects import TGObject

from src.bot.massage_service import templates as tmp
from src.bot.massage_service import buttons as kb


class MassageServiceFunctions(TGObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def send_calendar_menu(self):
        text = tmp.calendar_menu_text()
        buttons = kb.calendar_menu_btn(self.repo)
        return await self.respond(text, buttons=buttons)
