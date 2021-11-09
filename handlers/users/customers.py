from keyboards.default.start_keyboard import cancel
from keyboards.inline.customer_menu import menu
from keyboards.inline.customers import service_menu, date, options, car_category
from keyboards.inline.menu_keyboards import categoryMenu
from loader import dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.customers import personalData
from loader import Database as db

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


@dp.callback_query_handler(text_contains='fix')
async def register_user(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Enter your full name🧑🏼‍💼👨🏼‍💼</b>\n"
                              "<i>Ex: Mukhammadjonov Khamidullo", reply_markup=cancel)
    await personalData.full_name.set()


@dp.message_handler(state=personalData.full_name)
async def answer_fullname(message: Message, state: FSMContext):
    name = message.text
    if name == 'Cancel':
        await message.delete()

        await message.answer_photo(photo_url, caption="The process has been canceled❌ ", reply_markup=categoryMenu)
        await state.finish()
    else:
        await state.update_data(
            {"name": name}
        )
        await message.answer("Car category 🚗?: ", reply_markup=car_category)

        await personalData.car.set()


@dp.callback_query_handler(state=personalData.car)
async def answer_car(call:CallbackQuery, state: FSMContext):
    car = call.data
    if car == 'Cancel':
        await call.message.delete()
        await call.message.answer("The process has been canceled❌ ", reply_markup=categoryMenu)
        await call.answer(cache_time=60)
        await state.finish()
    else:
        await state.update_data(
            {"car": car}
        )
        await call.message.answer("<b>Your phone number ☎?: </b> \n"
                                  "<i>Ex: +998(xx)-xxx-xx-xx", reply_markup=ReplyKeyboardRemove(True))
        await personalData.phone_number.set()


@dp.message_handler(state=personalData.phone_number)
async def contact(message: Message, state: FSMContext):
    try:
        phone_number = int(message.text)
        if phone_number == 'Cancel':
            await message.delete()
            await message.answer("The process has been canceled❌ ", reply_markup=categoryMenu)
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
        await call.message.answer("The process has been canceled❌ ", reply_markup=categoryMenu)
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
        await call.message.answer("The process has been canceled❌ ", reply_markup=categoryMenu)
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
    await call.message.edit_reply_markup(reply_markup=menu)
    user_id = call.from_user.id
    await call.answer(
        "Your inquiry has been successfully submitted✅.\nPlease wait for master's response, he will get in touch "
        "within a minute⏰. ",
        cache_time=60, show_alert=True)
    data = await state.get_data()
    name = data.get("name")
    car = data.get("car")
    phone_number = data.get("phone")
    service = data.get("service")
    date = data.get("date")
    await db.apply(
        "insert into customers(name, car, phone_number, service, date, user_id) values (%s, %s, %s, %s, %s, %s)",
        (name, car, phone_number, service, date, user_id))
    await state.finish()


# Cancel button appears after customer fills the required data
@dp.callback_query_handler(text="cancel", state=personalData.confirm)
async def cancel_sending(call: CallbackQuery, state: FSMContext):
    await call.message.edit_caption(reply_markup=menu)
    await call.answer("The inquiry has been canceled ❌!", cache_time=60, show_alert=True)
    await state.finish()


