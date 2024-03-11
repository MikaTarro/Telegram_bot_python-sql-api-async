from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

"""
Тут создаем кнопки
command = Наша Команда
description = Описание
"""


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начинаем работу.'
        ),
        BotCommand(
            command='help',
            description='Помощь в работе Бота.'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


"""
set_my_commands = 1е Список кнопок = commands
                2е Значение = BotCommandScopeDefault()
"""
