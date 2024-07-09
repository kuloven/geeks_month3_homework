from aiogram import Dispatcher, types
from aiogram.filters import Command
from random import choice

def register_handlers(dp: Dispatcher):
    @dp.message(Command('random_recipe'))
    async def random_recipe(message: types.Message):
        recipes = [
            'Рецепт 1: Пицца\nИнгредиенты: тесто, кетчуп, майонез, моцарелла, колбаса',
            'Рецепт 2: Борщ\nИнгредиенты: свекла, капуста, картошка, морковь, мясо',
            'Рецепт 3: Омлет\nИнгредиенты: яйца, молоко, соль, перец',
            'Рецепт 4: Гороховый суп\nИнгредиенты: горох, картошка, мясо',
            'Рецепт 5: Мясо по-французски\nИнгредиенты: картошка, куриная голень, сыр, лук'
        ]
        random_recipe = choice(recipes)
        await message.reply(random_recipe)
