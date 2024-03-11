from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from telegram_bot.services.subscription import get_subscription_plans


START_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton('Buy subscription'), KeyboardButton('HELP')],
        [KeyboardButton('Menu')]
    ],
    resize_keyboard=True
)

MENU_KEYBOARD = ReplyKeyboardMarkup([
        [KeyboardButton('All notifications'), KeyboardButton('OnlyDumps')],
        [KeyboardButton('Min liquidity: '), KeyboardButton('Min dump: '), KeyboardButton('Min pump: ')],
        [KeyboardButton('Back to MAIN MENU')]
    ],
    resize_keyboard=True
)

async def get_sub_plan_keyboard() -> InlineKeyboardMarkup:
    sub_plans = await get_subscription_plans()
    keyboard = []
    for sub_plan in sub_plans:
        btn = InlineKeyboardButton(
            f'{sub_plan.months_count} month(s) - {sub_plan.price_in_usdt} USDT',
            callback_data=f'sub_plan_{sub_plan.months_count}'
        )
        keyboard.append([btn])
    return InlineKeyboardMarkup(keyboard)