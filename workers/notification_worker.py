import json
from core.redis import redis_client

QUEUE_KEY = "notifications:queue"


async def process_notifications():
    print("Worker de notificaciones inciado")

    while True:

        result = await redis_client.brpop(QUEUE_KEY, timeout=1)

        if result:

            _, message = result

            notification = json.loads(message)

            print(
                f"Notificacion procesada | "
                f"usuario: {notification['user_id']} | "
                f"{notification} | "
                f"umbral: ${notification['threshold']} | "
            )
