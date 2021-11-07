from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)


admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Clients 👤", callback_data='clients'),
        ],
        [
            InlineKeyboardButton(text='Complains 🤬', callback_data='complains'),
            InlineKeyboardButton(text='Feedbacks 💬', callback_data='feedback'),
        ],
        [
            InlineKeyboardButton(text="Web-Mode 🖥", callback_data='Web-mode'),
        ],

        [
            InlineKeyboardButton(text="Back ⏪", callback_data='back'),
        ],
    ]
)
get_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Back", callback_data='return'),
        ],
    ],
)
