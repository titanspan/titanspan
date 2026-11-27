"""Exercise native route discovery, dependency injection, and ASGI lifecycle.

The client checks HTTP output, service injection, startup, and shutdown.
"""

import pytest
from bootstrap.app import create_application
from fastapi.testclient import TestClient


@pytest.mark.integration
def test_http_routes_use_native_di_and_close_the_application() -> None:
    """Serve all starter endpoints through the real application lifecycle.

    The context-managed client closes the application after the requests.
    """
    application = create_application()

    with TestClient(application.asgi) as client:
        assert application.is_started

        welcome = client.get("/")
        assert welcome.status_code == 200
        assert welcome.json() == {
            "application": "Titanspan",
            "message": "Hello from Titanspan, developer!",
            "slogan": "Engineer beyond limits.",
        }

        health = client.get("/health")
        assert health.status_code == 200
        assert health.json() == {"status": "ok"}

        greeting = client.get("/api/v1/greetings/Ada")
        assert greeting.status_code == 200
        assert greeting.json() == {
            "application": "Titanspan",
            "message": "Hello from Titanspan, Ada!",
        }

    assert not application.is_started
