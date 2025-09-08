from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers_user import router
from app.database.models import async_main

import os
import asyncio

load_dotenv()
TG_TOKEN = int(os.getenv('TG_TOKEN',0))

async def main():
    await async_main()
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        
