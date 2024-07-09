from aiogram import Dispatcher, types

def register_handlers(dp: Dispatcher):
    @dp.message(lambda message: message.text.lower() == 'холодные напитки')
    async def cold_drinks(message: types.Message):
        # Пример ответа с картинкой и описанием напитка
        await message.answer_photo(
            photo='URL_К_ИЗОБРАЖЕНИЮ_НАПИТКА',
            caption='Название: Лимонад\nОписание: Освежающий лимонад с мятой и лимоном'
        )
