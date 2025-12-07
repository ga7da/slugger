import asyncio
import logging
import sys
import typing

import redis.asyncio as redis
from config import (
    ALPHABET,
    BATCH,
    MAX_POOL_SIZE,
    NEXT_ID_KEY,
    POOL_KEY,
    REDIS_URL,
)
from sqids import Sqids

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("pool_worker")

r = redis.from_url(REDIS_URL)

sqids = Sqids(min_length=6, alphabet=ALPHABET)


def encode_single(number: int) -> str:
    return sqids.encode([number])


async def generate_pool():
    logger.info("Starting pool generation...")

    while True:
        try:
            pool_size = await typing.cast(typing.Awaitable[int], r.scard(POOL_KEY))
            logger.info(f"Current pool size: {pool_size}/{MAX_POOL_SIZE}")

            if pool_size >= MAX_POOL_SIZE:
                logger.info("Pool is full, sleeping for 10 seconds...")
                await asyncio.sleep(10)
                continue

            next_id = await r.incrby(NEXT_ID_KEY, BATCH)
            start_id = next_id - BATCH

            slugs = [encode_single(i) for i in range(start_id, next_id)]
            await typing.cast(typing.Awaitable[int], r.sadd(POOL_KEY, *slugs))

            logger.info(
                f"Added {BATCH} new slugs to pool (IDs {start_id}-{next_id - 1})"
            )
            logger.info(f"Updated pool size: {pool_size + BATCH}")

            await asyncio.sleep(1)

        except Exception as e:
            logger.error(f"Error in pool generation: {str(e)}")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(generate_pool())
