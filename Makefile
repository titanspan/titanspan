.DEFAULT_GOAL := help

.PHONY: help setup install dev console test test-unit test-integration lint format \
	format-check syntax typecheck ci

help: ## Show available development commands
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z_-]+:.*## / {printf "%-18s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install the locked application and development dependencies
	uv sync --locked

setup: install ## Install dependencies and safely prepare local directories
	@mkdir -p storage/app/private storage/app/public
	@mkdir -p storage/framework/cache storage/framework/testing storage/logs
	@if test -e .env; then \
		printf '%s\n' '.env exists; leaving it unchanged'; \
	else \
		cp -n .env.example .env; \
	fi

dev: ## Start the local ASGI application with reload enabled
	uv run uvicorn app.asgi:app --reload

console: ## Run the unified native catalog (pass ARGS="about")
	uv run titanspan $(ARGS)

test: test-unit test-integration ## Run unit and HTTP integration tests

test-unit: ## Run isolated application tests
	uv run pytest tests/unit

test-integration: ## Run real ASGI application tests
	uv run pytest tests/integration

lint: ## Check Python source with Ruff
	uv run ruff check app bootstrap config routes tests

format: ## Format Python source with Ruff
	uv run ruff format app bootstrap config routes tests

format-check: ## Check Ruff formatting without changing files
	uv run ruff format --check app bootstrap config routes tests

syntax: ## Compile application and test Python files
	uv run python -m compileall -q app bootstrap config routes tests

typecheck: ## Run strict Pyright checks
	uv run pyright

ci: install lint format-check syntax typecheck test ## Run the local CI checks
