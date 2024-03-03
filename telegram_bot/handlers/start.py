from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.handlers.response import send_response
from telegram_bot.handlers import keyboards
from telegram_bot.services.users import create_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Maybe errors with update.message.chat_id, update.message.chat.username if bot wil be added in telegram channel
    await create_user(update.message.chat_id, update.message.chat.username)
    await send_response(update, context, response='Hello 4el', keyboard=keyboards.START_KEYBOARD)
