"""Configure native ASGI request limits and pooled HTTP clients."""

from app.environment import decimal_env, integer_env
from titanspan.support import env

config = {
    "server": {
        "max_body_size": integer_env("HTTP_MAX_BODY_SIZE", 10_485_760),
        "max_form_files": integer_env("HTTP_MAX_FORM_FILES", 100),
        "max_form_fields": integer_env("HTTP_MAX_FORM_FIELDS", 1000),
        "max_part_size": integer_env("HTTP_MAX_PART_SIZE", 1_048_576),
    },
    "client": {
        "timeout": decimal_env("HTTP_CLIENT_TIMEOUT", 5.0),
        "connect_timeout": decimal_env("HTTP_CONNECT_TIMEOUT", 5.0),
        "max_connections": integer_env("HTTP_MAX_CONNECTIONS", 100),
        "max_keepalive_connections": integer_env(
            "HTTP_MAX_KEEPALIVE_CONNECTIONS",
            20,
        ),
        "keepalive_expiry": decimal_env("HTTP_KEEPALIVE_EXPIRY", 5.0),
        "follow_redirects": env("HTTP_FOLLOW_REDIRECTS", False),
        "verify_tls": env("HTTP_VERIFY_TLS", True),
        "base_url": env("HTTP_CLIENT_BASE_URL", ""),
        "http2": env("HTTP_CLIENT_HTTP2", False),
    },
}
