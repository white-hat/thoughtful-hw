# Package Sorter

A production-style Python package that routes packages into three distribution stacks based on physical dimensions and mass.

## What it does

**Public API:** `sort(width, height, length, mass) -> "STANDARD" | "SPECIAL" | "REJECTED"`

Routes packages by applying these rules:
- **STANDARD**: neither bulky nor heavy
- **SPECIAL**: bulky XOR heavy (one but not both)
- **REJECTED**: both bulky AND heavy

**Bulky** = volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
**Heavy** = mass ≥ 20 kg

Inputs must be positive (raises `ValueError` otherwise).

## Directory structure

```
src/package_sorter/
├── __init__.py          # Public exports: Stack, sort()
└── sorting.py           # Core logic: sort(), _is_bulky(), _validate_non_negative()

tests/
└── test_sorting.py      # 9 parametrized tests + edge case coverage
```

## Key files

- **`src/package_sorter/sorting.py`** – Core business logic (40 lines)
  - `Stack` enum (STANDARD, SPECIAL, REJECTED)
  - `sort()` – main entry point; validates and routes
  - `_is_bulky()` – volume/dimension check
  - `_validate_non_negative()` – input validation

- **`tests/test_sorting.py`** – 12 test cases covering:
  - All three routing paths
  - Volume threshold (1,000,000 cm³)
  - Dimension threshold (150 cm)
  - Mass threshold (20 kg)
  - Float inputs
  - Boundary conditions and invalid inputs

- **`pyproject.toml`** – Project metadata, Python 3.11+, dependencies (none), dev tools config
- **`Makefile`** – Common dev commands
- **`.github/workflows/ci.yml`** – CI runs on main/PRs, tests on Python 3.11 + 3.14

## Architecture

**Single responsibility:** Package routing using a simple function-based design with typed parameters and clear separation of concerns (validation → classification → routing).

No external dependencies. Direct boolean logic with `StrEnum` for stack names.

## Local development

```bash
# Setup
make setup                    # Create .venv and install with dev tools

# Daily commands
make format                   # Format with ruff
make lint                     # Check with ruff + ty (type checking)
make test                     # Run pytest (no coverage)
make test-coverage            # Run tests with 80% coverage enforcement

# Build
make build                    # Create dist/ artifacts

# Info
make help                     # List all targets
```

All commands use `uv run` to stay within the virtualenv.

## Tech stack

| Tool | Purpose | Config |
|------|---------|--------|
| **uv** | Dependency & venv management | `pyproject.toml` |
| **ruff** | Linting & formatting | `pyproject.toml [tool.ruff]` |
| **ty** | Type checking | `pyproject.toml [tool.ty]` |
| **pytest** | Testing; coverage enforcement (80% min) | `pyproject.toml [tool.pytest.ini_options]` |
| **hatchling** | Build backend | `pyproject.toml [build-system]` |

## Project rules

- Preserve public API: `package_sorter.sort`
- Keep app code in `src/package_sorter/`, tests in `tests/`
- Prefer simple, typed functions over abstraction
- Update tests for every behavior change
- Run `make format && make lint && make test-coverage` before finishing

## CI/CD

GitHub Actions (`ci.yml`):
- Runs on `push` to `main` and all PRs
- Matrix: Python 3.11, 3.14
- Steps: setup → format-check → lint → test-coverage

Fails the build if any tool fails.

## Common gotchas

- Inputs must be positive; zero or negative raises `ValueError` listing all invalid fields
- Float inputs are accepted (e.g., 19.99 kg is not heavy, 20.0 kg is)
- Dimensions are in centimeters, mass in kilograms
- No external dependencies — keep it that way
