from aiogram import Bot
from aiogram.types import Message
from utils.database import Database
import os


async def viewn_profile(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    events = db.db_select_column('events', 'status', 0)
    if(events):
        await bot.send_message(message.from_user.id, f'🤖Ваши брони:')
        for event in events:
            await bot.send_message(message.from_user.id, f'🤖Записал вас на: {event[2]} число, время: {event[3]} \n\n'
                                                         f'\t\t🐋Стоимость сеанса 2000 рублей🐋.')
    else:
        await bot.send_message(message.from_user.id, f'🤖В настоящее время записей нет.')
