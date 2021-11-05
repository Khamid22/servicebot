from aiogram.dispatcher.filters.state import StatesGroup, State


class personalData(StatesGroup):
    full_name = State()
    car = State()
    phone_number = State()
    service_type = State()
    date = State()