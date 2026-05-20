import asyncio
import json
import os

import redis.asyncio as redis

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
QUEUE_KEY = "notifications:queue"
PORT = int(os.environ.get("PORT", "8000"))

redis_client = redis.from_url(REDIS_URL, decode_responses=True)


async def health_handler(reader, writer):
    await reader.read(1024)
    writer.write(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK")
    await writer.drain()
    writer.close()


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


async def main():
    server = await asyncio.start_server(health_handler, "0.0.0.0", PORT)
    await asyncio.gather(
        server.serve_forever(),
        process_notifications(),
    )


if __name__ == "__main__":
    asyncio.run(main())