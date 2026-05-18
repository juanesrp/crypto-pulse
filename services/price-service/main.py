import json
import os

import httpx
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,solana"
    "&vs_currencies=usd"
    "&include_24hr_change=true"
)
CACHE_KEY = "crypto:prices"
CACHE_TTL = 30

redis_client = redis.from_url(REDIS_URL, decode_responses=True)
app = FastAPI(title="Price Service")


@app.get("/prices")
async def get_prices():
    cached_data = await redis_client.get(CACHE_KEY)

    if cached_data:
        print("✓ Cache HIT — dato servido desde Redis")
        return json.loads(cached_data)

    print("✗ Cache MISS — consultando CoinGecko")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(COINGECKO_URL, timeout=10.0)
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Error consultando CoinGecko: {e}")

    await redis_client.setex(CACHE_KEY, CACHE_TTL, json.dumps(data))
    return data


@app.get("/health")
async def health():
    return {"status": "ok", "service": "price-service"}