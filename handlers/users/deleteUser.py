from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline.Confrim import answer
from states.delete import master
from states.mainmenu import mainmenu

from keyboards.inline.menu_keyboards import categoryMenu
from loader import dp, Database as db


@dp.callback_query_handler(text='delete', state=mainmenu.main_menu)
async def delete_account(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>🚮 DO YOU REALLY WANT TO DELETE YOUR ACCOUNT?</b>"
                              "\n    \n"
                              "<i>CHANGES ARE IRREVERSIBLE AND ALL YOUR DATA WILL BE DELETED ❗️</i>",
                              reply_markup=answer)
    await call.answer(cache_time=60)
    await master.delete.set()


# Deletes user's account after receiving the confirmation
@dp.callback_query_handler(text='yes', state=master.delete)
async def confirm(call: CallbackQuery, state: FSMContext):
    customer_id = call.from_user.id
    await call.message.delete()
    await db.delete_user(customer_id)
    await call.message.answer("Your account has been deleted, thank you for your using our service.")
    await call.answer(cache_time=60)
    await state.finish()


# User cancel the process and gets back to the main menu
@dp.callback_query_handler(text='cancel', state=master.delete)
async def cancels(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
                "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "
    customerID = call.from_user.id

    await call.message.answer_photo(photo_url, caption='<i>The customer mode has been activated ✅</i>'
                                                  f'\n   \n'
                                                  f'<b>Customer ID: {customerID}</b>', reply_markup=categoryMenu)
    await mainmenu.main_menu.set()
