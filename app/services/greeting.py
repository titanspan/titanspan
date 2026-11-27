"""Provide the application greeting used by HTTP and Console examples.

The service keeps the sample business rule independent of each entrypoint.
"""

from typing import Annotated

from titanspan.container import FromConfig


class GreetingService:
    """Create greetings using the application's configured name.

    The name comes from the native configuration repository.
    """

    def __init__(
        self,
        application_name: Annotated[str, FromConfig("app.name")],
    ) -> None:
        """Retain the configured name for each greeting.

        Args:
            application_name: Name loaded from the application config.
        """
        self._application_name = application_name

    @property
    def application_name(self) -> str:
        """Return the configured application name.

        The value is fixed for this service instance.
        """
        return self._application_name

    def greet(self, name: str) -> str:
        """Create a greeting for one recipient.

        Args:
            name: Recipient to greet.

        Returns:
            A greeting containing the configured application name.
        """
        return f"Hello from {self._application_name}, {name}!"
