.PHONY: help setup format format-check lint test test-coverage build serve

help:
	@printf "Available targets:\n"
	@printf "  setup          Create virtualenv and install dependencies\n"
	@printf "  format         Format the codebase\n"
	@printf "  format-check   Check formatting without modifying files\n"
	@printf "  lint           Run linting and type checks\n"
	@printf "  test           Run tests without coverage\n"
	@printf "  test-coverage  Run tests with coverage enforcement\n"
	@printf "  build          Build distribution artifacts\n"

setup:
	uv sync --extra dev

format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

lint:
	uv run ruff check .
	uv run ty check

test:
	uv run pytest --no-cov

test-coverage:
	uv run pytest

build:
	uv build

serve:  ## Start the development server
	uv run uvicorn package_sorter.api:app --reload
