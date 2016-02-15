#!/usr/bin/env python
import json
import requests

from telegram import Updater

from local import *


logger = logging.getLogger(__name__)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi! Boobogram Bot welcomes you! (.)(.)')


def help(bot, update):
    help_message = 'Just type "/boobs"! :)'
    bot.sendMessage(update.message.chat_id, text=help_message)


def echo(bot, update):
    message = 'What does "{}" mean?\nTry to type /help.'.format(update.message.text)
    bot.sendMessage(update.message.chat_id, text=message)


def boobs(bot, update):
    response = requests.get('{}noise/{}/'.format(BOOBS_API_URL, BOOBS_AMOUNT))

    if response.status_code == 200:
        photo_items_list = json.loads(response.text)

        for photo_item in photo_items_list:
            photo_url = photo_item.get('preview')

            if photo_url:
                bot.sendPhoto(update.message.chat_id, photo=BOOBS_MEDIA_URL + photo_url)
    else:
        bot.sendMessage(update.message.chat_id, text='Temporary unavailable :( ({})'.format(response.status_code))


def error(bot, update, error):
    logger.warn('Update "{}" caused error "{}"'.format(update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(BOOBS_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler('start', start)
    dp.addTelegramCommandHandler('help', help)
    dp.addTelegramCommandHandler('boobs', boobs)

    # on noncommand i.e message - echo the message on Telegram
    dp.addTelegramMessageHandler(echo)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
