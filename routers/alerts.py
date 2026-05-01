from fastapi import APIRouter

from pydantic import BaseModel

from services.alert_service import create_alert, get_alerts

router = APIRouter(prefix="/alerts", tags=["Alertas"])


class AlertCreate(BaseModel):
    user_id: str
    coin: str
    threshold: float


@router.post("")
async def create_alert_endpoint(alert: AlertCreate):
    await create_alert(alert.user_id, alert.coin, alert.threshold)
    return {"message": "Alerta creada", "alert": alert}


@router.get("/{user_id}")
async def get_alerts_endpoint(user_id: str):
    alerts = await get_alerts(user_id)
    return {"user_id": user_id, "alerts": alerts}
