from src.bot.bot_auth.functions import BotAuthFunctions
from src.bot.main_menu.functions import MainMenuFunctions
from src.bot.objects import TGObject
from src.repositories.users_repo import UsersRepository


class TextRouter(TGObject):
    def __init__(self, event, session):
        super().__init__(event, session)
        self.text = event.text
        self.session = session
        self._message_logger()
        self.users_repo = UsersRepository(session)

    async def text_handler(self):
        commands = {
            '/start': self.start_command,
            '/root': self.root_command,
            '⭕️ Отмена': self.start_command
        }

        if self.text in commands:
            return await commands[self.text]()

        await self.handle_user_state()

    async def handle_user_state(self):
        user = self.users_repo.find_user(self.user_id)

        state_handlers = {
            'phone_number_request': self.handle_auth_state,
            'auth_code_request': self.handle_auth_state,
            'two_factor_auth_request': self.handle_auth_state,
        }

        if user and user.state in state_handlers:
            await state_handlers[user.state]()

    async def handle_auth_state(self):
        await BotAuthFunctions(self.event, self.session).new_bot_filling()

    async def start_command(self):
        await self.delete()
        return await MainMenuFunctions(self.event, self.session).start_command()

    async def root_command(self):
        await self.delete()
        root = self.users_repo.find_root_by_user_id(self.user_id)
        if not root:
            self.users_repo.add_root(self.user_id)

        return await MainMenuFunctions(self.event, self.session).start_command()

    def _message_logger(self):
        text = f'——————————————————\n' \
               f'MESSAGE HANDLER\n' \
               f'User: {self.username} | {self.user_id}\n' \
               f'Message: {self.event.text or "Empty"}'
        print(text)

