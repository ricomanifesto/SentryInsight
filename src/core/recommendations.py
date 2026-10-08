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

ArgumentRelation = Literal["direct", "destination", "direct_destination"]
CoordinationRelation = Literal[
    "initial", "conjunctive", "alternative", "adversative", "sequential"
]


@dataclass(frozen=True)
class DirectiveClause:
    verb: str
    object_text: str
    object_role: str | None
    object_members: tuple[str, ...]
    polarity: Literal["affirmative", "negative"]
    conditions: tuple[str, ...]
    reference: bool = False
    argument_relation: ArgumentRelation = "direct"
    coordination: CoordinationRelation = "initial"


@dataclass(frozen=True)
class RecommendationDirective:
    source_text: str
    modality: Literal["advice", "imperative", "continuation", "unclassified"]
    clauses: tuple[DirectiveClause, ...]
    conditions: tuple[str, ...]
    ambiguous: bool = False


@dataclass(frozen=True)
class RecommendationBlock:
    source_text: str
    directives: tuple[RecommendationDirective | None, ...]


AUDIENCE = r"customers|users|admins|administrators|operators|owners|vendors|maintainers|organizations|you"
ADVICE_MODAL = (
    r"should|must|needs? to|(?:are|is) (?:not )?"
    r"(?:advised|recommended|urged|encouraged) (?:not )?to"
)
ADVICE_AUDIENCE = (
    rf"^(?:For {CVE_ID_PATTERN.pattern}(?: and {CVE_ID_PATTERN.pattern})*,\s*)?"
    rf"(?:{AUDIENCE})\b"
)
NEGATION = re.compile(r"\b(?:not|never|no|neither|nor|don't)\b", re.I)
CONDITION = re.compile(
    r"\b(?:if|unless|until|when|only|provided|depending|may|might|could)\b.*",
    re.I,
)
# A verb is insufficient to infer remediation. These closed argument frames
# own both recognized target shapes and their artifact projection.
ACTION_FRAMES: dict[str, dict[ArgumentRelation, dict[str, Action]]] = {
    "install": {"direct": {"patch": Action.PATCH}},
    "apply": {"direct": {"patch": Action.PATCH, "mitigation": Action.MITIGATE}},
    "patch": {
        "direct": dict.fromkeys(
            ("system", "identifier", "vulnerability", "release"), Action.PATCH
        )
    },
    **{
        verb: {
            "direct": dict.fromkeys(("system", "release"), Action.PATCH),
            "destination": {"release": Action.PATCH},
            "direct_destination": {"system": Action.PATCH},
        }
        for verb in ("upgrade", "update")
    },
    "mitigate": {
        "direct": dict.fromkeys(
            ("vulnerability", "identifier", "system"), Action.MITIGATE
        )
    },
    "investigate": {
        "direct": dict.fromkeys(
            ("evidence", "system", "vulnerability", "identifier"), Action.INVESTIGATE
        )
    },
    "review": {"direct": {"evidence": Action.INVESTIGATE, "advisory": Action.NONE}},
    "monitor": {
        "direct": dict.fromkeys(
            (
                "evidence",
                "monitoring",
                "advisory",
                "system",
                "identifier",
                "vulnerability",
            ),
            Action.MONITOR,
        )
    },
    "consult": {"direct": dict.fromkeys(("advisory", "support"), Action.NONE)},
    "contact": {"direct": {"support": Action.NONE}},
}
VERBS = frozenset(ACTION_FRAMES)
# These are complete direct-object phrases, not substring cues. Modifiers stay
# in object_text; unknown objects cannot establish a bare imperative.
OBJECT_ROLES = {
    "identifier": CVE_ID_PATTERN.pattern,
    "release": r"versions? \d+(?:\.\d+)*",
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
COORDINATION = re.compile(r"\s*((?:,\s*)?\b(?:and|or|but|then)\b|[,;])\s*", re.I)
COORDINATION_KINDS: dict[str, CoordinationRelation] = {
    "": "conjunctive",
    "and": "conjunctive",
    "or": "alternative",
    "but": "adversative",
    "then": "sequential",
    ";": "sequential",
}


def _nominal_members(text: str) -> tuple[str, ...] | None:
    """Complete noun phrases only; subordinate clauses cannot be subjects."""
    core = text.strip(" .!?")
    # Coordinated objects (logs and traffic) remain objects, not directives.
    parts = re.split(r"\s+and\s+|,\s*", core, flags=re.I)
    roles = []
    for part in parts:
        part = re.sub(
            r"^(?:(?:the|a|an|all|any|each|every|no|available|latest|security|affected|impacted|vulnerable)\s+)+",
            "",
            part,
            flags=re.I,
        )
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
    return tuple(roles)


def _object_members(text: str, depth: int = 0) -> tuple[str, ...] | None:
    if depth > 2:
        return None
    modifier = OBJECT_MODIFIER.search(text)
    core = text[: modifier.start()] if modifier else text
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
            and _object_members(tail, depth + 1) is None
        ):
            return None
    return _nominal_members(core)


def _argument(text: str) -> tuple[ArgumentRelation, tuple[str, ...]]:
    destination = re.match(r"^to\s+(.+)$", text, re.I)
    if destination:
        roles = _object_members(destination[1]) or ()
        return "destination", roles if set(roles) <= {"release"} else ()
    parts = re.split(r"\s+to\s+", text, maxsplit=1, flags=re.I)
    if len(parts) == 2:
        destination_roles = _object_members(parts[1])
        roles = _object_members(parts[0]) or ()
        return "direct_destination", (
            roles if destination_roles and set(destination_roles) <= {"release"} else ()
        )
    return "direct", _object_members(text) or ()


def _frame_actions(clause: DirectiveClause) -> dict[str, Action] | None:
    frame = ACTION_FRAMES.get(clause.verb, {}).get(clause.argument_relation, {})
    if not clause.object_members or not set(clause.object_members) <= frame.keys():
        return None
    return {role: frame[role] for role in clause.object_members}


def _advice_relation(text: str) -> tuple[str, str, bool] | None:
    audience = re.match(ADVICE_AUDIENCE, text, re.I)
    if not audience:
        return None
    remainder = text[audience.end() :].strip()
    modal = re.search(rf"\b(?P<modal>{ADVICE_MODAL})\s+(?P<body>.+)$", remainder, re.I)
    if not modal:
        return None
    qualifier = remainder[: modal.start()].strip()
    if qualifier:
        relation = re.fullmatch(r"(?:of|with|on|running|using)\s+(.+)", qualifier, re.I)
        roles = _nominal_members(relation[1]) if relation else None
        if not roles or not set(roles) <= {
            "system",
            "release",
            "identifier",
        }:
            return None
    return modal["modal"], modal["body"], bool(NEGATION.search(qualifier))


def _polarity_scope(text: str, inherited: bool) -> bool:
    advice = _advice_relation(text)
    if advice:
        inherited = advice[2] or bool(NEGATION.search(advice[0]))
        text = advice[1]
    return inherited or bool(re.match(r"^(?:do not|don't|not|never)\b", text, re.I))


def _clause(text: str, negative: bool) -> DirectiveClause | None:
    advice = _advice_relation(text)
    if advice:
        # An explicitly restated audience/modal owns its own polarity.
        negative = advice[2] or bool(NEGATION.search(advice[0]))
        text = advice[1]
    body = re.sub(r"^(?:(?:do not|don't|not|never)\s+)+", "", text, flags=re.I)
    if re.match(r"^(?:do so|do it|(?:this|that) action)\b", body, re.I):
        return DirectiveClause(
            "reference",
            body,
            None,
            (),
            "negative" if negative or NEGATION.search(text) else "affirmative",
            tuple(match.group() for match in CONDITION.finditer(text)),
            True,
        )
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
    relation, members = _argument(obj)
    return DirectiveClause(
        verb.casefold(),
        obj,
        None if not members else members[0] if len(set(members)) == 1 else "mixed",
        members,
        "negative" if negative or NEGATION.search(text) else "affirmative",
        tuple(match.group() for match in CONDITION.finditer(text)),
        argument_relation=relation,
    )


def parse_recommendation(text: str) -> RecommendationDirective | None:
    """Retain instruction structure independently from action prioritization."""
    normalized = " ".join(text.split()).rstrip(".!")
    conditions = tuple(match.group() for match in CONDITION.finditer(normalized))
    prefix = re.match(r"^(?:if|unless|when|until)\b[^,]+,\s*", normalized, re.I)
    if not prefix and re.match(
        r"^(?:only if|unless|until|provided that)\b", normalized, re.I
    ):
        return RecommendationDirective(
            text, "continuation", (), (normalized,), bool(NEGATION.search(normalized))
        )
    direct_text = normalized[prefix.end() :] if prefix else normalized
    advice = _advice_relation(direct_text)
    related_modal = re.search(rf"\b(?:{ADVICE_MODAL})\b", normalized, re.I)
    modality: Literal["advice", "imperative", "unclassified"] = (
        "advice" if advice else "unclassified" if related_modal else "imperative"
    )
    # Unknown modal relations may identify a constrained action target, never
    # positive advice. Direct audience ownership is still required above.
    body = (
        advice[1]
        if advice
        else (
            normalized[related_modal.end() :].strip() if related_modal else normalized
        )
    )
    conditions = (prefix.group().rstrip(", "),) if prefix else ()
    negative = bool(advice and (advice[2] or NEGATION.search(advice[0])))
    audience_negative = bool(advice and advice[2])
    shared_negative = _polarity_scope(body, negative)
    parts = COORDINATION.split(body)
    first = _clause(parts[0], shared_negative)
    if not first:
        return (
            RecommendationDirective(text, modality, (), conditions, True)
            if modality == "advice"
            else None
        )
    clauses = [first]
    ambiguous = "?" in normalized or modality == "unclassified"
    for connector, part in zip(parts[1::2], parts[2::2]):
        kind = COORDINATION_KINDS[connector.strip().strip(",").strip().casefold()]
        if kind == "alternative":
            conditions += ("Alternative source directives: " + body,)
        inherited_negative = (
            audience_negative if kind == "adversative" else shared_negative
        )
        clause = _clause(part, inherited_negative)
        if clause:
            clauses.append(replace(clause, coordination=kind))
            shared_negative = _polarity_scope(part, inherited_negative)
            restated = _advice_relation(part)
            if restated:
                audience_negative = restated[2]
        else:
            # A coordinated noun must complete a known object phrase. Unknown
            # verbs/clauses cannot silently disappear behind the first action.
            previous = clauses[-1]
            combined = previous.object_text + " and " + part
            relation, members = _argument(combined)
            role = (
                None
                if not members
                else members[0] if len(set(members)) == 1 else "mixed"
            )
            ambiguous |= role is None or kind not in {"conjunctive", "alternative"}
            clauses[-1] = replace(
                previous,
                object_text=combined,
                object_role=role,
                object_members=members,
                argument_relation=relation,
                conditions=previous.conditions
                + tuple(match.group() for match in CONDITION.finditer(part)),
                polarity=(
                    "negative"
                    if previous.polarity == "negative" or NEGATION.search(part)
                    else "affirmative"
                ),
            )
    ambiguous |= any(_frame_actions(c) is None and not c.reference for c in clauses)
    if (
        modality == "imperative"
        and first.object_role is None
        and not first.reference
        and not re.match(r"^(?:do not|don't|never)\s+", body, re.I)
    ):
        return None
    return RecommendationDirective(
        text, modality, tuple(clauses), conditions, ambiguous
    )


def directive_units(text: str) -> tuple[str, ...]:
    """Semicolon-separated statements retain order inside their source block."""
    return tuple(part.strip() for part in text.split(";") if part.strip())


def _targets(clause: DirectiveClause) -> set[tuple[Action, str]]:
    # The finding owns remediation/investigation scope. Monitoring objects can
    # establish narrower independent roles (e.g. evidence versus advisories).
    # Members, determiners and polarity share canonical identity; wording alone
    # cannot establish that two objects are independent.
    return {
        (action, role if action == Action.MONITOR else "finding")
        for role, action in (_frame_actions(clause) or {}).items()
        if action != Action.NONE
    }


def project_recommendation_action(blocks: Sequence[RecommendationBlock]) -> str:
    """Resolve qualified targets before prioritizing independent supported ones."""
    candidates: set[tuple[Action, str]] = set()
    constraints: set[tuple[Action, str]] = set()
    for block in blocks:
        previous: set[tuple[Action, str]] | None = None
        for directive in block.directives:
            if directive is None:
                # Intervening unparsed statements break explicit reference
                # ownership; they never become a guessed antecedent.
                previous = None
                continue
            if directive.modality == "continuation":
                if directive.ambiguous or directive.conditions:
                    if previous is None:
                        # Cross-block or missing antecedents are unresolved.
                        return Action.NONE.value
                    constraints.update(previous)
                continue
            if directive.ambiguous and (
                not directive.clauses
                or any(
                    _frame_actions(clause) is None and not clause.reference
                    for clause in directive.clauses
                )
            ):
                # Unknown targets cannot be proven independent of any action.
                return Action.NONE.value
            known: set[tuple[Action, str]] = set()
            antecedent = previous
            for clause in directive.clauses:
                if clause.reference:
                    if (
                        directive.ambiguous
                        or directive.conditions
                        or clause.conditions
                        or clause.polarity == "negative"
                    ):
                        if antecedent is None:
                            return Action.NONE.value
                        constraints.update(antecedent)
                    continue
                targets = _targets(clause)
                known.update(targets)
                antecedent = targets
                if (
                    directive.ambiguous
                    or directive.conditions
                    or clause.conditions
                    or clause.polarity == "negative"
                ):
                    constraints.update(targets)
                else:
                    candidates.update(targets)
            if any(not clause.reference for clause in directive.clauses):
                previous = known
    actions = {action for action, _ in candidates - constraints}
    return next(
        (action.value for action in Action if action in actions), Action.NONE.value
    )
