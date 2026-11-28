"""Define application commands for native Titanspan Console discovery."""

from titanspan.contracts import ConsoleOutput


def inspire(output: ConsoleOutput) -> None:
    """Display the Titanspan application slogan.

    Args:
        output: Native terminal output resolved by the application Container.
    """
    output.write("Engineer beyond limits.")
