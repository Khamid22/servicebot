from aiogram.types import CallbackQuery, Message

from keyboards.inline.customer_menu import menu
from keyboards.inline.menu_keyboards import categoryMenu
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
                                                       f'<b>Customer ID: {customerID}</b>', reply_markup=menu)
    await state.finish()


@dp.callback_query_handler(text_contains='back', state='*')
async def back(call: CallbackQuery, state: FSMContext):
    photo_url = "https://previews.123rf.com/images/belchonock/belchonock1709/belchonock170900423/85866608-interface-of" \
                "-modern-car-diagnostic-program-on-engine-background-car-service-concept-.jpg"

    await call.message.answer_photo(photo_url, caption=f"Welcome Mr {call.message.from_user.full_name}!\n"
                                                       'What service do you want to have💬:', reply_markup=categoryMenu)


@dp.message_handler(text_contains='✍🏻 Feedback', state=Letter.feedback)
async def feedback(msg: Message, state: FSMContext):
    photo_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fcar-repair-auto-diagnostic" \
                "-service-vector-isometric-illustration-car-repair-auto-diagnostic-service-vector-illustration" \
                "-image168498398&psig=AOvVaw28oGCszD8quIWDY5b7Yj7m&ust=1636365521132000&source=images&cd=vfe&ved" \
                "=0CAsQjRxqFwoTCKiagMSZhvQCFQAAAAAdAAAAABAO "
    await msg.answer_photo(photo_url, caption="<i> You can leave your feedback rating the master's work ethic: </i>")
