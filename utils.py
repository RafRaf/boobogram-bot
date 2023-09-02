import importlib
import inspect
import logging
import os

from telegram.ext import CommandHandler

from commands.abstract import AbstractCommand

logger = logging.getLogger(__name__)


async def echo_handler(update, context):
    if update.message.text:
        text = \
            f"What does \"{update.message.text}\" mean?\nTry to type /help."

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )


def autodiscovery(application):
    """
    Discover all available commands
    :param application: application
    """
    commands_module_name = "commands"
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
                    application.add_handler(CommandHandler(klass.COMMAND, klass().handler))
