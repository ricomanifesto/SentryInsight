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
uv run python -B scripts/validate_report.py tests/fixtures/source_attribution_report.md \
  --require-source-attribution \
  --source-attribution-entry '- **CISA: exploited KEV update**: Example Research - https://example.test/kev' \
  --source-attribution-entry '- **Parenthesized URL report**: Example Source - https://example.test/report(1)' \
  --source-attribution-entry '- **Source-only exploitation report**: Example Source'
