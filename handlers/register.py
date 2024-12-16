from aiogram import Router, F
from aiogram.types import Message
from services.users import add_user
from aiogram.types import ReplyKeyboardRemove

router = Router()


@router.message(F.text == "Teacher")
async def cmd_check_teacher(message: Message):
    await add_user(
        user_id=message.from_user.id,
        fullname=message.from_user.full_name,
        is_teacher=True
    )
    await message.answer("Ustoz sifatida ro'yhatdan o'tdingiz !", reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "Student")
async def cmd_check_student(message: Message):
    await add_user(
        user_id=message.from_user.id,
        fullname=message.from_user.full_name,
        is_student=True
    )

    await message.answer("Student sifatida ro'yhatdan o'tdingiz !", reply_markup=ReplyKeyboardRemove())
