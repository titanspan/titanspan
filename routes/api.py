"""Register versioned JSON API routes."""

from app.http.controllers.welcome import WelcomeController
from titanspan.routing import Router


def register_routes(router: Router) -> None:
    """Attach the starter API routes to the native Router.

    Args:
        router: Canonical route catalog supplied by Titanspan.
    """
    router.get(
        "/api/v1/greetings/{name}",
        (WelcomeController, "greet"),
    ).name("api.greetings.show")
