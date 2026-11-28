"""Configure private, public, and memory Filesystem disks."""

from titanspan.support import env

config = {
    "default": env("FILESYSTEM_DISK", "local"),
    "disks": {
        "local": {
            "driver": "local",
            "root": "storage/app/private",
        },
        "public": {
            "driver": "local",
            "root": "storage/app/public",
        },
        "memory": {"driver": "memory"},
    },
}
