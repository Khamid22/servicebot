from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back⏪"),
        ],
    ], resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cancel")
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)