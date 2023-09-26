from commands.abstract import AbstractCommand


class HelpCommand(AbstractCommand):
    COMMAND = "help"

    async def handler(self, update, context):
        help_lines = "\"/boobs\" - get random boobs\n"\
                     "\"/boobs\" model name - get boobs of your favorite model"

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=help_lines
        )
