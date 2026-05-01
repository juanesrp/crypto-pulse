from fastapi import APIRouter

from .prices import router as prices_router
from .alerts import router as alerts_router

router = APIRouter()
router.include_router(prices_router)
router.include_router(alerts_router)
