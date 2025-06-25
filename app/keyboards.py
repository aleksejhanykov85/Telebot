from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрироваться')],
],resize_keyboard=True,)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить проблему/предпочтение'),KeyboardButton(text='Установить напоминание')],
    [KeyboardButton(text='Составить меню на день'),KeyboardButton(text='Изменить данные')],
],resize_keyboard=True)


add_new_pref_dis = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Предпочтение")],
    [KeyboardButton(text='Проблему')]
],resize_keyboard=True)