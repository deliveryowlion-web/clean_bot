import asyncio
import logging
from maxapi import Bot, Dispatcher
from maxapi.types import MessageCreated

logging.basicConfig(level=logging.INFO)

TOKEN = "f9LHodD0cOJnos0uZOxzAEFU_LtgF-yXP51MaD8UCriLK-vRWi01ZmjpcOK8tRBpjtEYuGDu7nik9zIoMOUm"  # Ваш токен

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message_created()
async def handle_start(event: MessageCreated):
    if event.message.body and event.message.body.text == '/start':
        await event.message.answer("OK")
        print(f"Ответил на /start в чат {event.message.chat.id}")

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
