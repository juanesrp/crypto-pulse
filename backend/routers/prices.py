from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from services.price_service import get_prices
from services.alert_service import get_alerts
from services.notification_service import push_notification, get_queue_length

router = APIRouter(prefix="/prices", tags=["Precios"])


@router.get("")
async def get_prices_endpoint():
    return await get_prices()


@router.get("/check-alerts")
async def check_alerts(user_id: str, db: AsyncSession = Depends(get_db)):

    current_prices = await get_prices()

    alerts = await get_alerts(user_id, db)

    triggered = []

    for coin, threshold in alerts.items():
        if coin in current_prices:
            current_price = current_prices[coin]["usd"]

            if current_price >= threshold:
                await push_notification(user_id, coin, threshold, current_price)
                triggered.append(
                    {
                        "coin": coin,
                        "threshold": threshold,
                        "current_price": current_price,
                    }
                )

    queue_length = await get_queue_length()

    return {
        "user_id": user_id,
        "triggered_alerts": triggered,
        "pending_in_queue": queue_length,
    }
