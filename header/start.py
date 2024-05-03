from aiogram import types, Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_bot(message: types.Message):
    await message.edit(content="Salom test sifatida bot ishlamoqda bu vaqtincha hammasi!\nHammasi yaxshilikka")
