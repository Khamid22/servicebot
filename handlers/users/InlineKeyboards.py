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


# Done button appears after customer fills the required data and adds the customer to database
@dp.callback_query_handler(text="done", state=personalData.confirm)
async def cancel_buying(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer(
        "Your inquiry has been successfully submitted✅.\nPlease wait for master's response, he will get in touch within a minute⏰. ",
        cache_time=60, show_alert=True)

    data = await state.get_data()
    name = data.get("name")
    car = data.get("car")
    phone_number = data.get("phone")
    service = data.get("service")
    date = data.get("date")
    await db.apply("insert into customers(name, car, phone_number, service, date, user_id) values (%s, %s, %s, %s, %s, %s)",
                   (name, car, phone_number, service, date, user_id))
    await state.finish()


# Cancel button appears after customer fills the required data
@dp.callback_query_handler(text="cancel", state=personalData.confirm)
async def cancel_buying(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer("The inquiry has been canceled ❌!", cache_time=60, show_alert=True)

    await state.finish()
