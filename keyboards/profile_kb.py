from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import datetime


def profile_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Актуальные события")
    kb.button(text="Мои события") #TODO
    kb.button(text="Баланс")
    kb.button(text="История событий") #TODO
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите действие⬇️')


def date_kb():
    kb = InlineKeyboardBuilder()
    current_date = datetime.date.today()
    for i in range(7):
        current_date += datetime.timedelta(days=1)
        kb.button(text=f"{current_date.strftime('%d.%m')}",
                  callback_data=f"viewn_date_{current_date.strftime('%d.%m.%y')}")
    kb.adjust(1)
    return kb.as_markup()


def add_event(event_id, user_id):  # добавить запись
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Записаться', callback_data=f'add_event_{event_id}_{user_id}')
    kb.adjust(1)
    return kb.as_markup()


def delete_event(event_id, user_id):  # удалить запись
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Удалить Запись', callback_data=f'delete_event_{event_id}_{user_id}')
    kb.adjust(1)
    return kb.as_markup()

def balance_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='💸 Пополнить баланс 💸', callback_data=f'add_balance')
    kb.adjust(1)
    return kb.as_markup()