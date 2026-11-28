"""Exercise native framework commands and application command discovery."""

import pytest
from bootstrap.app import create_application
from titanspan.console import Console
from titanspan.console.cli import console as framework_console
from titanspan.console.testing import ConsoleTester


@pytest.mark.integration
def test_native_catalog_discovers_application_inspire_command() -> None:
    """Keep application commands in the framework's native command catalog."""
    native_console = framework_console.discover_commands()
    result = ConsoleTester(native_console).invoke(["inspire"])

    assert result.exit_code == 0
    assert "Engineer beyond limits." in result.stdout


@pytest.mark.integration
def test_custom_factory_has_an_independent_command_catalog() -> None:
    """Show the current public factory and built-in catalog composition gap."""
    native_console = framework_console.discover_commands()
    native_help = ConsoleTester(native_console).invoke(["--help"])
    application_console = Console(application_factory=create_application)
    application_help = ConsoleTester(application_console).invoke(["--help"])

    assert native_help.exit_code == 0
    assert "route:list" in native_help.stdout
    assert "inspire" in native_help.stdout
    assert application_help.exit_code == 0
    assert "route:list" not in application_help.stdout
