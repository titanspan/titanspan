![Titanspan mark](public/assets/titanspan-mark.png)

# Titanspan

**Engineer beyond limits.**

[![CI](https://github.com/titanspan/titanspan/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/titanspan/titanspan/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Titanspan is an expressive, async-first Python framework for intelligent
applications, AI agents, stateful workflows, and high-throughput data
processing.

This repository is the official application skeleton for Titanspan. It keeps
application code here and relies on the separate framework distribution for
native infrastructure.

## About Titanspan

The framework is pre-alpha and is not published on PyPI. This project pins a
verified framework commit from `main` in `uv.lock`. The starter demonstrates
Foundation, configuration, dependency injection, HTTP, Routing, Console,
Cache, Filesystem, Hashing, Logging, and synchronous Queue execution. Other
capabilities remain under development; see the
[framework roadmap](https://github.com/titanspan/framework/blob/main/ROADMAP.md)
and [integration requirements](https://github.com/titanspan/titanspan/issues/1).

- Framework: <https://github.com/titanspan/framework>
- Documentation: <https://titanspan.github.io/framework/>

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)
- GNU Make (optional)

## Installation

```sh
git clone https://github.com/titanspan/titanspan.git
cd titanspan
make setup
```

`make setup` installs the locked dependencies, creates local runtime
directories, and copies `.env.example` to `.env` only when `.env` does not
already exist. The application uses the pinned framework Git dependency; a
separate framework checkout is not required.

The same dependency installation is available with `uv sync --locked`.
`titanspan-app` is the local application project name. It is not the framework
distribution and is not published.

## Environment configuration

`config/` contains the native Titanspan configuration mappings. The defaults
run locally without external infrastructure:

- Cache uses process-local memory.
- Queue uses synchronous execution.
- Filesystem uses private local storage; public assets are mounted separately
  from `public/assets/`.
- Hashing uses Argon2id.
- Logging writes to the console.

Review `.env.example` for supported environment values. Keep credentials in
your local environment, do not commit `.env`, and keep debug mode disabled in
production. Redis and RabbitMQ Queue connections and Redis Cache are selectable
when their framework driver integrations are installed. They are not needed
for the default application.

## Running the application

Start the development server:

```sh
make dev
```

The application listens on <http://127.0.0.1:8000>. Its public endpoints are:

- `GET /` displays the branded welcome page.
- `GET /health` returns the application health status.
- `GET /api/v1/greetings/{name}` returns a JSON greeting.

`public/assets/` is mounted at `/assets`. Private application storage is not
served. To run with production dependencies from the checkout:

```sh
uv sync --locked --no-dev
uv run uvicorn app.asgi:app --host 0.0.0.0 --port 8000
```

Foundation owns the application lifecycle, request context, routing,
validation responses, and generic error handling. `bootstrap/app.py` is the
canonical ASGI composition root. The framework's current global Console does
not expose a public way to use this factory while retaining its built-in
command catalog; see the tracked [framework integration requirement](https://github.com/titanspan/titanspan/issues/1).

## Console and development commands

The framework's native Console includes its built-in commands and discovers
the application `inspire` command through the declared entry point:

```sh
make console ARGS="about"
make console ARGS="route:list"
make console ARGS="config:validate"
make console ARGS="inspire"
```

The Console and ASGI server use native application discovery from the project
root. Database migration and seeding commands are not available in the pinned
framework revision; SQLite integration is tracked in
[issue #1](https://github.com/titanspan/titanspan/issues/1). A Queue worker
requires a configured queued backend and its driver integration; the default
sync connection executes jobs inline and does not need a worker.

GNU Make targets:

| Command | Purpose |
| --- | --- |
| `make setup` | Install dependencies and safely initialize local files. |
| `make install` | Install the locked environment with uv. |
| `make dev` | Run the local ASGI server with reload enabled. |
| `make console ARGS="about"` | Run the native Titanspan Console. |
| `make test` | Run unit and integration tests. |
| `make lint` | Run Ruff lint checks. |
| `make format` | Format Python source with Ruff. |
| `make typecheck` | Run strict Pyright checks. |
| `make ci` | Run lock, lint, formatting, syntax, type, and test checks. |

## Application structure

```text
app/
  http/controllers/       Application HTTP actions
  jobs/                   Trusted native Queue jobs
  providers/              Application-specific container bindings
  services/               Application business logic
bootstrap/
  app.py                  Canonical Application composition root
  providers.py            Shared application provider inventory
  cache/                  Framework-generated bootstrap artifacts
config/                   Native component configuration
database/                 Database integration notes; native APIs pending
public/assets/            Publicly served branding and CSS
routes/
  api.py                  JSON API routes
  console.py              Application Console command discovery
  web.py                  Welcome and health routes
storage/
  app/private/            Private application files
  app/public/             Application-owned public disk files
  framework/              Runtime and test artifacts
  logs/                   Local file logs when selected
tests/
  conftest.py             Shared native application test helpers
  integration/            Framework, HTTP, Console, and Queue behavior
  unit/                   Isolated application behavior
```

The project declares its application providers and commands through native
`titanspan.providers` and `titanspan.commands` entry points. Foundation
automatically registers native framework providers. Add app-owned agents,
tools, workflows, memory, or data-processing code when the framework APIs they
need are available; this starter does not include substitute engines.

## Testing

```sh
make test
make ci
```

Integration tests use Titanspan's application testing helpers for HTTP,
configuration, and Queue behavior, and exercise the canonical ASGI bootstrap
and its shutdown lifecycle. The framework test helpers currently accept
provider inventories rather than the complete application factory; that
integration gap is recorded in [issue #1](https://github.com/titanspan/titanspan/issues/1).

## Documentation and contribution

- [Titanspan documentation](https://titanspan.github.io/framework/)
- [Framework source and contributions](https://github.com/titanspan/framework)
- [Skeleton contribution guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

Report starter issues in this repository. Direct framework defects and
framework feature requests to
[titanspan/framework](https://github.com/titanspan/framework).

## License

This skeleton is available under the [MIT License](LICENSE), consistent with
the Titanspan framework.
