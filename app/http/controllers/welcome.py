"""Render the branded welcome page and return the API greeting response."""

from html import escape

from app.services.greeting import GreetingService
from fastapi.responses import HTMLResponse

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

    def index(self) -> HTMLResponse:
        """Return a branded HTML welcome page.

        Returns:
            A small HTML page using the established public brand assets.
        """
        application_name = escape(self._greeting.application_name)
        return HTMLResponse(
            "<!doctype html>\n"
            '<html lang="en">\n'
            "<head>\n"
            '  <meta charset="utf-8">\n'
            '  <meta name="viewport" '
            'content="width=device-width, initial-scale=1">\n'
            f"  <title>{application_name} — {_SLOGAN}</title>\n"
            '  <link rel="stylesheet" href="/assets/app.css">\n'
            "</head>\n"
            "<body>\n"
            '  <main class="welcome">\n'
            '    <img class="mark" src="/assets/titanspan-mark.png" '
            'alt="Titanspan mark">\n'
            f'    <p class="eyebrow">{application_name}</p>\n'
            "    <h1>Engineer beyond limits.</h1>\n"
            '    <p class="intro">'
            "A clear foundation for ambitious Python applications."
            "</p>\n"
            '    <a href="https://titanspan.github.io/framework/">'
            "Explore the framework</a>\n"
            "  </main>\n"
            "</body>\n"
            "</html>\n",
        )

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
