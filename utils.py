import importlib
import inspect
import logging
import os

from commands.abstract import AbstractCommand

logger = logging.getLogger(__name__)


def echo_handler(bot, update):
    if update.message.text:
        message = 'What does "%s" mean?\nTry to type /help.' % update.message.text
        bot.sendMessage(update.message.chat_id, text=message)


def error_handler(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def autodiscovery(dispatcher):
    """
    Discover all available commands
    :param dispatcher: an updater's dispatcher
    """
    commands_module_name = 'commands'
    directory = os.fsencode(commands_module_name)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.py'):
            base_module_name = os.path.splitext(filename)[0]
            full_module_name = '.'.join((commands_module_name, base_module_name))

            # Command importing..
            module = importlib.import_module(full_module_name)

            # Iterate over classes and register discovered commands
            for _, klass in inspect.getmembers(module, inspect.isclass):
                if issubclass(klass, AbstractCommand) and klass is not AbstractCommand:
                    dispatcher.addTelegramCommandHandler(klass.COMMAND, klass().handler)
