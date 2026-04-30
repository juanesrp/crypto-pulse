from fastapi import APIRouter

from services.price_service import get_prices

router = APIRouter(prefix="/prices", tags=["Precios"])


@router.get("")
async def get_prices_endpoint():
    return await get_prices()
