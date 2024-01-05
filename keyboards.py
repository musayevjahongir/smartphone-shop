from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from db import get_brends, get_phones_by_brend
from pprint import pprint


def home_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton('Shop'), KeyboardButton('cart')],
            [KeyboardButton('about'), KeyboardButton('contact')],
        ],
        resize_keyboard=True
    )

def phones_keyboard(brend: str):
    phones = get_phones_by_brend(brend)

    keyboard = []
    i=1
    for phone in phones:
        keyboard.append(
            [
                InlineKeyboardButton(text=phone['name'], callback_data=f"phone:{brend}:{i}")
            ]
        )
        i+=1

    return InlineKeyboardMarkup(keyboard)

def brends_keyboard():
    keyboards_btns = []
    row = []
    for brend in get_brends():
        row.append(InlineKeyboardButton(brend, callback_data=f'brend:{brend}'))
        if len(row) == 2:
            keyboards_btns.append(row)
            row = []

    if row:
        keyboards_btns.append(row)

    return InlineKeyboardMarkup(
        keyboards_btns
    )

