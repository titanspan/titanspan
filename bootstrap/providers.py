"""List application providers shared by bootstrap and native test helpers.

The same provider classes are declared as ``titanspan.providers`` entry
points so the framework's native CLI and workers discover the app services.
"""

from app.providers.application import (
    AppQueueServiceProvider,
    AppServiceProvider,
)
from titanspan.contracts.foundation import ServiceProvider

PROVIDER_TYPES: tuple[type[ServiceProvider], ...] = (
    AppServiceProvider,
    AppQueueServiceProvider,
)


def application_providers() -> tuple[ServiceProvider, ...]:
    """Create fresh application providers for one Application instance.

    Returns:
        Provider instances in the declared application order.
    """
    return tuple(provider_type() for provider_type in PROVIDER_TYPES)
