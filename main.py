import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from tortoise import Tortoise
from config import init_db
from handlers.start import router  # start.py dan routerni import qilamiz


async def main():
    await init_db()
    try:
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()

        # start.py ichidagi routerni ro‘yxatdan o‘tkazamiz
        dp.include_router(router)

        # Pollingni boshlaymiz
        await dp.start_polling(bot)
    finally:
        await Tortoise.close_connections()


if __name__ == '__main__':
    asyncio.run(main())


