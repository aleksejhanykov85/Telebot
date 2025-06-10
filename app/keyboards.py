from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(tetx='Добавить проблему/предпочтения')],
    [KeyboardButton(text='Установить напоминание')]
],resize_keyboard=True,
input_field_placeholder='Выберите пункт меню:')