from aiogram.types import CallbackQuery, Message

from keyboards.default.customer import customer
from keyboards.default.start_keyboard import menuStart
from keyboards.inline.menu_keyboards import services
from loader import dp


@dp.callback_query_handler(text_contains="customer")
async def user(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('The customer mode has been activated ✅', reply_markup=customer)
    await call.message.answer('Available services: ', reply_markup=services)


@dp.message_handler(text_contains='back')
async def back(msg: Message):
    await msg.delete()
    await msg.answer("tip: fill out every required spaces precisely in order to receive quick responses",
                     reply_markup=menuStart)

