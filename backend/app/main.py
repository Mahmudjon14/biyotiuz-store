from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "7979500134:AAE3yoPTqCAmN3VVpR_Cf305N_no8_DoM0c"  # Bu yerga tokeningizni qo'ying

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Salom! Bot ishga tushdi!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
