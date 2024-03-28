from aiogram import Bot
from aiogram.types import Message
from utils.database import Database
import os

weather = os.getenv('WEATHER_TOKEN')


# привязка ответа по нажатию кнопки
async def get_weather(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id, f'{users[1]}, давай подскажу как дела за окном \n')
