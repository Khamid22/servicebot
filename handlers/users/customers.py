from keyboards.default.start_keyboard import cancel
from keyboards.inline.customers import service_menu, date, options, car_category
from keyboards.inline.menu_keyboards import categoryMenu, back
from loader import dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.customers import personalData
from states.mainmenu import mainmenu
from loader import Database as db, bot

photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
            "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg "


# ---- Car Service -----
@dp.callback_query_handler(text_contains='fix', state=mainmenu.main_menu)
async def register_user(call: CallbackQuery):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass

    await call.message.answer(f'<b>👤 Welcome, {call.from_user.full_name}</b>\n  \n'
                              f'<b>🚸 Step 1</b> of 5\n  \n'
                              f'<i>😊 Write your name here: </i>\n  \n'
                              f'<i>✍🏻 Example: Khamidullo</>', reply_markup=back)
    await personalData.full_name.set()


# Asks customers name and proceeds to the next question
@dp.message_handler(state=personalData.full_name)
async def answer_fullname(message: Message, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    name = message.text
    await state.update_data(
            {"name": name}
        )
    await message.answer(f'<b>🚸 Step 2</b> of 5\n  \n'
                         f'<i>😊 Select your car category </i>\n  \n', reply_markup=car_category)
    await personalData.car.set()


# asks customer what category of car does he/she drive
@dp.callback_query_handler(state=personalData.car)
async def answer_car(call: CallbackQuery, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    car = call.data
    await state.update_data(
            {"car": car}
    )
    await call.message.answer(f'<b>🚸 Step 3</b> of 5\n  \n'
                              f'<i>😊 Write your phone number here: </i>\n  \n'
                              f'<i>✍🏻 Example: +998(xx)-xxx-xx-xx</i>', reply_markup=back)
    await personalData.phone_number.set()


# asks customer his/her phone number
@dp.message_handler(state=personalData.phone_number)
async def contact(message: Message, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await message.delete()
        chat_id = message.chat.id
        message_id = message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    phone_number = message.text
    await state.update_data(
    {"phone": phone_number}
            )
    await message.answer(f'<b>🚸 Step 4</b> of 5\n  \n'
                              f'<i>😊 What service do you want?:  </i>\n  \n'
                              f'<i>✍🏻 Example: Cruise control</i>', reply_markup=service_menu)
    await personalData.service_type.set()

# asks what service to be provided
@dp.callback_query_handler(state=personalData.service_type)
async def answer_service(call: CallbackQuery, state: FSMContext):
    service_type = call.data
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await state.update_data(
            {"service": service_type}
        )

    await call.message.answer(f'<b>🚸 Step 5</b> of 5\n  \n'
                              f'<i>😊 Select appropriate date/time: </i>\n  \n'
                              f'<i>✍🏻 Example: Monday, 9:00-18:30</i>', reply_markup=date)
    await personalData.date.set()


# ask to choose appropriate date/time
@dp.callback_query_handler(state=personalData.date)
async def answer_date(call: CallbackQuery, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    date1 = call.data
    await state.update_data(
            {"date": date1}
        )
    # Collects all filled out information by the user in one place and waits for the user's confirmation
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


# if user confirms the data , it will be sent to the database where car master can get access to
@dp.callback_query_handler(text="done", state=personalData.confirm)
async def send_info(call: CallbackQuery, state: FSMContext):
    # tries to delete all previous message if there are no messages to delete it will ignore
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    user_id = call.from_user.id
    await call.answer(
        "Your inquiry has been successfully submitted✅.\nPlease wait for master's response, he will get in touch "
        "within a minute⏰. ",
        cache_time=60, show_alert=True)
    # inserting collecting data from memory into table(customers)
    data = await state.get_data()
    name = data.get("name")
    car = data.get("car")
    phone_number = data.get("phone")
    service = data.get("service")
    date = data.get("date")
    await db.apply(
        "insert into customers(name, car, phone_number, service, date, user_id) values (%s, %s, %s, %s, %s, %s)",
        (name, car, phone_number, service, date, user_id))

    customerID = call.message.from_user.id
    await call.message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                  f"Welcome {call.message.from_user.full_name}\n</b>"
                                                  "  \n"
                                                  "<i>The customer mode is activated </i>", reply_markup=categoryMenu)
    await mainmenu.main_menu.set()


# Cancel button appears after customer fills the required data
@dp.callback_query_handler(text="cancel", state=personalData.confirm)
async def cancel_sending(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        for i in range(message_id - 1, 100, -1):
            await bot.delete_message(chat_id=chat_id, message_id=i)
    except:
        pass
    await call.answer("The inquiry has been canceled ❌!", cache_time=60, show_alert=True)

    customerID = call.message.from_user.id
    await call.message.answer_photo(photo_url, caption=f"<b>Customer ID : {customerID}\n"
                                                       f"Welcome {call.message.from_user.full_name}\n</b>"
                                                       "  \n"
                                                       "<i>The customer mode is activated </i>",
                                    reply_markup=categoryMenu)
    await mainmenu.main_menu.set()


