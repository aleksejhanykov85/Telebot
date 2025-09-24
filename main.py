from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers_user import userr
from app.handlers_ai import air
from app.reminder import reminderr
from app.admin import adminr
from app.database.models import async_user
from app.database.recept_table import async_rec_and_ings


import logging
import os
import asyncio

logging.basicConfig(level=logging.INFO)

load_dotenv()
TG_TOKEN = (os.getenv('TG_TOKEN',0))

async def main():
    await async_user()
    await async_rec_and_ings()
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_routers(userr,air,
                      reminderr,
                      adminr)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        
