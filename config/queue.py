"""Configure native Queue for synchronous local execution.

The default connection runs without an external broker.
"""

from titanspan.support import env

config = {
    "default_connection": env("QUEUE_CONNECTION", "sync"),
    "default_queue": env("QUEUE_DEFAULT_QUEUE", "default"),
    "connections": {"sync": {"driver": "sync"}},
}
