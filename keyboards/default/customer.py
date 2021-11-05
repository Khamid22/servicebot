from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

customer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Car maintenance 🚗"),
        ],

        [
            KeyboardButton(text="✍🏻 Feedback"),
            KeyboardButton(text="🗣 Complain letter"),
        ],

        [
            KeyboardButton(text="Back"),
        ],
    ], resize_keyboard=True
)