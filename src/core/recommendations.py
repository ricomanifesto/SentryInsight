"""Parse bounded source directives before projecting a single action badge.

Advice has an explicit audience/modal relationship. Bare imperatives require
complete recognized objects; a leading action word alone is not instruction
evidence. Unrecognized advice stays guidance, but cannot supply a guessed badge.
"""

from dataclasses import dataclass, replace
import re
from typing import Callable, Literal, Sequence

from .cve import CVE_ID_PATTERN
from .report_artifact import Action
from .relations import OwnedClause

ArgumentRelation = Literal["direct", "destination", "direct_destination"]
CoordinationRelation = Literal[
    "initial", "conjunctive", "alternative", "adversative", "sequential"
]
VersionIdentity = Callable[[str], tuple[str, ...] | None]


@dataclass(frozen=True)
class RecommendationDirective:
    source_text: str
    modality: Literal["advice", "imperative", "continuation", "unclassified"]
    clauses: tuple[OwnedClause, ...]
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
    "install": {"direct": {"patch": Action.PATCH, "release": Action.PATCH}},
    "apply": {
        "direct": {
            "patch": Action.PATCH,
            "release": Action.PATCH,
            "mitigation": Action.MITIGATE,
        }
    },
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


def _nominal_members(
    text: str, version_identity: VersionIdentity | None = None
) -> tuple[str, ...] | None:
    """Complete noun phrases only; subordinate clauses cannot be subjects."""
    core = text.strip(" .!?")
    if version_identity and (identity := version_identity(core)):
        return tuple(
            "release" if role == "release_scope" else role for role in identity
        )
    correlative = re.fullmatch(r"neither (.+) nor (.+)", core, re.I)
    if correlative:
        left, right = (_nominal_members(part) for part in correlative.groups())
        return left + right if left and right else None
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


def _object_members(
    text: str, depth: int = 0, version_identity: VersionIdentity | None = None
) -> tuple[str, ...] | None:
    if depth > 2:
        return None
    if (
        version_identity
        and (identity := version_identity(text))
        and set(identity) == {"release_scope"}
    ):
        return tuple("release" for _ in identity)
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
            and _object_members(tail, depth + 1, version_identity) is None
            and not (
                version_identity and version_identity(text[modifier.start() :].strip())
            )
        ):
            return None
    return _nominal_members(core, version_identity)


def _argument(
    text: str, version_identity: VersionIdentity | None = None
) -> tuple[ArgumentRelation, tuple[str, ...]]:
    if (
        version_identity
        and (identity := version_identity(text))
        and set(identity) == {"release_scope"}
    ):
        return "direct", tuple("release" for _ in identity)
    destination = re.match(r"^to\s+(.+)$", text, re.I)
    if destination:
        roles = _object_members(destination[1], version_identity=version_identity) or ()
        return "destination", roles if set(roles) <= {"release"} else ()
    parts = re.split(r"\s+to\s+", text, maxsplit=1, flags=re.I)
    if len(parts) == 2:
        destination_roles = _object_members(parts[1], version_identity=version_identity)
        roles = _object_members(parts[0], version_identity=version_identity) or ()
        return "direct_destination", (
            roles if destination_roles and set(destination_roles) <= {"release"} else ()
        )
    return "direct", _object_members(text, version_identity=version_identity) or ()


def _frame_actions(clause: OwnedClause) -> dict[str, Action] | None:
    if clause.object_role == "implicit":
        # Only prohibited/qualified implicit arguments are admitted. Their
        # finite verb constrains its possible actions without asserting one.
        return {
            action.value: action
            for frame in ACTION_FRAMES.get(clause.verb, {}).values()
            for action in frame.values()
        }
    frame = ACTION_FRAMES.get(clause.verb, {}).get(clause.argument_relation, {})
    if not clause.object_members or not set(clause.object_members) <= frame.keys():
        return None
    return {role: frame[role] for role in clause.object_members}


@dataclass(frozen=True)
class DirectiveBinding:
    subject: str = ""
    modal: str = ""
    negative: bool = False
    audience_negative: bool = False
    qualifications: tuple[str, ...] = ()
    unsupported: bool = False


def _binding(text: str, inherited: DirectiveBinding) -> tuple[str, DirectiveBinding]:
    """Consume one subject/modal production, retaining its owner for children."""
    audience = re.match(ADVICE_AUDIENCE, text, re.I)
    state = inherited
    if audience:
        remainder = text[audience.end() :].strip()
        state = DirectiveBinding(subject=audience.group())
        modal = re.search(rf"\b(?:{ADVICE_MODAL})\s+", remainder, re.I)
        if not modal:
            return text, inherited
        qualifier = remainder[: modal.start()].strip()
        if qualifier:
            nominal = re.fullmatch(
                r"(?:of|with|on|running|using)\s+(.+)", qualifier, re.I
            )
            roles = _nominal_members(nominal[1]) if nominal else None
            if nominal and roles and set(roles) <= {"system", "release", "identifier"}:
                state = replace(
                    state,
                    audience_negative=bool(re.search(r"\bno\b", nominal[1], re.I)),
                )
            elif re.fullmatch(
                r"(?:deny|denies|say|says|wonder|question|are unsure)\s+(?:that|if|whether)\s+(?:they|operators|investigators)",
                qualifier,
                re.I,
            ):
                state = replace(state, qualifications=(qualifier,))
            else:
                return remainder[modal.end() :], replace(state, unsupported=True)
        text = remainder[modal.start() :]
    modal = re.match(rf"(?:{ADVICE_MODAL})\s+", text, re.I)
    if modal:
        # A repeated finite modal owns a new polarity, while the subject's
        # negative quantifier remains a property of that subject.
        state = replace(
            state,
            modal=modal.group().strip(),
            negative=state.audience_negative or bool(NEGATION.search(modal.group())),
        )
        text = text[modal.end() :]
    elif audience:
        return text, replace(state, unsupported=True)
    neg = re.match(r"(?:(?:do not|don't|not|never)\s+)+", text, re.I)
    if neg:
        state = replace(state, negative=True)
        text = text[neg.end() :]
    return text, state


def _directive_segments(body: str, version_identity: VersionIdentity | None):
    """Object conjunctions are parsed as objects, never unknown-clause fallback."""
    pieces = COORDINATION.split(body)
    result = [("initial", pieces[0])]
    alternatives = False
    for connector, part in zip(pieces[1::2], pieces[2::2]):
        relation = COORDINATION_KINDS[connector.strip().strip(",").strip().casefold()]
        alternatives |= relation == "alternative"
        if relation in {"conjunctive", "alternative"} and _object_members(
            part, version_identity=version_identity
        ):
            previous, text = result[-1]
            result[-1] = (previous, text + " and " + part)
        else:
            result.append((relation, part))
    return result, alternatives


def parse_recommendation(
    text: str, *, version_identity: VersionIdentity | None = None
) -> RecommendationDirective | None:
    """Parse complete directive relations; projection never reparses their text."""
    normalized = " ".join(text.split()).rstrip(".!")
    leading = re.match(r"^(?:if|unless|when|until)\b[^,]+,\s*", normalized, re.I)
    if not leading and re.match(
        r"^(?:only if|unless|until|provided that)\b", normalized, re.I
    ):
        return RecommendationDirective(
            text, "continuation", (), (normalized,), bool(NEGATION.search(normalized))
        )
    conditions = (leading.group().rstrip(", "),) if leading else ()
    source = normalized[leading.end() :] if leading else normalized
    source, initial_binding = _binding(source, DirectiveBinding())
    segments, alternative = _directive_segments(source, version_identity)
    if alternative:
        conditions += ("Alternative source directives: " + source,)
    clauses = []
    inherited = initial_binding
    advice = bool(initial_binding.subject or initial_binding.modal)
    for connector, raw in segments:
        if connector == "adversative":
            inherited = replace(inherited, negative=inherited.audience_negative)
        body, binding = _binding(raw, inherited)
        advice |= bool(binding.subject or binding.modal)
        reference = re.match(r"^(?:do so|do it|(?:this|that) action)\b", body, re.I)
        words = body.split()
        while (
            words
            and words[0].casefold() not in VERBS
            and words[0].casefold().endswith("ly")
        ):
            words.pop(0)
        verb = words.pop(0).casefold() if words else ""
        argument = " ".join(words)
        relation, members = (
            _argument(argument, version_identity) if verb in VERBS else ("direct", ())
        )
        own_conditions = tuple(match.group() for match in CONDITION.finditer(body))
        qualification = binding.qualifications + (
            ("Question",) if "?" in normalized else ()
        )
        implicit = bool(
            verb in VERBS
            and (binding.negative or conditions or own_conditions or qualification)
            and (not argument or CONDITION.fullmatch(argument))
        )
        if (
            not reference
            and verb in VERBS
            and re.match(
                r"^(?:it|that)(?:\s+(?:if|until|when|only|immediately)|$)",
                argument,
                re.I,
            )
        ):
            reference = True
        if reference:
            verb, argument, members = "reference", body, ()
        unsupported = binding.unsupported or (
            not reference and not implicit and (verb not in VERBS or not members)
        )
        if (
            unsupported
            and not advice
            and not clauses
            and not binding.negative
            and not re.match(r"^(?:do not|don't|never)\s+", raw, re.I)
        ):
            return None
        # Negative objects are owned by their nominal argument; a negation
        # inside a conditional tail cannot become predicate polarity.
        object_negative = bool(re.match(r"^(?:the )?(?:no|neither)\b", argument, re.I))
        clause = OwnedClause(
            text=raw,
            subject=binding.subject,
            kind="directive",
            verb=verb,
            modal=binding.modal,
            polarity=(
                "negative" if binding.negative or object_negative else "affirmative"
            ),
            conditions=own_conditions + qualification,
            unsupported=unsupported,
            object_text=argument,
            object_role=(
                "implicit"
                if implicit
                else (
                    None
                    if not members
                    else members[0] if len(set(members)) == 1 else "mixed"
                )
            ),
            object_members=members,
            reference=bool(reference),
            argument_relation=relation,
            coordination=connector,
        )
        if not clause.reference and _frame_actions(clause) is None:
            clause = replace(clause, unsupported=True)
        clauses.append(clause)
        inherited = binding
    return RecommendationDirective(
        text,
        "advice" if advice else "imperative",
        tuple(clauses),
        conditions,
        any(c.unsupported for c in clauses),
    )


def directive_units(text: str) -> tuple[str, ...]:
    """Semicolon-separated statements retain order inside their source block."""
    return tuple(part.strip() for part in text.split(";") if part.strip())


def _targets(clause: OwnedClause) -> set[tuple[Action, str]]:
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
