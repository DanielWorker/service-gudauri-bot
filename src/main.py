import asyncio
import atexit

from src.bot.bot import run_bot
from src.user_bots.user_bots import session_manager


async def main():
    tasks = [
        run_bot(),
        session_manager.load_existing_sessions(),
    ]

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        asyncio.run(session_manager.stop_all())
        print("Program terminated by the user")
