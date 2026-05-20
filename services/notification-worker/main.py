import asyncio
import json
import os

import redis.asyncio as redis

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
QUEUE_KEY = "notifications:queue"

redis_client = redis.from_url(REDIS_URL, decode_responses=True)


async def process_notifications():
    print("Worker de notificaciones iniciado")

    while True:
        result = await redis_client.brpop(QUEUE_KEY, timeout=1)

        if result:
            _, message = result
            notification = json.loads(message)
            print(
                f"Notificacion procesada | "
                f"usuario: {notification['user_id']} | "
                f"{notification} | "
                f"umbral: ${notification['threshold']}"
            )


if __name__ == "__main__":
    asyncio.run(process_notifications())