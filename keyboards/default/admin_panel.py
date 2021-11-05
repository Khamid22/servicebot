from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Clients 👤"),
        ],
        [
            KeyboardButton(text='Complains 🤬'),
            KeyboardButton(text='Feedbacks 💬'),
        ],
        [
            KeyboardButton(text="Web-Mode 🖥")
        ],

        [
            KeyboardButton(text="Back⏪"),
        ],
    ], resize_keyboard=True
)