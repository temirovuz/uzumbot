from aiogram.filters.callback_data import CallbackData


class CheckLanguage(CallbackData, prefix='lang'):
    action: str
