"""Exercise native Cache, Filesystem, Hashing, and Logging services."""

import pytest
from titanspan.facades.cache import Cache
from titanspan.facades.hash import Hash
from titanspan.facades.log import Log
from titanspan.facades.storage import Storage
from titanspan.testing import ApplicationTest


@pytest.mark.integration
def test_native_services_use_application_defaults(
    application_test: ApplicationTest,
) -> None:
    """Resolve default infrastructure through the native app context."""
    with application_test.application.context():
        assert Cache.put("starter:status", {"ready": True})
        assert Cache.get("starter:status") == {"ready": True}

        with Storage.fake("local") as fake:
            assert Storage.disk("local").put("welcome.txt", "ready")
            fake.assert_exists("welcome.txt")

        password_hash = Hash.make("local-test-password")
        assert Hash.check("local-test-password", password_hash)
        assert not Hash.check("incorrect-password", password_hash)

        Log.info("Titanspan application services are ready")
