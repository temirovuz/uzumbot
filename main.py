import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import bot_token
from header import router


async def main():
    bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot=bot)
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
