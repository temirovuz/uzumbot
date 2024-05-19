from aiogram.fsm.state import StatesGroup, State


class AddShop(StatesGroup):
    name = State()


class AddFoodCategory(StatesGroup):
    name = State()


class AddFood(StatesGroup):
    name = State()
    price = State()
    image = State()
    category = State()
    shop = State()


class AddImage(StatesGroup):
    shop = State()
    category = State()
    image = State()


class AddBasket(StatesGroup):
    user = State()
    food = State()
