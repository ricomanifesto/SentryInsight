"""Public site origins, read from the committed publication/site.json.

Each site has a legacy Pages root and a confirmed production origin; the
"emitted" origin is the one current pages, metadata and links use. Validators
accept either configured origin while the sites move between them, so reports
that carry the legacy origin keep validating unchanged.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

SITE_CONFIG_PATH = Path(__file__).resolve().parents[2] / "publication" / "site.json"
SITES = ("SentryDigest", "SentryInsight", "GRCInsight")


@lru_cache(maxsize=1)
def _origins() -> dict[str, dict[str, str]]:
    origins = json.loads(SITE_CONFIG_PATH.read_text())["origins"]
    for site in SITES:
        entry = origins[site]
        if entry["legacy"] != f"https://ricomanifesto.github.io/{site}/":
            raise ValueError(f"{site} legacy origin is not its Pages root")
        production = entry["production"]
        if not production.startswith("https://") or not production.endswith(".com/"):
            raise ValueError(f"{site} production origin must be an https host root")
        if entry["emitted"] not in ("legacy", "production"):
            raise ValueError(f"{site} emitted origin must be legacy or production")
    return origins


def emitted_origin(site: str) -> str:
    entry = _origins()[site]
    return entry[entry["emitted"]]


def accepted_origins(site: str) -> tuple[str, ...]:
    entry = _origins()[site]
    return (entry["legacy"], entry["production"])


def rewrite_public_urls(text: str) -> str:
    """Project retained legacy links onto the configured serving origins.

    Only the exact, configured URL roots are changed. Paths, query strings,
    fragments, and the immutable source reports remain untouched.
    """
    for site in SITES:
        entry = _origins()[site]
        text = text.replace(entry["legacy"], emitted_origin(site))
    return text
