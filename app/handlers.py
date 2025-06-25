from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, or_f
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
from aiogram import types
import datetime as dt
import asyncio


import app.keyboards as kb


user_dict = {"name":None,
        "age":None,
        "diseases":None,
        "preferences":None,
        "current_weight":None,
        "desired_weight":None,
        "height":None,}

router = Router()


# ///////////////////
# Hanldlers for users
# ///////////////////


class Reg(StatesGroup):
    user_id = State()
    name = State()
    age = State()
    diseases = State()
    preferences = State()
    current_weight = State()
    desired_weight = State()
    height = State()


class Add_reminder(StatesGroup):
    new_rem = State()


class Add_new_pref(StatesGroup):
    new_pref = State()


class Add_new_dis(StatesGroup):
    new_dis = State()


# set_for_check = set()
markup = types.ReplyKeyboardRemove()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    # if user_id in set_for_check:
    #     await message.answer('Вы уже зарегистрированы!',reply_markup=markup)
    # else:
    await message.answer((f'''Привет {message.from_user.first_name}!
я бот, который поможет составить тебе меню по нужным тебе КБЖУ с учетом предпочтений и проблем со здоровьем.
Для начала нужно зарегистрироваться'''),reply_markup=kb.reg)
     

@router.message(or_f(F.text == 'Зарегистрироваться', F.text == 'Изменить данные'))
async def reg_age(message: Message, state: FSMContext):
    # user_id = message.from_user.id
    # set_for_check.add(user_id)
    await state.set_state(Reg.age)
    await message.answer('Введите возраст',reply_markup=markup)
    

@router.message(Reg.age)
async def reg_diseases(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    user_dict['age'] = message.text
    await state.set_state(Reg.diseases)
    await message.answer('Введите проблемы со здоровьем (если отсутствуют поставьте -)')


@router.message(Reg.diseases)
async def reg_preferences(message: Message, state: FSMContext):
    await state.update_data(diseases=message.text)
    user_dict['diseases'] = [message.text]
    await state.set_state(Reg.preferences)
    await message.answer('Введите вкусовые предпочтения (если отсутствуют поставьте -)')


@router.message(Reg.preferences)
async def reg_current_weight(message: Message, state: FSMContext):
    await state.update_data(preferences=message.text)
    user_dict['preferences'] = [message.text]
    await state.set_state(Reg.current_weight)
    await message.answer('Введите текущий вес')


@router.message(Reg.current_weight)
async def reg_desired_weight(message: Message, state: FSMContext):
    await state.update_data(current_weight=message.text)
    user_dict['current_weight'] = message.text
    await state.set_state(Reg.desired_weight)
    await message.answer('Введите желаемый вес')


@router.message(Reg.desired_weight)
async def reg_height(message: Message, state: FSMContext):
    await state.update_data(desired_weight=message.text)
    user_dict['desired_weight'] = message.text
    await state.set_state(Reg.height)
    await message.answer('Введите рост')


@router.message(Reg.height)
async def finally_reg(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    user_dict['height'] = message.text
    data = await state.get_data()
    await message.answer(f'''{data["age"]}
{data["diseases"]}
{data["preferences"]}
{data["current_weight"]}
{data["desired_weight"]}
{data["height"]}
''', reply_markup=kb.main)
    await state.clear()


@router.message(F.text == 'Добавить проблему/предпочтение')
async def add_new(message: Message):
    await message.answer("Выберите что добавить", reply_markup=kb.add_new_pref_dis)


@router.message(F.text == 'Предпочтение')
async def add_new_pref(message: Message, state: FSMContext):
    await state.set_state(Add_new_pref.new_pref)
    await message.answer('Добавлять по одному предпочтению за раз', reply_markup=markup)


@router.message(Add_new_pref.new_pref)
async def add_new_pref(message: Message, state: FSMContext):
    await state.update_data(new_pref=message.text)
    new_pref = message.text
    user_dict['preferences'].append(new_pref)
    pref = user_dict['preferences']
    await message.answer(f"{", ".join(pref)}", reply_markup=kb.main)
    await state.clear()


@router.message(F.text == 'Проблему')
async def add_new_pref(message: Message, state: FSMContext):
    await state.set_state(Add_new_dis.new_dis)
    await message.answer('Добавлять по одной проблеме за раз', reply_markup=markup)


@router.message(Add_new_dis.new_dis)
async def add_new_pref(message: Message, state: FSMContext):
    await state.update_data(new_dis=message.text)
    new_dis = message.text
    user_dict['diseases'].append(new_dis)
    dis = user_dict['diseases']
    await message.answer(f"{", ".join(dis)}", reply_markup=kb.main)
    await state.clear()


# ////////////////
# Hanldlers for AI
# ////////////////


class Gen(StatesGroup):
    wait = State()

@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подождите, Ваш запрос обрабатывается")

@router.message(F.text == 'Составить меню на день')
async def generating(message: Message, state: FSMContext):
    max_len = 4096
    await state.set_state(Gen.wait)
    text_for_ii = f'''Составь меню на один день
c учетом моих пожеланий: {user_dict['preferences']}
и моих болезней: {user_dict['diseases']}'''
    responce = await ai_generate(text_for_ii)
    for i in range(0, len(responce), max_len):
        part = responce[i:i + max_len]
        await message.answer(part)
    await state.clear()


# /////////////
# Time reminder
# /////////////


@router.message(F.text == 'Установить напоминание')
async def remind(message: Message, state: FSMContext):
    await state.set_state(Add_reminder.new_rem)
    await message.answer('Напишите в какое время Вам напоминить?\nВ формате ДД.ММ ЧЧ:ММ', reply_markup=markup)


@router.message(Add_reminder.new_rem)
async def add_rem(message: Message, state: FSMContext):
    await state.update_data(new_rem=message.text)
    time_from_user = dt.datetime.strptime(message.text.strip(), '%d.%m %H:%M')
    time_from_user = time_from_user.replace(year=dt.datetime.now().year)
    time_rem = dt.datetime.now()
    await asyncio.sleep((time_from_user-time_rem).total_seconds())
    await message.answer('Напоминаю!')


@router.message()
async def not_but(message: Message):
    await message.answer('Выберите кнопку')