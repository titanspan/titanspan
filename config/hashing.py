"""Configure the native password hashing algorithms and work factors."""

from app.environment import integer_env
from titanspan.support import env

config = {
    "driver": env("HASHING_DRIVER", "argon2id"),
    "argon2id": {
        "time_cost": integer_env("ARGON2_TIME_COST", 3),
        "memory_cost": integer_env("ARGON2_MEMORY_COST", 65_536),
        "parallelism": integer_env("ARGON2_PARALLELISM", 4),
        "hash_length": integer_env("ARGON2_HASH_LENGTH", 32),
        "salt_length": integer_env("ARGON2_SALT_LENGTH", 16),
    },
    "bcrypt": {
        "rounds": integer_env("BCRYPT_ROUNDS", 12),
        "prefix": env("BCRYPT_PREFIX", "2b"),
    },
    "max_concurrent_operations": integer_env("HASH_MAX_CONCURRENCY", 2),
}
