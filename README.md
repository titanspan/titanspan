![Titanspan mark](assets/titanspan-mark.png)

# Titanspan

**Engineer beyond limits.**

[![CI](https://github.com/titanspan/titanspan/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/titanspan/titanspan/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Titanspan is an expressive, async-first Python framework for intelligent
applications, AI agents, stateful workflows, and high-throughput data
processing.

This repository provides the official application skeleton for building with
Titanspan. It depends on the framework and keeps application code separate
from framework infrastructure.

## About Titanspan

The framework is pre-alpha and has not been published to PyPI. This skeleton
pins it to a verified commit on the framework's `main` branch. The working
example uses Foundation, configuration, dependency injection, HTTP, Routing,
and Console. The framework roadmap identifies AI agents, stateful workflows,
and authentication as planned, with advanced Database and Queue capabilities
still in progress. The sample Queue job runs inline by default. This starter
does not configure persistence, an external queue broker, authentication, or
an AI provider.

- Framework repository: <https://github.com/titanspan/framework>
- Documentation: <https://titanspan.github.io/framework/>
- Roadmap: <https://github.com/titanspan/framework/blob/main/ROADMAP.md>

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)
- GNU Make (optional; the same commands are available through `uv run`)

## Installation

```sh
git clone https://github.com/titanspan/titanspan.git
cd titanspan
uv sync --locked
cp .env.example .env
```

The lockfile pins the framework source commit. No separate framework checkout
or external service is required.

## Environment configuration

`config/app.py` maps these settings through Titanspan's configuration loader:

| Variable | Default | Purpose |
| --- | --- | --- |
| `APP_NAME` | `Titanspan` | Name shown by the example application. |
| `APP_ENV` | `local` | Application environment label. |
| `APP_DEBUG` | `false` | Enables detailed development diagnostics when set to `true`. |
| `QUEUE_CONNECTION` | `sync` | Runs registered jobs inline without a broker. |
| `QUEUE_DEFAULT_QUEUE` | `default` | Logical queue name used by the example. |

Keep secrets in your local `.env` or deployment environment. Do not commit
credentials or enable debug mode in production.

## Running the application

```sh
make dev
```

The server listens on <http://127.0.0.1:8000>. The same command can be run
without Make:

```sh
uv run uvicorn app.asgi:app --reload
```

Example endpoints:

- `GET /` returns the welcome response.
- `GET /health` returns the local health status.
- `GET /api/v1/greetings/{name}` returns a configured JSON greeting.

Foundation's ASGI lifecycle supplies request context, request IDs, validation
responses, and safe generic server errors. Add app-specific middleware or
exception handlers through the native builder when an application policy
needs them.

The native Titanspan Console uses the same application service and lifecycle.
The queue command dispatches a registered job through the native synchronous
connection:

```sh
make console ARGS="greet developer"
make console ARGS="queue:greet developer"
```

## Running tests

```sh
make test
```

The suite includes an isolated service test and integration tests for HTTP,
native Queue fakes, the Console, route discovery, dependency injection, and
application shutdown. Run `make ci` to check the lockfile, lint, formatting,
syntax, strict types, and both test groups.

## Application structure

```text
app/
  console/                 Native application command
  http/middleware/         Application-owned HTTP middleware
  http/controllers/        Application-owned HTTP controller
  jobs/                    Native Queue job declarations
  models/                  Application-owned models
  providers/               Application service registrations
  services/                Application business logic
  asgi.py                   Canonical ASGI application
bootstrap/app.py            Titanspan composition root
config/app.py               Environment-backed app settings
config/queue.py             Synchronous native Queue settings
database/
  factories/                Application data factories
  migrations/               Database schema migrations
  seeders/                  Development data seeders
routes/web.py               Native route discovery hook
storage/                    Application runtime files
tests/integration/          Real ASGI application behavior
tests/unit/                 Isolated application behavior
```

Add application modules when they have a real use. As framework APIs become
available, applications can organize their own agents, tools, workflows,
memory, and data-processing code under `app/`; this starter does not provide
temporary engines for those features. Database model, migration, factory, and
seeder examples await the framework's standard Database dependencies and
automatic provider and Console registration. See [Database integration](database/README.md).

## Documentation

Read the [Titanspan documentation](https://titanspan.github.io/framework/)
for verified framework APIs and the [framework repository](https://github.com/titanspan/framework)
for source, issues, and framework contributions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for skeleton-specific contribution
guidance. Report framework defects and propose framework APIs in
[titanspan/framework](https://github.com/titanspan/framework).

## License

This skeleton is available under the [MIT License](LICENSE), consistent with
the Titanspan framework.
