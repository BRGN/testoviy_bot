import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
import json
import random
import google.generativeai as genai
import os

genai.configure(api_key="TOKEN")

model = genai.GenerativeModel('gemini-1.5-flash')
# Вставьте сюда токен вашего бота
API_TOKEN = 'TOKEN'

# Создание объектов бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Загрузка данных из JSON файла
with open(r'\kard.json', 'r', encoding='utf-8') as f:
    kard_data = json.load(f)

# Функция для отправки случайного стикера
async def send_random_stickers(message: Message):
    # Берем случайные 3 ID без повторений
    random_ids = random.sample(kard_data, 3)
    
    for kard in random_ids:
        sticker_id = kard['id']
        sticker_name = kard['name']
        response = model.generate_content(f"Опиши карту таро {sticker_name}")
        await bot.send_message(message.chat.id, sticker_name)
        await bot.send_sticker(message.chat.id, sticker_id)
        await bot.send_sticker(message.chat.id, response)
        await asyncio.sleep(0.5)  # Пауза между отправками

# Обработка команды /start
@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я буду отправлять тебе случайные стикеры из списка.')

# Обработка команды 
@dp.message(lambda message: message.text == 'карты')
async def get_stickers(message: Message):
    await send_random_stickers(message)

# Главная функция для запуска бота
async def main():
    # Запуск бота
    # Запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
