"""Register the application greeting service with Titanspan.

This provider adds application-specific wiring to Foundation's Container.
"""

from app.services.greeting import GreetingService
from titanspan.contracts.container import ServiceRegistry
from titanspan.contracts.foundation import ServiceProvider


class GreetingServiceProvider(ServiceProvider):
    """Register the greeting service as an application singleton.

    The service lifetime is owned by the framework's application Container.
    """

    def register(self, container: ServiceRegistry) -> None:
        """Bind the service in the framework-owned container.

        Args:
            container: Canonical Titanspan service registry.
        """
        container.singleton(GreetingService, GreetingService)
