from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu_keyboards import categoryMenu
from loader import dp

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


@dp.message_handler(commands=['reset'], state='*')
async def bot_start(message: Message, state: FSMContext):
    chat_id = message.from_user.id
    await message.delete()
    await message.answer_photo(photo_url, caption=f"Welcome Mr {message.from_user.full_name}!\n"
                                                  'What service do you want to have💬:', reply_markup=categoryMenu)
    await message.answer("<i> All the previous actions have been deleted</i>❗️", reply_markup=ReplyKeyboardRemove(True))
    await state.finish()