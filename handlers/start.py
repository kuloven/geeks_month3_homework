from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def start_handler(message: types.Message):
        print(message.from_user)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Наш адрес", callback_data="address")],
            [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
            [InlineKeyboardButton(text="О нас", callback_data="about")],
            [InlineKeyboardButton(text="Наш сайт", url="http://example.com")],
            [InlineKeyboardButton(text="Instagram профиль", url="http://instagram.com/example")],
            [InlineKeyboardButton(text="Отзывы", callback_data="feedback")],
            [InlineKeyboardButton(text="Наши вакансии", callback_data="jobs")]
        ])
        await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=keyboard)
