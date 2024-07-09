from aiogram import Dispatcher, types
from aiogram.filters import Command

def register_handlers(dp: Dispatcher):
    @dp.message(Command('myinfo'))
    async def myinfo(message: types.Message):
        user = message.from_user
        response = (
            f"Ваш id: {user.id}\n"
            f"Ваше имя: {user.first_name}\n"
            f"Ваш username: @{user.username if user.username else 'Не указан'}"
        )
        await message.reply(response)
