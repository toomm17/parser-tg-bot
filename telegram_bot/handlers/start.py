from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.handlers.response import send_response


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response='Hello 4el')