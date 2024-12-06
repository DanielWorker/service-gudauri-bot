from datetime import datetime, timedelta

from telethon import events

import src.settings as stg
from src import api
from src.database import session_maker
from src.repositories.users_repo import UsersRepository

from src.user_bots.conversation.functions import ConversationService


@events.register(events.NewMessage(incoming=True))
async def message_handler(event):
    if not event.is_private:
        return

    sender = await event.get_sender()
    if sender.bot:
        return

    try:
        with session_maker() as session:
            users_repo = UsersRepository(session)
            user_id = event.sender_id if hasattr(event, 'sender_id') else event.user_id

            text = event.text if hasattr(event, 'text') else ''
            if not text:
                return

            user = users_repo.find_user(user_id)
            if not user:
                users_repo.add_user(
                    user_id,
                    event.sender.first_name,
                    event.sender.last_name,
                    event.sender.username
                )

            return await ConversationService(event, session).handle_message()

    except Exception:
        stg.logger.exception("")
