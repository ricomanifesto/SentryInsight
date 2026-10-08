"""Parse bounded source directives before projecting a single action badge.

Advice has an explicit audience/modal relationship. Bare imperatives require
complete recognized objects; a leading action word alone is not instruction
evidence. Unrecognized advice stays guidance, but cannot supply a guessed badge.
"""

from dataclasses import dataclass, replace
import re
from typing import Literal, Sequence

from .cve import CVE_ID_PATTERN
from .report_artifact import Action


@dataclass(frozen=True)
class DirectiveClause:
    verb: str
    object_text: str
    object_role: str | None
    polarity: Literal["affirmative", "negative"]


@dataclass(frozen=True)
class RecommendationDirective:
    source_text: str
    modality: Literal["advice", "imperative", "continuation"]
    clauses: tuple[DirectiveClause, ...]
    conditions: tuple[str, ...]
    ambiguous: bool = False


AUDIENCE = r"customers|users|admins|administrators|operators|owners|vendors|maintainers|organizations|you"
ADVICE = re.compile(
    rf"^(?:For [^,]+,\s*)?(?:{AUDIENCE})\b.*?\b"
    r"(?P<modal>should|must|needs? to|(?:are|is) (?:not )?"
    r"(?:advised|recommended|urged|encouraged) (?:not )?to)\s+(?P<body>.+)$",
    re.I,
)
NEGATION = re.compile(r"\b(?:not|never|no|neither|nor|don't)\b", re.I)
CONDITION = re.compile(
    r"\b(?:if|unless|until|when|only|provided|depending|may|might|could)\b.*",
    re.I,
)
VERBS = frozenset(
    {
        "install",
        "apply",
        "patch",
        "upgrade",
        "update",
        "consult",
        "review",
        "contact",
        "mitigate",
        "investigate",
        "monitor",
    }
)
# These are complete direct-object phrases, not substring cues. Modifiers stay
# in object_text; unknown objects cannot establish a bare imperative.
OBJECT_ROLES = {
    "identifier": CVE_ID_PATTERN.pattern,
    "patch": r"patch(?:es)?|updates?|hotfix(?:es)?|fix(?:es)?",
    "mitigation": r"workarounds?|mitigations?",
    "evidence": r"logs|indicators(?: of compromise)?|suspicious activity|alerts?|incidents?",
    "system": r"appliances?|systems?|servers?|gateways?|devices?|software|installations?|products?",
    "vulnerability": r"vulnerabilit(?:y|ies)|flaws?|risks?|issues?",
    "advisory": r"(?:vendor |security )?advisor(?:y|ies)|documentation",
    "support": r"support|(?:the )?vendor",
    "monitoring": r"(?:network )?traffic|activity",
}
OBJECT_MODIFIER = re.compile(
    r"\s+\b(?:for|on|with|from|before|after|until|when|if|only)\b", re.I
)
COORDINATION = re.compile(
    r"\s*(,\s*(?:and\s+|or\s+)?|;\s*|\band\b|\bor\b|\bthen\b)\s*", re.I
)


def _object_role(text: str, depth: int = 0) -> str | None:
    if depth > 2:
        return None
    modifier = OBJECT_MODIFIER.search(text)
    core = (text[: modifier.start()] if modifier else text).strip(" .!?")
    if modifier:
        relation = modifier.group().strip().casefold()
        tail = text[modifier.end() :].strip()
        if relation in {"before", "after"}:
            # A subordinate activity is context, not a coordinated directive.
            tail = re.sub(
                r"^(?:installing|applying|upgrading|updating|reviewing|monitoring|investigating|mitigating)\s+",
                "",
                tail,
                flags=re.I,
            )
        if (
            relation not in {"until", "when", "if", "only"}
            and _object_role(tail, depth + 1) is None
        ):
            return None
    core = re.sub(
        r"^(?:(?:the|a|an|available|latest|security)\s+)+", "", core, flags=re.I
    )
    # Coordinated objects (logs and traffic) remain objects, not directives.
    parts = re.split(r"\s+and\s+|,\s*", core, flags=re.I)
    roles = []
    for part in parts:
        role = next(
            (
                role
                for role, grammar in OBJECT_ROLES.items()
                if re.fullmatch(grammar, part, re.I)
            ),
            None,
        )
        if role is None:
            return None
        roles.append(role)
    return roles[0] if len(set(roles)) == 1 else "mixed"


def _clause(text: str, negative: bool) -> DirectiveClause | None:
    body = re.sub(r"^(?:(?:do not|don't|not|never)\s+)+", "", text, flags=re.I)
    words = body.split()
    while (
        words
        and words[0].casefold() not in VERBS
        and words[0].casefold().endswith("ly")
    ):
        words.pop(0)
    body = " ".join(words)
    verb, separator, obj = body.partition(" ")
    if verb.casefold() not in VERBS or not separator or not re.search(r"\w", obj):
        return None
    return DirectiveClause(
        verb.casefold(),
        obj,
        _object_role(obj),
        "negative" if negative or NEGATION.search(text) else "affirmative",
    )


def parse_recommendation(text: str) -> RecommendationDirective | None:
    """Retain instruction structure independently from action prioritization."""
    normalized = " ".join(text.split()).rstrip(".!")
    conditions = tuple(match.group() for match in CONDITION.finditer(normalized))
    if re.search(r"\b(?:do so|do it|this action|that action)\b", normalized, re.I):
        return RecommendationDirective(
            text, "continuation", (), conditions, bool(NEGATION.search(normalized))
        )
    advice = ADVICE.fullmatch(normalized)
    modality: Literal["advice", "imperative"] = "advice" if advice else "imperative"
    body = advice["body"] if advice else normalized
    negative = bool(advice and NEGATION.search(advice["modal"]))
    parts = COORDINATION.split(body)
    first = _clause(parts[0], negative)
    if not first:
        return (
            RecommendationDirective(text, modality, (), conditions, True)
            if advice
            else None
        )
    clauses = [first]
    ambiguous = "?" in normalized
    for connector, part in zip(parts[1::2], parts[2::2]):
        clause = _clause(part, negative)
        if clause:
            clauses.append(clause)
            if re.search(r"\bor\b", connector, re.I):
                conditions += ("Alternative source directives: " + body,)
        else:
            # A coordinated noun must complete a known object phrase. Unknown
            # verbs/clauses cannot silently disappear behind the first action.
            previous = clauses[-1]
            combined = previous.object_text + " and " + part
            role = _object_role(combined)
            ambiguous |= role is None
            clauses[-1] = replace(previous, object_text=combined, object_role=role)
    ambiguous |= any(c.object_role is None for c in clauses)
    if (
        modality == "imperative"
        and first.object_role is None
        and not re.match(r"^(?:do not|don't|never)\s+", body, re.I)
    ):
        return None
    return RecommendationDirective(
        text, modality, tuple(clauses), conditions, ambiguous
    )


def project_recommendation_action(directives: Sequence[RecommendationDirective]) -> str:
    """Project parsed affirmative clauses only; source qualifications dominate."""
    if any(
        d.ambiguous or d.conditions or any(c.polarity == "negative" for c in d.clauses)
        for d in directives
    ):
        return Action.NONE.value
    actions = set()
    for directive in directives:
        for clause in directive.clauses:
            verb, role = clause.verb, clause.object_role
            if verb in {"patch", "upgrade", "update"} or (
                verb in {"apply", "install"} and role == "patch"
            ):
                actions.add(Action.PATCH)
            elif verb == "mitigate" or (verb == "apply" and role == "mitigation"):
                actions.add(Action.MITIGATE)
            elif verb == "investigate" or (verb == "review" and role == "evidence"):
                actions.add(Action.INVESTIGATE)
            elif verb == "monitor":
                actions.add(Action.MONITOR)
    return next(
        (action.value for action in Action if action in actions), Action.NONE.value
    )
