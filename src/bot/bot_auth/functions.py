import re

from telethon.errors import PhoneMigrateError, PhoneCodeExpiredError, SendCodeUnavailableError, PhoneCodeInvalidError, \
    SessionPasswordNeededError, PasswordHashInvalidError

from src.bot.main_menu.functions import MainMenuFunctions
from src.bot.objects import TGObject
from src import settings as stg
from src.user_bots.user_bots import session_manager


class BotAuthFunctions(TGObject):
    def __init__(self, event, session):
        super().__init__(event, session)

    async def new_bot_filling(self):
        user = self.repo.find_user(self.user_id)

        if user.state == 'phone_number_request':
            return await self.phone_number_request()

        elif user.state == 'auth_code_request':
            return await self.auth_code_request(user)

        elif user.state == 'two_factor_auth_request':
            return await self.two_factor_auth_request(user)

    async def phone_number_request(self):
        phone_number = self.event.text.replace(' ', '').replace('-', '')
        result = re.findall(r'^\+\d{5,17}$', phone_number)
        if result:
            code_sent = await self.send_code(phone_number)
            if code_sent:
                return await self.respond('📩 Вам отправлен код, введите его в формате /code12345')
            else:
                return await self.event.respond('Не удалось отправить код')

        else:
            return await self.event.respond('Введен неверный номер телефона')

    async def auth_code_request(self, user):
        state_data = user.state_data
        phone_number = state_data.get('phone_number')
        phone_code_hash = state_data.get('phone_code_hash')
        code = self.event.text[5:]

        await self.tg_connect(phone_number)

        try:
            await self.tg_client.sign_in(
                phone=phone_number,
                code=code,
                phone_code_hash=phone_code_hash
            )
            return await self.bot_login_completed(phone_number)
        except (PhoneCodeExpiredError, SendCodeUnavailableError, PhoneCodeInvalidError):
            stg.logger.exception('')
            await self.respond('Code Expired')
            await self.send_code(phone_number)

        except SessionPasswordNeededError:
            self.repo.update_user(self.user_id, state='two_factor_auth_request')
            text = 'Введите пароль двух-факторной аутентификации'
            await self.respond(text)

    async def two_factor_auth_request(self, user):
        state_data = user.state_data
        phone_number = state_data.get('phone_number')
        password = self.event.text

        await self.tg_connect(phone_number)

        try:
            await self.tg_client.sign_in(password=password)
            return await self.bot_login_completed(phone_number)
        except PhoneCodeExpiredError:
            stg.logger.exception('')
            await self.send_code(phone_number)
            await self.respond('Код аутентификации просрочен, введите новый код')
        except PasswordHashInvalidError:
            await self.respond('Введен неверный пароль, попробуйте еще раз')

    async def send_code(self, phone_number):
        await self.tg_connect(phone_number)

        try:
            sent_code = await self.tg_client.send_code_request(phone_number)
        except PhoneMigrateError as e:
            await self.tg_client.disconnect()
            await self.tg_client.session.set_dc(e.new_dc)
            await self.tg_client.connect()

            sent_code = await self.tg_client.send_code_request(phone_number)
        except ConnectionError:
            await self.tg_connect(phone_number)
            sent_code = await self.tg_client.send_code_request(phone_number)
        except Exception:
            stg.logger.exception('')
            sent_code = None

        state_data = None
        if sent_code:
            state_data = {
                'phone_number': phone_number,
                'phone_code_hash': sent_code.phone_code_hash
            }
            self.repo.update_user(self.user_id, state='auth_code_request', state_data=state_data)

        return state_data

    async def bot_login_completed(self, phone_number):
        if not self.tg_client and self.tg_client.is_connected():
            await self.tg_connect(phone_number)

        bot_user = await self.tg_client.get_me()
        await self.tg_disconnect()

        user_id = bot_user.id

        user = self.repo.find_user(user_id)
        if not user:
            self.repo.add_user(bot_user.id, bot_user.first_name, bot_user.last_name, bot_user.username)

        if not user.bot:
            self.repo.add_bot(user_id, phone_number)

        await session_manager.handle_new_session(phone_number)
        stg.logger.info(f'Bot {bot_user.id} logged in')

        self.repo.update_user(self.user_id, state=None, state_data=None)
        await self.respond('🎉 Вы успешно авторизовались!')
        return await MainMenuFunctions(self.event, self.session).start_command()
