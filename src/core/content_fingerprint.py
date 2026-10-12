"""Track the source article set behind the last published report.

The analysis model runs at temperature=1, so the rendered report text
never matches byte-for-byte between runs even when the underlying
articles are unchanged. Fingerprinting the retained article evidence (rather
than the model's rendered output) lets the workflow detect "nothing new
happened" and skip the paid analysis/TTS steps entirely.
"""

import hashlib
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from .reporting import (
    ReportingGroundingError,
    normalize_reporting_url,
    prepare_reporting_input,
)

FINGERPRINT_PATH = ".sentryinsight-articles-fingerprint"


def compute_articles_fingerprint(articles: List[Dict[str, Any]]) -> str:
    """Identify the normalized evidence actually consumed by generation."""
    groups: dict[str, list[str]] = {}
    for article in articles:
        prepared = prepare_reporting_input(article)
        try:
            identity = normalize_reporting_url(prepared.url)
        except ReportingGroundingError:
            identity = prepared.url or prepared.title
        record = json.dumps(asdict(prepared), sort_keys=True, ensure_ascii=False)
        groups.setdefault(identity, []).append(record)
    # Different sources may arrive in any order. Conflicting versions of one
    # source retain their order: generation's existing duplicate policy has not
    # changed. Only an entirely identical group is safely collapsed.
    records = [
        [group[0]] if len(set(group)) == 1 else group
        for _, group in sorted(groups.items())
    ]
    payload = json.dumps({"semantic_input_version": 2, "sources": records})
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def read_stored_fingerprint(path: str = FINGERPRINT_PATH) -> Optional[str]:
    """Read the fingerprint recorded for the last published report, if any."""
    fingerprint_path = Path(path)
    if not fingerprint_path.exists():
        return None
    return fingerprint_path.read_text().strip() or None


def write_stored_fingerprint(fingerprint: str, path: str = FINGERPRINT_PATH) -> None:
    """Persist the fingerprint for the report just published."""
    Path(path).write_text(fingerprint + "\n")
