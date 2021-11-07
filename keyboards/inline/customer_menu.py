from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Car maintenance 🚗", callback_data="fix"),
        ],

        [
            InlineKeyboardButton(text="✍🏻 Feedback", callback_data='feedback'),
            InlineKeyboardButton(text="🗣 Complain letter", callback_data='complain'),
        ],

        [
            InlineKeyboardButton(text="🔙 Back", callback_data="back"),
        ],
    ]
)
