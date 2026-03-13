# AGENTS

## Purpose

Maintain a small, reliable Python solution for the package sorting task.

## Stack

- Python with `uv`
- Lint/format: `ruff`
- Type checks: `ty`
- Tests/coverage: `pytest`, `pytest-cov`

## Project rules

- Keep application code in `src/package_sorter/`
- Keep tests in `tests/`
- Prefer simple, typed functions over extra abstraction
- Preserve the public API: `package_sorter.sort`
- Update tests for every behavior change

## Setup

Run `make setup` before starting if `.venv` is missing, or whenever dependencies change.

## Before finishing

Run:

```bash
make format
make lint
make test-coverage
```
