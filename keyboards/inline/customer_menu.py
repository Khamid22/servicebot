from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Car maintenance 🚗", callback_data="fix"),
        ],

        [
            InlineKeyboardButton(text="✍🏻 Feedback", callback_data='feedback'),
            InlineKeyboardButton(text="☎️ Contact", callback_data='contact'),
        ],

        [
            InlineKeyboardButton(text="🔙 Back", callback_data="back"),
        ],
    ]
)
