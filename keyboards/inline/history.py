from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# keyboards for updating or setting new profile
cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cancel", callback_data='cancel'),
        ],
    ]
)