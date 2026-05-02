from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.database import get_db
from models.user import User
from schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["Usuarios"])


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail=f"Usuario {user_id} no encontrado")

    return user
