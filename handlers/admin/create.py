from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.create_kb import place_kb, date_kb, time_kb

from state.create import CreateState


async def create_event(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'В какой бассейн вы хотите пойти', reply_markup=place_kb())
    await state.set_state(CreateState.place)


async def select_place(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Место выбрано ! \n'
                              f'Давайте выберем дату', reply_markup=date_kb())
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.date)


async def select_date(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Я сохранил выбранную дату! \n'
                              f'Выберите время', reply_markup=time_kb())
    await state.update_data(date=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.time)


async def select_time(call: CallbackQuery, state: FSMContext):
    await state.update_data(time=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(f'Отлично! Я всё записал!')
    create_data = await state.get_data()
    print(place_kb, create_data)