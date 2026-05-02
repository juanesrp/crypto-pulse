from uuid import UUID
from pydantic import BaseModel


class AlertCreate(BaseModel):
    user_id: UUID
    coin: str
    threshold: float


class AlertResponse(BaseModel):
    user_id: UUID
    coin: str
    threshold: float
