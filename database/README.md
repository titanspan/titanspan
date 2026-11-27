# Database integration

The framework revision pinned in `pyproject.toml` still packages Database as
an optional component. Its `database` extra supplies SQLAlchemy, Alembic, and
SQLite support; Foundation selects the Database provider only when those
dependencies are installed, and the framework Console registers Database
commands conditionally.

This application keeps the conventional migration, factory, and seeder
directories ready for native files. It does not add the framework extra,
duplicate its dependencies, or register an optional built-in provider. The
framework integration prerequisite is to make Database dependencies and
provider and Console registration part of the standard installation. Add the
SQLite configuration, model, migration, factory, and seeder after that
revision is pinned and verified.
