from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton


def contact():
    keyboard = KeyboardBuilder(KeyboardButton)
    keyboard.add(*[
        KeyboardButton(text='Contact me', request_contact=True),
    ])
    return keyboard.as_markup(resize_keyboard=True)


def location():
    keyboard = KeyboardBuilder(KeyboardButton)
    keyboard.add(*[
        KeyboardButton(text='Location me', request_location=True),
    ])
    return keyboard.as_markup(resize_keyboard=True)


def regions():
    keyboard = KeyboardBuilder(KeyboardButton)
    keyboard.add(*[
        KeyboardButton(text='Regions', callback_data='test'),
        KeyboardButton(text='Regions', callback_data='test2'),
        KeyboardButton(text='Regions', callback_data='test3'),
        KeyboardButton(text='Regions', callback_data='test4'),
    ])
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)
