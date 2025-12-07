import os

REDIS_URL = os.getenv("SLUGGER_REDIS_URL", "redis://localhost:6379/0")

POOL_KEY = os.getenv("SLUGGER_POOL_KEY", "slugs:pool")
NEXT_ID_KEY = os.getenv("SLUGGER_NEXT_ID_KEY", "slugs:next_id")

BATCH = int(os.getenv("SLUGGER_BATCH", "100000"))
MAX_POOL_SIZE = int(os.getenv("SLUGGER_MAX_POOL_SIZE", "300000"))

ALPHABET = os.getenv(
    "SLUGGER_ALPHABET",
    "xP0HzRo4ZVWAByj71sTXYOfGJEQmgqCdMei6hpSbc25NKwUt9lL3IF8nDkvaru",
)
