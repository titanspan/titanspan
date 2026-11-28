"""Configure the native console and local file logging channels."""

from pathlib import Path

from titanspan.support import env

config = {
    "default": env("LOG_CHANNEL", "console"),
    "channels": {
        "console": {
            "driver": "console",
            "level": env("LOG_LEVEL", "info"),
            "formatter": "console",
        },
        "single": {
            "driver": "single",
            "path": Path("storage/logs/titanspan.log"),
            "level": env("LOG_LEVEL", "info"),
            "formatter": "text",
        },
    },
}
