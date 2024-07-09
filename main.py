import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

# Загрузка обработчиков
from handlers import start, myinfo, random_recipe, dishes

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

# Регистрация обработчиков
start.register_handlers(dp)
myinfo.register_handlers(dp)
random_recipe.register_handlers(dp)
dishes.register_handlers(dp)

async def main():
    logging.basicConfig(level=logging.INFO)
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
