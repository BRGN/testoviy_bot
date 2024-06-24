import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
import os

# Вставьте сюда токен вашего бота
API_TOKEN = '6952552382:AAHqCP-v0CvJFODDUpJGNiimPgy6N8JUgFs'

# Создание объектов бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(Command('start'))
async def start_command(message: Message):
    await message.answer('Привет! Отправь мне стикер, и я верну его тебе.')

# Обработка стикеров
@dp.message(F.sticker)
async def sticker_handler(message: Message):
    sticker_id = message.sticker.file_id
    print(sticker_id)
    with open(r'A:\bot_taro\kard.json', 'a') as f:
        f.write(f'{sticker_id}\n')
    await message.answer_sticker(sticker_id)

# Главная функция для запуска бота
async def main():
    # Регистрация обработчиков
    dp.message.register(start_command, Command("start"))
    dp.message.register(sticker_handler, F.sticker)

    # Запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
