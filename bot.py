import os
from maxapi import Bot
import asyncio

TOKEN = os.getenv("MAX_BOT_TOKEN")
if not TOKEN:
    raise Exception("Токен не найден")

bot = Bot(token=TOKEN)

@bot.message_handler(commands=['start'])
async def start(msg):
    await msg.answer("OK")

async def main():
    print("Бот запущен")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())
