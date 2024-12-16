# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.filters import Command
# from models.user import User
# from app.keyboards import button
# from aiogram import Router, F
# from aiogram.types import Message
# from services.users import add_user
# from aiogram.types import ReplyKeyboardRemove
# router = Router()
#
#
# @router.message(Command('start'))
# async def cmd_start(message: Message):
#     user = await User.get_or_none(user_id=message.from_user.id)
#     if not user:
#         await message.answer("Assalomu Aleykum Xurmatli foydalanuvchi.\nRo'yhatdan o'tish uchun tanlang:",
#                          reply_markup=button)
#     else:
#         await message.answer("Sizda ro'yhatdan o'tgansiz.")
#
# @router.message(F.text == "Teacher")
# async def cmd_check_teacher(message: Message):
#     await add_user(
#         user_id=message.from_user.id,
#         full_name=message.from_user.full_name,
#         is_teacher=True
#     )
#     await message.answer("Ustoz sifatida ro'yhatdan o'tdingiz !", reply_markup=ReplyKeyboardRemove())
#
#
# @router.message(F.text == "Student")
# async def cmd_check_student(message: Message):
#     await add_user(
#         user_id=message.from_user.id,
#         full_name=message.from_user.full_name,
#         is_student=True
#     )
#
#     await message.answer("Student sifatida ro'yhatdan o'tdingiz !", reply_markup=ReplyKeyboardRemove())

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command
from models.user import User
from services.users import add_user,create_lesson
from app.keyboards import button,teacher_keyboard,stdent_keyboard
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from models.user import User
from models.user import Lesson


router = Router()



@router.message(Command('start'))
async def cmd_start(message: Message):
    # Foydalanuvchini bazadan tekshirish
    user = await User.get_or_none(user_id=message.from_user.id)
    if not user:
        await message.answer(
            "Assalomu Aleykum Xurmatli foydalanuvchi.\nRo'yhatdan o'tish uchun tanlang:",
            reply_markup=button
        )
    else:
        await message.answer("Siz allaqachon ro'yhatdan o'tgansiz.")


@router.message(F.text == "Teacher")
async def cmd_check_teacher(message: Message):
    try:
        # Foydalanuvchi ustoz sifatida ro‘yxatdan o‘tganligini tekshirish
        user = await User.get_or_none(user_id=message.from_user.id)
        if user and user.is_teacher:
            await message.answer("Siz allaqachon ustoz sifatida ro'yhatdan o'tgansiz.", reply_markup=teacher_keyboard)
            return

        # Foydalanuvchini ustoz sifatida ro'yxatdan o'tkazish
        await add_user(
            user_id=message.from_user.id,
            full_name=message.from_user.full_name,
            is_teacher=True
        )
        await message.answer("Ustoz sifatida ro'yhatdan o'tdingiz!", reply_markup=teacher_keyboard)
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {str(e)}")


@router.message(F.text == "Student")
async def cmd_check_student(message: Message):
    try:
        # Foydalanuvchi talaba sifatida ro‘yxatdan o‘tganligini tekshirish
        user = await User.get_or_none(user_id=message.from_user.id)
        if user and user.is_student:
            await message.answer("Siz allaqachon talaba sifatida ro'yhatdan o'tgansiz.",
                                 reply_markup=stdent_keyboard)
            return

        # Foydalanuvchini talaba sifatida ro'yxatdan o'tkazish
        await add_user(
            user_id=message.from_user.id,
            full_name=message.from_user.full_name,
            is_student=True
        )
        await message.answer("Talaba sifatida ro'yhatdan o'tdingiz!", reply_markup=stdent_keyboard)
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {str(e)}")
################################################################################################################


# router = Router()

class LessonState(StatesGroup):
    title = State()
    description = State()



@router.message(F.text == "Dars qo'shish")
async def cmd_add_lesson(message: Message, state: FSMContext):
    user = await User.get_or_none(user_id=message.from_user.id)
    if not user or not user.is_teacher:
        await message.answer("Siz ustoz sifatida ro'yhatdan o'tmagansiz!")
        return

    await state.set_state(LessonState.title)
    await message.answer("Darsning nomini kiriting:")

@router.message(LessonState.title)
async def set_lesson_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(LessonState.description)
    await message.answer("Darsning tavsifini kiriting:")

@router.message(LessonState.description)
async def set_lesson_description(message: Message, state: FSMContext):
    # Davlatdan ma'lumotlarni olish
    data = await state.get_data()
    title = data['title']
    description = message.text
    teacher_id = User.user_id

    # Darsni yaratish
    try:
        lesson = await create_lesson(title, description, teacher_id)
        await message.answer(f"Dars muvaffaqiyatli yaratildi!\nDars: {lesson.title}")
    except Exception as e:
        await message.answer(f"Darsni yaratishda xatolik yuz berdi: {str(e)}")

    # Davlatni tozalash
    await state.clear()

