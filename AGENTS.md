# Application guidance

This repository is the official application skeleton for Titanspan. Keep it
conventional, runnable, and focused on application-owned code.

## Repository boundaries

- The framework distribution and import namespace are `titanspan`; its
  canonical repository is <https://github.com/titanspan/framework>.
- This project is named `titanspan-app` for local tooling. Do not publish it as
  the `titanspan` distribution or copy framework internals here.
- Consult <https://titanspan.github.io/framework/> and the exact framework
  revision in `uv.lock` before relying on a public API.
- Report skeleton defects in this repository. Report framework defects and
  feature requests to <https://github.com/titanspan/framework>.
- The framework is pre-alpha. Read its roadmap and the open
  [integration requirements](https://github.com/titanspan/titanspan/issues/1)
  before adopting unfinished components.

## Application structure

- `bootstrap/app.py` is the canonical application composition root. Preserve
  Foundation's lifecycle and add only app-owned providers or settings.
- `bootstrap/providers.py` lists app-owned providers and supplies fresh
  instances to native testing helpers.
- `bootstrap/cache/` is reserved for generated framework bootstrap artifacts.
- `config/` contains trusted Titanspan configuration mappings. Map environment
  values explicitly through Titanspan's `env` helper and use accepted native
  keys only.
- `app/environment.py` converts numeric dotenv values into the integer and
  decimal types expected by strict native configuration contracts.
- `routes/web.py` and `routes/api.py` expose native
  `register_routes(router)` hooks. `routes/console.py` declares app commands
  discovered through the `titanspan.commands` entry point.
- `app/http/controllers/` contains HTTP actions; `app/services/` contains
  application business logic; `app/providers/` contains application-specific
  bindings and lifecycle behavior.
- `app/jobs/` contains trusted native Queue jobs with serializable payloads.
- Add `app/models/`, `database/` components, agents, tools, workflows, memory,
  or data-processing modules only when the pinned framework exposes the
  required native APIs. Do not add empty packages, mock engines, an app-owned
  ORM, or replacement infrastructure.
- `public/assets/` contains files explicitly served at `/assets`. Keep private
  application files under `storage/app/private/`; do not expose that directory.
- `storage/` is for local runtime files. Generated logs, caches, databases,
  credentials, and test artifacts must remain ignored.
- `tests/unit/` covers isolated application behavior. `tests/integration/`
  covers the real Framework and ASGI behavior.

## Framework ownership and current boundaries

Foundation automatically registers native providers. Do not register built-in
providers from application code. `AppServiceProvider` owns application
bindings; `AppQueueServiceProvider` extends the native Queue provider only to
register trusted application jobs.

The current pinned revision provides infrastructure-free defaults for
in-memory Cache, local Filesystem, Argon2id Hashing, console Logging, and
synchronous Queue execution. Redis Cache and Redis or RabbitMQ Queue
connections may be selected when their framework driver integrations are
installed. Do not make those external services necessary to install or start
the application.

Database does not yet have verified standard-install dependencies, provider,
or commands at the pinned revision. Do not add speculative Database
configuration, models, migrations, factories, or seeders. Authentication,
Sessions, Mail, and native Views also remain framework-dependent; check the
framework documentation and issue #1 before documenting or using them.

The native global Console discovers built-in commands and app command entry
points, but its public API does not currently accept this application's full
bootstrap factory while retaining the built-in catalog. Likewise, native
`ApplicationTest` helpers accept providers and configuration rather than a
complete factory. Preserve focused coverage of both the native helpers and
`bootstrap.app.create_application`; track missing framework contracts in
issue #1 instead of adding duplicate runtimes.

## Engineering standards

- Use strict type annotations, absolute imports, four-space indentation, and
  a maximum of 80 columns for Python source.
- Follow Ruff lint and format rules; keep Pyright in strict mode.
- Preserve explicit sync and async boundaries. Keep blocking work out of async
  handlers.
- Add physically multiline Google-style docstrings for public application
  code and comments only when they explain non-obvious behavior.
- Use Titanspan's Application, Container, Configuration, Console, HTTP,
  Routing, and component APIs. Do not introduce competing infrastructure.
- Use uv exclusively for project dependency management. Update `uv.lock` when
  project dependencies or the framework revision changes.

## Development commands

- `make setup` installs the lock and creates local directories; it creates
  `.env` from `.env.example` only when no `.env` exists.
- `make install` installs the locked project and development dependencies.
- `make dev` starts the local ASGI application.
- `make console ARGS="about"` runs the native Titanspan command catalog.
- `make test` runs unit and integration tests.
- `make lint`, `make format`, `make typecheck`, and `make syntax` run
  individual checks.
- `make ci` runs the lock, lint, format, syntax, strict type, and test checks.
- For a production-only environment, run `uv sync --locked --no-dev` and
  serve `app.asgi:app` with Uvicorn.

## Tests and configuration

- Add a unit test for isolated behavior and an integration test when changing
  routes, provider registration, configuration, jobs, or lifecycle behavior.
- Keep tests deterministic and local. Do not require paid APIs, external
  databases, brokers, or model providers for the default suite.
- Exercise application services inside `application.context()` when using
  native facades outside an HTTP or job execution scope.
- Keep `.env`, credentials, private data, generated files, and local databases
  out of Git. Debug mode must remain disabled in production.
- Verify all documented commands and configuration against the pinned
  framework source. Never present planned or unfinished framework features as
  available.
