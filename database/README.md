# Database integration

The framework revision pinned in `pyproject.toml` still packages Database as
an optional component. Its `database` extra supplies SQLAlchemy, Alembic, and
SQLite support; Foundation selects the Database provider only when those
dependencies are installed, and the framework Console registers Database
commands conditionally.

The application pins framework revision
`ab0538c4cdeaa6d69fbaaf8b54eabd5eafca7be3`. At this revision, the clean
standard installation has no verified native Database provider or Database
Console commands.

This application keeps the conventional migration, factory, and seeder
responsibilities documented for later native files. It does not add the
framework extra, duplicate its dependencies, register an optional built-in
provider, or create speculative Database configuration and models. The
framework integration prerequisite is to make Database dependencies,
automatic provider registration, and Console registration part of the
standard installation. Then add SQLite configuration, the User model and
migration, a factory, a seeder, and native integration tests against the
verified public APIs.

Follow the canonical [Database integration issue](https://github.com/titanspan/titanspan/issues/1)
for the capability snapshot and acceptance criteria.
