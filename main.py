import asyncio
import logging

from aiogram import Bot, Dispatcher


from config import bot_token
from header import router


async def main():
    bot = Bot(token=bot_token)
    dp = Dispatcher(bot=bot)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
