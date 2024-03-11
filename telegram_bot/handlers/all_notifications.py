from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.handlers.response import send_response
from telegram_bot.handlers.decorators import subscriber


@subscriber
async def all_notifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response='YOUR NOTIFICATIONS BRO')
