#!/usr/bin/env bash
# Synthetic-only validation for pull requests and main pushes. It reads no
# committed report, archive or rendered page, packages nothing, takes no
# screenshot and uploads nothing, so a code-only head validates without
# repackaging a prior release. scripts/local_validation.sh remains the
# offline/local legacy helper.
set -euo pipefail

cd "$(dirname "$0")/.."

export PYTHONDONTWRITEBYTECODE=1

uv sync --group dev --frozen
uv run ruff check .
uv run black --check .
uv run ty check
uv run python -B -W error -m pytest -q -p no:cacheprovider \
  tests/test_defensive_package.py \
  tests/test_defensive_workflows.py \
  tests/test_paid_readiness.py \
  tests/test_paid_verification.py \
  tests/test_critical_first_order.py \
  tests/test_vendor_link_references.py \
  tests/test_bounded_reasoning_route.py
node --test --test-concurrency=1 publication/test/*.test.js
