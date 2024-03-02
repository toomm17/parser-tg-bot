from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.handlers.response import send_response


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response='HELP 4 U BRO')