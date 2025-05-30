import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = "7979500134:AAE3yoPTqCAmN3VVpR_Cf305N_no8_DoM0c"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Biyoti Uz botiga xush kelibsiz!")

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
