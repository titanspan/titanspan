"""Declare application-specific service and Queue provider behavior.

Foundation continues to register all other native framework providers.
"""

from app.jobs.greet import GreetRecipient
from app.services.greeting import GreetingService
from titanspan.contracts.container import ServiceRegistry
from titanspan.contracts.foundation import ServiceProvider
from titanspan.queue import QueueServiceProvider


class AppServiceProvider(ServiceProvider):
    """Bind services owned by the application to Titanspan's Container."""

    def register(self, container: ServiceRegistry) -> None:
        """Register the greeting service used by the API example.

        Args:
            container: Canonical application service registry.
        """
        container.singleton(GreetingService, GreetingService)


class AppQueueServiceProvider(QueueServiceProvider):
    """Replace Queue's default provider with this application's trusted jobs."""

    def __init__(self) -> None:
        """Register only job classes owned by this application."""
        super().__init__(jobs=(GreetRecipient,))
