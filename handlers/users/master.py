from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.default.start_keyboard import back
from keyboards.inline.admin import Master_panel
from keyboards.inline.menu_keyboards import categoryMenu
from keyboards.default.admin_panel import admin_menu

from states.Master import admin_panel

from loader import dp



# Asks the password for master's panel
@dp.callback_query_handler(text='master')
async def master(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Please enter the password: ')
    await admin_panel.secret_key.set()


# After entering the password, admin's panel shows up
@dp.message_handler(state=admin_panel.secret_key)
async def password(message: Message, state: FSMContext):
    secret_key = message.text
    pass_key = "master007"
    if secret_key == pass_key:
        await message.answer('Welcome dear master!', reply_markup=admin_menu)
        await message.answer('Master-Panel Control👨🏻‍🔧:', reply_markup=Master_panel)
        # Manipulates reserved list from customers

            # gets back to menu
    elif secret_key == 'Back⏪':
        await message.delete()
        await message.answer("What service do you want to have💬:", reply_markup=categoryMenu)
        await state.finish()
    else:
        await message.delete()
        await message.answer('Invalid password,try again', reply_markup=back)


@dp.message_handler(text="Back⏪")
async def about_us(msg: Message):
    await msg.delete()
    await msg.answer("What service do you want to have💬: ", reply_markup=categoryMenu)
