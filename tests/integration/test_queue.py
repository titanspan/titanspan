"""Exercise application job registration with the native Queue fake.

The fake records application payloads without connecting to a broker.
"""

import pytest
from app.jobs.greet import GreetRecipient
from titanspan.facades.queue import Queue
from titanspan.testing import AsyncApplicationTest


@pytest.mark.integration
@pytest.mark.anyio
async def test_queue_fake_records_the_registered_job(
    async_application_test: AsyncApplicationTest,
) -> None:
    """Dispatch through the app Queue facade without opening a broker.

    The test verifies registration and serialization of the recipient payload.
    """
    async with async_application_test:
        with async_application_test.application.context():
            async with Queue.fake() as fake:
                receipt = await Queue.dispatch_async(
                    GreetRecipient("Ada"),
                )

                assert receipt.state == "queued"
                fake.assert_pushed(GreetRecipient)
                fake.assert_pushed_with(GreetRecipient, recipient="Ada")


@pytest.mark.integration
@pytest.mark.anyio
async def test_sync_connection_executes_registered_job(
    async_application_test: AsyncApplicationTest,
) -> None:
    """Run the registered job inline with Container-injected services."""
    async with async_application_test:
        with async_application_test.application.context():
            receipt = await Queue.dispatch_async(
                GreetRecipient("Ada"),
                connection="sync",
            )

    assert receipt.state == "executed"
    assert receipt.result == "Hello from Titanspan, Ada!"
