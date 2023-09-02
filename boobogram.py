import logging

from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder
)

from settings import BOOBS_TOKEN
from utils import autodiscovery, echo_handler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOOBS_TOKEN).build()
    application.add_handler(
        MessageHandler(
            filters.TEXT & (~filters.COMMAND),
            echo_handler
        )
    )

    # Load all commands
    #
    autodiscovery(application)

    application.run_polling()
