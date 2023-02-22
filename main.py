import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from commands.register import register_user_commands


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=os.getenv('token'))
    dp = Dispatcher()
    register_user_commands(dp)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt,SystemExit):
        print('bot stopped')