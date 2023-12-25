from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import keyboards
from db import get_phone_by_id, add_item


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='salom',
        reply_markup=keyboards.home_keyboard()
    )

def shop(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='start shopping',
        reply_markup=keyboards.brends_keyboard()
    )

def send_phones(update: Update, context: CallbackContext):
    brend = update.callback_query.data.split(':')[1]

    update.callback_query.message.reply_text(
        text='start shopping',
        reply_markup=keyboards.phones_keyboard(brend)
    )

def send_phone(update: Update, context: CallbackContext):
    brend, doc_id = update.callback_query.data.split(':')[1:]

    phone = get_phone_by_id(brend, doc_id)

    update.callback_query.message.reply_photo(
        photo=phone['img_url'],
        caption=f'{phone["name"]}\n\nbrend: {phone["company"]}\ncolor: {phone["color"]}\nram: {phone["RAM"]}\nmemory: {phone["memory"]}\nprice: {phone["price"]}',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('add cart', callback_data=f"add:{brend}:{doc_id}"),
                    InlineKeyboardButton('close', callback_data=f"close-phone"),
                ]
            ]
        )
    )

def close_phone(update: Update, context: CallbackContext):
    update.callback_query.message.delete()

def add_cart(update: Update, context: CallbackContext):
    user = update.effective_user
    brend, doc_id = update.callback_query.data.split(':')[1:]

    add_item(user.id, brend, doc_id)

    update.callback_query.answer(text='added item.', show_alert=True)
