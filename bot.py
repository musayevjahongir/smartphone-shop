from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import get_token
import handlers


def main():
    TOKEN = get_token()

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text('Shop'), handlers.shop))
    dp.add_handler(MessageHandler(Filters.text('cart'), handlers.cart))
    dp.add_handler(CallbackQueryHandler(handlers.send_phones, pattern='brend:'))
    dp.add_handler(CallbackQueryHandler(handlers.send_phone, pattern='phone:'))
    dp.add_handler(CallbackQueryHandler(handlers.close_phone, pattern='close'))
    dp.add_handler(CallbackQueryHandler(handlers.add_cart, pattern='add:'))
    dp.add_handler(CallbackQueryHandler(handlers.clear_basket, pattern='clear-basket'))
    dp.add_handler(MessageHandler(Filters.text('contact'), handlers.send_contact))
    dp.add_handler(MessageHandler(Filters.text('about'), handlers.about))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
