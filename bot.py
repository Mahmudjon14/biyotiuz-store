import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Log yozuvlarini sozlash
logging.basicConfig(level=logging.INFO)

# .env fayldan tokenni yuklash
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

# Bot va dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
