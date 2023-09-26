from commands.abstract import AbstractCommand


class StartCommand(AbstractCommand):
    COMMAND = "start"

    async def handler(self, update, context):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hi! Boobogram Bot welcomes you! (.)(.)"
        )
