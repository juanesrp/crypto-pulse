from fastapi import APIRouter
from services.session_service import (
    add_user,
    remove_user,
    get_connected_count,
    is_connected,
)

router = APIRouter(prefix="/sessions", tags=["Sesiones"])


@router.post("/{user_id}")
async def connect_user(user_id: str):
    await add_user(user_id)
    count = await get_connected_count()
    return {"message": f"Usuario {user_id} conectado", "connected_now": count}


@router.delete("/{user_id}")
async def disconnect_user(user_id: str):
    await remove_user(user_id)
    count = await get_connected_count()
    return {"message": f"Usuario {user_id} desconectado", "connected_now": count}


@router.get("/count")
async def connected_count():
    count = await get_connected_count()
    return {"connected_users": count}


@router.get("/{user_id}/status")
async def user_status(user_id: str):
    connected = await is_connected(user_id)
    return {"user_id": user_id, "connected": connected}
