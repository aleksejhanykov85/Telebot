from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
from aiogram import types

import app.keyboards as kb


router = Router()

class Reg(StatesGroup):
    user_id = State()
    name = State()
    age = State()
    diseases = State()
    preferences = State()
    current_weight = State()
    desired_weight = State()
    height = State()

user_dict = {"name":None,
        "age":None,
        "diseases":None,
        "preferences":None,
        "current_weight":None,
        "desired_weight":None,
        "height":None,}

class Gen(StatesGroup):
    wait = State()

set_for_check = set()
markup = types.ReplyKeyboardRemove()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    if user_id in set_for_check:
        
        await message.answer('Вы уже зарегистрированы!',reply_markup=markup)
    else:
        await message.answer((f'''Привет {message.from_user.first_name}!
я бот, который поможет составить тебе меню по нужным тебе КБЖУ с учетом предпочтений и проблем со здоровьем.
Для начала нужно зарегистрироваться'''),reply_markup=kb.reg)
     

@router.message(F.text == 'Зарегистрироваться')
async def reg_name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    set_for_check.add(user_id)
    await state.set_state(Reg.name)
    await message.answer('Введите имя',reply_markup=markup)


@router.message(Reg.name)
async def reg_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_dict['name'] = message.text
    await state.set_state(Reg.age)
    await message.answer('Введите возраст',reply_markup=markup)
    

@router.message(Reg.age)
async def reg_diseases(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    user_dict['age'] = message.text
    await state.set_state(Reg.diseases)
    await message.answer('Введите проблемы со здоровьем (если отсутствуют поставьте -)',reply_markup=markup)


@router.message(Reg.diseases)
async def reg_preferences(message: Message, state: FSMContext):
    await state.update_data(diseases=message.text)
    user_dict['diseases'] = message.text
    await state.set_state(Reg.preferences)
    await message.answer('Введите вкусовые предпочтения (если отсутствуют поставьте -)',reply_markup=markup)


@router.message(Reg.preferences)
async def reg_current_weight(message: Message, state: FSMContext):
    await state.update_data(preferences=message.text)
    user_dict['preferences'] = message.text
    await state.set_state(Reg.current_weight)
    await message.answer('Введите текущий вес',reply_markup=markup)


@router.message(Reg.current_weight)
async def reg_desired_weight(message: Message, state: FSMContext):
    await state.update_data(current_weight=message.text)
    user_dict['current_weight'] = message.text
    await state.set_state(Reg.desired_weight)
    await message.answer('Введите желаемый вес',reply_markup=markup)


@router.message(Reg.desired_weight)
async def reg_height(message: Message, state: FSMContext):
    await state.update_data(desired_weight=message.text)
    user_dict['desired_weight'] = message.text
    await state.set_state(Reg.height)
    await message.answer('Введите рост',reply_markup=markup)


@router.message(Reg.height)
async def finally_reg(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    user_dict['height'] = message.text
    data = await state.get_data()
    await message.answer(f'''{data["name"]}
{data["age"]}
{data["diseases"]}
{data["preferences"]}
{data["current_weight"]}
{data["desired_weight"]}
{data["height"]}
{data}
''', reply_markup=kb.main)
    await state.clear()


@router.message(F.text == 'Составить меню на неделю')
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    await message.answer(message.text)
    responce = await ai_generate(message.text)
    await message.answer(responce)
    await state.clear()


@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подождите, Ваш запрос обрабатывается")


