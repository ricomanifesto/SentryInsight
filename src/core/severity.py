"""Complete rating relations; source/document owners supply eligible spans.

A rating cue is retained even when its entire proposition cannot establish an
affirmative rating. No prefix, suffix, numeric maximum or model-selected prose
can override that uncertainty. This is optional triage evidence, not an event
or version parser.
"""

from dataclasses import dataclass
import re

from .assertion_bindings import CVE_LIST
from .assertion_qualifiers import NAME
from .cve import extract_cve_ids
from .advisory_relations import bind_advisory

BAND = r"critical|high|medium|low"
COUNT = r"\d+|one|two|three|four|five|six|seven|eight|nine|ten"
RATED_NOUN = rf"(?P<label>{BAND})(?:-severity)? (?:vulnerabilit(?:y|ies)|flaws?|bugs?)"
SUBJECT = rf"(?:{CVE_LIST}|[Ii]t|[Tt]he (?:vulnerability|flaw|bug))"
CVSS = (
    r"CVSS(?: v(?:ersion)?\s*[34](?:\.\d)?)?"
    r"(?:\s+(?:base )?(?:score|rating)(?: of| is)?\s*:?|\s*:)\s*"
    r"(?P<score>10(?:\.0)?|[0-9](?:\.\d)?)(?: out of 10(?:\.0)?)?"
)
RATING_CUE = re.compile(
    rf"\b(?:CVSS\b|severity(?: rating)?\s*:|rated (?:{BAND})\b|"
    rf"(?:{BAND})(?:-severity)? (?:vulnerabilit(?:y|ies)|flaws?|bugs?)\b)",
    re.I,
)


@dataclass(frozen=True)
class RatingRelation:
    text: str
    source_url: str = ""
    cves: tuple[str, ...] = ()
    source_block: str = ""
    start: int = 0
    end: int = 0
    predicate: str = "unclassified"
    values: tuple[str, ...] = ()
    complete: bool = False


@dataclass(frozen=True)
class SeverityAssessment:
    value: str
    relations: tuple[RatingRelation, ...]

    @property
    def context(self):
        return tuple(dict.fromkeys(relation.text for relation in self.relations))


def _band(score):
    value = float(score)
    return (
        "critical"
        if value >= 9
        else (
            "high"
            if value >= 7
            else "medium" if value >= 4 else "low" if value > 0 else "unknown"
        )
    )


# Each production consumes the complete proposition. Qualifications and
# unknown continuations remain in the unclassified relation, never stripped.
RATING_PRODUCTIONS = (
    ("label", rf"Severity(?: rating)?\s*:\s*(?P<label>{BAND})"),
    ("rated", rf"{SUBJECT} (?:is|was|are|were) rated (?P<label>{BAND})"),
    ("scalar", rf"(?:(?:a|an|the|{COUNT}) )?{RATED_NOUN}"),
    ("existence", rf"(?:A|An|The) {RATED_NOUN} (?:is|was|are|were) present"),
    (
        "identity",
        rf"{SUBJECT} (?:is|are|was|were) (?:a |an )?{RATED_NOUN}"
        rf"(?: in (?-i:{NAME}))?"
        rf"(?:, with a {CVSS}| that allows remote code execution)?",
    ),
    ("score_label", rf"(?:Its )?{CVSS}"),
    ("score_possession", rf"{SUBJECT} (?:has|carries|is assigned) a {CVSS}"),
    ("score_assignment", rf"{CVSS} (?:is|was|has been) assigned"),
)


def rating_relation(text, *, source_url="", cves=(), source_block=""):
    """Bind one complete source statement, preserving rejected rating data."""
    if not RATING_CUE.search(text):
        return None
    body = text.strip().removesuffix(".")
    values = ()
    predicate = "unclassified"
    if (
        (declaration := bind_advisory(text))
        and declaration.complete
        and not (declaration.declaration_conditions or declaration.relative_conditions)
    ):
        predicate = "advisory_declaration"
        values = (declaration.severity.lower(),)
    else:
        for kind, production in RATING_PRODUCTIONS:
            if match := re.fullmatch(production, body, re.I):
                predicate = kind
                groups = match.groupdict()
                values = tuple(
                    value
                    for value in (
                        groups.get("label", "").lower(),
                        _band(groups["score"]) if groups.get("score") else "",
                    )
                    if value
                )
                break
    block = source_block or text
    start = block.find(text)
    return RatingRelation(
        text,
        source_url,
        tuple(extract_cve_ids(text)) or tuple(cves),
        block,
        start,
        start + len(text) if start >= 0 else -1,
        predicate,
        values,
        bool(values),
    )


def project_ratings(relations):
    relations = tuple(relations)
    values = {value for relation in relations for value in relation.values}
    value = (
        next(iter(values))
        if len(values) == 1 and all(relation.complete for relation in relations)
        else "unknown"
    )
    return SeverityAssessment(value, relations)
