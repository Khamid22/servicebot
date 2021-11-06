from aiogram.dispatcher import FSMContext
from aiogram.types import Message, message

from keyboards.default.start_keyboard import back, menuStart
from keyboards.inline.menu_keyboards import reject
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
        await message.answer("Try again later.", reply_markup=menuStart)
        await state.finish()
    else:
        await message.delete()
        await message.answer('Invalid password,try again', reply_markup=back)


@dp.message_handler(text="Back⏪", state="*")
async def about_us(msg: Message, state: FSMContext):
    await msg.delete()
    await msg.answer("Consider leaving your feedbacks!", reply_markup=menuStart)
    await state.finish()


@dp.message_handler(text="Clients 👤", state=admin_panel.reservations)
async def show_customer(message: Message):
    await message.delete()
    customers = await db.all_customers()
    for customer in customers:
        customer_id = customer.get("user_id")
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

        await message.answer(msg, reply_markup=reject(customer_id))


@dp.callback_query_handler(text_contains='reject', state='*')
async def reject_customer(call: CallbackQuery, state=FSMContext):
    customer_id = call.data.split('#')[1]

    await call.message.delete()
    await db.delete_customer(customer_id)
    await call.answer("Customer rejected successfully", cache_time=60, show_alert=True)
    try:
        await dp.bot.send_message(chat_id=customer_id, text="Sizi master reject qildi")

    except:
        await call.message.answer(f"Can't notify the {customer_id}")
