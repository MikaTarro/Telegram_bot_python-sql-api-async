from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')
# переменные дл взаимодейств с ботом
bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


# start_bot = оповещает ADMIN о запуске
async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Бот был запущен')


dp.startup.register(start_bot)


# даем проверку на ошибку : если что-то НЕ ТО , то бот= break.
async def start():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
