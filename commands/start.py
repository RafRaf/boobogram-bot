from commands.abstract import AbstractCommand


class StartCommand(AbstractCommand):
    COMMAND = 'start'

    def handler(self, bot, update):
        bot.sendMessage(update.message.chat_id, text='Hi! Boobogram Bot welcomes you! (.)(.)')
