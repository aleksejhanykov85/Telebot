from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить проблему/предпочтения')],
    [KeyboardButton(text='Установить напоминание')]
],resize_keyboard=True,
input_field_placeholder='Выберите пункт меню:')