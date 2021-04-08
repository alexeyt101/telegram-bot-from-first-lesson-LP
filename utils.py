from emoji import emojize
from random import choice, randint

from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, ничья'
    else:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы проиграли'
    return message


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def create_main_keyboard():
    return ReplyKeyboardMarkup([['Прислать котика!', KeyboardButton('Мои координаты', request_location=True)]])



