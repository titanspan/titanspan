"""Register application commands with the native Titanspan Console.

Every command uses the framework-owned parser and application lifecycle.
"""

from typing import Annotated

from app.jobs.greet import GreetRecipient
from app.services.greeting import GreetingService
from bootstrap.app import create_application
from titanspan import Application
from titanspan.console import Argument, Console
from titanspan.contracts import ConsoleOutput
from titanspan.contracts.foundation import ServiceProvider
from titanspan.facades.queue import Queue


def _create_console_application(provider: ServiceProvider) -> Application:
    """Build an application that includes Console's output binding.

    Args:
        provider: Output provider supplied by the native command host.

    Returns:
        An application using the canonical service container and lifecycle.
    """
    return create_application(provider)


console = Console(
    name="titanspan-app",
    description="Engineer beyond limits.",
    application_factory=_create_console_application,
)


@console.command("greet")
def greet(
    name: Annotated[str, Argument(description="Name to greet.")],
    greeting: GreetingService,
    output: ConsoleOutput,
) -> None:
    """Print a greeting using the application service.

    Args:
        name: Recipient supplied on the command line.
        greeting: Service resolved from the application container.
        output: Native terminal output service.
    """
    output.write(greeting.greet(name))


@console.command("queue:greet")
def queue_greet(
    name: Annotated[str, Argument(description="Name to greet.")],
    output: ConsoleOutput,
) -> None:
    """Run a registered job on the default synchronous connection.

    Args:
        name: Recipient supplied on the command line.
        output: Native terminal output service.
    """
    receipt = Queue.dispatch_sync(GreetRecipient(name))
    if not isinstance(receipt.result, str):
        raise TypeError("The greeting job returned no message.")
    output.write(receipt.result)
