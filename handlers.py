from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import keyboards
from db import get_phone_by_id, add_item, get_items, clear_items


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

def cart(update: Update, context: CallbackContext):
    user = update.effective_user

    items = get_items(user_id=user.id)

    text = "your basket\n\n"
    total = 0
    for item in items:
        phone = get_phone_by_id(item['brend'], item['phone_id'])
        total += phone['price']

        text += f"# {phone['name']} - {phone['price']}\n"

    text += f"\ntotal: {total}"


    update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('buy', callback_data='buy'),
                    InlineKeyboardButton('clear', callback_data='clear-basket'),
                ],
                [
                    InlineKeyboardButton('close', callback_data='close-basket'),
                ]
            ]
        )
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
                    InlineKeyboardButton('close', callback_data=f"close"),
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

def clear_basket(update: Update, context: CallbackContext):
    user = update.effective_user

    clear_items(user.id)

    update.callback_query.answer(text='removed items.', show_alert=True)
    close_phone(update, context)

def send_contact(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    text= "Tanlagan maxsulotlaringizni rasmiylashtirish uchun adminimiz bilan bog'laning!"

    bot.sendMessage(user.id, text)
    bot.sendContact(chat_id=user.id, phone_number='+998990235051', first_name='Jahongir')

def about(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    text= "Biz orqali turli brenddagi mobile telefonlarni sotib olishingiz mumkin. Bizni tanlaganingiz uchun raxmat!!!"

    bot.sendMessage(user.id, text)