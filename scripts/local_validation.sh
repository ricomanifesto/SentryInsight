#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export PYTHONDONTWRITEBYTECODE=1

python3 -B -m pytest tests -q -p no:cacheprovider
python3 -B scripts/validate_report.py index.md
