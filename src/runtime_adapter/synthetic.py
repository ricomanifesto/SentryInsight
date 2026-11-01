"""Synthetic fixtures for adapter tests and the local recovery demo.

The passing report is adapted from an existing workflow fixture that already
passes the unchanged validators. URLs use reserved example domains and the key
is a visibly fake placeholder.
"""

from __future__ import annotations

import copy
from typing import Any

FAKE_PROVIDER_KEY = "fake-openrouter-key-not-real"
SYNTHETIC_MODEL = "openrouter/example/synthetic-model:free"

_ARTICLES: list[dict[str, Any]] = [
    {
        "title": "Example report",
        "link": "https://example.test/report",
        "source": "Example Source",
        "content": (
            "CVE-2026-1234 is actively exploited in the wild. Install the update."
        ),
    }
]

PASSING_REPORT = """# Exploitation Report

## Executive Summary

Recent exploitation activity is concentrated in edge systems.

## Active Exploitation Details

### Example Vulnerability (CVE-2026-1234)
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: source-1e8f5cb3245d
- **Affected Versions**: Not stated in supplied sources.
- **Exceptions**: Not stated in supplied sources.
- **Recommended Actions**: CVE-2026-1234 is actively exploited in the wild. \
Install the update.
- **Vendor Links**: Not stated in supplied sources.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
"""

# Cites a reporting key that no supplied article provides.
GROUNDING_REJECTED_REPORT = PASSING_REPORT.replace(
    "- **Reporting**: source-1e8f5cb3245d", "- **Reporting**: source-000000000000"
)


def synthetic_articles() -> list[dict[str, Any]]:
    return copy.deepcopy(_ARTICLES)


def synthetic_config(**analysis: Any) -> dict[str, Any]:
    settings: dict[str, Any] = {
        "model": SYNTHETIC_MODEL,
        "max_tokens": 4000,
        "max_input_tokens": 100000,
    }
    settings.update(analysis)
    return {"analysis": settings}


def completion_body(text: str = PASSING_REPORT) -> dict[str, Any]:
    return {"choices": [{"message": {"content": text}}]}
