from aiogram import types, Router, F

router = Router()


# --------------------------> Shops add <-----------------------------------
@router.message(F.text == "Do'kon qo'shish")
async def _add_shops(message: types.Message):
    await message.reply("Do'kon qo'shish")


# --------------------------> Foods Category Add <-----------------------------------
@router.message(F.text == "Foods Catergoriya qo'shish")
async def _add_food_cat(message: types.Message):
    await message.reply("Do'kon qo'shish")


# --------------------------> Foods Add <-----------------------------------
@router.message(F.text == "Foods qo'shish")
async def _add_food(message: types.Message):
    await message.reply("Do'kon qo'shish")


# --------------------------> Drinks Add <-----------------------------------
@router.message(F.text == "Ichimliklar qo'shish")
async def _add_drink(message: types.Message):
    await message.reply("Do'kon qo'shish")


# --------------------------> Images Add <-----------------------------------
@router.message(F.text == "Rasmlar qo'shish")
async def _add_image(message: types.Message):
    await message.reply("Do'kon qo'shish")


# --------------------------> Send Message <-----------------------------------
@router.message(F.text == "Xabar yuborish")
async def _add_send_message(message: types.Message):
    await message.reply("Do'kon qo'shish")
