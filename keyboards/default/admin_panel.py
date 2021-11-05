from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back⏪"),
        ],
    ], resize_keyboard=True
)