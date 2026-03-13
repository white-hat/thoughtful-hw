# Package Sorter

A small, production-style Python solution for Smarter Technology's package dispatch task.

## Problem

Implement `sort(width, height, length, mass)` to route packages into one of three stacks:

- `STANDARD`: neither bulky nor heavy
- `SPECIAL`: bulky or heavy, but not both
- `REJECTED`: both bulky and heavy

Rules:

- A package is bulky when its volume is at least `1_000_000 cm^3`
- A package is also bulky when any dimension is at least `150 cm`
- A package is heavy when its mass is at least `20 kg`

## Project layout

- `src/package_sorter/`: application code
- `tests/`: unit tests covering decision boundaries and representative scenarios

## Quick start

This repository is set up for `uv`, `ruff`, `ty`, and `pytest`.

## Environment setup

1. Install `uv` if it is not already available.
2. Ensure Python `3.11` or newer is available to `uv`.
3. Create the virtual environment and install dependencies:

```bash
make setup
```

This creates `.venv` and installs the project with the development toolchain.

If Python `3.11` is not installed yet, you can install it with:

```bash
uv python install 3.11
```

## Development commands

```bash
make help
make format
make lint
make test
make test-coverage
```

Run `make help` to see the available commands.

## Build package

This repository can be built as a standard Python package.

```bash
make build
```

This creates distribution artifacts in `dist/`.

## Coverage

Test coverage is configured through `pytest-cov` and generates:

- terminal coverage with missing lines
- a failing exit code when total coverage drops below `80%`

## Input behavior

- dimensions are interpreted as centimeters
- mass is interpreted as kilograms
- non-positive inputs raise `ValueError`

## CI

GitHub Actions runs `make setup`, `make format-check`, `make lint`, and `make test-coverage`
on each push and pull request across Python `3.11` and `3.14`.

## Example

```python
from package_sorter import sort

assert sort(100, 100, 100, 10) == "SPECIAL"
assert sort(10, 10, 10, 1) == "STANDARD"
assert sort(150, 10, 10, 20) == "REJECTED"
```
