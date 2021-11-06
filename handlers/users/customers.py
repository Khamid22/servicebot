from keyboards.default.start_keyboard import menuStart, cancel
from keyboards.inline.customers import service_menu, date, options
from keyboards.inline.menu_keyboards import categoryMenu
from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.customers import personalData
from loader import Database as db


@dp.message_handler(text_contains='Car maintenance 🚗')
async def register_user(msg: Message):
    await msg.delete()
    await msg.answer("Enter your full name🧑🏼‍💼👨🏼‍💼", reply_markup=cancel)
    await personalData.full_name.set()


@dp.message_handler(state=personalData.full_name)
async def answer_fullname(message: Message, state: FSMContext):
    name = message.text
    if name == 'Cancel':
        await message.delete()
        await message.answer("The process has been canceled❌ ", reply_markup=menuStart)
        await state.finish()
    else:
        await state.update_data(
            {"name": name}
        )
        await message.answer("Car category 🚗?: ")

        await personalData.car.set()


@dp.message_handler(state=personalData.car)
async def answer_car(message: Message, state: FSMContext):
    car = message.text
    if car == 'Cancel':
        await message.delete()
        await message.answer("The process has been canceled❌ ", reply_markup=menuStart)
        await state.finish()
    else:
        await state.update_data(
            {"car": car}
        )
        await message.answer("Your phone number ☎?: ")
        await personalData.phone_number.set()


@dp.message_handler(state=personalData.phone_number)
async def contact(message: Message, state: FSMContext):
    try:
        phone_number = int(message.text)
        if phone_number == 'Cancel':
            await message.delete()
            await message.answer("The process has been canceled❌ ", reply_markup=menuStart)
            await state.finish()
        else:
            await state.update_data(
                {"phone": phone_number}
            )
            await message.answer("What service do you need🛠?: ", reply_markup=service_menu)
            await personalData.service_type.set()
    except ValueError:
        await message.answer("Please enter a valid phone number! ")

@dp.callback_query_handler(state=personalData.service_type)
async def answer_service(call: CallbackQuery, state: FSMContext):
    service_type = call.data
    if service_type == 'Cancel':
        await call.message.delete()
        await call.message.answer("The process has been canceled❌ ", reply_markup=menuStart)
        await state.finish()
    else:
        await state.update_data(
            {"service": service_type}
        )
        await call.message.answer("Choose appropriate time and date🕛: ", reply_markup=date)
        await personalData.date.set()


@dp.callback_query_handler(state=personalData.date)
async def answer_date(call: CallbackQuery, state: FSMContext):

    date1 = call.data
    if date1 == 'Cancel':
        await call.message.delete()
        await call.message.answer("The process has been canceled❌ ", reply_markup=menuStart)
        await state.finish()
    else:
        await state.update_data(
            {"date": date1}
        )

        data = await state.get_data()
        name = data.get("name")
        car = data.get("car")
        phone_number = data.get("phone")
        service2 = data.get("service")
        date2 = data.get("date")

        msg = "Customer's info📝: \n"
        msg += f"Client👤- {name}\n"
        msg += f"Car🚗 - {car}\n"
        msg += f"Phone-number📞 - {phone_number}\n"
        msg += f"Service🛠 - {service2}\n"
        msg += f"Date/time⏱ - {date2}"
        await call.message.answer(msg, reply_markup=options)

        await personalData.confirm.set()


@dp.callback_query_handler(text="done", state=personalData.confirm)
async def send_info(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    user_id = call.from_user.id
    await call.answer(
        "Your inquiry has been successfully submitted✅.\nPlease wait for master's response, he will get in touch "
        "within a minute⏰. ",
        cache_time=60, show_alert=True)
    await call.message.answer("Consider leaving your feedback!", reply_markup=menuStart)
    data = await state.get_data()
    name = data.get("name")
    car = data.get("car")
    phone_number = data.get("phone")
    service = data.get("service")
    date = data.get("date")
    await db.apply("insert into customers(name, car, phone_number, service, date, user_id) values (%s, %s, %s, %s, %s, %s)",
                   (name, car, phone_number, service, date, user_id))
    await state.finish()


# Cancel button appears after customer fills the required data
@dp.callback_query_handler(text="cancel", state=personalData.confirm)
async def cancel_sending(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer("The inquiry has been canceled ❌!", cache_time=60, show_alert=True)
    await call.message.answer("Consider leaving your feedback!", reply_markup=menuStart)

    await state.finish()

