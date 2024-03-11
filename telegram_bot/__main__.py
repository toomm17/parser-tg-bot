import logging 

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters
)

from telegram_bot import config, handlers
from telegram_bot.db import close_db


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


COMMAND_HANDLERS = {
    'start': handlers.start,
    'help': handlers.help_,
    'settings': handlers.settings
}

MESSAGE_HANDLERS = {
    filters.Text('Buy subscription'): handlers.buy_sub,
    filters.Text('HELP'): handlers.help_,
    filters.Text('Menu'): handlers.menu,
    filters.Text('All notifications'): handlers.all_notifications,
    filters.Text('OnlyDumps'): handlers.only_dumps,
    filters.Text('Min liquidity: '): handlers.min_liquidity,
    filters.Text('Min dump: '): handlers.min_dump,
    filters.Text('Min pump: '): handlers.min_pump,
    filters.Text('Back to MAIN MENU'): handlers.start,
}

CALLBACK_HANDLERS = {

}

if not config.TELEGRAM_BOT_TOKEN:
    raise Exception(
        "TELEGRAM_BOT_TOKEN env variable wasn't implemented in .env"
    )


def main() -> None:
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    for filter, message_handler in MESSAGE_HANDLERS.items():
        application.add_handler(MessageHandler(filter, message_handler))

    application.run_polling()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())

    finally:
        close_db()
