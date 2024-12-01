from telethon import TelegramClient

from src.repositories.users_repo import UsersRepository
import src.settings as stg


class Base:
    def __init__(self, event, session):
        self.event = event
        self.chat_id = event.chat_id
        self.peer_id = (
            None if not event.input_chat
            else event.input_chat.channel_id if event.is_channel
            else event.input_chat.user_id if event.is_private
            else event.input_chat.chat_id
        )
        self.message_id = (
            event.message_id if hasattr(event, 'message_id')
            else event.id if hasattr(event, 'id')
            else None
        )
        self.user_id = (
            event.sender_id if hasattr(event, 'sender_id')
            else event.user_id
        )
        self.username = (
            event.sender.username if hasattr(event, 'sender') and event.sender
            else None
        )
        self.tg_client = None
        self.bot = stg.bot
        self.users_repo = UsersRepository(session)
        self.session = session

    async def tg_connect(self, phone_number):
        if self.tg_client and self.tg_client.is_connected():
            return

        tg_client = TelegramClient(stg.path_to_sessions + f'{phone_number}', api_id=stg.BOT_API_ID, api_hash=stg.BOT_API_HASH, base_logger='telegram')
        self.tg_client = tg_client

        if not tg_client.is_connected():
            try:
                await tg_client.connect()
            except Exception:
                stg.logger.exception('')

    async def tg_disconnect(self):
        if self.tg_client and self.tg_client.is_connected():
            try:
                await self.tg_client.disconnect()
            except Exception:
                stg.logger.exception('')

    async def respond(self, *args, **kwargs):
        return await self.event.respond(*args, **kwargs)

    async def reply(self, *args, **kwargs):
        return await self.event.reply(*args, **kwargs)

    async def delete(self):
        try:
            await self.event.delete()
        except:
            pass


class CObject(Base):
    def __init__(self, event, session):
        super().__init__(event, session)
        self.callback = '/'.join(event.data.decode("utf-8").split('/')[1:])


class TGObject(Base):
    def __init__(self, event, session):
        super().__init__(event, session)
        self.text = self.event.text
