# import os
# import asyncio
# from aiogram import Router, F, Bot
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
# from models import async_session, User, Broadcast
# from dotenv import load_dotenv

# load_dotenv()
# ADMIN_ID = int(os.getenv('ADMIN_ID',0))

# admin_router = Router()


# class BroadcastState(StatesGroup):
#     waiting_for_broadcast_text = State()
    

# def admin_main_menu():
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="Статистика", callback_data='stats')],
#         [InlineKeyboardButton(text="Рассылка", callback_data='broadcast')],
#         [InlineKeyboardButton(text="Доп. настройки", callback_data='settings')]
#     ])
#     return keyboard

# def back_menu():
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Назад', callback_data='back')]
#     ])
#     return keyboard

# @admin_router.message(Command("/admin"))
# async def admin_panel(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         await message.answer("У Вас нет доступа к этой команде.")
#         return
#     await message.answer("Добро пожаловать в админ-панель!", reply_markup=admin_main_menu())
    
# @admin_router.callback_query(F.data == "back")
# async def back_to_main(callback: CallbackQuery):
#     await callback.message.edit_text("Админ-панель: Выберите действие", reply_markup=admin_main_menu())
#     await callback.answer()
    
# @admin_router.callback_query(F.data == "stats")
# async def process_stats(callback: CallbackQuery):
#     db = async_session()
#     total_users = db.query(User).count()
#     active_users = db.query(User).filter(User.active == True).count()
#     db.close
    
#     text = f"Статистика:\nВсего пользователей: {total_users}\nАктивных пользователей: {active_users}"
#     await callback.message.edit_text(text, reply_markup=back_menu())
#     await callback.answer
    
# @admin_router.callback_query(F.data == "broadcast")
# async def process_broadcast(callback: CallbackQuery, state: FSMContext):
#     await callback.message.edit_text("Введите текст для рассылки: ", reply_markup=back_menu())
#     await state.set_state(BroadcastState.waiting_for_broadcast_text)
#     await callback.answer()
    
# @admin_router.callback_query(F.data == "settings")
# async def process_settings(callback: CallbackQuery):
#     await callback.message.edit_text("Доп. настройки:", reply_markup=back_menu())
#     await callback.answer()
    
# @admin_router.message(BroadcastState.waiting_for_broadcast_text)
# async def handle_broadcast_text(message: Message, state: FSMContext, bot: Bot):
#     broadcast_text = message.text
#     db = async_session()
#     users_list = db.query(User).filter(User.active == True).all()
#     count = 0
#     for user in users_list:
#         try:
#             await bot.send_message(user.telegram_id, broadcast_text)
#             count += 1
#         except Exception as e:
#             print(f"Не удалось отправить сообщение {user.telegram_id}: {e}")
            
#     new_broadcast = Broadcast(message=broadcast_text)
#     db.add(new_broadcast)
#     db.commit()
#     db.close()
#     await message.answer(f"Рассылка завершена! Сообщение отправлено {count} пользователям.")
#     await state.clear()