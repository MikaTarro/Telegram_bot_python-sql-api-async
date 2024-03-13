from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database


async def start_register(message: Message, state: FSMContext):
    await message.answer(f'🐣Давай начнем регистрацию!🐥\n'
                         f'Для начала скажите, как я могу к вам обращаться ?☘️')
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'🤖Отлично!\n'
                         f'📲Теперь укажи номер телефона, чтобы быть вкурсе Обновлений!\n'
                         f'Формат телефона: +7xxxxxxxxxx \n\n'
                         f'🚦Я чувствителен к формату🚦')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)


async def register_phone(message: Message, state: FSMContext):
    if (re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        msg = f'🤖Приятно познакомиться 👑 {reg_name.title()} 👑 \n\n📱Ваш номер телефона {reg_phone}'
        await message.answer(msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()

    else:
        await message.answer(f'Номер указан в неправильном формате..')
