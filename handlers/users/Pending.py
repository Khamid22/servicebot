from handlers.users.customers import photo_url
from keyboards.default.start_keyboard import back
from keyboards.inline.history import cancel
from keyboards.inline.menu_keyboards import categoryMenu
from loader import dp, Database as db, bot
from states.mainmenu import mainmenu
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="Pending", state=mainmenu.main_menu)
async def mydata(call: CallbackQuery, state: FSMContext):
    await call.message.answer("<b> Your reservations: </b>", reply_markup=back)
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass

    data = await db.get_customer_datas(user_id=call.from_user.id)
    customer_id = data.get("user_id")
    name = data.get("name")
    number = data.get("phone_number")
    car = data.get("car")
    service = data.get("service")
    date = data.get("date")

    msg = f"<b>↪️  Reservation ↩️\n" \
          f"Customer ID: {customer_id}</b>  "
    msg += f"\n   \n"
    msg += f"Name: {name}\n"
    msg += f"Phone: {number}\n"
    msg += f"Car : {car}\n"
    msg += f"Service: {service}\n"
    msg += f"Date: {date}\n \n"
    msg += "<i>One of the available masters will respond you back, please be patient</i>"

    await call.message.answer(msg, reply_markup=cancel)
    await mainmenu.main_menu.set()


@dp.callback_query_handler(text="cancel", state=mainmenu.main_menu)
async def cancels_reservation(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    customer_id = call.from_user.id
    await db.cancel_reservation(customer_id)
    await call.answer("Your reservation has been canceled.", cache_time=60, show_alert=True)
    await call.message.answer_photo(photo_url, caption=f"<b>Customer ID : {customer_id}\n"
                                                       f"Welcome {call.from_user.full_name}\n</b>"
                                                       "  \n"
                                                       "<i>The customer mode is activated </i>",
                                    reply_markup=categoryMenu)
    await mainmenu.main_menu.set()
