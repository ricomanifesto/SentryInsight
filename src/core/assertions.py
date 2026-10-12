"""Finite assertion relations: bind qualifiers before projecting evidence state."""

from dataclasses import dataclass, replace
import re
from typing import Literal

from .cve import CVE_ID_PATTERN, extract_cve_ids
from .condition_boundaries import bind_condition_boundaries
from .relations import EvidenceReporter, OwnedClause
from .source_document import ADVISORY_DECLARATION, reporting_envelope

CVE_LIST = rf"{CVE_ID_PATTERN.pattern}(?:\s*(?:,\s*(?:and\s+)?|and\s+){CVE_ID_PATTERN.pattern})*"
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
    ("vulnerability", re.compile(rf"^(?:{CVE_LIST})\b\s*", re.I)),
    ("vulnerability", DESCRIPTIVE_SUBJECT),
    (
        "actor",
        re.compile(
            r"^(?:the\s+)?(?:attackers?|operators?|(?:threat\s+)?actors?)\s+",
            re.I,
        ),
    ),
)


def _bind_subject(text: str) -> SubjectBinding | None:
    """Bind a closed subject production without discarding unknown modifiers.

    Actor determiners and compound heads are nominal ownership, not predicate
    modifiers. Any unconsumed bridge remains with the strict predicate owner.
    """
    for kind, production in SUBJECT_PRODUCTIONS:
        if match := production.match(text):
            return SubjectBinding(kind, match.group().rstrip(), match.end())
    return None


POSSIBILITY_WORDS = ("potentially", "likely", "possibly", "probably", "unlikely")
TOPIC = re.compile(r"\b(?:exploit\w*|weaponiz\w*)\b", re.I)
BOUNDARY = re.compile(
    r"([;,]\s*(?:and|but|while|whereas)\b|[;,]|\b(?:and|but|while|whereas)\b)", re.I
)
CONDITION = re.compile(r"\b(?:if|unless)\b", re.I)
REQUIRED_ADJUNCT = re.compile(
    r"\b(?:if|unless|when|until|once|although|though|only|provided|depending)\b", re.I
)
PREDICATE_MODIFIERS = frozenset(POSSIBILITY_WORDS) | {
    "also",
    "currently",
    "now",
    "still",
    "not",
    "never",
    "actively",
    "newly",
    "recently",
    "widely",
    "publicly",
    "successfully",
    "extensively",
}
FINITE_PREDICATE_HEADS = frozenset(
    {
        "is",
        "are",
        "was",
        "were",
        "has",
        "have",
        "had",
        "may",
        "might",
        "could",
        "can",
        "will",
        "would",
    }
)
# Complete auxiliary productions have explicit semantics. Perfect evidence
# without an owned qualification is deliberately unresolved; unknown chains
# never acquire a state from an incidental auxiliary elsewhere in the prefix.
AUXILIARY_STATES = {
    **{(word,): "current" for word in ("is", "are")},
    **{(word, "being"): "current" for word in ("is", "are")},
    **{(word,): "past" for word in ("was", "were")},
    **{(word, "being"): "past" for word in ("was", "were")},
    ("had", "been"): "past",
    ("has", "been"): "unspecified",
    ("have", "been"): "unspecified",
    ("have", "begun"): "past",
    ("has", "begun"): "past",
    ("had", "begun"): "past",
    **{
        (word, *tail): "possible"
        for word in ("may", "might", "could", "would")
        for tail in ((), ("be",), ("have", "been"))
    },
    **{
        (word, "known", "to", "be"): state
        for word, state in (
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        )
    },
}

REPORTER_SUBJECT = r"(?:[Tt]he (?:vendor|company|researchers|agencies)|[A-Z][A-Za-z/-]*(?: [A-Z][A-Za-z/-]*){0,3}|it)"
REPORTER_EVIDENCE = re.compile(
    rf"^(?P<subject>{REPORTER_SUBJECT}) (?P<finite>has|have|had) "
    r"(?P<negative>not )?found (?P<double>no )?evidence that (?P<event>.+)$"
)
REPORTER_DENIAL = re.compile(
    rf"^(?P<subject>{REPORTER_SUBJECT}) denied that (?P<event>it .+)$"
)
QUOTED_EVENT = re.compile(
    rf"^(?:Separately, )?(?P<reporter>{REPORTER_SUBJECT})(?: in [A-Z][a-z]+)? "
    r"patched a (?:[A-Z][A-Za-z0-9-]* )?(?:modem |software |security )?flaw, "
    rf"(?P<identity>{CVE_ID_PATTERN.pattern}), that it (?P<report>said|denied)\s*:\s*"
    r'["“](?P<event>[^"”]+)["”](?P<suffix>.*)$'
)


def _quoted_event(text):
    match = QUOTED_EVENT.fullmatch(text)
    if not match:
        return None
    event = _unit(match["event"])
    suffix = match["suffix"].strip()
    # A separate patch-level context sentence has its own finite predicate.
    # Unknown residuals, including another assertion, cannot hide in this span.
    context = (
        re.fullmatch(
            r"(?:[A-Z][A-Za-z0-9-]* )?(?:phones|devices) at patch level \d{4}-\d{2}-\d{2} or later have that fix\.",
            suffix,
        )
        if suffix
        else True
    )
    return replace(
        event,
        text=text,
        cves=tuple(extract_cve_ids(match["identity"])),
        attribution="quoted",
        reporter=EvidenceReporter(
            match["reporter"],
            match["report"],
            "affirmative",
            "denied quote" if match["report"] == "denied" else "",
        ),
        unsupported=event.unsupported or not context,
    )


MONEY = r"\$[\d,]+(?:\.\d+)?(?: million)?"
COUNT = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten)"
ENTITY = r"(?:[A-Z][A-Za-z0-9'’.-]*\s*){1,7}(?:\([A-Z]+\))?"
END_MARKS = r'[.!?"”]*'
CAPABILITY_PREREQUISITE = re.compile(
    rf"(?P<subject>{CVE_LIST}) (?P<aux>is|are) (?P<negative>not )?exploitable "
    r"(?P<condition>if (?P<feature>[A-Z][A-Za-z0-9-]*)"
    r", which is supported only on some (?:[A-Z][A-Za-z0-9-]* |\d+ ){1,5}models, "
    r"is (?P<condition_negative>not )?turned on)"
)


def source_qualification(text):
    """Own finite prerequisite/protection context without asserting an event.

    These are complete source paragraphs, including quoted attribution and
    default/exception clauses. A recognized family with an unknown residual is
    required unsupported context; it cannot disappear into optional excerpts.
    """
    name = r"(?:[A-Z][A-Za-z0-9-]*|\d+|\([A-Za-z0-9-]+\)|over)(?: (?:[A-Z][A-Za-z0-9-]*|\d+|\([A-Za-z0-9-]+\)|over)){0,14}"
    families = (
        (
            rf"^Leveraging the {CVE_LIST} flaw also ",
            rf"Leveraging the {CVE_LIST} flaw also (?:requires|(?P<negative>does not require)) either {name} or {name} to be enabled\.",
        ),
        (
            rf'^["“]{name} also (?:requires|does not require) ',
            rf'["“]{name} also (?:requires|(?P<negative>does not require)) a {name} mapped to a {name} interface '
            rf"with at least one peer {name} learned \(for example, {name} or an ingress-replication static peer\),"
            rf'["”] reads {name}[’\']s advisory\.',
        ),
        (
            rf"^In the case of {CVE_LIST}, ",
            rf"In the case of {CVE_LIST}, {name} must (?P<negative>not )?be explicitly activated, as it is disabled by default\."
            rf"(?: {name} switches with {name} ASICs do not support the feature and are unaffected by this flaw\.)?",
        ),
        (
            rf"^{name} also provides temporary ",
            rf"{name} also provides temporary {name} shields for all {COUNT} flaws, "
            r"which is a protection system for switches that cannot yet be upgraded and rebooted\.",
        ),
    )
    for prefix, complete in families:
        if re.match(prefix, text):
            matched = re.fullmatch(complete, text)
            return OwnedClause(
                text=text,
                source_text=text,
                cves=tuple(extract_cve_ids(text)),
                kind="context",
                modal="capability",
                context_role="composed:source_qualification",
                conditions=(text,),
                polarity=(
                    "negative"
                    if matched and matched.groupdict().get("negative")
                    else "affirmative"
                ),
                unsupported=matched is None,
            )
    return None


def _closed_composition(core):
    """Closed event compositions own their complete participants and adjuncts.

    An event's finite predicate supplies tense; completed outcomes, purpose
    clauses and technique nouns have distinct roles. No topic substring or
    incidental date supplies a state, and a residual cannot be accepted here.
    """
    base = OwnedClause(text=core, cves=tuple(extract_cve_ids(core)))
    declaration = ADVISORY_DECLARATION.match(core)
    if declaration and re.fullmatch(
        r"(?:[A-Z][A-Za-z0-9-]* )+data center network operating system that could be exploited "
        r"to run arbitrary code with root privileges on (?:[A-Z][A-Za-z0-9-]* )+switches[.!?]*",
        core[declaration.end() :],
    ):
        return replace(
            base, modal="capability", context_role="composed:advisory_capability"
        )
    capability = CAPABILITY_PREREQUISITE.fullmatch(core.rstrip('.!?"”'))
    if capability:
        return replace(
            base,
            subject=capability["subject"],
            verb="exploitable",
            modal="capability",
            polarity="negative" if capability["negative"] else "affirmative",
            finite=True,
            context_role="composed:capability_prerequisite",
            conditions=(capability["condition"],),
        )
    prerequisite = re.fullmatch(
        rf"(?P<subject>An attacker) (?P<predicate>needs (?:no|an) account|does not need an account) to exploit (?P<target>it|{CVE_LIST}){END_MARKS}",
        core,
    )
    if prerequisite:
        return replace(
            base,
            subject=prerequisite["subject"],
            modal="capability",
            context_role="composed:prerequisite",
            purposes=("to exploit " + prerequisite["target"],),
        )
    pattern = re.fullmatch(
        rf"The (?:first|second|third) pattern is exploitation of {CVE_LIST}, "
        rf"an SQL injection flaw in {ENTITY}, an open-source BI tool that companies connect to their databases{END_MARKS}",
        core,
    )
    if pattern:
        return replace(
            base,
            kind="assertion",
            verb="exploitation",
            modal="unknown",
            context_role="composed:nominal_pattern",
        )
    reported_past = re.fullmatch(
        rf"(?P<reporter>{REPORTER_SUBJECT}) said a third party exploited {CVE_LIST} in its {ENTITY} "
        rf"and had access from [A-Z][a-z]+ \d{{1,2}} to [A-Z][a-z]+ \d{{1,2}}{END_MARKS}",
        core,
    )
    if reported_past:
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            context_role="composed:reported_past",
            reporter=EvidenceReporter(reported_past["reporter"], "said", "affirmative"),
        )
    patch_event = re.fullmatch(
        rf"More recently, in [A-Z][a-z]+, it released security updates for two more actively exploited "
        rf"{ENTITY} RCE zero-days \({CVE_LIST}\) that let attackers deploy custom web shells and tunneling malware, "
        rf"steal credentials, gain root access, and spread into victims\' internal networks{END_MARKS}",
        core,
    )
    if patch_event:
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            context_role="composed:historical_patch_event",
        )
    capability_frame = (
        re.fullmatch(
            rf"Insufficient input validation; it can be exploited through a crafted HTTP request sent to the {ENTITY}, a feature that is disabled by default{END_MARKS}",
            core,
        )
        or re.fullmatch(
            rf"Improper validation of MPLS echo-request packets allows exploitation through a crafted request sent to an affected device[’\']s IP address{END_MARKS}",
            core,
        )
        or re.fullmatch(
            rf"Improper validation of IP traffic can be exploited through crafted packets sent to an IP interface; all three require {ENTITY} to be enabled{END_MARKS}",
            core,
        )
    )
    if capability_frame:
        return replace(base, modal="capability", context_role="composed:capability")
    if re.fullmatch(
        rf"The advisory lists {COUNT} known flaws that it says were (?P<negative>not )?successfully exploited{END_MARKS}",
        core,
    ):
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            polarity="negative" if "were not " in core else "affirmative",
            context_role="composed:exhaustive_list",
            reporter=EvidenceReporter("The advisory", "says", "affirmative"),
        )
    nominal = re.sub(
        r"\b(?:post-exploitation tools|manual exploitation techniques|exploited bugs|Known Exploited Vulnerabilities catalog)\b",
        "NOMINAL_CONTEXT",
        core,
        flags=re.I,
    )
    if nominal != core and not TOPIC.search(nominal):
        return replace(base, context_role="composed:technique")
    patch_capability = re.fullmatch(
        rf"Earlier this month, {ENTITY} issued emergency updates to address a {ENTITY} denial-of-service zero-day flaw "
        rf"\({CVE_LIST}\) that researchers and admins later said could also be exploited to gain remote code execution{END_MARKS}",
        core,
    )
    if patch_capability:
        return replace(base, modal="capability", context_role="composed:capability")
    purpose = (
        re.fullmatch(
            rf"(?:The agent maps unfamiliar login surfaces, discovers security weaknesses, and )?"
            rf"generates purpose-built automation to exploit them{END_MARKS}",
            core,
        )
        or re.fullmatch(
            rf"(?:The competition identifies|{ENTITY} organizes the competition to identify) "
            rf"zero-day flaws before attackers exploit them in the wild{END_MARKS}",
            core,
        )
        or re.fullmatch(
            rf"These state-sponsored hackers continue to aggressively target and access networks and systems throughout the world "
            rf"in an effort to identify and steal files and otherwise exploit victims' vulnerabilities{END_MARKS}",
            core,
        )
    )
    if purpose:
        return replace(
            base, verb="exploit", context_role="composed:purpose", purposes=(core,)
        )
    alleged_tool = re.fullmatch(
        rf"A second {ENTITY} tool is {ENTITY}, which allegedly enabled the exploitation of computer networks "
        rf"through spear-phishing attacks and the deployment of follow-on payloads{END_MARKS}",
        core,
    )
    if alleged_tool:
        return replace(
            base,
            modal="capability",
            context_role="composed:alleged_capability",
            reporting=("allegedly",),
        )
    demonstration = re.fullmatch(
        rf"The (?:(?:[A-Z][A-Za-z0-9]* ){{0,2}}(?:\d{{4}} )?)?(?:hacking |research )?contest (?:has )?concluded, "
        rf"with (?:hackers|researchers) collecting {MONEY} in rewards after exploiting {COUNT} zero-day flaws{END_MARKS}",
        core,
    ) or re.fullmatch(
        rf"In total, today security researchers exploited {COUNT} zero-days for {MONEY} in cash on the final day of the contest{END_MARKS}",
        core,
    )
    if demonstration:
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            context_role="composed:research",
        )
    campaign = re.fullmatch(
        r"Analysis of these incidents shows that attackers (?P<aux>are|were) (?P<negative>not )?probing websites and APIs for "
        r"(?:access-control|configuration|authentication)(?:, (?:and )?(?:access-control|configuration|authentication))* weaknesses, "
        rf"and exploiting known (?:\(n-day\) )?vulnerabilities{END_MARKS}",
        core,
    )
    if campaign:
        return replace(
            base,
            kind="assertion",
            subject="attackers",
            verb="exploiting",
            tense=AUXILIARY_STATES[(campaign["aux"],)],
            finite=True,
            polarity="negative" if campaign["negative"] else "affirmative",
            context_role="composed:coordinated_activity",
            reporter=EvidenceReporter(
                "Analysis of these incidents", "shows", "affirmative"
            ),
        )
    weaponization = re.fullmatch(
        r"A file upload vulnerability(?: in a popular web-based recreation management software platform designed for local municipalities and parks)? "
        rf"has been weaponized to compromise {COUNT} servers by adding a new account, using it to upload web shells, "
        rf"and ultimately stealing payment data{END_MARKS}",
        core,
    )
    if weaponization:
        return replace(
            base,
            kind="assertion",
            verb="weaponized",
            tense="past",
            finite=True,
            context_role="composed:completed_outcome",
        )
    intrusion = re.fullmatch(
        rf"(?:On [A-Z][a-z]+ \d{{1,2}}, \d{{4}}, during|During) the first breach, (?:he|the attacker) drained (?:about )?{MONEY}"
        rf"(?: out of {ENTITY}'?s liquidity pool)? by exploiting a flaw in its smart contract code to issue (?:zero-token )?withdrawal commands, "
        rf"which forced the exchange to pay rewards(?: he wasn't entitled to)?{END_MARKS}",
        core,
    ) or re.fullmatch(
        rf"Three weeks later, (?:he|the attacker) hit (?:the exchange|{ENTITY}) again, exploiting a separate coding error that "
        rf"(?:caused the exchange's transaction-verification logic to use [\d,]+ instead of [\d,]+ and )?allowed him to withdraw "
        rf"(?:its assets|nearly \d+% of the assets held in {ENTITY}'?s liquidity pools while depositing effectively zero tokens){END_MARKS}",
        core,
    )
    if intrusion:
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            context_role="composed:intrusion",
        )
    capability = re.fullmatch(
        rf"Tracked as {CVE_ID_PATTERN.pattern}, this flaw stems from a memory overflow weakness that attackers can exploit "
        r"to gain remote code execution \(RCE\) on targeted devices or trigger a denial-of-service state that can cause crashes"
        + END_MARKS,
        core,
    )
    if capability:
        return replace(
            base, verb="exploit", modal="capability", context_role="composed:capability"
        )
    return None


def _reported_event(text):
    """A finite evidence operator composes with the existing event owner."""
    absence = re.fullmatch(
        rf'["“]?(?:(?P<asof>As of the publication of the bulletin), )?'
        rf"(?:(?P<group>{CVE_LIST}) were discovered during internal security testing, and )?"
        rf"(?P<reporter>{REPORTER_SUBJECT}) (?:(?P<outer>said) it )?"
        rf"(?P<finite>is not aware|was unaware) of "
        rf"(?:any unmitigated exploits of (?P<target>{CVE_LIST})|public announcements or malicious exploitation)"
        rf"(?P<time> at the time of publishing the advisories)?{END_MARKS}",
        text,
    )
    if absence:
        return OwnedClause(
            text=text,
            cves=tuple(extract_cve_ids(text)),
            kind="assertion",
            context_role="composed:reporter_absence",
            verb="exploitation",
            finite=True,
            reporter=EvidenceReporter(
                absence["reporter"],
                " ".join(filter(None, (absence["outer"], absence["finite"]))),
                "negative",
                as_of=absence["asof"] or (absence["time"] or "").strip(),
            ),
        )
    denied = REPORTER_DENIAL.fullmatch(text)
    core = denied["event"] if denied else text
    match = REPORTER_EVIDENCE.fullmatch(core)
    if not match:
        return None
    event = _unit(match["event"])
    # Reporter absence cannot make an unclassified embedded assertion safe.
    # Its full finite event still needs a supported subject/predicate/argument.
    reporter = EvidenceReporter(
        denied["subject"] if denied else match["subject"],
        match["finite"],
        "negative" if match["negative"] else "affirmative",
        "denied report" if denied else "double negation" if match["double"] else "",
    )
    adjunct = re.fullmatch(
        r"(?:in the wild|at the time of publication|last year|last week|today|yesterday)?",
        event.object_text.strip(" .!?"),
        re.I,
    )
    return replace(
        event,
        text=text,
        reporter=reporter,
        unsupported=event.unsupported or event.kind != "assertion" or adjunct is None,
    )


PARTICIPIAL_PREDICATE_HEADS = frozenset(
    {
        "exploited",
        "weaponized",
        "affected",
        "vulnerable",
        "exploitable",
    }
)
PREDICATE_HEADS = (
    FINITE_PREDICATE_HEADS | PARTICIPIAL_PREDICATE_HEADS | {"be", "been", "being"}
)
ADJUNCT_INTRODUCERS = frozenset(
    {
        "after",
        "before",
        "when",
        "because",
        "since",
        "until",
        "once",
        "although",
        "though",
        "unless",
        "if",
        "where",
        "during",
        "upon",
        "in",
        "by",
        "on",
        "at",
        "through",
        "via",
        "against",
        "for",
        "to",
        "from",
        "with",
        "without",
        "as",
        "within",
        "across",
        "under",
        "over",
        "throughout",
        "around",
        "despite",
    }
)
PREDICATE_ADVERBS = frozenset(
    {
        "worldwide",
        "abroad",
        "overseas",
        "here",
        "there",
        "today",
        "yesterday",
        "tomorrow",
        "tonight",
        "earlier",
        "later",
        "again",
        "already",
        "often",
        "sometimes",
        "always",
        "ever",
        "soon",
        "twice",
        "ago",
        "overnight",
    }
)
TIME_UNIT = r"(?:second|minute|hour|day|week|fortnight|month|quarter|year|weekend|night|morning|afternoon|evening)s?"
WEEKDAY = r"(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)(?: (?:morning|afternoon|evening|night))?"
QUANTITY = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|several|many|multiple|numerous|a|an|(?:hundreds|thousands|millions|dozens) of)"
NOMINAL_ADJUNCT = re.compile(
    rf"(?:(?:the )?(?:last|next|previous|following|this|that|every|each|all) (?:{QUANTITY} )?(?:{TIME_UNIT}|{WEEKDAY})"
    rf"|{QUANTITY} {TIME_UNIT}"
    rf"|{WEEKDAY}"
    rf"|(?:(?:more|less|fewer) than |at (?:least|most) |up to )?{QUANTITY} (?:times|occasions))(?= |$)"
)


def _predicate_head(clause: str) -> str:
    # Only known modifiers may precede an inherited predicate. In particular,
    # an arbitrary -ly suffix is not enough: it can also occur in noun subjects.
    words = clause.casefold().rstrip(".!?").split()
    for index, word in enumerate(words):
        if word not in PREDICATE_MODIFIERS:
            if word in PARTICIPIAL_PREDICATE_HEADS:
                # An adjective/participle can instead introduce a noun subject:
                # "newly affected issue" is not the prior CVE's predicate.
                # Parse the continuation as adverbs followed by an optional
                # adjunct. A new noun phrase ends attribution regardless of
                # which lexical verb follows it. An adjunct's own finite verb
                # does not establish a new subject for the main predicate.
                tail = words[index + 1 :]
                while tail:
                    token = tail[0]
                    if token in ADJUNCT_INTRODUCERS:
                        break
                    nominal = NOMINAL_ADJUNCT.match(" ".join(tail))
                    if nominal:
                        tail = tail[len(nominal.group().split()) :]
                        continue
                    if (
                        token in PREDICATE_MODIFIERS | PREDICATE_ADVERBS
                        or re.fullmatch(r"[a-z]+ly", token)
                    ):
                        tail = tail[1:]
                        continue
                    return ""
            return word
    return ""


def _reporting(text):
    """An explicit reporting adjunct has its own complete finite relation."""
    match = re.search(
        r"\s+as\s+(?:(?:was|is)\s+|(?:investigators|researchers|the vendor)\s+)"
        r"(?:confirmed|confirm|observed|observe|detected|detect)"
        r"(?:\s+(?:today|yesterday|last year|last week|two years ago))?[.!?]*$",
        text,
        re.I,
    )
    return (text[: match.start()], (match.group().strip(),)) if match else (text, ())


def _prefix(text):
    """Consume a governing operator, not matching words in predicate arguments."""
    modal, negative = "", False
    epistemic = re.match(
        r"^(?:It is )?(unknown|unclear|unconfirmed|unverified|possible)\s+(?:whether|which|that)\s+",
        text,
        re.I,
    )
    if epistemic:
        modal = "possible" if epistemic[1].lower() == "possible" else "unknown"
        text = text[epistemic.end() :]
    absent = re.match(
        r"^(?:There is |There are )?(?:no (?:evidence|signs?|reports?|known exploitation|exploitation)|without (?:evidence|reports?))\s*(?:(?:that|of)\s+)?",
        text,
        re.I,
    )
    if absent:
        negative = True
        text = text[absent.end() :]
    return text, modal, negative


INTRUSION_FRAMES = (
    re.compile(
        r"\b(?:gained|obtained) access\b[^.!?;]*?\bby exploiting (?:a |the )?"
        r"(?:vulnerability|flaw|bug)\s*\(?(?P<cve>CVE-\d{4}-\d{4,})\)?",
        re.I,
    ),
    re.compile(
        r"(?P<cve>CVE-\d{4}-\d{4,})\s*,\s*which\s+(?P<subject>[^.!?;]*?)\bbegan exploiting\b"
        r"(?=\s*(?:[,.!?;]|$)|\s+(?:as|in|on|during|before|after)\b)",
        re.I,
    ),
)


def _intrusion_frames(text):
    return [match for frame in INTRUSION_FRAMES for match in frame.finditer(text)]


def _intrusion(text):
    """Consume one closed historical frame and its non-predicate context."""
    frames = _intrusion_frames(text)
    if not frames:
        return None
    frame = frames[0]
    prefix = frame.groupdict().get("subject") or text[: frame.start()]
    suffix = text[frame.end() :].strip(" ,")
    cves = tuple(extract_cve_ids(text))
    # The prefix governs this event; the suffix remains separately attributed
    # context. These productions cannot create an ongoing-activity predicate.
    qualifier = re.search(
        r"\b(?:(?P<unknown>is alleged to have|reportedly|speculated that|unknown whether|denied|disputed)"
        r"|(?P<possible>may have|might have|could have|possibly|potentially)"
        r"|(?P<negative>never|not))\b",
        prefix,
        re.I,
    )
    modal = (
        "unknown"
        if qualifier and qualifier["unknown"]
        else "possible" if qualifier and qualifier["possible"] else ""
    )
    return OwnedClause(
        text=text,
        cves=cves,
        attribution="explicit",
        kind="assertion",
        verb="exploited",
        tense="past",
        modal=modal,
        polarity="negative" if qualifier and qualifier["negative"] else "affirmative",
        unsupported=len(frames) != 1
        or len(cves) != 1
        or bool(TOPIC.search(prefix) or TOPIC.search(suffix))
        or not _tail(suffix),
    )


def _tail(text):
    """A complete predicate may have an adjunct, never an unbound noun subject."""
    words = text.casefold().strip(" ,.!?").split()
    while words:
        token = words[0]
        if token in ADJUNCT_INTRODUCERS - {
            "when",
            "once",
            "until",
            "although",
            "though",
            "if",
            "unless",
        }:
            return True
        nominal = NOMINAL_ADJUNCT.match(" ".join(words))
        if nominal:
            words = words[len(nominal.group().split()) :]
        elif token in PREDICATE_MODIFIERS | PREDICATE_ADVERBS:
            words.pop(0)
        else:
            return False
    return True


def _unit(raw):
    if quoted := _quoted_event(raw):
        return quoted
    core, reporting = _reporting(raw)
    if intrusion := _intrusion(core):
        return replace(intrusion, text=raw, reporting=reporting)
    label = re.match(r"^([^:]+):\s*", core)
    if label and not TOPIC.search(label[1]):
        core = core[label.end() :]
    core, modal, negative = _prefix(core.strip())
    if composed := _closed_composition(core):
        return replace(
            composed,
            text=raw,
            modal=modal or composed.modal,
            polarity="negative" if negative else composed.polarity,
            reporting=reporting,
        )
    if reported := _reported_event(core):
        return replace(
            reported, text=raw, modal=modal or reported.modal, reporting=reporting
        )
    cves = tuple(extract_cve_ids(core))
    base = OwnedClause(
        text=raw,
        cves=cves,
        attribution="explicit" if cves else "unscoped",
        reporting=reporting,
    )
    other = re.fullmatch(
        rf"(?P<reporter>{REPORTER_SUBJECT}) warned of several other "
        r"(?:[A-Z][A-Za-z0-9-]* ){0,4}vulnerabilities that attackers have abused since the start of the year[.!?]*",
        core,
    )
    if other:
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            attribution="other",
            reporter=EvidenceReporter(other["reporter"], "warned", "affirmative"),
        )
    onset = re.fullmatch(
        rf"(?:The development comes as )?(?:Three|three|Two|two|The|the) "
        rf"(?:different )?(?:vulnerabilities|flaws) in "
        rf"(?:[A-Z][A-Za-z0-9-]*(?: and)? ){{1,8}}(?:appliances|systems|devices) "
        rf"\({CVE_LIST}\) (?:have|had) come under active exploitation in the wild[.!?]*",
        core,
    )
    if onset:
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            context_role="composed:onset",
        )
    if re.fullmatch(
        r"(?:Current exploitation activity is not established by the supplied evidence|"
        r"the combined exploitation status is unknown|"
        rf"Reporting contains conflicting exploitation evidence for {CVE_LIST})[.!?]*",
        core,
        re.I,
    ):
        return replace(base, kind="assertion", verb="exploitation", modal="unknown")
    if re.fullmatch(
        r"Researchers attribute attacks exploiting CVE-\d{4}-\d{4,} to [^.!?]+[.!?]*",
        core,
        re.I,
    ):
        # Attribution of an attack to an actor is descriptive context; it does
        # not establish whether exploitation is ongoing or historical.
        return replace(base, verb="attribute", object_text=core)
    # Nominal evidence/assessment forms have explicit owners and no auxiliary
    # whose tense could be borrowed from a reporting adjunct.
    nominal = re.sub(r"^Although\s+", "", core, flags=re.I)
    nominal = re.sub(rf"^{CVE_LIST}\s+", "", nominal, flags=re.I)
    nominal = re.sub(
        r"^(?:Supplied reporting (?:states|confirms|describes)|Some supplied reporting states(?: that)?)\s+",
        "",
        nominal,
        flags=re.I,
    )
    if re.fullmatch(
        r"exploitation is (?:unconfirmed|unknown|unclear)[.!?]*", nominal, re.I
    ):
        return replace(base, kind="assertion", verb="exploitation", modal="unknown")
    if re.fullmatch(
        r"Recent exploitation activity is concentrated in [^.!?]+[.!?]*", nominal, re.I
    ):
        return replace(base, kind="assertion", verb="exploitation", tense="current")
    if re.fullmatch(r"Opportunistic exploitation[.!?]*", nominal, re.I):
        return base
    if re.fullmatch(
        rf"exploitation status(?: for (?:{CVE_LIST}|this source finding))? is (?:unknown|unclear)(?: from the supplied evidence| for the gateway)?[.!?]*",
        nominal,
        re.I,
    ):
        return replace(base, kind="assertion", verb="exploitation", modal="unknown")
    if re.fullmatch(
        r"(?:has an? )?exploitation more likely(?: assessment)?[.!?]*", nominal, re.I
    ):
        return replace(base, kind="assertion", verb="exploitation", modal="possible")
    noun = re.fullmatch(
        rf"(?:(?P<qualifier>active|potential|possible) )?exploitation(?: of| for)?(?: {CVE_LIST})?(?: (?P<aux>has not been|has been|was|is))?(?: (?P<event>confirmed|observed|detected))?(?P<tail>[^.!?]*)[.!?]*",
        nominal,
        re.I,
    )
    if noun:
        auxiliary = (noun["aux"] or "").lower()
        certainty = (noun["qualifier"] or "").lower()
        unknown_tail = bool(noun["tail"].strip() and not _tail(noun["tail"]))
        return replace(
            base,
            kind="assertion",
            verb="exploitation",
            modal=modal
            or ("possible" if certainty in {"potential", "possible"} else ""),
            polarity="negative" if negative or "not" in auxiliary else "affirmative",
            tense="past" if auxiliary in {"was", "has been"} else "current",
            unsupported=unknown_tail
            or not (negative or auxiliary or certainty or noun["event"]),
        )
    if negative and TOPIC.search(raw):
        return replace(
            base,
            kind="assertion",
            verb="exploitation",
            polarity="negative",
            modal=modal,
        )
    # CVE subjects and actor/object frames are distinct productions. An opaque
    # new subject cannot inherit a previous vulnerability's predicate.
    body = re.sub(r"^Although\s+", "", core, flags=re.I)
    owner = _bind_subject(body)
    if owner:
        base = replace(base, subject=owner.text)
        body = body[owner.end :]
    elif cves:
        # Direct ownership without a supported subject/argument production.
        return replace(
            base,
            kind="assertion" if TOPIC.search(core) else "context",
            unsupported=bool(TOPIC.search(core)),
        )
    words = body.strip(" .!?").split()
    tense, finite, correlative = "unspecified", False, None
    auxiliaries = []
    modifiers = PREDICATE_MODIFIERS | {
        "be",
        "been",
        "being",
        "begun",
        "have",
        "had",
        "has",
        "is",
        "are",
        "was",
        "were",
        "may",
        "might",
        "could",
        "can",
        "will",
        "would",
        "to",
        "yet",
        "known",
        "observed",
        "first",
    }
    while words and words[0].lower() in modifiers:
        word = words.pop(0).lower()
        if word in FINITE_PREDICATE_HEADS | {
            "be",
            "been",
            "being",
            "begun",
            "known",
            "to",
        }:
            auxiliaries.append(word)
        if (
            word == "not"
            and words
            and words[0].lower() in {"only", "just", "merely", "simply"}
        ):
            words.pop(0)
            correlative = (modal, "negative" if negative else "affirmative")
        elif word in {"not", "never"}:
            negative = True
        elif word in POSSIBILITY_WORDS or word in {"may", "might", "could", "would"}:
            modal = modal or "possible"
        if word in FINITE_PREDICATE_HEADS:
            finite = True
    auxiliary_state = AUXILIARY_STATES.get(tuple(auxiliaries))
    if auxiliary_state == "possible":
        modal = modal or "possible"
    elif auxiliary_state:
        tense = auxiliary_state
    verb = words.pop(0).lower() if words else ""
    argument = " ".join(words)
    if verb == "under" and re.fullmatch(
        r"(?:limited, targeted|active) exploitation", argument, re.I
    ):
        return replace(
            base,
            kind="assertion",
            verb="exploitation",
            modal=modal,
            polarity="negative" if negative else "affirmative",
            tense=tense,
            finite=finite,
            unsupported=auxiliary_state is None,
        )
    if owner and owner.kind == "actor":
        if re.fullmatch(
            r"(?:(?:the|a|an|another) (?:(?:vulnerable|affected) )?[a-z]+|it)",
            argument,
            re.I,
        ):
            argument = ""
        target = re.match(r"CVE-\d{4}-\d{4,}\b\s*", argument, re.I)
        if target:
            argument = argument[target.end() :]
        if verb == "exploited" and not finite:
            tense = "past"
        elif verb == "exploit" and not auxiliaries:
            tense = "current"
    if (
        not auxiliaries
        and verb == "weaponized"
        and re.fullmatch(r"in (?:the wild|attacks)", argument, re.I)
    ):
        tense = "current"
    known = verb in {"exploit", "exploited", "exploiting", "weaponized"}
    context = verb in {
        "affected",
        "vulnerable",
        "exploitable",
        "allows",
        "allow",
        "permits",
        "permit",
        "patched",
        "disclosed",
    }
    # A copular capability is not an observation. Its adjuncts must either
    # have been consumed by a complete prerequisite production or remain an
    # explicit unsupported required relation; never silently discard a tail.
    if verb == "exploitable":
        supported = not argument and tuple(auxiliaries) in {
            ("is",),
            ("are",),
            ("was",),
            ("were",),
        }
        return replace(
            base,
            kind="context" if supported else "assertion",
            context_role="capability" if supported else "",
            verb=verb,
            modal="capability",
            polarity="negative" if negative else "affirmative",
            finite=finite,
            unsupported=not supported,
        )
    return replace(
        base,
        kind="assertion" if known or TOPIC.search(core) else "context",
        verb=verb,
        modal=modal,
        polarity="negative" if negative else "affirmative",
        tense=tense,
        object_text=argument,
        unsupported=(known and bool(auxiliaries) and auxiliary_state is None)
        or (known and not _tail(argument))
        or (not known and not context and bool(TOPIC.search(core))),
        finite=finite,
        correlative=correlative,
    )


def _agent_capabilities(sentence):
    """Consume the frozen agent subject and every coordinated capability frame.

    A purpose infinitive is attached to its generating predicate. This cannot
    hide an additional event, missing object or unclassified coordination tail.
    """
    text = sentence.strip('"“”').rstrip(".!")
    subject = re.match(
        r"(?P<phase>In the discovery and login phases )?(?P<subject>[Tt]he agent) ",
        text,
    )
    if not subject:
        return None
    frames = {
        "acts": r"(?P<negative>does not act|acts) without step-by-step supervision",
        "maps": r"(?:autonomously )?(?P<negative>does not map|maps) unfamiliar login surfaces",
        "discovers": r"(?P<negative>does not discover|discovers) security weaknesses",
        "generates": r"(?P<negative>does not generate|generates) purpose-built automation to exploit them",
    }
    remaining = text[subject.end() :]
    clauses = []
    while remaining:
        for verb, grammar in frames.items():
            predicate = re.match(grammar + r"(?=$|,| and )", remaining)
            if predicate:
                clauses.append(
                    OwnedClause(
                        text=predicate.group(),
                        source_text=sentence,
                        subject=subject["subject"],
                        verb=verb,
                        modal="capability",
                        context_role="composed:agent_capability",
                        polarity=(
                            "negative"
                            if predicate["negative"].startswith("does not")
                            else "affirmative"
                        ),
                        conditions=(
                            (subject["phase"].strip(),) if subject["phase"] else ()
                        ),
                        purposes=("to exploit them",) if verb == "generates" else (),
                    )
                )
                remaining = remaining[predicate.end() :]
                break
        else:
            return None
        if remaining:
            boundary = re.match(r",? (?:and )?", remaining)
            if not boundary:
                return None
            remaining = remaining[boundary.end() :]
            if not remaining:
                return None
    return clauses or None


def parse_assertions(sentence):
    """Resolve coordination using each parsed relation's owned qualifiers once."""
    if qualification := source_qualification(sentence):
        return [qualification]
    if envelope := reporting_envelope(sentence):
        return [
            replace(
                clause,
                text=sentence,
                reporter=clause.reporter
                or EvidenceReporter(
                    envelope.subject,
                    envelope.finite,
                    "affirmative",
                    as_of=envelope.adjunct,
                ),
            )
            for clause in parse_assertions(envelope.body)
        ]
    if quoted := _quoted_event(sentence):
        return [quoted]
    if capabilities := _agent_capabilities(sentence):
        return capabilities
    composed = _unit(sentence)
    if composed.context_role.startswith("composed:"):
        return [composed]
    leading = re.fullmatch(
        r"(?P<condition>(?:If|Unless) [A-Za-z][\w-]*(?: and [A-Za-z][\w-]*)* "
        r"(?:is|are|was|were) [A-Za-z][\w-]*),\s*(?P<event>.+)",
        sentence,
    )
    if leading:
        relations = parse_assertions(leading["event"])
        return [
            replace(
                item,
                conditions=(leading["condition"], *item.conditions),
                unsupported=item.unsupported or len(relations) != 1,
            )
            for item in relations
        ]
    identities = [(m.start(), m.end()) for m in re.finditer(CVE_LIST, sentence, re.I)]
    frames = _intrusion_frames(sentence)
    # Object conjunctions and the relative subject belong to these exact
    # productions. Coordinated predicates outside them use the ordinary owner.
    protected = identities + [(frame.start(), frame.end()) for frame in frames]
    protected.extend(
        (frame.start(), frame.end())
        for frame in CAPABILITY_PREREQUISITE.finditer(sentence)
    )
    parts = bind_condition_boundaries(
        sentence,
        boundary=BOUNDARY,
        condition=REQUIRED_ADJUNCT,
        starts_relation=lambda right: bool(
            _bind_subject(right)
            or TOPIC.search(BOUNDARY.split(right, maxsplit=1)[0])
            or _predicate_head(right) in PREDICATE_HEADS
            or _unit(BOUNDARY.split(right, maxsplit=1)[0]).finite
        ),
        protected=protected,
        can_qualify=lambda prefix: _unit(prefix).kind == "assertion",
    )
    results = []
    previous = OwnedClause()
    groups = []
    for index, part in enumerate(parts):
        raw = part.text
        boundary = " ".join(part.connector.lower().split())
        group = None
        if boundary in {"but", ", but"} and groups:
            relation = "correlative"
            group = groups.pop()
        elif boundary in {"but", ", but"}:
            relation = "adversative"
        elif boundary in {"and", ", and"}:
            relation = "additive"
        else:
            relation = "boundary" if index else "root"
            groups.clear()
        clause = _unit(part.predicate)
        clause = replace(
            clause,
            text=raw,
            conditions=clause.conditions + part.conditions,
            unsupported=clause.unsupported
            or part.unsupported
            or any(not CONDITION.match(value) for value in part.conditions),
        )
        head = _predicate_head(raw)
        inherited_subject = (
            relation in {"additive", "adversative", "correlative"}
            and head in PREDICATE_HEADS
            and len(previous.cves) == 1
        )
        if not clause.cves and inherited_subject:
            clause = replace(clause, cves=previous.cves, attribution="coordinated")
        modal = clause.modal
        negative = clause.polarity == "negative"
        if group is not None:
            modal = group[0] or modal
            negative |= group[1] == "negative"
        elif relation == "additive":
            if previous.modal == "unknown":
                modal = "unknown"
            elif inherited_subject and not clause.finite:
                modal = previous.modal or modal
            if inherited_subject and not clause.finite:
                negative |= previous.polarity == "negative"
        clause = replace(
            clause,
            relation=relation,
            modal=modal,
            polarity="negative" if negative else "affirmative",
        )
        if (
            inherited_subject
            and not clause.finite
            and clause.tense == "unspecified"
            and previous.tense in {"current", "past"}
        ):
            clause = replace(clause, tense=previous.tense)
        if clause.kind == "assertion" and clause.assertion_status is None:
            clause = replace(clause, unsupported=True)
        if clause.correlative is not None:
            groups.append(
                (
                    clause.correlative[0]
                    or (previous.modal if relation == "additive" else ""),
                    clause.correlative[1],
                )
            )
        results.append(clause)
        previous = clause
    if any(
        item.reporter or item.context_role.startswith("composed:") for item in results
    ):
        # Recognizing an owned composition does not license discarding an
        # unclassified coordinated remainder of that same source statement.
        owner = tuple(sorted({cve for item in results for cve in item.cves}))
        results = [
            (
                replace(
                    item, kind="assertion", cves=item.cves or owner, unsupported=True
                )
                if item.kind == "context"
                and not item.context_role
                and item.verb
                not in {
                    "affected",
                    "vulnerable",
                    "exploitable",
                    "allows",
                    "allow",
                    "permits",
                    "permit",
                    "patched",
                    "disclosed",
                }
                else item
            )
            for item in results
        ]
    return results
