from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Yes, I do ✅', callback_data='yes'),
            InlineKeyboardButton(text='Cancel ❌', callback_data='cancel'),
        ],
    ]
)

call = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Call", callback_data="call")
        ]
    ]
)