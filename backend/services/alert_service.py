import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import core.redis as redis_core
from models.alert import Alert

CACHE_PREFIX = "alert:user:"


async def create_alert(user_id: str, coin: str, threshold: float, db: AsyncSession):

    user_key = str(user_id)

    result = await db.execute(
        select(Alert).where(Alert.user_id == uuid.UUID(user_id), Alert.coin == coin)
    )

    existing_alert = result.scalar_one_or_none()

    if existing_alert:
        existing_alert.threshold = threshold
    else:
        new_alert = Alert(user_id=uuid.UUID(user_id), coin=coin, threshold=threshold)
        db.add(new_alert)

    await db.commit()

    await redis_core.redis_client.hset(f"{CACHE_PREFIX}{user_key}", coin, str(threshold))


async def get_alerts(user_id: str, db: AsyncSession):

    user_key = str(user_id)

    cached = await redis_core.redis_client.hgetall(f"{CACHE_PREFIX}{user_key}")

    if cached:
        print(f"Alertas de {user_key} desde Redis")
        return {coin: float(value) for coin, value in cached.items()}

    print(f"✗ Alertas de {user_key} desde PostgreSQL")
    result = await db.execute(select(Alert).where(Alert.user_id == uuid.UUID(user_id)))
    alerts = result.scalars().all()

    data = {}
    for alert in alerts:
        await redis_core.redis_client.hset(
            f"{CACHE_PREFIX}{user_key}", alert.coin, str(alert.threshold)
        )
        data[alert.coin] = alert.threshold

    return data
