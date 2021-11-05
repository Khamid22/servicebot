from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.customers import personalData

from keyboards.inline.menu_keyboards import services, categoryMenu
from loader import dp, Database as db
from states.customers import personalData


@dp.callback_query_handler(text_contains="customer")
async def user(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Available services: ', reply_markup=services)


@dp.callback_query_handler(text="back")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('What service do you want to have💬: ', reply_markup=categoryMenu)


