import asyncio

import redis.asyncio as redis
import typing
from sqids import Sqids

from config import (
    REDIS_URL,
    POOL_KEY,
    NEXT_ID_KEY,
    BATCH,
    MAX_POOL_SIZE,
    ALPHABET,
)

r = redis.from_url(REDIS_URL)

sqids = Sqids(min_length=6, alphabet=ALPHABET)


def encode_single(number: int) -> str:
    return sqids.encode([number])


async def generate_pool():
    while True:
        pool_size = await typing.cast(typing.Awaitable[int], r.scard(POOL_KEY))
        if pool_size >= MAX_POOL_SIZE:
            await asyncio.sleep(10)
            continue

        next_id = await r.incrby(NEXT_ID_KEY, BATCH)
        start_id = next_id - BATCH

        slugs = [encode_single(i) for i in range(start_id, next_id)]
        await typing.cast(typing.Awaitable[int], r.sadd(POOL_KEY, *slugs))

        current_size = await typing.cast(typing.Awaitable[int], r.scard(POOL_KEY))
