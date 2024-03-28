from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database


async def start_register(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id,
                               f'{users[1]} \n 🫵 Chill -> Иди за Кофе! ☕️\n ✅Уже зарегистрированы')
    else:
        await bot.send_message(message.from_user.id, f'🐣Давай начнем регистрацию!🐥\n'
                                                     f'🤖Для начала скажите, как я могу к вам обращаться ❔')
        await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'🤖Отлично!\n'
                                                 f'📲Теперь укажи номер телефона, чтобы быть вкурсе Обновлений!\n'
                                                 f'Формат телефона: +7xxxxxxxxxx \n\n'
                                                 f'🚦Я чувствителен к формату🚦')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)


# async def register_city(message: Message, state: FSMContext, bot: Bot):
#     await bot.send_message(message.from_user.id, f'Напиши свой город)
#     await state.update_data(regcity=message.text)
#     await state.set_state(RegisterState.regCity)


async def register_phone(message: Message, state: FSMContext, bot: Bot):
    if (re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        reg_city = reg_data.get('regcity')
        msg = f'🤖Приятно познакомиться 👑 {reg_name.title()}👑 \n\n📱Ваш номер телефона {reg_phone}'
        await bot.send_message(message.from_user.id, msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()

    else:
        await bot.send_message(message.from_user.id, f'Номер указан в неправильном формате..')
