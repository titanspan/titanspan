"""Convert normalized environment values into native numeric settings."""

import math

from titanspan.support import env


def integer_env(name: str, default: int) -> int:
    """Read one integer setting from process or dotenv configuration.

    Args:
        name: Environment key mapped by application configuration.
        default: Integer used when the key is unset.

    Returns:
        The configured integer value.

    Raises:
        ValueError: If a configured value is not an integer literal.
    """
    value = env(name, default)
    if isinstance(value, bool):
        raise ValueError(f"Environment variable [{name}] must be an integer.")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as error:
            message = f"Environment variable [{name}] must be an integer."
            raise ValueError(message) from error
    raise ValueError(f"Environment variable [{name}] must be an integer.")


def decimal_env(name: str, default: float) -> float:
    """Read one finite numeric setting from process or dotenv configuration.

    Args:
        name: Environment key mapped by application configuration.
        default: Floating point value used when the key is unset.

    Returns:
        The configured finite float value.

    Raises:
        ValueError: If a configured value is not a finite number.
    """
    value = env(name, default)
    if isinstance(value, bool):
        raise ValueError(f"Environment variable [{name}] must be numeric.")
    if isinstance(value, (int, float)):
        selected = float(value)
    elif isinstance(value, str):
        try:
            selected = float(value)
        except ValueError as error:
            message = f"Environment variable [{name}] must be numeric."
            raise ValueError(message) from error
    else:
        raise ValueError(f"Environment variable [{name}] must be numeric.")
    if not math.isfinite(selected):
        raise ValueError(f"Environment variable [{name}] must be finite.")
    return selected
