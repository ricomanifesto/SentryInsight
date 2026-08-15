"""Shared heading identity used by validation and static publication."""

import re


def normalize_heading_identity(value: str) -> str:
    """Return the normalized fragment identity for reader-visible heading text."""
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
