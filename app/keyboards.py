from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Student"),KeyboardButton(text="Teacher")],
], resize_keyboard=True)

teacher_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Dars qo'shish")],
        [KeyboardButton(text="Qatnashuvchilarni kuzatish"), KeyboardButton(text="Natijalarni kuzatish")]
    ],
    resize_keyboard=True
)

stdent_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Darslarni ko'rish"), KeyboardButton(text="Darslda qatnasish")],
        [KeyboardButton(text="Imtihonlarda qatnashish"), KeyboardButton(text="Natijalarni ko'rish")]
    ],
    resize_keyboard=True
)