from telegram import Update
from telegram.ext import CallbackContext
import keyboards


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
