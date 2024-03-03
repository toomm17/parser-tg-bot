from typing import List
from dataclasses import dataclass

from telegram_bot.db import fetch_all


@dataclass
class SubscriptionPrice:
    id: int
    months_count: int
    price_in_usdt: int


async def get_subscription_plans() -> List[SubscriptionPrice]:
    result = await fetch_all('SELECT * FROM sub_plan')
    return [SubscriptionPrice(**sub_plan) for sub_plan in result]


