"""Test the greeting service without starting external infrastructure.

This unit check exercises the application's business rule in isolation.
"""

import pytest
from app.services.greeting import GreetingService


@pytest.mark.unit
def test_greeting_uses_application_name_and_recipient() -> None:
    """Include both configured application and recipient in the message.

    The exact result verifies that both input values reach the service.
    """
    greeting = GreetingService("Example App")

    assert greeting.greet("Ada") == "Hello from Example App, Ada!"
