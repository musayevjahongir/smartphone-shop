from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import get_token
import handlers


def main():
    TOKEN = get_token()

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text('Shop'), handlers.shop))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
