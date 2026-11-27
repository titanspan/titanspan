"""Expose the canonical Titanspan ASGI application to an ASGI server.

The module exports the single instance created by the bootstrap factory.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bootstrap.app import create_application

if TYPE_CHECKING:
    from fastapi import FastAPI

application = create_application()
app: FastAPI = application.asgi

__all__ = ["app", "application"]
