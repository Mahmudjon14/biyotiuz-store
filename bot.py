from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import logging
import os

# .env fayldagi o'zgaruvchilarni yuklash
load_dotenv()

# .env fayldan BOT_TOKEN ni olish
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# Bu yerga sizning handlerlaringiz yoki komandalar kiradi
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Salom! Bu Biyoti Uz botidir.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
