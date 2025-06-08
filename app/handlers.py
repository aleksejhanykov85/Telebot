from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
from aiogram import Bot, Dispatcher
from config import TG_TOKEN
from aiogram import types

router = Router()


class Gen(StatesGroup):
    wait = State()

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

@router.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [
            types.KeyboardButton(text="1. Добавить проблемы со здоровьем/пожелания"),
            types.KeyboardButton(text="2. Установить напоминание")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Ввыберите одну из цифр"
    )
    await message.answer("Выберите что хотите:", reply_markup=keyboard)

    @dp.message_handler(F.text.lower() == "1")
    async def btn1(message: types.Message):
        await message.reply("Что вы хотите добавить?")

    @dp.message_handler(F.text.lower() == "2")
    async def btn2(message: types.Message):
        await message.reply("Через сколько Вам напомнить?")
    await message.answer('Привет!\nнапишите Ваш запрос')


@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подождите, Ваш запрос обрабатывается")


@router.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    responce = await ai_generate(message.text)
    await message.answer(responce)
    await state.clear()