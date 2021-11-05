from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Available number of services for the customer
service_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="tuning", callback_data="tuning"),
            InlineKeyboardButton(text="cruise control", callback_data="cruise control")
        ],
        [
            InlineKeyboardButton(text="repairing motor", callback_data="repairing motor"),
            InlineKeyboardButton(text="balancing tiers", callback_data="balancing tiers")
        ],

        [

        ]

    ]
)


# setting up date and time for the customer's arrival
date = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Monday, 9:00-18:00", callback_data="Monday, 9:00-18:00"),
            InlineKeyboardButton(text="Tuesday, 11:00-18:00", callback_data="Tuesday, 11:00-18:00")
        ],

        [
            InlineKeyboardButton(text="Wednesday, 9:00-16:00", callback_data="Wednesday, 9:00-16:00"),
            InlineKeyboardButton(text="Thursday, 10:00-18:00", callback_data="Thursday, 10:00-18:00"),
        ],
        [
            InlineKeyboardButton(text="Friday, 10:00-18:00", callback_data="Friday, 10:00-18:00"),
            InlineKeyboardButton(text="Saturday, 9:00-13:00", callback_data="Saturday, 9:00-13:00"),
        ],
        [
            InlineKeyboardButton(text='Sunday, 10:00-17:00', callback_data='Sunday, 10:00-17:00')
        ]
    ]
)

options = InlineKeyboardMarkup(row_width=2)
done = InlineKeyboardButton(text='Done ✅', callback_data='done')
options.insert(done)
done = InlineKeyboardButton(text='Cancel ❌ ', callback_data='cancel')
options.insert(done)