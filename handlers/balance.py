from aiogram import Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from utils.database import Database
import os
from keyboards.profile_kb import balance_kb


# Создаем кнопку, для просмотра\пополнения баланса
async def viewn_balance(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    user = db.select_user_id(message.from_user.id)  # инфо пользователя который обратился к хэндлеру
    await bot.send_message(message.from_user.id, f'Ваш баланс:  {user[4]} руб.', reply_markup=balance_kb())


async def add_balance(call: CallbackQuery):  # функция по добавлению баланса
    await call.bot.send_invoice(
        chat_id=call.from_user.id,
        title='Пополнить баланс',
        description='Пополнение баланса',
        provider_token=os.getenv('TOKEN_YOUKASSA'),
        payload='add_balance',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Пополнить баланс на 500р.',
                amount=50000
            )
        ],
        start_parameter='TARO_Mbot',
        provider_data=None,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        reply_markup=None,
        request_timeout=60
    )


async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    print(pre_checkout_query)


async def success_payment(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    balances = db.select_user_id(message.from_user.id)
    balance = balances[4] + message.successful_payment.total_amount // 100
    db.balance_user_edit(message.from_user.id, balance)
    db.balance_system(f'+{message.successful_payment.total_amount // 100}', message.from_user.id)
    await bot.send_message(message.from_user.id,
                           f'Ваш баланс успешно пополнен на {message.successful_payment.total_amount // 100} р.')
