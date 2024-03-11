from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard
"""
Тут мы даем нашим кнопкам-> действия
"""


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Я 🤖C-3PO: Протокольный дроид!🤖 \n'
                                                 f'🚀Помогу писать ответы за вас 🤓 \n'
                                                 f'💫На любом языке🌍 с переводом🎩🪄\n\n\n', reply_markup=register_keyboard)
