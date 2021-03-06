from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main-menu keyboards
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Car Service ๐", callback_data="fix"),
        ],

        [
            InlineKeyboardButton(text="โ๐ป Feedback", callback_data='feedback'),
            InlineKeyboardButton(text="โ๏ธ Contact", callback_data='contact'),
        ],

        [
            InlineKeyboardButton(text='๐Local Services',
                                 url='https://www.google.com/maps/search/car+service/@40.7793108,72.3517614,14.08z'),
            InlineKeyboardButton(text='๐Share',
                                 switch_inline_query='\n ๐๐  Reach out car services within a second!๐คฉ๐คฉ'),
        ],
        [

            InlineKeyboardButton(text='๐ฐ About us', callback_data='abouts'),
        ],
        [
            InlineKeyboardButton(text='Delete Account ๐', callback_data='delete'),
        ]
    ],
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Backโช", callback_data='back'),
        ],
    ]
)


