"""Exercise the native Console command and its application services.

The tests use the production parser, container, and lifecycle.
"""

import pytest
from app.console import console
from titanspan.console.testing import ConsoleTester


@pytest.mark.integration
def test_greet_command_resolves_application_service() -> None:
    """Run the real parser and resolve the greeting through Titanspan DI.

    The command receives its service from the native application Container.
    """
    result = ConsoleTester(console).invoke(["greet", "Ada"])

    assert result.exit_code == 0
    assert "Hello from Titanspan, Ada!" in result.stdout


@pytest.mark.integration
def test_queue_command_executes_the_native_sync_job() -> None:
    """Resolve the registered job and return its result from inline work.

    The command exercises Queue's synchronous application connection.
    """
    result = ConsoleTester(console).invoke(["queue:greet", "Ada"])

    assert result.exit_code == 0
    assert "Hello from Titanspan, Ada!" in result.stdout
