from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main-menu keyboards
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Car Service 🚗", callback_data="fix"),
        ],

        [
            InlineKeyboardButton(text="✍🏻 Feedback", callback_data='feedback'),
            InlineKeyboardButton(text="☎️ Contact", callback_data='contact'),
        ],

        [
            InlineKeyboardButton(text='📍Local Services',
                                 url='https://www.google.com/maps/search/car+service/@40.7793108,72.3517614,14.08z'),
            InlineKeyboardButton(text='🖇Share',
                                 switch_inline_query='\n 🚗🛠 Reach out car services within a second!🤩🤩'),
        ],
        [

            InlineKeyboardButton(text='🔰 About us', callback_data='abouts'),
        ],
        [
            InlineKeyboardButton(text='Delete Account 🗑', callback_data='delete'),
        ]
    ],
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back⏪", callback_data='back'),
        ],
    ]
)


