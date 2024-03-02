from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


START_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton('Buy subscription')],
    ],
    resize_keyboard=True
)


