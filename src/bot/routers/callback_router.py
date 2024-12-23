from telethon.errors import MessageIdInvalidError, MessageTooLongError, MessageNotModifiedError

from src.bot.main_menu.callbacks import MainMenuCallback
from src.bot.massage_service.callback import MassageServiceCallback
from src.database import session_maker
from src.settings import logger


class CallbackRouter:
    def __init__(self, event):
        self.event = event
        self.callback_query = event.data.decode("utf-8")
        self._callback_logger()
        self.callback_mapping = {
            'mm/': MainMenuCallback,
            'ms/': MassageServiceCallback,
        }

    async def route_callback(self):
        routed = False
        try:
            routed = await self._route_to_callback()

        except MessageIdInvalidError:
            await self._handle_invalid_message_id()
        except MessageTooLongError:
            await self._handle_message_too_long()
        except MessageNotModifiedError:
            pass
        except Exception:
            logger.exception("")

        if routed:
            await self.event.answer()

        return routed

    async def _route_to_callback(self):
        if self.callback_query == 'cancel_button':
            await self.event.delete()
            return True

        for prefix, callback_class in self.callback_mapping.items():
            if self.callback_query.startswith(prefix):
                with session_maker() as session:
                    callback_instance = callback_class(self.event, session)
                    await callback_instance.callback_handler()
                    return True
        return False

    async def _handle_invalid_message_id(self):
        msg = await self.event.get_message()
        await self.event.respond(msg.text, buttons=msg.buttons)
        await self.event.answer('Something went wrong, please use a new message')

    async def _handle_message_too_long(self):
        await self.event.answer('Message was too long', alert=True)

    def _callback_logger(self):
        text = f'——————————————————\n' \
               f'CALLBACK HANDLER\n' \
               f'User: {self.event.sender.username} | {self.event.sender_id}\n' \
               f'Callback: {self.callback_query}'
        print(text)

