import os

import httpx

PRICE_SERVICE_URL = os.environ.get("PRICE_SERVICE_URL", "http://localhost:8001")


async def get_prices():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRICE_SERVICE_URL}/prices", timeout=10.0)
        response.raise_for_status()
        return response.json()