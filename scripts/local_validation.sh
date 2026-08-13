#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export PYTHONDONTWRITEBYTECODE=1

uv sync --group dev --frozen
uv run ruff check .
uv run black --check .
uv run ty check
uv run python -B -W error -m pytest tests -q -p no:cacheprovider
uv run python -B scripts/validate_report.py index.md
uv run python -B scripts/validate_report.py docs/index.md
