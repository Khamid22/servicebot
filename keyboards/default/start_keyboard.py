from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛠 Services'),
            KeyboardButton(text='🔰 About us')
        ]
    ], resize_keyboard=True
)

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