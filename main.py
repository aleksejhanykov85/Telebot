import asyncio
from aiogram import Bot, Dispatcher
from config import TG_TOKEN

from app.handlers import router
from app.database.models import async_main

async def main():
    await async_main()
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        
