from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.menu_keyboards import categoryMenu
from states.mainmenu import mainmenu
from keyboards.default.start_keyboard import register
from loader import dp, Database as db, bot

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


# Start command - runs the bot
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: Message, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    # Checks user from database while registering them according to their unique id and registers them
    is_customer = await db.check_user(message.from_user.id)
    if not is_customer:
        await message.answer(f"<b> 🚫 You are not fully registered yet!</b>\n"
                             f"    \n"
                             f"<i>❗️Please for registration, send my your contact on "
                             f"your telegram account!</i>", reply_markup=register)
        # Enters into state --register--
        await mainmenu.register.set()
    else:
        customerID = message.from_user.id
        # tries to delete all previous message if there are no messages to delete it will ignore
        try:
            await message.delete()
            chat_id = message.chat.id
            message_id = message.message_id
            for i in range(message_id - 1, 100, -1):
                await bot.delete_message(chat_id=chat_id, message_id=i)
        except:
            pass
        # If user already exists in database, it will not register again
        await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                      f"Welcome {message.from_user.full_name}\n</b>"
                                                      "  \n"
                                                      "<i>The customer mode is activated </i>",
                                   reply_markup=categoryMenu)
        await mainmenu.main_menu.set()


# If user have not been found in the database, bot requires a phone number from the user and adds him/her to the
# database
@dp.message_handler(content_types=["contact"], state=mainmenu.register)
async def get_contact(message: Message, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    customerID = message.from_user.id
    # Inserting the phone number and user_id to the new database called 'users'
    await db.apply("insert into users(phone_number, chat_id) values (%s, %s)", (str(message.contact.phone_number),
                                                                                customerID))
    await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                  f"Welcome {message.from_user.full_name}\n</b>"
                                                  "  \n"
                                                  "<i>The customer mode is activated </i>", reply_markup=categoryMenu)
    await mainmenu.main_menu.set()
