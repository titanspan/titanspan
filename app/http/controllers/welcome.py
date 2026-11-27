"""Handle the welcome page and the example JSON greeting endpoint.

Controller actions return JSON-ready data through native route dispatch.
"""

from app.services.greeting import GreetingService

_SLOGAN = "Engineer beyond limits."


class WelcomeController:
    """Serve a welcome response and configured greetings.

    Both actions delegate message creation to the application service.
    """

    def __init__(self, greeting: GreetingService) -> None:
        """Retain the service resolved by the Titanspan container.

        Args:
            greeting: Application-owned greeting service.
        """
        self._greeting = greeting

    def index(self) -> dict[str, str]:
        """Return the application welcome response.

        Returns:
            Application name, slogan, and a sample greeting.
        """
        return {
            "application": self._greeting.application_name,
            "message": self._greeting.greet("developer"),
            "slogan": _SLOGAN,
        }

    def greet(self, name: str) -> dict[str, str]:
        """Return a JSON greeting for one path parameter.

        Args:
            name: Recipient supplied in the route path.

        Returns:
            The configured application name and greeting.
        """
        return {
            "application": self._greeting.application_name,
            "message": self._greeting.greet(name),
        }
