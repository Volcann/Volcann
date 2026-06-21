.PHONY: help setup test lint lint-yaml clean

.DEFAULT_GOAL := help

help:
	@echo "========================================================================"
	@echo "                       Volcann DevEx Task Runner                        "
	@echo "========================================================================"
	@echo "Available commands:"
	@echo "  make setup      - Install pre-commit hooks and prepare development env"
	@echo "  make test       - Run the local python validation tests"
	@echo "  make lint       - Run yaml lint and pre-commit checks locally"
	@echo "  make clean      - Clean up temporary python cache files"
	@echo "========================================================================"

setup:
	@if command -v pre-commit >/dev/null 2>&1; then \
		pre-commit install; \
	else \
		pip install pre-commit; \
		pre-commit install; \
	fi

test:
	python3 -m unittest discover -s tests

lint: lint-yaml
	@if command -v pre-commit >/dev/null 2>&1; then \
		pre-commit run --all-files; \
	else \
		python3 -m unittest discover -s tests; \
	fi

lint-yaml:
	@if command -v yamllint >/dev/null 2>&1; then \
		yamllint -c .yamllint .github/workflows/*.yml; \
	fi

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
