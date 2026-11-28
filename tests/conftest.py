"""Share real Titanspan application test contexts across the suite."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from bootstrap.providers import application_providers
from titanspan.testing import ApplicationTest, AsyncApplicationTest

_APPLICATION_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def application_test() -> Iterator[ApplicationTest]:
    """Start one synchronous native test application for a test.

    Yields:
        The real Application and in-process ASGI client.
    """
    test_application = ApplicationTest(
        base_path=_APPLICATION_ROOT,
        service_providers=application_providers(),
    )
    with test_application:
        yield test_application


@pytest.fixture
def async_application_test() -> AsyncApplicationTest:
    """Create one asynchronous native test application for a test.

    Returns:
        The real Application and asynchronous in-process ASGI client context.
    """
    return AsyncApplicationTest(
        base_path=_APPLICATION_ROOT,
        service_providers=application_providers(),
    )
