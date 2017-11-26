import json

from unittest.mock import Mock, patch

from commands.boobs import BoobsCommand
from commands.help import HelpCommand
from commands.start import StartCommand

from settings import BOOBS_MEDIA_URL


def get_request_mock(content, code=200):
    """
    Request object (Mock)
    :param content: Content
    :param code: HTTP code
    :return: Request object
    """
    request_mock = Mock()
    request_mock.status_code = code
    request_mock.text = json.dumps(content)
    return request_mock


def use_command(klass):
    """
    Wrapper for a test cases
    :param klass: Command Class
    """
    def decorator(func):
        def inner(*args, **kwargs):
            return func(klass(), Mock(), Mock(), *args, **kwargs)
        return inner
    return decorator


@use_command(HelpCommand)
def test_help(command, bot, update):
    command.handler(bot, update)
    text = '"/boobs" - get random boobs\n"/boobs" model name - get boobs of your favorite model'

    # waiting for `sendMessage` call
    bot.sendMessage.assert_called_with(update.message.chat_id, text=text)


@use_command(StartCommand)
def test_start(command, bot, update):
    command.handler(bot, update)
    text = 'Hi! Boobogram Bot welcomes you! (.)(.)'

    # waiting for `sendMessage` call
    bot.sendMessage.assert_called_with(update.message.chat_id, text=text)


@patch('commands.boobs.BoobsCommand._make_request')
@use_command(BoobsCommand)
def test_boobs(command, bot, update, make_request):
    photo_url = 'image.jpg'
    make_request.return_value = get_request_mock([{'id': 1, 'preview': photo_url}])

    # command name
    update.message.text = 'boobs'

    # run handler
    command.handler(bot, update)

    # waiting for `sendPhoto` call
    bot.sendPhoto.assert_called_with(update.message.chat_id, photo=BOOBS_MEDIA_URL + photo_url)
