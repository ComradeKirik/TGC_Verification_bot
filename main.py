import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import start_handler, apply_handler


load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start_handler.router)
dp.include_router(apply_handler.router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
