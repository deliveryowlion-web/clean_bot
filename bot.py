import os
from umaxbot import Bot, Dispatcher, types
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv("MAX_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Добавьте его в файл .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я твой новый бот, созданный с чистого листа. Всё работает!")

async def main():
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())