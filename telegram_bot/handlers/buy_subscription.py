from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.handlers import keyboards
from telegram_bot.handlers.response import send_response


async def buy_sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = await keyboards.get_sub_plan_keyboard()
    await send_response(
        update,
        context,
        response='Please select subscriptions plan',
        keyboard=keyboard
    )
