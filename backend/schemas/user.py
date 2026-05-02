from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr  # EmailStr valida que sea un correo válido


class UserResponse(BaseModel):
    id: UUID
    username: str
    first_name: str
    last_name: str
    email: str
    is_active: bool
    created_at: datetime

    # model_config le dice a Pydantic que puede leer los datos directamente
    # desde un objeto de SQLAlchemy (no solo desde diccionarios).
    model_config = {"from_attributes": True}
