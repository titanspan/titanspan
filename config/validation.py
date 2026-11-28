"""Configure native Pydantic-backed application validation."""

from titanspan.support import env

config = {
    "strict": env("VALIDATION_STRICT", False),
    "from_attributes": env("VALIDATION_FROM_ATTRIBUTES", False),
}
