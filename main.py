import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import random
from random import choice



import logging


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message):
    print(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    user = message.from_user
    response = (
        f"Ваш id: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваш username: @{user.username if user.username else 'Не указан'}"
    )
    await message.reply(response)


@dp.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    recipes = [
        'Рецепт 1: Пицца\nИнгредиенты: тесто, кетчуп, майонез, моцарелла, колбаса',
        'Рецепт 2: Борщ\nИнгредиенты: свекла, капуста, картошка, морковь, мясо',
        'Рецепт 3: Омлет\nИнгредиенты: яйца, молоко, соль, перец',
        'Рецепт 4: Гороховый суп\nИнгредиенты: горох, картошка, мясо',
        'Рецепт 5: Мясо по французски\nИнгредиенты: картошка, куринная голень, сыр любой, лук по желанию'
    ]
    random_recipe = choice(recipes)
    await message.reply(random_recipe)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())