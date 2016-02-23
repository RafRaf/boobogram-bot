#!/usr/bin/env python
import json
import random
import requests

from telegram import Updater

from local import *


logger = logging.getLogger(__name__)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi! Boobogram Bot welcomes you! (.)(.)')


def help(bot, update):
    help_lines = [
        '"/boobs" - get random boobs',
        '"/boobs model name" - get boobs of your favorite model',
    ]

    bot.sendMessage(update.message.chat_id, text='\n'.join(help_lines))


def echo(bot, update):
    if update.message.text:
        message = 'What does "{}" mean?\nTry to type /help.'.format(update.message.text)
        bot.sendMessage(update.message.chat_id, text=message)


def get_random_boobs_proc():
    response = requests.get('{}noise/{}/'.format(BOOBS_API_URL, BOOBS_AMOUNT))

    if response.status_code == 200:
        return json.loads(response.text)


def get_boobs_by_model_proc(model_name):
    response = requests.get('{}boobs/model/{}/'.format(BOOBS_API_URL, model_name))

    if response.status_code == 200:
        photo_items_list = json.loads(response.text)

        if len(photo_items_list) > BOOBS_AMOUNT:
            photo_items_id_list = [item['id'] for item in photo_items_list]
            processed_photo_items_list = set()

            while len(processed_photo_items_list) != BOOBS_AMOUNT:
                processed_photo_items_list.add(random.choice(photo_items_id_list))

            return [item for item in photo_items_list if item['id'] in processed_photo_items_list]

        return photo_items_list


def boobs(bot, update):
    cmd, *params = update.message.text.split()

    if params:
        photo_items_list = get_boobs_by_model_proc(' '.join(params))
    else:
        photo_items_list = get_random_boobs_proc()

    if isinstance(photo_items_list, list):
        for photo_item in photo_items_list:
            photo_url = photo_item.get('preview')

            if photo_url:
                bot.sendPhoto(update.message.chat_id, photo=BOOBS_MEDIA_URL + photo_url)
    else:
        bot.sendMessage(update.message.chat_id, text='Nothing :(')


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
