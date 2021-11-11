from aiogram.dispatcher.filters.state import StatesGroup, State


class mainmenu(StatesGroup):
    register = State()
    main_menu = State()
