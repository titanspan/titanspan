"""Exercise application job registration with the native Queue fake.

The fake records application payloads without connecting to a broker.
"""

import pytest
from app.jobs.greet import GreetRecipient
from bootstrap.app import create_application
from titanspan.facades.queue import Queue


@pytest.mark.integration
@pytest.mark.anyio
async def test_queue_fake_records_the_registered_job() -> None:
    """Dispatch through the app Queue facade without opening a broker.

    The test verifies registration and serialization of the recipient payload.
    """
    application = create_application()

    async with application:
        async with Queue.fake() as fake:
            receipt = await Queue.dispatch_async(GreetRecipient("Ada"))

            assert receipt.state == "queued"
            fake.assert_pushed(GreetRecipient)
            fake.assert_pushed_with(GreetRecipient, recipient="Ada")
