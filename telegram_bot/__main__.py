import logging 

from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from telegram_bot import config, handlers


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


COMMAND_HANDLERS = {
    'start': handlers.start,
    'help': handlers.help_
}

MESSAGE_HANDLERS = {}

if not config.TELEGRAM_BOT_TOKEN:
    raise Exception(
        "TELEGRAM_BOT_TOKEN env variable wasn't implemented in .env"
    )


def main() -> None:
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    for message, message_handler in MESSAGE_HANDLERS.items():
        application.add_handler(MessageHandler(message, message_handler))

    application.run_polling()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())


