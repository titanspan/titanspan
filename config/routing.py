"""Configure native route discovery from the conventional routes folder."""

from titanspan.support import env

config = {
    "discover": env("ROUTES_DISCOVER", True),
    "modules": (),
}
