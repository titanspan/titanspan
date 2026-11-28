"""Register browser-facing welcome and health routes.

Foundation discovers this module through the native route hook.
"""

from app.http.controllers.welcome import WelcomeController
from titanspan.routing import Router


def health() -> dict[str, str]:
    """Return the local application health status.

    Returns:
        A JSON-ready status mapping.
    """
    return {"status": "ok"}


def register_routes(router: Router) -> None:
    """Attach native routes to the application-owned Router.

    Args:
        router: Route catalog supplied by Titanspan during startup.
    """
    router.get("/", (WelcomeController, "index")).name("welcome")
    router.get("/health", health).name("health")
