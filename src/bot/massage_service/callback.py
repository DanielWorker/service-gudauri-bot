from src.bot.objects import CObject
from src.bot.utils import execute_callback

from src.bot.massage_service import templates as tmp
from src.bot.massage_service import buttons as kb


class MassageServiceCallback(CObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def callback_handler(self):
        callback_functions = {
            'calendar_menu': self.calendar_menu,
            'navigate_calendar': self.navigate_calendar,
            'select_month': self.select_month,
            'select_calendar_date': self.select_calendar_date,
        }

        return await execute_callback(self.callback, callback_functions)

    async def calendar_menu(self):
        text = tmp.calendar_menu_text()
        buttons = kb.calendar_menu_btn(self.repo)
        return await self.event.edit(text, buttons=buttons)

    async def navigate_calendar(self, year, month):
        buttons = kb.calendar_menu_btn(self.repo, int(year), int(month))
        return await self.event.edit(buttons=buttons)

    async def select_month(self, year):
        buttons = kb.select_month_btn(int(year))
        return await self.event.edit(buttons=buttons)

    async def select_calendar_date(self, due_date):
        bookings = self.repo.get_massage_booking_for_selected_date(due_date)
        text = tmp.selected_date_booking_text(due_date, bookings)
        buttons = kb.back_to_calendar_menu_btn()
        return await self.event.edit(text, buttons=buttons)
