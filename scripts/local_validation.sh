#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export PYTHONDONTWRITEBYTECODE=1

uv sync --group dev --frozen
uv run ruff check .
uv run black --check .
uv run ty check
# Prepare the same explicit, hash-verified tokenizer cache used by the manual
# verification workflow, including on clean CI runners with no inherited cache.
export TIKTOKEN_CACHE_DIR="${TIKTOKEN_CACHE_DIR:-$PWD/test-results/tokenizer}"
uv run python -B -c 'import tiktoken; tiktoken.get_encoding("cl100k_base")'
uv run python -B -W error -m pytest tests -q -p no:cacheprovider
uv run python -B scripts/validate_report.py index.md
uv run python -B scripts/build_site.py --check
uv run python -B scripts/package_pages.py --output test-results/pages
npm ci
npm run test:browser
