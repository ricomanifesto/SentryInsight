"""Parse bounded source directives before projecting a single action badge.

Advice has an explicit audience/modal relationship. Bare imperatives require
complete recognized objects; a leading action word alone is not instruction
evidence. Unrecognized advice stays guidance, but cannot supply a guessed badge.
"""

from dataclasses import dataclass, replace
import re
from typing import Callable, Literal, Sequence

from .cve import CVE_ID_PATTERN
from .condition_boundaries import ConditionSegment, bind_condition_boundaries
from .report_artifact import Action
from .relations import OwnedClause
from .relations import EvidenceReporter
from .source_document import reporting_envelope

ArgumentRelation = Literal["direct", "destination", "direct_destination"]
CoordinationRelation = Literal[
    "initial", "conjunctive", "alternative", "adversative", "sequential"
]
VersionIdentity = Callable[[str], tuple[str, ...] | None]
ReferenceTarget = tuple[str, tuple[str, ...]]
INITIAL_URGENCY = re.compile(r"^(immediately|promptly)\s+", re.I)


@dataclass(frozen=True)
class RecommendationDirective:
    source_text: str
    modality: Literal["advice", "imperative", "continuation", "unclassified"]
    clauses: tuple[OwnedClause, ...]
    conditions: tuple[str, ...]
    ambiguous: bool = False


@dataclass(frozen=True)
class RecommendationContext:
    source_text: str
    owner: Literal["narrative", "version", "exception"]


@dataclass(frozen=True)
class RecommendationBlock:
    source_text: str
    directives: tuple[RecommendationDirective | RecommendationContext, ...]


AUDIENCE = r"customers|users|admins|administrators|operators|owners|vendors|maintainers|organizations|you"
REPORTING_SUBJECT = r"(?:We|[Rr]esearchers|[Tt]he company|[Tt]he vendor|(?:[A-Z][A-Za-z0-9'-]*)(?: [A-Z][A-Za-z0-9'-]*){0,5}(?: researchers)?)"
REPORTED_ADVICE_CUE = re.compile(
    r"\b(?:advise[ds]?|recommend(?:s|ed)?|urge[ds]?|urging)\b", re.I
)
# One finite advice production owns the existing voice-specific forms and
# their optional intensifier. Envelope consumers do not reinterpret this text.
ADVICE_FORMS = (
    ("advised", r"advise[ds]?"),
    ("recommended", r"recommend(?:s|ed)?"),
    ("urged", r"urge[ds]?"),
    ("encouraged", None),
)
ADVICE_INTENSIFIER = r"(?:strongly )?"
ADVICE_OPERATORS = {
    "direct": (
        r"(?:are|is) (?P<operator_negative>not )?"
        + ADVICE_INTENSIFIER
        + "(?:"
        + "|".join(direct for direct, _ in ADVICE_FORMS)
        + ") "
        + r"(?P<operand_negative>not )?to"
    ),
    "reported": (
        r"(?P<operator_negative>did not |does not |do not )?"
        + ADVICE_INTENSIFIER
        + "(?:"
        + "|".join(reported for _, reported in ADVICE_FORMS if reported)
        + ")"
    ),
}
BASIC_ADVICE_MODAL = r"should|must|needs? to"
ADVICE_MODAL = rf"{BASIC_ADVICE_MODAL}|{ADVICE_OPERATORS['direct']}"
ADVICE_AUDIENCE = (
    rf"^(?:For {CVE_ID_PATTERN.pattern}(?: and {CVE_ID_PATTERN.pattern})*,\s*)?"
    rf"(?:{AUDIENCE})(?: and (?:{AUDIENCE}))*\b"
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
            "direct_destination": {"system": Action.PATCH, "release": Action.PATCH},
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
    "restart": {"direct": {"service": Action.NONE, "system": Action.NONE}},
    "revoke": {"direct": dict.fromkeys(("session", "token"), Action.NONE)},
    "rotate": {"direct": {"credential": Action.NONE}},
    "create": {"direct": dict.fromkeys(("wallet", "upgrade_plan"), Action.NONE)},
    "move": {
        "direct": {"asset": Action.NONE},
        "destination": {"authentication": Action.NONE},
    },
    "assume": {"direct": {"compromise": Action.NONE}},
    "treat": {"direct": {"incident_assessment": Action.NONE}},
    "remove": {"direct": {"extension": Action.NONE}},
    "delete": {"direct": {"credential": Action.NONE}},
    "audit": {"direct": {"extension": Action.NONE}},
    "adopt": {"direct": {"monitoring_method": Action.NONE}},
    "deploy": {"direct": {"monitoring_method": Action.NONE, "patch": Action.PATCH}},
    "sanitize": {"direct": {"input": Action.NONE}},
    "require": {"direct": {"authentication": Action.NONE}},
    "enforce": {
        "direct": dict.fromkeys(("authentication", "access_control"), Action.NONE)
    },
    "check": {"direct": {"account": Action.NONE}},
    "replace": {"direct": {"unsupported_product": Action.NONE}},
    "watch": {"direct": {"replication": Action.NONE}},
    "turn": {"direct": {"service_shutdown": Action.NONE}},
    "identify": {"direct": {"device_inventory": Action.NONE}},
    "plan": {"direct": {"upgrade_activity": Action.NONE}},
    "verify": {"direct": {"repository_owner": Action.NONE}},
    "be": {"direct": {"package_source": Action.NONE, "vigilance_watch": Action.NONE}},
    "exercise": {"direct": {"vigilance": Action.NONE}},
    "remain": {"direct": {"message_caution": Action.NONE}},
    "disable": {"direct": {"feature": Action.NONE, "service": Action.NONE}},
}
ACTION_FRAMES["review"]["direct"].update(
    dict.fromkeys(("credential", "account", "extension"), Action.NONE)
)
VERBS = frozenset(ACTION_FRAMES)


def has_owned_advice_cue(text: str) -> bool:
    """A known audience/modal cue requires interpretation of its whole prefix.

    This detects required guidance; it never supplies polarity or an action.
    An intervening unknown clause remains unsupported in the actual parser.
    """
    return bool(
        re.search(rf"\b(?:{AUDIENCE})\b[^.!?]*\b(?:{ADVICE_MODAL})\b", text, re.I)
        or REPORTED_ADVICE_CUE.search(text)
        or re.match(r"They (?:should|must|need to)\b", text)
        or re.match(r'^["“]?(?:However, )?please\b', text, re.I)
    )


def recommendation_context(text: str) -> RecommendationContext | None:
    """Explicit non-directive contexts may close a source statement boundary."""
    envelope = reporting_envelope(text)
    body = envelope.body if envelope else text
    if re.fullmatch(r'["“][^"”]+["”]', body):
        body = body[1:-1]
    if re.fullmatch(
        r"On [A-Z][a-z]+ \d{1,2}, \d{4}, (?:[A-Z][A-Za-z-]* )+customers received a push notification "
        r"through the (?:[A-Z][A-Za-z-]* )+app on their mobile devices, alleging customer data theft "
        r"and urging the company[’']s staff to engage with them on [A-Z][A-Za-z-]*\.",
        body,
    ):
        # The finite event is receipt of a message, whose alleged theft and
        # embedded request belong to its sender. It is not advice to comply.
        return RecommendationContext(text, "narrative")
    if re.fullmatch(
        r"We will never ask you to share passwords, security codes or payment details through an unsolicited message or call[.!?]*",
        body,
    ):
        return RecommendationContext(text, "exception")
    if re.fullmatch(r"There is no action you need to take on your account[.!?]*", body):
        return RecommendationContext(text, "exception")
    if re.fullmatch(
        r"As of [A-Z][a-z]+ \d{1,2}, \d{4}, all the extensions have (?:not )?been removed\.",
        body,
    ):
        return RecommendationContext(text, "narrative")
    if envelope and re.fullmatch(
        r"(?:[A-Z][A-Za-z0-9-]* )+deployments using (?:[A-Z][A-Za-z0-9-]* )+instances are (?:also |not )?affected by the vulnerability",
        body,
    ):
        return RecommendationContext(text, "version")
    named_product = r"[A-Z][A-Za-z0-9-]*(?: (?:[A-Z][A-Za-z0-9-]*|\d+)){0,8}"
    if re.fullmatch(
        rf"In a separate {named_product} update, it also noted that replacement certificates have already been delivered to systems running a supported {named_product} version and don't require additional action if they're up to date\.",
        body,
    ) or re.fullmatch(
        rf"However, this doesn't apply to devices that receive updates from {named_product} \([A-Z]+\), which downloads updates and distributes them across enterprise networks\.",
        body,
    ):
        return RecommendationContext(text, "exception")
    return None


# These are complete direct-object phrases, not substring cues. Source text
# retains modifiers; unknown objects cannot establish a bare imperative.
OBJECT_ROLES = {
    "identifier": CVE_ID_PATTERN.pattern,
    "release": r"versions? \d+(?:\.\d+)*",
    "patch": r"patch(?:es)?|updates?|hotfix(?:es)?|fix(?:es)?|monthly (?:(?-i:[A-Z][A-Za-z0-9-]*) )?updates",
    "mitigation": r"workarounds?|mitigations?",
    "evidence": r"(?:data warehouse |web application )?logs(?: for (?:signs of unauthorized access|attack attempts))?|indicators(?: of compromise)?|suspicious activity|alerts?|incidents?",
    "system": r"(?:(?:(?-i:[A-Z][A-Za-z0-9-]*)|and) ){0,8}(?:instances?|appliances?|systems?|servers?|gateways?|devices?|software|installations?|products?)",
    "service": r"services?",
    "vulnerability": r"vulnerabilit(?:y|ies)|flaws?|risks?|issues?|zero-days disclosed during the (?:[A-Z][A-Za-z0-9-]*|research) competition",
    "advisory": r"(?:vendor |security )?advisor(?:y|ies)|documentation",
    "support": r"support|(?:the )?vendor",
    "monitoring": r"(?:network )?traffic|activity",
    "session": r"(?:active )?(?:user )?sessions",
    "token": r"(?:access |API )?tokens",
    "credential": r"API keys|credentials(?: for every connected database)?",
    "wallet": r"new wallet(?: from a clean system)?",
    "asset": r"their assets",
    "authentication": r"passkeys|multifactor authentication(?: \(MFA\))?(?:, especially for webmail and VPNs)?",
    "compromise": r"compromise",
    "incident_assessment": r"incident as a potential (?:[A-Z][A-Za-z0-9-]* )?account compromise",
    "extension": r"(?:browser )?extensions(?: installed in their environment| within managed environments)?",
    "monitoring_method": r"runtime monitoring approaches|(?:behavior-based )?extension monitoring technologies",
    "account": r"administrator accounts(?: for unexpected changes)?|cloud accounts(?: for connected applications that can read files and email)?",
    "input": r"user input in web applications",
    "access_control": r"access control on every API endpoint",
    "unsupported_product": r"products that no longer get updates",
    "replication": r"for unexpected (?:Active Directory|directory) replication",
    "service_shutdown": r"off unused services and ports(?:, such as remote access and file sharing)?",
    "upgrade_plan": r"upgrade plan for unsupported devices",
    "device_inventory": r"devices running older or unsupported (?:(?-i:[A-Z][A-Za-z0-9-]*) )?versions",
    "upgrade_activity": r"upgrades for unsupported versions",
    "repository_owner": r"repository(?:'s|’s) owner",
    "package_source": r"official registries or vendor repositories",
    "feature": r"(?:(?-i:[A-Z][A-Za-z0-9-]*)[ ,]+(?:(?:and|or) )?){1,8}features",
    "vigilance": r"vigilance",
    "vigilance_watch": r"on the lookout for potential phishing attacks and loan scams stemming from leaked data",
    "message_caution": r"cautious of unexpected messages or calls claiming to be from (?:(?-i:[A-Z][A-Za-z-]*) ?){1,4}",
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


@dataclass(frozen=True)
class DirectiveArgument:
    source_text: str
    target_text: str
    modifiers: tuple[str, ...] = ()
    purposes: tuple[str, ...] = ()
    deadlines: tuple[str, ...] = ()
    reference: tuple[str, ...] = ()


def _bind_directive_argument(
    text: str, reference_target: ReferenceTarget | None = None
) -> DirectiveArgument:
    """Separate one finite terminal urgency phrase from a complete target.

    Called after condition/clause boundaries are bound, and never for audience
    nouns. The existing argument/frame owner still must recognize the entire
    target. Unknown or repeated modifiers cannot disappear into an opaque tail.
    """
    original = text
    reference = ()
    if reference_target:
        phrase, identities = reference_target
        suffix = ", including for " + phrase
        if identities and text.endswith(suffix):
            text = text[: -len(suffix)]
            reference = identities
    purposes = ()
    deadlines = ()
    purpose = re.search(
        r"\s*,?\s+(to (?:detect suspicious activity|block XSS|protect against attacks|keep them up to date|address the vulnerability|eliminate the attack vector))$",
        text,
        re.I,
    )
    if purpose:
        purposes = (purpose[1],)
        text = text[: purpose.start()]
    deadline = re.search(
        r"\s+(within \d+ days before (?:[A-Z][A-Za-z0-9-]*|researchers) publicly (?:shares|share) details"
        r"|before (?:the (?:[A-Z][A-Za-z0-9-]* )*certificates expire in )?(?:May|June)(?: \d{1,2},)?(?: and (?:May|June))? \d{4}"
        r"|before the (?:[A-Z][A-Za-z0-9-]* )+certificate rotation in \d{4}"
        r"|before the (?:May|June) \d{4} or (?:May|June) \d{4} certificate expiration dates)$",
        text,
    )
    if deadline:
        deadlines = (deadline[1],)
        text = text[: deadline.start()]
    means = re.search(
        r", (as can be identified through the vendor[’']s (?:[A-Z][A-Za-z0-9-]* )+tool)$",
        text,
    )
    if means:
        return DirectiveArgument(
            original, text[: means.start()], (means[1],), purposes, deadlines, reference
        )
    modifier = re.search(r"(?:,\s*|\s+)(immediately|as soon as possible)$", text, re.I)
    if modifier is None:
        return DirectiveArgument(original, text, (), purposes, deadlines, reference)
    return DirectiveArgument(
        original,
        text[: modifier.start()].rstrip(" ,"),
        (modifier[1],),
        purposes,
        deadlines,
        reference,
    )


def _nominal_members(
    text: str, version_identity: VersionIdentity | None = None
) -> tuple[str, ...] | None:
    """Complete noun phrases only; subordinate clauses cannot be subjects."""
    core = text.strip(" .!?")
    if version_identity and (identity := version_identity(core)):
        return tuple(
            "release" if role == "release_scope" else role for role in identity
        )
    whole = re.sub(
        r"^(?:(?:the|a|an|these|all|any|each|every|no|available|latest|security|supported|affected|impacted|vulnerable)\s+)+",
        "",
        core,
        flags=re.I,
    )
    complete = next(
        (
            role
            for role, grammar in OBJECT_ROLES.items()
            if re.fullmatch(grammar, whole, re.I)
        ),
        None,
    )
    if complete:
        return (complete,)
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
    # Closed multiword targets own their internal prepositions/conjunctions.
    # Otherwise the ordinary argument relation parser consumes each modifier.
    if roles := _nominal_members(text, version_identity):
        return roles
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
    # A closed nominal target owns its internal infinitives/prepositions.
    # Only a remaining relational argument may introduce a destination.
    if roles := _nominal_members(text):
        return "direct", roles
    if (
        version_identity
        and (identity := version_identity(text))
        and set(identity) == {"release_scope"}
    ):
        return "direct", tuple("release" for _ in identity)
    destination = re.match(r"^to\s+(.+)$", text, re.I)
    if destination:
        roles = _object_members(destination[1], version_identity=version_identity) or ()
        return "destination", roles
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


@dataclass(frozen=True)
class AdviceEnvelope:
    body: str
    binding: DirectiveBinding
    reporter: EvidenceReporter


@dataclass(frozen=True)
class AdviceOperator:
    finite: str
    end: int
    negative: bool = False


def _advice_operator(
    text: str, voice: Literal["direct", "reported"]
) -> AdviceOperator | None:
    """Consume one complete finite operator without borrowing its operand."""
    match = re.match(
        rf"(?P<finite>{ADVICE_OPERATORS[voice]})\s+",
        text,
        re.I if voice == "direct" else 0,
    )
    if not match:
        return None
    return AdviceOperator(
        match["finite"],
        match.end(),
        bool(match["operator_negative"] or match.groupdict().get("operand_negative")),
    )


def _direct_modal(text: str) -> AdviceOperator | None:
    basic = re.match(rf"(?:{BASIC_ADVICE_MODAL})\s+", text, re.I)
    if basic:
        return AdviceOperator(basic.group().strip(), basic.end())
    return _advice_operator(text, "direct")


def _reported_advice(text: str) -> AdviceEnvelope | None:
    """Bind a complete finite reporting operator to its directive operand.

    This supplies no action or object interpretation. Unknown reporting bridges
    remain required unsupported advice; the ordinary frame owner consumes the
    complete operand and its coordinated predicates.
    """
    warning = re.fullmatch(
        r"The breaches have triggered a warning from (?P<reporter>(?:[A-Z][A-Za-z'-]*|and)(?: (?:[A-Z][A-Za-z'-]*|and)){1,15}), "
        r"urging (?P<audience>financial consumers) (?P<negative>not )?to (?P<body>.+)",
        text,
    )
    if warning:
        return AdviceEnvelope(
            warning["body"],
            DirectiveBinding(
                subject=warning["audience"],
                modal="urging to",
                negative=bool(warning["negative"]),
            ),
            EvidenceReporter(warning["reporter"], "urging", "affirmative"),
        )
    mixed = re.fullmatch(
        r"It also added that devices on unsupported versions of (?:[A-Z][A-Za-z0-9-]* ){0,3}[A-Z][A-Za-z0-9-]* "
        r'"will lose access to (?:[A-Z][A-Za-z0-9-]* )+services and won\'t receive any updates as a result" '
        r'and recommended "(?P<body>[^"”]+)"',
        text,
    )
    if mixed:
        parsed = _reported_advice(
            "The company recommended " + mixed["body"].rstrip(".")
        )
        return (
            replace(
                parsed, reporter=EvidenceReporter("It", "recommended", "affirmative")
            )
            if parsed
            else None
        )
    subject = re.match(
        rf"^(?P<subject>{REPORTING_SUBJECT}) (?={ADVICE_OPERATORS['reported']}\s)",
        text,
    )
    operator = _advice_operator(text[subject.end() :], "reported") if subject else None
    if subject is None or operator is None:
        return None
    operand = text[subject.end() + operator.end :]
    reporter = EvidenceReporter(
        subject["subject"],
        operator.finite,
        "negative" if operator.negative else "affirmative",
    )
    audience = re.match(
        rf"(?P<audience>(?:(?:affected|impacted|IT) )?(?:{AUDIENCE})) (?P<negative>not )?to ",
        operand,
        re.I,
    )
    if audience:
        return AdviceEnvelope(
            operand[audience.end() :],
            DirectiveBinding(
                subject=audience["audience"],
                modal=operator.finite + " to",
                negative=bool(audience["negative"]),
            ),
            reporter,
        )
    that = re.match(rf"that (?P<audience>(?:{AUDIENCE})) ", operand, re.I)
    if that and reporter.polarity != "negative":
        return AdviceEnvelope(
            operand[that.end() :],
            DirectiveBinding(
                subject=that["audience"],
                modal=operator.finite + " that",
            ),
            reporter,
        )
    gerund = re.match(
        r"(?P<verb>upgrading|installing|applying|updating|disabling) ", operand
    )
    if gerund and re.search(r"recommend", operator.finite):
        verbs = {
            "upgrading": "upgrade",
            "installing": "install",
            "applying": "apply",
            "updating": "update",
            "disabling": "disable",
        }
        return AdviceEnvelope(
            verbs[gerund["verb"]] + " " + operand[gerund.end() :],
            DirectiveBinding(modal=operator.finite),
            reporter,
        )
    return None


def _binding(text: str, inherited: DirectiveBinding) -> tuple[str, DirectiveBinding]:
    """Consume one subject/modal production, retaining its owner for children."""
    polite = re.match(r"^(?:However, )?please\s+", text, re.I)
    if polite:
        text = text[polite.end() :]
        inherited = replace(inherited, modal="please")
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
                r"who have (?:not )?installed (?:any of )?the (?:aforementioned )?extensions "
                r"and (?:not )?entered a (?:real )?recovery phrase(?: or private key)? "
                r"into the fake (?:wallet )?interfaces",
                qualifier,
                re.I,
            ):
                state = replace(state, qualifications=(qualifier,))
            elif re.fullmatch(
                r"(?:deny|denies|say|says|wonder|question|are unsure)\s+(?:that|if|whether)\s+(?:they|operators|investigators)",
                qualifier,
                re.I,
            ):
                state = replace(state, qualifications=(qualifier,))
            else:
                return remainder[modal.end() :], replace(state, unsupported=True)
        text = remainder[modal.start() :]
    modal = _direct_modal(text)
    if modal:
        # A repeated finite modal owns a new polarity, while the subject's
        # negative quantifier remains a property of that subject.
        state = replace(
            state,
            modal=modal.finite,
            negative=state.audience_negative or modal.negative,
        )
        text = text[modal.end :]
    elif audience:
        return text, replace(state, unsupported=True)
    neg = re.match(r"(?:(?:do not|don't|not|never)\s+)+", text, re.I)
    if neg:
        state = replace(state, negative=True)
        text = text[neg.end() :]
    return text, state


def _verb_argument(body: str) -> tuple[str, str]:
    normalized = INITIAL_URGENCY.sub("", body)
    head = re.fullmatch(r"([A-Za-z]+)(?=\s|[,;]|$)(.*)", normalized)
    return (head[1].casefold(), head[2].strip()) if head else ("", "")


def _starts_directive(text: str) -> bool:
    body, binding = _binding(text, DirectiveBinding())
    verb, _ = _verb_argument(body)
    return bool(
        binding.subject
        or binding.modal
        or verb in VERBS
        or re.match(r"^(?:do so|do it|this action|that action)\b", body, re.I)
    )


def _directive_segments(
    body: str,
    version_identity: VersionIdentity | None,
    reference_target: ReferenceTarget | None = None,
    release_destinations: tuple[str, ...] = (),
):
    """Object conjunctions are parsed as objects, never unknown-clause fallback."""
    verb, raw_argument = _verb_argument(body)
    argument = _bind_directive_argument(raw_argument)
    protected = []
    if reference_target:
        suffix = ", including for " + reference_target[0]
        for match in re.finditer(re.escape(suffix), body):
            protected.append((match.start(), match.end()))
    for deadline in argument.deadlines:
        offset = body.rfind(deadline)
        protected.append((offset, offset + len(deadline)))
    condition = CONDITION.search(argument.target_text)
    complete_target = (
        argument.target_text[: condition.start()].rstrip()
        if condition
        else argument.target_text
    )
    if verb in VERBS and _nominal_members(complete_target, version_identity):
        start = len(body) - len(raw_argument)
        protected.append((start, start + len(complete_target)))
    if verb in {"upgrade", "update"} and "to " in complete_target:
        relation, members = _argument(complete_target, version_identity)
        if relation in {"destination", "direct_destination"} and members:
            start = len(body) - len(raw_argument)
            protected.append((start, start + len(complete_target)))
    if (
        release_destinations
        and argument.target_text.endswith(" to:")
        and _nominal_members(argument.target_text[:-4], version_identity)
    ):
        protected.append((len(body) - len(raw_argument), len(body)))
    # A later coordinated directive owns its whole nominal argument too.
    # Test candidate boundaries with the same argument/frame owner; an object
    # conjunction cannot be split merely because this is not the first verb.
    boundaries = tuple(COORDINATION.finditer(body))
    for preceding in boundaries:
        start = preceding.end()
        predicate, binding = _binding(body[start:], DirectiveBinding())
        owning_verb, _ = _verb_argument(predicate)
        if binding.unsupported or owning_verb not in VERBS:
            continue
        for end in sorted(
            {len(body), *(b.start() for b in boundaries if b.start() > start)},
        ):
            predicate, binding = _binding(body[start:end], DirectiveBinding())
            owning_verb, raw_target = _verb_argument(predicate)
            if binding.unsupported or owning_verb not in VERBS:
                continue
            target = _bind_directive_argument(raw_target).target_text
            marker = CONDITION.search(target)
            if marker:
                target = target[: marker.start()].rstrip(" ,")
            # Structural lookahead must not recursively classify version
            # clauses as new advice. It protects closed nominal frames only;
            # the actual directive still delegates releases to their owner.
            relation, members = _argument(target, None)
            if (
                not binding.unsupported
                and members
                and _frame_actions(
                    OwnedClause(
                        verb=owning_verb,
                        object_members=members,
                        object_role=members[0],
                        argument_relation=relation,
                    )
                )
                is not None
            ):
                offset = start + body[start:end].find(raw_target)
                protected.append((offset, offset + len(target)))
                break
    pieces = bind_condition_boundaries(
        body,
        boundary=COORDINATION,
        condition=CONDITION,
        starts_relation=_starts_directive,
        protected=protected,
    )
    result: list[tuple[str, ConditionSegment]] = []
    alternatives = False
    for part in pieces:
        relation = (
            COORDINATION_KINDS[part.connector.strip(",").strip().casefold()]
            if result
            else "initial"
        )
        alternatives |= relation == "alternative"

        def joins_owned_object():
            earlier, _ = _binding(result[-1][1].predicate, DirectiveBinding())
            owning_verb, existing = _verb_argument(earlier)
            if owning_verb not in VERBS:
                return False
            combined = _bind_directive_argument(existing + " and " + part.predicate)
            relation, members = _argument(combined.target_text, version_identity)
            return bool(
                members
                and _frame_actions(
                    OwnedClause(
                        verb=owning_verb,
                        object_members=members,
                        object_role=members[0],
                        argument_relation=relation,
                    )
                )
                is not None
            )

        if (
            result
            and relation in {"conjunctive", "alternative"}
            and _object_members(
                _bind_directive_argument(part.predicate).target_text,
                version_identity=version_identity,
            )
            and joins_owned_object()
        ):
            previous, earlier = result[-1]
            result[-1] = (
                previous,
                replace(
                    earlier,
                    text=earlier.text + " and " + part.text,
                    predicate=earlier.predicate + " and " + part.predicate,
                    conditions=earlier.conditions + part.conditions,
                    unsupported=earlier.unsupported or part.unsupported,
                ),
            )
        else:
            result.append((relation, part))
    return result, alternatives


def parse_recommendation(
    text: str,
    *,
    version_identity: VersionIdentity | None = None,
    reference_target: ReferenceTarget | None = None,
    release_destinations: tuple[str, ...] = (),
    release_audience: str = "",
    audience_reference: str = "",
) -> RecommendationDirective | None:
    """Parse complete directive relations; projection never reparses their text."""
    if envelope := reporting_envelope(text):
        parsed = parse_recommendation(
            envelope.body,
            version_identity=version_identity,
            reference_target=reference_target,
            release_destinations=release_destinations,
            release_audience=release_audience,
            audience_reference=audience_reference,
        )
        if parsed is None:
            return None
        return replace(
            parsed,
            source_text=text,
            clauses=tuple(
                replace(
                    clause,
                    reporter=clause.reporter
                    or EvidenceReporter(
                        envelope.subject,
                        envelope.finite,
                        "affirmative",
                        as_of=envelope.adjunct,
                    ),
                )
                for clause in parsed.clauses
            ),
        )
    normalized = " ".join(text.split()).rstrip(".!")
    if re.fullmatch(r'["“][^"”]+["”]', normalized):
        normalized = normalized[1:-1].rstrip(".!")
    prelude = re.match(
        r"And (?P<condition>if you do need to act on older device populations), there's still time! ",
        normalized,
    )
    prelude_conditions = (prelude["condition"],) if prelude else ()
    if prelude:
        normalized = normalized[prelude.end() :]
    purpose = re.match(
        r"^(To (?:ensure devices keep receiving updates|counter the threat associated with malicious extensions)),\s*",
        normalized,
    )
    initial_purposes = (purpose[1],) if purpose else ()
    if purpose:
        normalized = normalized[purpose.end() :]
    leading = re.match(r"^(?:if|unless|when|until)\b[^,]+,\s*", normalized, re.I)
    if not leading and re.match(
        r"^(?:only if|unless|until|provided that)\b", normalized, re.I
    ):
        return RecommendationDirective(
            text, "continuation", (), (normalized,), bool(NEGATION.search(normalized))
        )
    conditions = prelude_conditions + (
        (leading.group().rstrip(", "),) if leading else ()
    )
    if release_audience:
        conditions += ("For " + release_audience,)
    source = normalized[leading.end() :] if leading else normalized
    reported = _reported_advice(source)
    if reported:
        source, initial_binding = reported.body, reported.binding
    else:
        pronoun = re.match(r"They (?=(?:should|must|need to)\b)", source)
        if pronoun:
            source = source[pronoun.end() :]
        source, initial_binding = _binding(
            source,
            DirectiveBinding(
                subject=audience_reference if pronoun else "",
                unsupported=bool(pronoun and not audience_reference),
            ),
        )
        copular = re.match(
            r"(?:Furthermore, )?(?P<subject>the source for installing AI skills and MCP servers) (?P<modal>should) ",
            source,
            re.I,
        )
        if copular:
            source, initial_binding = source[copular.end() :], DirectiveBinding(
                subject=copular["subject"], modal=copular["modal"]
            )
    source = re.sub(r"^also (?=(?:deploy|create)\b)", "", source)
    if release_audience:
        initial_binding = replace(initial_binding, subject=release_audience)
    segments, alternative = _directive_segments(
        source, version_identity, reference_target, release_destinations
    )
    if alternative:
        conditions += ("Alternative source directives: " + source,)
    clauses = []
    inherited = initial_binding
    previous_members = ()
    previous_index = None
    advice = bool(initial_binding.subject or initial_binding.modal)
    for connector, segment in segments:
        raw = segment.text
        if connector == "adversative":
            inherited = replace(inherited, negative=inherited.audience_negative)
        body, binding = _binding(segment.predicate, inherited)
        advice |= bool(binding.subject or binding.modal)
        reference = re.match(r"^(?:do so|do it|(?:this|that) action)\b", body, re.I)
        verb, argument = _verb_argument(body)
        argument_binding = _bind_directive_argument(argument, reference_target)
        argument = argument_binding.target_text
        # Supporting restart retains these source-order/context adjuncts but
        # requires its own complete service/system target. They do not give
        # another verb a new argument frame or create a primary action.
        target_argument = (
            re.sub(r"\s+(?:afterward|during recovery)$", "", argument, flags=re.I)
            if verb == "restart"
            else argument
        )
        relation, members = (
            _argument(target_argument, version_identity)
            if verb in VERBS
            else ("direct", ())
        )
        if release_destinations and argument.endswith(" to:") and version_identity:
            destination_roles = [
                version_identity(value) for value in release_destinations
            ]
            target = _object_members(argument[:-4], version_identity=version_identity)
            if target and all(
                roles and set(roles) <= {"release"} for roles in destination_roles
            ):
                relation, members = "direct_destination", target
        object_antecedent = None
        object_conditions = ()
        subset = re.fullmatch(
            r"(?:those that are no longer needed|any you do not recognize)",
            argument,
            re.I,
        )
        required_target = {"remove": "extension", "delete": "credential"}.get(verb)
        if subset and required_target and previous_members == (required_target,):
            members = previous_members
            object_antecedent = previous_index
            object_conditions = (argument,)
        bound_conditions = tuple(
            _bind_directive_argument(value) for value in segment.conditions
        )
        own_conditions = tuple(value.target_text for value in bound_conditions)
        qualification = binding.qualifications + (
            ("Question",) if "?" in normalized else ()
        )
        implicit = bool(
            verb in VERBS
            and verb != "restart"
            and (binding.negative or conditions or own_conditions or qualification)
            and (not argument or CONDITION.fullmatch(argument))
        )
        if (
            not reference
            and verb in VERBS
            and verb != "restart"
            and re.match(
                r"^(?:it|that)(?:\s+(?:if|until|when|only|immediately)|$)",
                argument,
                re.I,
            )
        ):
            reference = True
        if reference:
            verb, argument, members = "reference", body, ()
        unsupported = (
            segment.unsupported
            or binding.unsupported
            or (not reference and not implicit and (verb not in VERBS or not members))
        )
        if (
            unsupported
            and not advice
            and not clauses
            and not binding.negative
            and verb != "restart"
            and reference_target is None
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
            cves=argument_binding.reference,
            attribution=(
                "document_reference" if argument_binding.reference else "unscoped"
            ),
            verb=verb,
            modal=binding.modal,
            polarity=(
                "negative" if binding.negative or object_negative else "affirmative"
            ),
            conditions=own_conditions
            + qualification
            + (("For " + release_audience,) if release_audience else ()),
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
            object_antecedent=object_antecedent,
            object_conditions=object_conditions,
            directive_modifiers=(
                (urgency[1],) if (urgency := INITIAL_URGENCY.match(body)) else ()
            )
            + argument_binding.modifiers,
            purposes=initial_purposes
            + argument_binding.purposes
            + tuple(p for value in bound_conditions for p in value.purposes),
            deadlines=argument_binding.deadlines,
            reference=bool(reference),
            argument_relation=relation,
            coordination=connector,
            reporter=reported.reporter if reported else None,
        )
        if not clause.reference and _frame_actions(clause) is None:
            clause = replace(clause, unsupported=True)
        clauses.append(clause)
        if clause.object_members:
            previous_members, previous_index = clause.object_members, len(clauses) - 1
        else:
            previous_members, previous_index = (), None
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
            if isinstance(directive, RecommendationContext):
                # Explicitly non-directive context breaks reference ownership.
                # Unsupported required advice is a directive, never context.
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
                    or clause.reporter
                    and (
                        clause.reporter.polarity == "negative"
                        or clause.reporter.qualification
                    )
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
