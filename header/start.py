from aiogram import types, Router
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start_bot(message: types.Message):
    await message.reply(text="Salom test sifatida bot ishlamoqda bu vaqtincha hammasi!\nHammasi yaxshilikka")


@router.message(Command('info'))
async def info(message: types.Message):
    await message.answer('Bot haqida qisqacha malumot beramiz')


@router.message(Command('admin'))
async def admin(message: types.Message):
    await message.answer(text='Kerakli bolimni tanlang')
