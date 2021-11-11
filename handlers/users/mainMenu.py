from aiogram.types import CallbackQuery, Message
from keyboards.inline.menu_keyboards import categoryMenu, back
from loader import dp, bot
from states.feedback import Letter
from states.mainmenu import mainmenu
from aiogram.dispatcher import FSMContext

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg"


# About US - keyboard in the main panel
@dp.callback_query_handler(text="abouts", state=mainmenu.main_menu)
async def about_us(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
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


@dp.callback_query_handler(text_contains='back', state='*')
async def back_menu(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id - 1
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass
    customerID = call.from_user.id
    await call.message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                        f"Welcome {call.from_user.full_name}\n</b>"
                                                        "  \n"
                                                        "<i>The customer mode is activated </i>", reply_markup=categoryMenu)
    await mainmenu.main_menu.set()


@dp.callback_query_handler(text_contains='feedback', state=mainmenu.main_menu)
async def feedbacks(call: CallbackQuery, state: FSMContext):
    await Letter.feedback.set()


@dp.message_handler(state=Letter.feedback)
async def copy_to_channel(message: Message, state: FSMContext):
    await message.copy_to(-1001782072708)
    await state.finish()
