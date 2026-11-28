"""Configure native memory and optional Redis Cache stores."""

from titanspan.support import env

config = {
    "default": env("CACHE_STORE", "memory"),
    "prefix": env("CACHE_PREFIX", "titanspan"),
    "stores": {
        "memory": {"driver": "memory"},
        "redis": {
            "driver": "redis",
            "options": {
                "url": env(
                    "CACHE_REDIS_URL",
                    "redis://127.0.0.1:6379/0",
                ),
            },
        },
    },
}
