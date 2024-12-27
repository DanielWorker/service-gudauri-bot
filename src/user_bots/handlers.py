from telethon import events

import src.settings as stg
from src.database import session_maker
from src.repositories.base import BaseRepository
from src.user_bots.conversation.commands import ConversationCommands

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
            repo = BaseRepository(session)
            user_id = event.sender_id if hasattr(event, 'sender_id') else event.user_id

            user_entity = await event.client.get_entity(user_id)
            user = repo.find_user(user_id)
            if not user:
                repo.add_user(
                    user_id,
                    user_entity.first_name,
                    user_entity.last_name,
                    user_entity.username
                )

            routed = await ConversationCommands(event, session).text_router()
            if not routed:
                return await ConversationService(event, session).handle_message()

    except Exception:
        stg.logger.exception("")
