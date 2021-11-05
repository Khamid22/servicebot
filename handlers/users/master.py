from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default.start_keyboard import back
from keyboards.inline.menu_keyboards import categoryMenu, reject
from states.Master import admin_panel
from aiogram.types import CallbackQuery
from keyboards.default.admin_panel import admin_menu
from loader import dp, Database as db


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
        await message.answer('The master mode has been activated 👨🏻‍🔧✅: ', reply_markup=admin_menu)
        await admin_panel.reservations.set()
        # Manipulates reserved list from customers

        # gets back to menu
    elif secret_key == 'Back⏪':
        await message.delete()
        await message.answer("Have a nice day sir 😎", reply_markup=categoryMenu)
        await state.finish()
    else:
        await message.delete()
        await message.answer('Invalid password,try again', reply_markup=back)


@dp.message_handler(text="Back⏪")
async def about_us(msg: Message):
    await msg.delete()
    await msg.answer("What service do you want to have💬: ")


@dp.message_handler(text="Clients 👤", state=admin_panel.reservations)
async def show_customer(message: Message):
    await message.delete()
    customers = await db.all_customers()
    for customer in customers:
        name = customer.get("name")
        car = customer.get("car")
        phone_number = customer.get("phone_number")
        service2 = customer.get("service")
        date2 = customer.get("date")

        msg = "Customer's info📝: \n"
        msg += f"Client👤- {name}\n"
        msg += f"Car🚗 - {car}\n"
        msg += f"Phone-number📞 - {phone_number}\n"
        msg += f"Service🛠 - {service2}\n"
        msg += f"Date/time⏱ - {date2}"

        await message.answer(msg, reply_markup=reject)


@dp.callback_query_handler(text_contains = 'reject', state='*')
async def reject(call:CallbackQuery, state=FSMContext):
