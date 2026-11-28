"""Configure native event discovery and its generated manifest path."""

from titanspan.support import env

config = {
    "discovery_modules": (),
    "manifest_path": env(
        "EVENTS_MANIFEST_PATH",
        "bootstrap/cache/events.json",
    ),
    "deferred_buffer_limit": 10_000,
    "max_dispatch_depth": 32,
}
