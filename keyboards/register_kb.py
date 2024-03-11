from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard= ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='🛫Давай зарегистрируем тебя!🛬'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Для продолжения нажми на кнопку ниже')