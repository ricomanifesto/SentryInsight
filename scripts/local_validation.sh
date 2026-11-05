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
# The closed runner/capture proofs must execute in CI, never skip because the
# author's private fixture path is absent. This is the exact public snapshot.
export SENTRY_FROZEN_FEED="$PWD/tests/fixtures/full-feed-canary.xml"
uv run python -B -c 'import os; from pathlib import Path; from scripts.prepare_full_feed_canary import verify_feed; verify_feed(Path(os.environ["SENTRY_FROZEN_FEED"]).read_bytes())'
uv run python -B -W error -m pytest tests -q -p no:cacheprovider
uv run python -B scripts/validate_report.py index.md
uv run python -B scripts/build_site.py --check
uv run python -B scripts/package_pages.py --output test-results/pages
npm ci
npm run test:browser
