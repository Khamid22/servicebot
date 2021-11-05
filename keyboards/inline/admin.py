from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Master_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Clients 👤', callback_data='clients')
        ],
        [
            InlineKeyboardButton(text='Web-Mode 🖥', callback_data='web-mode')
        ],
    ],
)
