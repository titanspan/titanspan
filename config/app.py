"""Map documented process and dotenv settings into app configuration.

The native ``env`` helper reads process and local dotenv values.
"""

from titanspan.support import env

config = {
    "name": env("APP_NAME", "Titanspan"),
    "env": env("APP_ENV", "local"),
    "debug": env("APP_DEBUG", False),
    "url": env("APP_URL", "http://127.0.0.1:8000"),
}
