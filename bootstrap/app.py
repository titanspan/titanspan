"""Compose the canonical Titanspan application for ASGI hosts.

Native framework providers are automatic. Trusted application providers are
discovered from this project's declared ``titanspan.providers`` entry points.
"""

from collections.abc import Mapping
from pathlib import Path
from typing import cast

from fastapi.staticfiles import StaticFiles
from titanspan import Application
from titanspan.config import ConfigManager
from titanspan.contracts.foundation import ServiceProvider

_APPLICATION_ROOT = Path(__file__).resolve().parents[1]
_PUBLIC_ASSETS = _APPLICATION_ROOT / "public" / "assets"


def create_application(
    *additional_providers: ServiceProvider,
) -> Application:
    """Build the application from its root and trusted provider inventory.

    Configuration is loaded by Titanspan from ``config/`` under the
    application root. Routes are discovered from ``routes/web.py`` and
    ``routes/api.py`` during startup. The default ASGI middleware and
    exception handling remain owned by Foundation.

    Args:
        *additional_providers: Host-specific providers, such as the native
            Console output binding, added to the same composition.

    Returns:
        One fully composed, not-yet-started Titanspan application.
    """
    builder = (
        Application.builder()
        .with_base_path(_APPLICATION_ROOT)
        .discover_providers()
        .with_logging(_logging_configuration())
    )
    for provider in additional_providers:
        builder.with_service_provider(provider)
    application = builder.build()
    application.asgi.mount(
        "/assets",
        StaticFiles(directory=_PUBLIC_ASSETS),
        name="public-assets",
    )
    return application


def _logging_configuration() -> Mapping[str, object]:
    """Read the logging namespace through Titanspan's trusted loader.

    Returns:
        Native logging settings from ``config/logging.py``.

    Raises:
        TypeError: If the logging configuration is not a mapping.
    """
    configuration = ConfigManager(_APPLICATION_ROOT).load().get("logging")
    if not isinstance(configuration, Mapping):
        raise TypeError("The logging configuration must be a mapping.")
    return cast("Mapping[str, object]", configuration)
