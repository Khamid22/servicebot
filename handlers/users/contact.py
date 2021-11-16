from keyboards.default.start_keyboard import back
from keyboards.inline.menu_keyboards import categoryMenu
from loader import dp, Database as db, bot
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
import time

from states.mainmenu import mainmenu


# Access to have a direct contact with masters
@dp.callback_query_handler(text="contact", state=mainmenu.main_menu)
async def available_masters(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await call.message.answer("Available admins: ", reply_markup=back)
    masters = await db.all_masters()
    photo_url = "https://th.bing.com/th/id/R.bb0e37e58eb152721e86903df9056918?rik=%2fzTAWcxxEt2r9Q&pid=ImgRaw&r=0"
    for master in masters:
        master_id = master.get("admin_id")
        name = master.get("full_name")
        number = master.get("phone_number")
        experience = master.get("Work_Experience")
        service = master.get("ServiceName")
        location = master.get("Location")

        msg = f"Master ID: {master_id}\n"
        msg += f"Name: {name}\n"
        msg += f"Number: {number}\n"
        msg += f"Experience: {experience}\n"
        msg += f"Workshop: {service}\n"
        msg += f"Location: {location}"
        time.sleep(0.8)
        await call.message.answer_photo(photo_url, msg)
    await state.finish()


@dp.message_handler(text="Back⏪", state="*")
async def return_back(message: Message, state: FSMContext):
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
                "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "
    customerID = message.from_user.id
    await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                  f"Welcome {message.from_user.full_name}\n</b>"
                                                  "  \n"
                                                  "<i>The customer mode is activated </i>",
                               reply_markup=categoryMenu)
    await mainmenu.main_menu.set()
