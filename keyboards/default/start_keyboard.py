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
    ], resize_keyboard=True
)
phone = ReplyKeyboardMarkup(
    [[
        KeyboardButton(text="Send my number📞", request_contact=True),
    ]], resize_keyboard=True, one_time_keyboard=True
)