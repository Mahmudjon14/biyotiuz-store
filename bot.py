import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 7864621105))

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Mahsulotlar
products = {
    "Drill": {"price": 500000, "photo": "https://via.placeholder.com/200", "tag": "Top"},
    "Grinder": {"price": 300000, "photo": "https://via.placeholder.com/200", "tag": "New"},
    "Welder": {"price": 800000, "photo": "https://via.placeholder.com/200", "tag": "Discount"}
}

categories = ["Drill", "Grinder", "Welder"]

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("🛒 Kategoriyalar", "🔍 Qidirish").add(KeyboardButton("📞 Telefon raqamni yuborish", request_contact=True))

@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    await msg.answer("Salom! Bu Biyoti Uz botidir.", reply_markup=main_menu)

@dp.message_handler(lambda msg: msg.text == "🛒 Kategoriyalar")
async def show_categories(msg: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for cat in categories:
        keyboard.add(cat)
    keyboard.add("🔙 Orqaga")
    await msg.answer("Kategoriyalardan birini tanlang:", reply_markup=keyboard)

@dp.message_handler(lambda msg: msg.text in categories)
async def show_products(msg: types.Message):
    product = products.get(msg.text)
    if product:
        caption = f"{msg.text}\nNarxi: {product['price']} so‘m\nTeg: {product['tag']}"
        await bot.send_photo(msg.chat.id, photo=product['photo'], caption=caption)
    else:
        await msg.answer("Bu kategoriya mavjud emas.")

@dp.message_handler(lambda msg: msg.text == "🔍 Qidirish")
async def search_prompt(msg: types.Message):
    await msg.answer("Mahsulot nomini yuboring:")

@dp.message_handler(lambda msg: msg.text not in ["🛒 Kategoriyalar", "🔍 Qidirish", "🔙 Orqaga"])
async def handle_search(msg: types.Message):
    query = msg.text.lower()
    for name, item in products.items():
        if query in name.lower():
            caption = f"{name}\nNarxi: {item['price']} so‘m\nTeg: {item['tag']}"
            await bot.send_photo(msg.chat.id, photo=item['photo'], caption=caption)
            return
    await msg.answer("Mahsulot topilmadi.")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact_handler(msg: types.Message):
    contact = msg.contact.phone_number
    await msg.answer(f"Raqamingiz qabul qilindi: {contact}")
    await bot.send_message(ADMIN_ID, f"Yangi foydalanuvchi raqam yubordi: {contact}")

@dp.message_handler(lambda msg: msg.text == "🔙 Orqaga")
async def back_handler(msg: types.Message):
    await msg.answer("Asosiy menyu", reply_markup=main_menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
