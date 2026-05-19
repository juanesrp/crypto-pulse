import core.redis as redis_core

SET_KEY = "connected:users"


async def add_user(user_id: str):

    await redis_core.redis_client.sadd(SET_KEY, f"user:{user_id}")


async def remove_user(user_id: str):

    await redis_core.redis_client.srem(SET_KEY, f"user:{user_id}")


async def get_connected_count() -> int:

    return await redis_core.redis_client.scard(SET_KEY)


async def is_connected(user_id: str) -> bool:

    result = await redis_core.redis_client.sismember(SET_KEY, f"user:{user_id}")
    return bool(result)
