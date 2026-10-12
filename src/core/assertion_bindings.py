"""Shared existing subject and complete CVE/object binding productions."""

from dataclasses import dataclass
import re
from typing import Literal
from .cve import CVE_ID_PATTERN, extract_cve_ids

CVE_LIST = rf"{CVE_ID_PATTERN.pattern}(?:\s*(?:,\s*(?:and\s+)?|and\s+){CVE_ID_PATTERN.pattern})*"
NAME = r"[A-Z][A-Za-z0-9'-]*(?: [A-Z][A-Za-z0-9'-]*){0,6}"
PRODUCT_HEAD = (
    r"operating systems?|systems?|software|servers?|gateways?|appliances?|switch(?:es)?"
)
PRODUCT_PRODUCTION = rf"(?P<name>{NAME}) (?P<data>data center )?(?P<network>network )?(?P<head>{PRODUCT_HEAD})"
# Embedding the same production must not duplicate named captures in a parent
# relation. Its accepted language remains the typed product owner's language.
PRODUCT_NOMINAL = re.sub(r"\(\?P<\w+>", "(?:", PRODUCT_PRODUCTION)


@dataclass(frozen=True)
class ProductBinding:
    text: str
    name: str
    modifiers: tuple[str, ...]
    head: str


def bind_product(text):
    """Bind a complete named product argument, never an arbitrary noun tail."""
    match = re.fullmatch(PRODUCT_PRODUCTION, text)
    if match is None:
        return None
    return ProductBinding(
        text,
        match["name"],
        tuple(match[key].strip() for key in ("data", "network") if match[key]),
        match["head"],
    )


@dataclass(frozen=True)
class TargetBinding:
    text: str
    start: int
    end: int
    cves: tuple[str, ...] = ()
    kind: str = "empty"


def bind_target(text: str, start: int = 0, *, implicit: bool = False):
    """Consume an exact existing identity list or complete implicit object."""
    match = re.match(rf"(?:{CVE_LIST})\b", text[start:], re.I)
    kind = "explicit"
    if match is None and implicit:
        match = re.fullmatch(
            r"(?:(?:the|a|an|another) (?:(?:vulnerable|affected) )?[a-z]+|it)",
            text[start:].rstrip(" .!?"),
            re.I,
        )
        kind = "implicit"
    if match is None:
        return None
    end = start + match.end()
    value = text[start:end]
    return TargetBinding(value, start, end, tuple(extract_cve_ids(value)), kind)


DESCRIPTIVE_SUBJECT = re.compile(
    rf"^(?i:(?:two|the) )(?:(?:[A-Z][A-Za-z0-9-]* ){{0,4}})"
    rf"(?i:zero-days|vulnerabilities|flaws) \((?P<identities>{CVE_LIST})\)\s+"
)


@dataclass(frozen=True)
class SubjectBinding:
    """A complete nominal prefix; predicate semantics belong to its consumer."""

    kind: Literal["vulnerability", "actor"]
    text: str
    end: int


SUBJECT_PRODUCTIONS = (
    ("vulnerability", DESCRIPTIVE_SUBJECT),
    (
        "actor",
        re.compile(
            r"^(?:the\s+)?(?:attackers?|operators?|(?:threat\s+)?actors?)\s+",
            re.I,
        ),
    ),
)


def bind_subject(text: str) -> SubjectBinding | None:
    """Bind a closed subject production without discarding unknown modifiers.

    Actor determiners and compound heads are nominal ownership, not predicate
    modifiers. Any unconsumed bridge remains with the strict predicate owner.
    """
    if target := bind_target(text):
        end = target.end
        while end < len(text) and text[end].isspace():
            end += 1
        return SubjectBinding("vulnerability", target.text, end)
    for kind, production in SUBJECT_PRODUCTIONS:
        if match := production.match(text):
            return SubjectBinding(kind, match.group().rstrip(), match.end())
    return None


REPORTER_SUBJECT = r"(?:[Tt]he (?:vendor|company|researchers|agencies)|[A-Z][A-Za-z/-]*(?: [A-Z][A-Za-z/-]*){0,3}|it)"
