from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.menu_keyboards import categoryMenu
from states.mainmenu import mainmenu
from keyboards.default.start_keyboard import register
from loader import dp, Database as db, bot

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: Message, state: FSMContext):
    try:
        chat_id = message.chat.id
        message_id = message.message_id - 1
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass
    chat_id = message.from_user.id
    is_customer = await db.check_user(message.from_user.id)
    if not is_customer:
        await message.delete()
        await message.answer(f"<b> 🚫 You are not fully registered yet!</b>\n"
                             f"    \n"
                             f"<i>❗️Please for registration, send my your contact on "
                             f"your telegram account!</i>", reply_markup=register)
        await mainmenu.register.set()
    else:
        customerID = message.from_user.id
        await message.delete()
        await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                      f"Welcome {message.from_user.full_name}\n</b>"
                                                      "  \n"
                                                      "<i>The customer mode is activated </i>", reply_markup=categoryMenu)
        await mainmenu.main_menu.set()


@dp.message_handler(content_types=["contact"], state=mainmenu.register)
async def get_contact(message: Message, state: FSMContext):
    try:
        chat_id = message.chat.id
        message_id = message.message_id - 1
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass
    customerID = message.from_user.id
    await db.apply("insert into users(phone_number, chat_id) values (%s, %s)", (str(message.contact.phone_number),
                                                                            customerID))
    await message.delete()
    await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                  f"Welcome {message.from_user.full_name}\n</b>"
                                                  "  \n"
                                                  "<i>The customer mode is activated </i>", reply_markup=categoryMenu)
    await mainmenu.main_menu.set()
