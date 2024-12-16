from aiogram import Dispatcher
from handlers import start, register


def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(register.router)