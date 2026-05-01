import json
from core.redis import redis_client

QUEUE_KEY = "notifications:queue"


async def push_notification(
    user_id: str, coin: str, threshold: float, current_price: float
):

    message = json.dumps(
        {
            "user_id": user_id,
            "coin": coin,
            "threshold": threshold,
            "current_price": current_price,
        }
    )

    await redis_client.lpush(QUEUE_KEY, message)
    print(f"-> Notificacion encolada para usuario {user_id}: {coin} a {current_price}")


async def get_queue_length() -> int:

    return await redis_client.llen(QUEUE_KEY)
