from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import get_token
import handlers


def main():
    TOKEN = get_token()

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text('Shop'), handlers.shop))
    dp.add_handler(CallbackQueryHandler(handlers.send_phones, pattern='brend:'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
