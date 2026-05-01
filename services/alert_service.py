from core.redis import redis_client


async def create_alert(user_id: str, coin: str, threashold: float):

    key = f"alert:user:{user_id}"

    await redis_client.hset(key, coin, str(threashold))


async def get_alerts(user_id: str):

    key = f"alert:user:{user_id}"

    raw_alerts = await redis_client.hgetall(key)

    result = {}

    for coin, value in raw_alerts.items():
        result[coin] = float(value)

    return result
