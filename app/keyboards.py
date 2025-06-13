from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрироваться')],
],resize_keyboard=True,)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить проблему/предпочтения')],
    [KeyboardButton(text='Установить напоминание')],
    [KeyboardButton(text='Составить меню на неделю')],
],resize_keyboard=True,
input_field_placeholder='Выберите пункт меню:')