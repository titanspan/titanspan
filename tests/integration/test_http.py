"""Exercise native route discovery, dependency injection, and ASGI lifecycle."""

import pytest
from bootstrap.app import create_application
from fastapi.testclient import TestClient
from titanspan.testing import ApplicationTest


@pytest.mark.integration
def test_http_routes_use_native_test_context(
    application_test: ApplicationTest,
) -> None:
    """Serve welcome, health, and API routes through native testing.

    The fixture closes the application after the in-process requests.
    """
    application = application_test.application
    client = application_test.client
    assert application.is_started

    welcome = client.get("/")
    assert welcome.status_code == 200
    assert welcome.headers["content-type"].startswith("text/html")
    assert "Engineer beyond limits." in welcome.text

    health = client.get("/health")
    assert health.status_code == 200
    assert health.json() == {"status": "ok"}

    greeting = client.get("/api/v1/greetings/Ada")
    assert greeting.status_code == 200
    assert greeting.json() == {
        "application": "Titanspan",
        "message": "Hello from Titanspan, Ada!",
    }

    assert application.is_started


@pytest.mark.integration
def test_production_bootstrap_serves_only_public_assets() -> None:
    """Mount the tracked public assets and close the canonical application."""
    application = create_application()
    with TestClient(application.asgi) as client:
        asset = client.get("/assets/titanspan-mark.png")
        assert asset.status_code == 200
        assert asset.headers["content-type"] == "image/png"
        assert b"<svg" not in asset.content
        private_path = client.get("/storage/app/private")
        assert private_path.status_code == 404

    assert not application.is_started
