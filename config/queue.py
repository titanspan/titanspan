"""Configure native Queue with local and selectable broker connections.

The default connection runs synchronously without an external broker.
"""

from titanspan.support import env

config = {
    "default_connection": env("QUEUE_CONNECTION", "sync"),
    "default_queue": env("QUEUE_DEFAULT_QUEUE", "default"),
    "namespace": env("QUEUE_NAMESPACE", "titanspan"),
    "connections": {
        "sync": {"driver": "sync"},
        "redis": {
            "driver": "redis_stream",
            "options": {
                "url": env(
                    "QUEUE_REDIS_URL",
                    "redis://127.0.0.1:6379/0",
                ),
            },
        },
        "rabbitmq": {
            "driver": "rabbitmq",
            "options": {
                "url": env(
                    "QUEUE_RABBITMQ_URL",
                    "amqp://localhost:5672/%2F",
                ),
            },
        },
    },
}
