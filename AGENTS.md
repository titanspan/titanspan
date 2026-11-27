# Application guidance

This repository is the official starter for applications built with
Titanspan. Keep it small, runnable, and focused on application-owned code.

## Repository boundaries

- The framework distribution and import namespace are `titanspan` and are
  maintained in <https://github.com/titanspan/framework>.
- This repository is an application, named `titanspan-app` for local project
  tooling. Do not copy framework internals or change framework APIs here.
- Report starter defects in this repository. Report framework defects and
  framework feature requests in the framework repository.
- Consult <https://titanspan.github.io/framework/> and the pinned framework
  source before relying on an API. The framework is pre-alpha; confirm its
  roadmap before adopting unfinished components.

## Application structure

- `bootstrap/app.py` is the application composition root.
- `config/` contains trusted Titanspan configuration mappings.
- `routes/` contains native `register_routes(router)` discovery hooks.
- `app/http/controllers/` contains HTTP actions.
- `app/http/middleware/` contains app-owned HTTP policies when needed.
- `app/jobs/` contains native Queue jobs with serializable payloads.
- `app/models/` contains application models when supported by an integrated
  framework component.
- `app/services/` contains application business logic.
- `app/providers/` binds application services to the native container.
- `app/console/` contains native application commands.
- `database/migrations/`, `database/factories/`, and `database/seeders/`
  reserve application-owned Database conventions. Check `database/README.md`
  for the current framework integration prerequisite.
- `tests/unit/` and `tests/integration/` separate isolated behavior from
  real framework and ASGI integration.
- Add agents, tools, workflows, memory, jobs, or data-processing modules only
  when the framework exposes the APIs the application needs. Do not add mock
  engines or empty placeholder modules.

## Engineering standards

- Use strict type annotations, absolute imports, four-space Python indentation,
  and an 80-column source limit.
- Follow Ruff formatting and lint rules and keep Pyright in strict mode.
- Keep blocking work explicit and preserve sync/async boundaries.
- Add Google-style multiline docstrings for public application code.
- Use the Titanspan application container, configuration loader, Console,
  HTTP, and Routing APIs; do not introduce competing infrastructure.

## Development commands

- `make install` installs the locked environment with uv.
- `make dev` starts the ASGI application.
- `make console ARGS="greet developer"` runs the sample Console command.
- `make console ARGS="queue:greet developer"` runs a native sync job.
- `make test` runs unit and integration tests.
- `make lint`, `make format`, and `make typecheck` run the individual checks.
- `make syntax` checks Python compilation.
- `make ci` runs the lock, lint, format, syntax, type, and test checks.

## Tests and configuration

- Add a unit test for isolated behavior and an integration test when changing
  routes, service registration, or the application lifecycle.
- Keep integration tests local and deterministic; do not require paid APIs or
  external databases, brokers, or model providers to start the starter.
- Map environment values explicitly from `config/` using Titanspan's `env`
  helper. Keep `.env`, credentials, private data, and production secrets out
  of Git. Keep debug mode disabled in production.
- Update `uv.lock` whenever project dependencies or the pinned framework
  revision change. Do not add framework runtime dependencies directly unless
  application code requires them.
