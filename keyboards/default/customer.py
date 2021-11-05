from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

customer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗣 Complain letter"),
        ],

        [
            KeyboardButton(text="✍🏻 Feedback")
        ],

        [
            KeyboardButton(text="Back"),
        ],
    ], resize_keyboard=True
)