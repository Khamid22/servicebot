from aiogram.types import CallbackQuery
from keyboards.inline.menu_keyboards import services, categoryMenu
from loader import dp


@dp.callback_query_handler(text_contains="customer")
async def user(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Available services: ', reply_markup=services)


@dp.callback_query_handler(text="back")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('What service do you want to have💬: ', reply_markup=categoryMenu)


@dp.callback_query_handler(text="done")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer(
        "Your inquiry has been successfully submitted✅.\nPlease wait for master's response, he will get in touch within a minute⏰. ",
        cache_time=60, show_alert=True)


# Cancel button appears after customer fills the required data
@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer("The inquiry has been canceled ❌!", cache_time=60, show_alert=True)
