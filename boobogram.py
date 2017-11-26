#!/usr/bin/env python
from telegram import Updater

from settings import BOOBS_TOKEN
from utils import echo_handler, error_handler, autodiscovery


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(BOOBS_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    autodiscovery(dp)

    # on noncommand i.e message - echo the message on Telegram
    dp.addTelegramMessageHandler(echo_handler)

    # log all errors
    dp.addErrorHandler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
