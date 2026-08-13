"""CVE identifier extraction."""

import re

CVE_ID_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])CVE[-\s]?(\d{4})[-\s]?(\d{4,})" r"(?![A-Za-z0-9]|\.\.\.|…)",
    re.IGNORECASE,
)


def extract_cve_ids(text: str) -> list[str]:
    """Extract normalized CVE IDs in source order without duplicates."""
    cve_ids = (
        f"CVE-{match.group(1)}-{match.group(2)}"
        for match in CVE_ID_PATTERN.finditer(text)
    )
    return list(dict.fromkeys(cve_ids))
