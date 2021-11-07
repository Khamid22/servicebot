from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu_keyboards import categoryMenu, back
from loader import dp, Database as db

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
                "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    chat_id = message.from_user.id
    await db.apply("insert into users(chat_id) values(%s)",
                   chat_id)
    await message.delete()
    await message.answer_photo(photo_url, caption=f"Welcome Mr {message.from_user.full_name}!\n"
                                                  'What service do you want to have💬:', reply_markup=categoryMenu)


@dp.callback_query_handler(text="abouts")
async def about_us(call: CallbackQuery):
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


@dp.callback_query_handler(text="back", state='*')
async def about_us(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo_url, caption="What service do you want to have💬:", reply_markup=categoryMenu)


@dp.callback_query_handler(text="cancel", state='*')
async def about_us(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer_photo(photo_url, caption="What service do you want to have💬:", reply_markup=categoryMenu)