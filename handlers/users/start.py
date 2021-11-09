from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from states.mainmenu import mainmenu
from keyboards.default.start_keyboard import register
from keyboards.inline.menu_keyboards import categoryMenu, back
from loader import dp, Database as db

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


@dp.message_handler(CommandStart())
async def bot_start(message: Message, state: FSMContext):
    chat_id = message.from_user.id
    await db.apply("insert into users(chat_id) values(%s)",
                   chat_id)
    await message.delete()
    await message.answer(f"<b> 🚫 You are not fully registered yet!</b>\n"
                         f"    \n"
                         f"<i>❗️Please for registration, send my your contact on "
                         f"your telegram account!</i>", reply_markup=register)
    await mainmenu.main_menu.set()


@dp.message_handler(content_types=["contact"], state=mainmenu.main_menu)
async def get_contact(message: Message, state: FSMContext):
    customerID = message.from_user.id
    await db.apply("insert into customers(phone_number, user_id) values (%s, %s)", (str(message.contact.phone_number),
                                                                                    customerID))
    await message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}</b>"
                                                  f"Welcome {message.from_user.full_name}"
                                                  "The customer mode is activated ", reply_markup=categoryMenu)


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

# # Customer's inline keyboard
# @dp.callback_query_handler(text="back", state=mainmenu.main_menu)
# async def about_us(call: CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await call.message.answer_photo(photo_url, caption="What service do you want to have💬:", reply_markup=categoryMenu)
#
#
# @dp.message_handler(text="Cancel", state='*')
# async def about_us(message: Message, state: FSMContext):
#     await message.delete()
#     photo_url = "https://www.onedealer.com/wp-content/uploads/2018/09/shutterstock_626286728-1.jpg"
#     customerID = message.from_user.id
#     await message.answer_photo(photo_url, caption='<i>The customer mode has been activated ✅</i>'
#                                                   f'\n   \n'
#                                                   f'<b>Customer ID: {customerID}</b>', reply_markup=menu)
#     await state.finish()
