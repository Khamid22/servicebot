from keyboards.inline.menu_keyboards import back
from loader import dp, Database as db, bot
from aiogram.types import CallbackQuery
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
        for i in range(message_id - 1, 2, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    masters = await db.all_masters()
    for master in masters:
        master_id = master.get("admin_id")
        name = master.get("full_name")
        number = master.get("phone_number")
        experience = master.get("Work_Experience")
        service = master.get("ServiceName")
        location = master.get("Location")

        msg = f"👨🏻‍🔧 <b>Master ID: {master_id}</b>\n " \
              f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
        msg += f"<b>Name:</b> <i>{name}</i>\n"
        msg += f"<b>Number:</b> <i>{number}</i>\n"
        msg += f"<b>Experience:</b> <i>{experience}</i>\n"
        msg += f"<b>Workshop:</b> <i>{service}</i>\n"
        msg += f"<b>Location:</b> <i>{location}</i>"
        time.sleep(0.8)
        await call.message.answer(msg, reply_markup=back)
    await state.finish()

