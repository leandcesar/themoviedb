.DEFAULT_GOAL := help

PYTHON ?= python3
VENV ?= .venv
VENV_BIN := $(VENV)/bin
VENV_PYTHON := $(VENV_BIN)/python
VENV_STAMP := $(VENV)/.installed
PIP := $(VENV_PYTHON) -m pip
CHECK_PATHS := examples themoviedb tests
REQUIREMENTS := requirements.txt requirements-test.txt requirements-dev.txt

.PHONY: help install hooks-install test testall lint format format-check security hooks check

help: ## List available targets.
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ {printf "%-14s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

$(VENV_STAMP): $(REQUIREMENTS)
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade -r requirements-dev.txt
	touch $(VENV_STAMP)

install: $(VENV_STAMP) ## Create or update the development environment.

hooks-install: install ## Install the repository Git hooks.
	$(VENV_BIN)/pre-commit install --install-hooks

test: install ## Run the full test suite.
	$(VENV_PYTHON) -m pytest

testall: install ## Run tests with every configured Nox interpreter.
	$(VENV_PYTHON) -m nox

lint: install ## Run static analysis.
	$(VENV_BIN)/ruff check .
	$(VENV_BIN)/mypy themoviedb

format: install ## Apply Black and isort formatting.
	$(VENV_BIN)/black $(CHECK_PATHS)
	$(VENV_BIN)/isort $(CHECK_PATHS)

format-check: install ## Verify formatting without changing files.
	$(VENV_BIN)/black --check $(CHECK_PATHS)
	$(VENV_BIN)/isort --check-only $(CHECK_PATHS)

security: install ## Run security-oriented checks.
	$(VENV_BIN)/pre-commit run bandit --all-files
	$(VENV_BIN)/pre-commit run detect-private-key --all-files

hooks: install ## Run every pre-commit hook on the repository.
	$(VENV_BIN)/pre-commit run --all-files

check: lint format-check security test ## Run the local quality gate.
