"""Run the application-owned Titanspan Console.

The module entrypoint delegates parsing and execution to the native Console.
"""

from app.console import console


def main() -> None:
    """Parse and execute the selected application command.

    Console owns command output and application startup and shutdown.
    """
    console.run()


if __name__ == "__main__":
    main()
