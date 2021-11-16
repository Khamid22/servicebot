from aiogram import types

from loader import dp


# Don't understand bot :D
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("I don't understand... sorry")
