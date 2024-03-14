from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def create_event(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Я запустил функцию create event')

