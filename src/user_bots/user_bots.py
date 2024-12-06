import asyncio
import os
from sqlite3 import OperationalError

from telethon import TelegramClient

import src.settings as stg


HANDLERS = {
    '+48572779167.session': 'src.user_bots.handlers.message_handler',
}


class SessionManager:
    def __init__(self):
        self.clients = dict()
        self.retry_delay = 1

    async def load_existing_sessions(self):
        session_files = [
            session_file for session_file in os.listdir(stg.path_to_sessions)
            if session_file.endswith('.session') and not session_file.startswith('bot')
        ]
        await asyncio.gather(*(self.add_session(session_file) for session_file in session_files))

    async def add_session(self, session_name):
        session_path = stg.path_to_sessions + session_name
        client = TelegramClient(session_path, stg.BOT_API_ID, stg.BOT_API_HASH)

        # if session_name == '+48572779167.session':
        if session_name == '+995511227921.session':
            from src.user_bots.handlers import message_handler
            client.add_event_handler(message_handler)

        await client.start()

        is_auth = await client.is_user_authorized()
        if not is_auth:
            await stg.bot.send_message(stg.dev_user_id, f'{session_name} disconnected')
            print(f"Session expired: {session_name}")
            return None

        self.clients[session_name] = client
        print(f"Started session: {session_name}")

        asyncio.create_task(self.run_client(client, session_name))

    async def run_client(self, client, session_name):
        try:
            await client.run_until_disconnected()
        except (OperationalError, ConnectionError, Exception) as e:
            stg.logger.error(f"Error in session {session_name}: {e}")
            await asyncio.sleep(self.retry_delay)
            self.retry_delay = min(self.retry_delay * 2, 60)
        finally:
            await self.close_session(session_name, client)
            await self.add_session(session_name)

    async def handle_new_session(self, session_name):
        await self.add_session(f'{session_name}.session')

    def find_session(self, session_name):
        return self.clients.get(f'{session_name}.session')

    async def stop_all(self):
        for client in self.clients.values():
            await client.disconnect()

    async def close_session(self, session_name, cached_client):
        client = self.clients.get(session_name, cached_client)
        if client:
            try:
                if client.is_connected():
                    await client.disconnect()
            except Exception as e:
                stg.logger.error(f"Failed to disconnect session: {e}")
            finally:
                if client.session:
                    client.session.close()
                self.clients.pop(session_name, None)


session_manager = SessionManager()
