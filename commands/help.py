from commands.abstract import AbstractCommand


class HelpCommand(AbstractCommand):
    COMMAND = 'help'

    def handler(self, bot, update):
        help_lines = "\"/boobs\" - get random boobs\n"\
                     "\"/boobs\" model name - get boobs of your favorite model"
        bot.sendMessage(update.message.chat_id, text=help_lines)
