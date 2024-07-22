.PHONY: help install uninstall reinstall test lint format security clear
.DEFAULT_GOAL := help

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

define PRINT_HELP_PYSCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?$$', line)
	if match:
		target = match.groups()
		print("%s" % (target))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

$(VENV)/bin/activate: requirements-dev.txt requirements-test.txt requirements.txt
	@python3 -m venv $(VENV)
	@$(PIP) install -U pip
	@$(PIP) install -r requirements-dev.txt
	@$(VENV)/bin/pre-commit install
	@$(VENV)/bin/pre-commit install --hook-type commit-msg

install: $(VENV)/bin/activate

uninstall:
	@rm -rf $(VENV)

reinstall: uninstall install

test: $(VENV)/bin/activate
	@$(VENV)/bin/pytest --cov-report html

testall: $(VENV)/bin/activate
	@$(VENV)/bin/nox

lint: $(VENV)/bin/activate
	@$(VENV)/bin/pre-commit run mypy --all-files
	@$(VENV)/bin/pre-commit run ruff --all-files

format: $(VENV)/bin/activate
	@$(VENV)/bin/pre-commit run black --all-files
	@$(VENV)/bin/pre-commit run isort --all-files
	@$(VENV)/bin/pre-commit run check-docstring-first --all-files
	@$(VENV)/bin/pre-commit run end-of-file-fixer --all-files
	@$(VENV)/bin/pre-commit run fix-encoding-pragma --all-files
	@$(VENV)/bin/pre-commit run trailing-whitespace --all-files

security: $(VENV)/bin/activate
	@$(VENV)/bin/pre-commit run bandit --all-files
	@$(VENV)/bin/pre-commit run detect-private-key --all-files
	@$(VENV)/bin/pre-commit run debug-statements --all-files

clear:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@rm -fr .tox/
	@rm -fr .nox/
	@rm -f .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache
	@rm -fr .mypy_cache
	@rm -fr .ruff_cache
