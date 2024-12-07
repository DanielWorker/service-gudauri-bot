import asyncio

from telethon import TelegramClient, events

import src.settings as stg
from src.bot.routers.callback_router import CallbackRouter
from src.bot.routers.text_router import TextRouter
from src.database import session_maker
from src.settings import path_to_sessions

bot = TelegramClient(path_to_sessions + 'bot', stg.BOT_API_ID, stg.BOT_API_HASH, base_logger='telegram')
bot.start(bot_token=stg.BOT_TOKEN)

stg.bot = bot


@bot.on(events.NewMessage())
async def message_handler(event):
    try:
        if event.sender_id == stg.BOT_ID:
            return

        with session_maker() as session:
            await TextRouter(event, session).text_handler()
    except:
        stg.logger.exception('')


@bot.on(events.CallbackQuery())
async def callback_handler(event):
    await CallbackRouter(event).route_callback()


async def run_bot():
    print('\n\n=== Bot started ===')
    while True:
        try:
            await bot.run_until_disconnected()
        except Exception as e:
            if e == 'Cannot send requests while disconnected':
                bot.start()
            stg.logger.error(f"Bot crashed: {e}")
            await asyncio.sleep(5)
