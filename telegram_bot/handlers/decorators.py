from functools import wraps

from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.db import fetch_one
from telegram_bot.handlers.response import send_response


def subscriber(handler):
    @wraps(handler)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        is_sub = await fetch_one(
        'SELECT id FROM subscribers WHERE telegram_id = (:telegram_id)',
        {'telegram_id': update.message.chat_id}
        )
        if not is_sub:
            return await send_response(update, context, response='Only for sub')
        await handler(update, context)
    return wrapper
