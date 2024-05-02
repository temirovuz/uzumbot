from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardButton


def language():
    keyboard = KeyboardBuilder(InlineKeyboardButton)
    keyboard.add(
        *[
            InlineKeyboardButton(text='🇷🇺 Русский', callback_data=CheckLanguage(action='ru').pack()),
            InlineKeyboardButton(text='🇺🇿 Uzbek', callback_data=CheckLanguage(action='uz').pack())
        ]
    )
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)
