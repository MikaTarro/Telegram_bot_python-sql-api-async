from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command

from utils.commands import set_commands
from handlers.start import get_start
from handlers.weather import get_weather
from state.register import RegisterState
from state.create import CreateState
from handlers.profile import viewn_event, viewn_event_date
from handlers.register import start_register, register_name, register_phone
from handlers.admin.create import create_event, select_place, select_date, select_time
from filters.CheckAdmin import CheckAdmin

# навести порядок в импортах!!
load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')
weather = os.getenv('WEATHER_TOKEN')

""" переменные дл взаимодейств с ботом """

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

""" создаем свой айдишник
from aiogram.filters import CommandStart
"""

# @dp.message(CommandStart())
# async def command_start_handler(message):
#     await message.answer(f'Твой id: {message.from_user.id}')

""" start_bot = оповещает ADMIN о запуске """


async def start_bot(bot: Bot):
    await bot.send_message(1375989844, text='🤖Ro-Bot был запущен')


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))
dp.message.register(get_weather, Command(commands='weather'))

# лепим хэндлеры регистрации*
dp.message.register(start_register, F.text == '🛫Давай зарегистрируем тебя!🛬')
dp.message.register(register_name, RegisterState.regName)
# dp.message.register(register_city, RegisterState.regCity)
dp.message.register(register_phone, RegisterState.regPhone)

# хэндлер создание события
dp.message.register(create_event, Command(commands='help'), CheckAdmin())
dp.callback_query.register(select_place, CreateState.place)
dp.callback_query.register(select_date, CreateState.date)
dp.callback_query.register(select_time, CreateState.time)
# хенд профиля
dp.message.register(viewn_event, F.text == 'Актуальные события')
dp.callback_query.register(viewn_event_date, F.data.startswith('viewn_date_'))

""" даем проверку на ошибку : если что-то НЕ ТО , то бот= break. """


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
