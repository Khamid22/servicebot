from aiogram.dispatcher.filters.state import StatesGroup, State


class Letter(StatesGroup):
    feedback = State()
    complain = State()