from aiogram.types import CallbackQuery, Message

from keyboards.inline.menu_keyboards import categoryMenu, back
from loader import dp, bot
from states.feedback import Letter
from states.mainmenu import mainmenu
from aiogram.dispatcher import FSMContext

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg"


# Provides proper information about the bot ----About Us keyboard ----
@dp.callback_query_handler(text="abouts", state=mainmenu.main_menu)
async def about_us(call: CallbackQuery, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await call.message.answer(
        "Welcome dear users 🙂 \n     \nThis bot was created to help you get an instant car service within a minute. "
        "Here is a list of commands and short guidance about using this bot😁😁.\n     \n/start - starts the bot\n    "
        " \nCustomer👨🏼‍💼 - for those who need a master's help\n      \nMaster👨🏻‍🔧 - for master seeking more "
        "clients\n     \nLocalServices📍 - depicts nearby available car services according to your current "
        "location.\n     \nAfter pressing a customer button, you will be responsible to fill out all the necessary "
        "information you are asked for so as to get as faster response as possible.📨\n     \nFor any bugs and "
        "feedback, feel free to contact at @Pythonista_77 or @DeveloperTimurbek👨🏻‍💻💬.",
        reply_markup=back)
    await state.finish()


# Get's back to main menu (back button)
@dp.callback_query_handler(text='back', state='*')
async def back_menu(call: CallbackQuery, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    customerID = call.from_user.id
    await call.message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                       f"Welcome {call.from_user.full_name}\n</b>"
                                                       "  \n"
                                                       "<i>The customer mode is activated </i>",
                                    reply_markup=categoryMenu)
    await mainmenu.main_menu.set()


# customer can write feedback about service they had and the bot sends it to he specific group
@dp.callback_query_handler(text='feedback', state='*')
async def feedbacks(call: CallbackQuery, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await call.message.answer("""<b>You can write your feedback about the quality of master's work here: </b> \n"""
                              f"   \n <i>Customer ID: {call.from_user.id}</i>", reply_markup=back)
    await Letter.feedback.set()


# The written message by customer will be sent to the group with the id number added below
@dp.message_handler(state=Letter.feedback)
async def copy_to_channel(message: Message, state: FSMContext):
    await message.forward(-1001782072708)  # ----- id of the channel ------
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
    await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                  f"Welcome {message.from_user.full_name}\n</b>"
                                                  "  \n"
                                                  "<i>The customer mode is activated </i>", reply_markup=categoryMenu)
    await mainmenu.main_menu.set()
