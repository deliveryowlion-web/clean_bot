import os
from maxapi import Bot, types
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv("MAX_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Добавьте его в переменные окружения.")

bot = Bot(token=TOKEN)

@bot.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Бот работает на maxapi.")

async def main():
    print("Бот запущен...")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())
