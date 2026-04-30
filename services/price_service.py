import httpx
import json


from core.redis import redis_client

CACHE_KEY = "crypto:prices"

CACHE_TTL = 30

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,solana"
    "&vs_currencies=usd"
    "&include_24hr_change=true"
)


async def get_prices():

    cached_data = await redis_client.get(CACHE_KEY)

    if cached_data:
        print("✓ Cache HIT — dato servido desde Redis")
        return json.loads(cached_data)

    print("✗ Cache MISS — consultando CoinGecko")

    async with httpx.AsyncClient() as client:
        response = await client.get(COINGECKO_URL)
        data = response.json()

    await redis_client.setex(CACHE_KEY, CACHE_TTL, json.dumps(data))

    return data
