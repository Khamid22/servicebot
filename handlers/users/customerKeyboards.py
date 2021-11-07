from aiogram.types import CallbackQuery, Message

from keyboards.default.customer import customer
from keyboards.default.start_keyboard import menuStart
from loader import dp
from states.feedback import Letter
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text_contains="customer", state='*')
async def user(call: CallbackQuery, state: FSMContext):
    photo_url = "https://www.onedealer.com/wp-content/uploads/2018/09/shutterstock_626286728-1.jpg"
    customerID = call.from_user.id

    await call.message.delete()
    await call.message.answer_photo(photo_url, caption='<i>The customer mode has been activated ✅</i>'
                                                       f'\n   \n'
                                                       f'<b>Customer ID: {customerID}</b>', reply_markup=customer)
    await state.finish()


@dp.message_handler(text_contains='Back', state='*')
async def back(msg: Message, state: FSMContext):
    await msg.delete()
    await msg.answer("Tip 💬: Fill out every required spaces precisely in order to receive quick responses",
                     reply_markup=menuStart)
    await state.finish()


@dp.message_handler(text_contains='✍🏻 Feedback', state=Letter.feedback)
async def feedback(msg: Message, state: FSMContext):
    photo_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fcar-repair-auto-diagnostic" \
                "-service-vector-isometric-illustration-car-repair-auto-diagnostic-service-vector-illustration" \
                "-image168498398&psig=AOvVaw28oGCszD8quIWDY5b7Yj7m&ust=1636365521132000&source=images&cd=vfe&ved" \
                "=0CAsQjRxqFwoTCKiagMSZhvQCFQAAAAAdAAAAABAO "
    await msg.answer_photo(photo_url, caption="<i> You can leave your feedback rating the master's work ethic: </i>")