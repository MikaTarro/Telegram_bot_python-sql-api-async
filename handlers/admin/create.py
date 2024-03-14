from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.create_kb import place_kb

from state.create import CreateState

async def create_event(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'В какой бассейн вы хотите пойти', reply_markup=place_kb())
    await state.set_state(CreateState.place)
