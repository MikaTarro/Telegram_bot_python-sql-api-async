from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from utils.database import Database
import os
from keyboards.profile_kb import date_kb, add_event, delete_event
from utils.function import list_gamer


async def viewn_event(message: Message, bot=Bot):
    await bot.send_message(message.from_user.id, f"Выберите дату события", reply_markup=date_kb())


# тут он выводит выбор даты , а дальше не работает ...

async def viewn_event_date(call: CallbackQuery):
    await call.answer()
    date = call.data.split("_")[-1] # делим строку даты по нижнему подчерк и берем последний элемент
    db = Database(os.getenv('DATABASE_NAME'))  # подключились к БД
    events = db.select_events('0', date)  # в евентс передаем ФУНКЦИЮ с Статус=0 и Датой

    if (events):  # если в Евентс что то есть, то выводим информацию через цикл FOR
        # создаем таблицу РЕКОРДС инфо о ЗАПИСАВШИХСЯ НА ИВЕНТ\событие
        await call.message.answer(f'Актуальные события:')
        for event in events:
            persons = db.select_person(event[0])  # данные об людях записанных на событие
            gamers = list_gamer(persons)  # создаем список участников function.py
            msg = (f'🤖Событие состоится: \n\n'
                   f'🏬{event[9]} (Адрес: {event[10]}) \n\n'
                   f'📆{event[2]} в {event[3]}\n\n'
                   f'💭{gamers}')

            if not (
                    db.check_user(event[0],
                                  call.from_user.id)):  # Если человек НЕ записался то выводим кнопку с записью
                await call.message.answer(msg, reply_markup=add_event(event[0], call.from_user.id))
            else:  # Если он ЗАПИСАН то добавляем копку с удалением записи
                await call.message.answer(msg, reply_markup=delete_event(event[0], call.from_user.id))
    else:  # Если никто не бронировал дату то Сообщим
        await call.message.answer(f'📝В выбранную дату записей нет')
