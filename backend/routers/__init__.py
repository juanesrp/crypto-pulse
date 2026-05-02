from fastapi import APIRouter

from .prices import router as prices_router
from .alerts import router as alerts_router
from .sessions import router as sessions_router
from .users import router as users_router
from .auth import router as auth_router

router = APIRouter()
router.include_router(prices_router)
router.include_router(alerts_router)
router.include_router(sessions_router)
router.include_router(users_router)
router.include_router(auth_router)
