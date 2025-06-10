from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate
import app.keyboards as kb

router = Router()

class Gen(StatesGroup):
    wait = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}!\nнапишите Ваш запрос',reply_markup=kb.main)


@router.message(Gen.wait)
async def stop_flood(message: Message):
    await message.answer("Подождите, Ваш запрос обрабатывается")


@router.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    responce = await ai_generate(message.text)
    await message.answer(responce)
    await state.clear()