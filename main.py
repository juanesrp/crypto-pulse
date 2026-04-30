from fastapi import FastAPI
from routers.prices import router as prices_router


app = FastAPI(
    title="CryptoPulse API",
    description="API de precios de criptomonedas",
    version="0.1.0",
)

app.include_router(prices_router)


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "crypto-pulse"}
