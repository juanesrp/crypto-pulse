from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router as api_routers
from workers.notification_worker import process_notifications

from core.database import create_tables
import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    task = asyncio.create_task(process_notifications())
    yield
    task.cancel()


app = FastAPI(
    title="CryptoPulse API",
    description="API de precios de criptomonedas",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_routers)


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "crypto-pulse"}
