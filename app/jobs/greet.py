"""Define the infrastructure-free greeting job example.

Its payload contains only a serializable recipient value.
"""

from dataclasses import dataclass
from typing import ClassVar

from app.services.greeting import GreetingService
from titanspan.queue import Job


@dataclass(frozen=True, slots=True)
class GreetRecipient(Job):
    """Return a configured greeting through native Queue execution.

    The job uses only an application service supplied by the native Container.
    """

    recipient: str
    job_name: ClassVar[str | None] = "app.greet-recipient"

    def handle(self, greeting: GreetingService) -> str:
        """Build the message using a Container-resolved app service.

        Args:
            greeting: Application service resolved for this job attempt.

        Returns:
            The greeting returned by the synchronous Queue connection.
        """
        return greeting.greet(self.recipient)
