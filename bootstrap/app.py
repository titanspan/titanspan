"""Compose one Titanspan application for HTTP and Console hosts.

Foundation remains the owner of built-in services and application lifecycle.
"""

from pathlib import Path

from app.jobs.greet import GreetRecipient
from app.providers.greeting import GreetingServiceProvider
from titanspan import Application
from titanspan.contracts.foundation import ServiceProvider
from titanspan.queue import QueueServiceProvider

_APPLICATION_ROOT = Path(__file__).resolve().parents[1]


def create_application(
    *additional_providers: ServiceProvider,
) -> Application:
    """Build the application from its root, config files, and providers.

    Configuration is loaded by Titanspan from ``config/`` under the
    application root. Routes are discovered from the same root at startup.
    The native ASGI host supplies request context and safe default error
    responses as part of the framework lifecycle.

    Args:
        *additional_providers: Host-specific providers registered after the
            application greeting provider.

    Returns:
        One fully composed, not-yet-started Titanspan application.
    """
    builder = Application.builder().with_base_path(_APPLICATION_ROOT)
    builder.with_service_provider(GreetingServiceProvider())
    # Replace Foundation's built-in provider with this app's trusted jobs.
    builder.with_service_provider(
        QueueServiceProvider(jobs=(GreetRecipient,)),
    )
    for provider in additional_providers:
        builder.with_service_provider(provider)
    return builder.build()
