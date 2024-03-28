from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard
from keyboards.profile_kb import profile_kb
from utils.database import Database
import os
"""
Тут мы даем нашим кнопкам-> действия
"""


async def get_start(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id, f'Привет {users[1]}!', reply_markup=profile_kb())
    else:
        await bot.send_message(message.from_user.id, f'🤖я Ro-Bot!🤖 \n'
                                                 f'🚀Помогу записать тебя в бассейн 🤓 \n'
                                                 f'💫запись открыта на неделю вперед🌍 время с 9 до 22🎩🪄\n\n\n', reply_markup=register_keyboard)
