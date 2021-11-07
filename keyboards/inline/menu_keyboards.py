from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main-menu keyboards
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👨🏼‍💼Customer', callback_data='customer'),
            InlineKeyboardButton(text='👨🏻‍🔧Master', callback_data='master'),
        ],
        [
            InlineKeyboardButton(text='📍Local Services',
                                 url='https://www.google.com/maps/search/car+service/@40.7793108,72.3517614,14.08z')
        ],
        [
            InlineKeyboardButton(text='🖇Share',
                                 switch_inline_query='\n 🚗🛠 Reach out car services within a second!🤩🤩')
        ]
    ],
)


def reject(customer_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Reject ❌', callback_data=f'reject#{customer_id}')
            ]
        ]
    )
    return keyboard


