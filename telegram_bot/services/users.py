import logging
from dataclasses import dataclass

from telegram_bot.db import execute, fetch_one


logger = logging.getLogger(__name__)


@dataclass
class User:
    telegram_id: int
    username: str
    created_at: str  # timestamp
    balance: float

    def string_to_datetime(self):
        pass


async def create_user(telegram_user_id: int, telegram_username: str) -> None:
    already_in_db = await get_user_by_id(telegram_user_id)
    if not already_in_db:
        await execute(
            'INSERT OR IGNORE INTO users (telegram_id, username, balance) VALUES (:telegram_id, :username, :balance);',
            {'telegram_id': telegram_user_id, 'username': telegram_username, 'balance': 0}
        )
        logger.info('Create new user with telegram_id %s and username %s' % (telegram_user_id, telegram_username))


async def get_user_by_id(telegram_user_id: int) -> User | None:
    result = await fetch_one(
        'SELECT * FROM users WHERE telegram_id = (:telegram_id)',
        {'telegram_id': telegram_user_id}
    )
    return User(**result) if result else None


async def get_user_by_name(telegram_username: str) -> User | None:
    result = await fetch_one(
        'SELECT * FROM users WHERE username = (:username)',
        {'username': telegram_username}
    )
    return User(**result) if result else None


async def add_to_balance(telegram_user_id: int, balance: int) -> None:
    pass


async def remove_from_balance(telegram_user_id: int, balance: int) -> None:
    pass
