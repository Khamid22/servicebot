from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import Database as db


#Car category
async def cars():
    keyboard = InlineKeyboardMarkup(row_width=3)
    car_categories = await db.list_of_cars()
    for car in car_categories:
        keyboard.insert(InlineKeyboardButton(car.get("car_category"), callback_data=f"settings_car{car.get('id')}"))
    return keyboard


# Available number of services for the customer
async def services_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    list_services = await db.list_of_services()
    for service in list_services:
        keyboard.insert(InlineKeyboardButton(service.get("name"), callback_data=f"settings_service{service.get('id')}"))
    return keyboard


# setting up date and time for the customer's arrival
async def dates():
    keyboard = InlineKeyboardMarkup(row_width=3)
    week = await db.list_of_days()
    for day in week:
        keyboard.insert(InlineKeyboardButton(day.get("date/time"), callback_data=f"settings_date{day.get('id')}"))
    return keyboard

options = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Done ✅', callback_data='done'),
            InlineKeyboardButton(text='Cancel ❌ ', callback_data='cancel'),
        ],
    ],
)
