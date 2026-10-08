"""Finite assertion relations: bind qualifiers before projecting evidence state."""

from dataclasses import replace
import re

from .cve import extract_cve_ids
from .relations import OwnedClause

CVE_LIST = r"CVE-\d{4}-\d{4,}(?:\s*(?:,|and)\s*CVE-\d{4}-\d{4,})*"
DESCRIPTIVE_SUBJECT = re.compile(
    rf"^(?i:(?:two|the) )(?:(?:[A-Z][A-Za-z0-9-]* ){{0,4}})"
    rf"(?i:zero-days|vulnerabilities|flaws) \((?P<identities>{CVE_LIST})\)\s+"
)

POSSIBILITY_WORDS = ("potentially", "likely", "possibly", "probably", "unlikely")
TOPIC = re.compile(r"\b(?:exploit\w*|weaponiz\w*)\b", re.I)
BOUNDARY = re.compile(
    r"([;,]\s*(?:and|but|while|whereas)\b|[;,]|\b(?:and|but|while|whereas)\b)", re.I
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


def _intrusion(text):
    """Two closed historical frames, expressed using the same owned relation."""
    cves = tuple(extract_cve_ids(text))
    if len(cves) != 1:
        return None
    cve = re.escape(cves[0])
    access = re.search(
        rf"\b(?:gained|obtained) access\b[^.!?;]*?\bby exploiting (?:a |the )?(?:vulnerability|flaw|bug)\s*\(?{cve}\)?",
        text,
        re.I,
    )
    relative = re.search(
        rf"{cve}\s*,\s*which\s+(?P<subject>[^.!?;]*?)\bbegan exploiting\b"
        r"(?=\s*(?:[,.!?;]|$)|\s+(?:as|in|on|during|before|after)\b)",
        text,
        re.I,
    )
    if not access and not relative:
        return None
    if access:
        prefix = text[: access.start()]
    elif relative:
        prefix = relative["subject"]
    else:
        return None
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
    conditions = tuple(
        m.group() for m in re.finditer(r"\b(?:if|unless)\b[^.!?]*", text, re.I)
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
        conditions=conditions,
    )


def _tail(text):
    """A complete predicate may have an adjunct, never an unbound noun subject."""
    words = text.casefold().strip(" .!?").split()
    while words:
        token = words[0]
        if token in ADJUNCT_INTRODUCERS:
            return True
        nominal = NOMINAL_ADJUNCT.match(" ".join(words))
        if nominal:
            words = words[len(nominal.group().split()) :]
        elif token in PREDICATE_MODIFIERS | PREDICATE_ADVERBS or re.fullmatch(
            r"[a-z]+ly", token
        ):
            words.pop(0)
        else:
            return False
    return True


def _unit(raw):
    core, reporting = _reporting(raw)
    label = re.match(r"^([^:]+):\s*", core)
    if label and not TOPIC.search(label[1]):
        core = core[label.end() :]
    core, modal, negative = _prefix(core.strip())
    cves = tuple(extract_cve_ids(core))
    base = OwnedClause(
        text=raw,
        cves=cves,
        attribution="explicit" if cves else "unscoped",
        reporting=reporting,
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
    subject = re.match(
        rf"^(?:{CVE_LIST})\b\s*", body, re.I
    ) or DESCRIPTIVE_SUBJECT.match(body)
    actor = re.match(r"^(?:attackers?|actors?|operators?)\s+", body, re.I)
    owner = subject or actor
    if owner:
        body = body[owner.end() :]
    elif cves:
        # Direct ownership without a supported subject/argument production.
        return replace(
            base,
            kind="assertion" if TOPIC.search(core) else "context",
            unsupported=bool(TOPIC.search(core)),
        )
    words = body.strip(" .!?").split()
    tense, finite, correlative = "unspecified", False, None
    modifiers = PREDICATE_MODIFIERS | {
        "be",
        "been",
        "being",
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
            if word in {"was", "were", "had"}:
                tense = "past"
            elif word in {"is", "are"}:
                tense = "current"
    verb = words.pop(0).lower() if words else ""
    argument = " ".join(words)
    if actor:
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
    conditions = tuple(
        m.group() for m in re.finditer(r"\b(?:if|unless)\b.*", argument, re.I)
    )
    return replace(
        base,
        kind="assertion" if known or TOPIC.search(core) else "context",
        verb=verb,
        modal=modal,
        polarity="negative" if negative else "affirmative",
        tense=tense,
        conditions=conditions,
        object_text=argument,
        unsupported=(known and not _tail(argument))
        or (not known and not context and bool(TOPIC.search(core))),
        finite=finite,
        correlative=correlative,
    )


def parse_assertions(sentence):
    """Resolve coordination using each parsed relation's owned qualifiers once."""
    if intrusion := _intrusion(sentence):
        return [intrusion]
    identities = [(m.start(), m.end()) for m in re.finditer(CVE_LIST, sentence, re.I)]
    parts = []
    start = 0
    for boundary in BOUNDARY.finditer(sentence):
        if any(
            left <= boundary.start() and boundary.end() <= right
            for left, right in identities
        ):
            continue
        parts.extend((sentence[start : boundary.start()], boundary.group()))
        start = boundary.end()
    parts.append(sentence[start:])
    results = []
    previous = OwnedClause()
    groups = []
    for index in range(0, len(parts), 2):
        raw = parts[index].strip()
        if not raw:
            continue
        boundary = " ".join(parts[index - 1].lower().split()) if index else ""
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
        clause = _unit(raw)
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
    return results
