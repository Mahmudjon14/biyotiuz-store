import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Logger
logging.basicConfig(level=logging.INFO)

# Telegram bot
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# FastAPI server
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Biyoti Uz bot ishlayapti"}

# Bot handler
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Salom! Biyoti Uz botiga xush kelibsiz!")

# Async background bot start
async def start_bot():
    await dp.start_polling()

# Run both bot and FastAPI together
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())  # Fon rejimida Telegram bot ishlaydi
    uvicorn.run(app, host="0.0.0.0", port=10000)  # Render uchun HTTP port ochiladi
