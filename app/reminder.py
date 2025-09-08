# /////////////
# Time reminder
# /////////////

from app.handlers_user import router, markup
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import main

import datetime as dt
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Add_reminder(StatesGroup):
    new_rem = State()

@router.message(F.text == 'Установить напоминание')
async def remind(message: Message, state: FSMContext):
    await state.set_state(Add_reminder.new_rem)
    await message.answer('Напишите в какое время Вам напоминить?\nВ формате ДД.ММ ЧЧ:ММ', reply_markup=markup)

@router.message(Add_reminder.new_rem)
async def add_rem(message: Message, state: FSMContext):
    await state.update_data(new_rem=message.text)
    try:
        time_from_user = dt.datetime.strptime(message.text.strip(), '%d.%m %H:%M')
        logger.info(f"{time_from_user} успешно преобразованно")
    except Exception as e:
        logger.error(f"Не получилось преобразовать\n Ошибка: {e}", exc_info=True)
    time_from_user = time_from_user.replace(year=dt.datetime.now().year)
    time_rem = dt.datetime.now()
    await asyncio.sleep((time_from_user-time_rem).total_seconds())
    await message.answer('Напоминаю!', reply_markup=main)
    logger.info("Операция прошла успешно")