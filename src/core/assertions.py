"""Finite assertion relations: bind qualifiers before projecting evidence state."""

from dataclasses import replace
import re

from .cve import CVE_ID_PATTERN, extract_cve_ids
from .exploitation_contract import has_required_event
from .assertion_predicates import (
    operator_tense,
    BOUNDARY,
    CONDITION,
    CVE_LIST,
    REQUIRED_ADJUNCT,
    FINITE_PREDICATE_HEADS as FINITE_PREDICATE_HEADS,
    bind_predicate,
    bind_target as bind_target,
    AUXILIARY_WORDS,
    PREFIX_WORDS,
)
from .condition_boundaries import bind_condition_boundaries, leading_assertion_condition
from .assertion_qualifiers import (
    EPISTEMIC_MODIFIERS,
    REPORTED_MODIFIERS,
    REPORTED_PATTERN,
    TIME_DIRECTIONS,
    assertion_scope,
    bind_qualifiers,
    detach_reporting,
    modifier_term,
    qualifier_terms,
)
from .relations import (
    ActorParticipation,
    EvidenceOperation,
    EvidenceReporter,
    OwnedClause,
    ScopeOperator,
    ScopeTerm,
    TemporalConstraint,
)
from .source_document import reporting_envelope
from .advisory_relations import bind_advisory

from .assertion_bindings import (
    SubjectBinding,
    bind_subject as _bind_subject,
    REPORTER_SUBJECT,
    NAME,
    SYSTEM_ARGUMENT,
)


def _actor_at(clause, text, offset):
    participant = clause.actor_participation
    return participant.rebase(text, offset) if participant else None


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
        actor_participation=_actor_at(event, text, match.start("event")),
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
    if prerequisite := _configuration_prerequisite(text):
        return prerequisite
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


def _configuration_prerequisite(text):
    """Explicit vulnerability purpose owns configuration necessity, not advice.

    Complete protocol/provider alternatives are arguments of that necessity.
    Existing reporting/condition owners retain their qualifications; no role
    or residual can be discarded to make a prerequisite complete.
    """
    envelope = reporting_envelope(text)
    body = envelope.body if envelope else text
    leading = leading_assertion_condition(body)
    core = leading["event"] if leading else body
    if not re.match(r"To be vulnerable,\s+", core, re.I):
        return None
    alias = r"(?: \([A-Za-z][A-Za-z0-9]*\))?"
    provider = rf"(?:(?:a|an) )?(?:{NAME}{alias} )?(?:Identity|Service) Provider{alias}"
    match = re.fullmatch(
        rf"To be vulnerable, (?P<system>{SYSTEM_ARGUMENT}) must (?P<negative>not )?be configured as "
        rf"{provider}(?: or {provider})?{END_MARKS}",
        core,
    )
    return OwnedClause(
        text=text,
        source_text=text,
        subject=match["system"] if match else "",
        kind="context",
        modal="capability",
        verb="configured",
        polarity="negative" if match and match["negative"] else "affirmative",
        context_role="composed:configuration_prerequisite",
        conditions=((leading["condition"],) if leading else ()) + (core,),
        reporter=(
            EvidenceReporter(
                envelope.subject, envelope.finite, "affirmative", as_of=envelope.adjunct
            )
            if envelope
            else None
        ),
        unsupported=match is None,
    )


def _closed_composition(core):
    """Closed event compositions own their complete participants and adjuncts.

    An event's finite predicate supplies tense; completed outcomes, purpose
    clauses and technique nouns have distinct roles. No topic substring or
    incidental date supplies a state, and a residual cannot be accepted here.
    """
    base = OwnedClause(text=core, cves=tuple(extract_cve_ids(core)))
    if advisory := bind_advisory(core):
        required_unknown = not advisory.complete and has_required_event(core)
        return replace(
            base,
            kind="assertion" if required_unknown else "context",
            modal="capability" if advisory.complete else "",
            polarity=advisory.frame.polarity if advisory.frame else "affirmative",
            scopes=(advisory.frame.scope,) if advisory.frame else (),
            conditions=advisory.declaration_conditions + advisory.relative_conditions,
            unsupported=required_unknown,
            context_role="composed:advisory_capability",
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
        rf"More recently, in [A-Z][a-z]+, it released security updates for two more (?P<activity>actively) exploited "
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
            scopes=(
                assertion_scope(
                    core,
                    (modifier_term(core, *patch_event.span("activity")),),
                    event_tense="past",
                ),
            ),
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
    exhaustive = re.fullmatch(
        rf"The advisory lists {COUNT} known flaws that it says (?P<event>were (?:not )?successfully exploited){END_MARKS}",
        core,
    )
    if exhaustive:
        frame = bind_predicate(exhaustive["event"], voice="vulnerability")
        return replace(
            base,
            kind="assertion",
            verb="exploited",
            tense="past",
            finite=True,
            polarity=frame.polarity,
            scopes=(frame.scope,),
            context_role="composed:exhaustive_list",
            reporter=EvidenceReporter("The advisory", "says", "affirmative"),
        )
    nominal = re.sub(
        r"\b(?:post-exploitation tools|manual exploitation techniques|exploited bugs|Known Exploited Vulnerabilities catalog)\b",
        "NOMINAL_CONTEXT",
        core,
        flags=re.I,
    )
    if nominal != core and not has_required_event(nominal):
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
            tense=operator_tense((campaign["aux"],)),
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
    scopes = event.scopes
    if match["negative"]:
        offset = denied.start("event") if denied else 0
        start, end = match.span("negative")
        start, end = start + offset, end + offset
        scopes += (
            assertion_scope(
                text,
                operators=(
                    ScopeOperator(text[start:end], start, end, "absence", "evidence"),
                ),
            ),
        )
    return replace(
        event,
        text=text,
        reporter=reporter,
        actor_participation=_actor_at(
            event, text, match.start("event") + (denied.start("event") if denied else 0)
        ),
        scopes=scopes,
        unsupported=event.unsupported or event.kind != "assertion",
    )


def _prefix(text):
    """Consume a governing operator, not matching words in predicate arguments."""
    original = text
    modal, negative = "", False
    operators = []
    offset = 0
    epistemic = re.match(
        r"^(?:It is )?(unknown|unclear|unconfirmed|unverified|possible)\s+(?:whether|which|that)\s+",
        text,
        re.I,
    )
    if epistemic:
        modal = "possible" if epistemic[1].lower() == "possible" else "unknown"
        text = text[epistemic.end() :]
        offset = epistemic.end()
        operators.append(
            ScopeOperator(original[:offset], 0, offset, "qualification", "event")
        )
    absent = re.match(
        r"^(?:There is |There are )?(?:no (?:evidence|signs?|reports?|(?P<nominal>known exploitation|exploitation))|without (?:evidence|reports?))\b\s*(?:(?:that|of)\s+)?",
        text,
        re.I,
    )
    if absent:
        negative = True
        text = text[absent.end() :]
        end = offset + absent.end()
        operators.append(
            ScopeOperator(original[offset:end], offset, end, "absence", "evidence")
        )
        if absent["nominal"]:
            # Preserve the assertion's noun head after consuming its negative
            # determiner, so nominal predicates still consume their own tail.
            text = "exploitation " + text
    scopes = (assertion_scope(original, operators=operators),) if operators else ()
    return text, modal, negative, scopes


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
        r"\b(?:(?P<unknown>is alleged to have|speculated that|unknown whether|denied|disputed)"
        r"|(?P<possible>may have|might have|could have)"
        r"|(?P<negative>never|not))\b",
        prefix,
        re.I,
    )
    modal = (
        "unknown"
        if qualifier and qualifier["unknown"]
        else "possible" if qualifier and qualifier["possible"] else ""
    )
    qualifiers = bind_qualifiers(suffix)
    # Only the already accepted terminal operator/modifier sequence belongs
    # to this event. Words inside its actor or preceding disclosure do not.
    tokens = list(re.finditer(r"\S+", prefix))
    positioned = {}
    # A leading modifier owns the complete existing intrusion proposition,
    # including its actor. Internal actor/reporting words are not that edge.
    for token in tokens:
        if token.group().casefold() not in EPISTEMIC_MODIFIERS:
            break
        positioned[token.start()] = token
    for token in reversed(tokens):
        if token.group().casefold() not in PREFIX_WORDS:
            break
        positioned[token.start()] = token
    terms, operators, prefix_time = [], [], []
    for _, token in sorted(positioned.items()):
        word = token.group().casefold()
        if word in {"not", "never"}:
            operators.append(
                ScopeOperator(
                    token.group(), token.start(), token.end(), "negation", "event"
                )
            )
        elif word not in AUXILIARY_WORDS:
            terms.append(modifier_term(prefix, token.start(), token.end()))
            if word in TIME_DIRECTIONS:
                prefix_time.append(
                    TemporalConstraint("event", TIME_DIRECTIONS[word], token.group())
                )
    prefix_scope = assertion_scope(prefix, terms, operators, event_tense="past")
    if not modal and any(term.kind == "epistemic" for term in terms):
        modal = "possible"
    if qualifier and qualifier["unknown"]:
        prefix_scope = replace(
            prefix_scope,
            operators=prefix_scope.operators
            + (
                ScopeOperator(
                    qualifier[0], *qualifier.span(), "qualification", "envelope"
                ),
            ),
        )
    tail_scope = assertion_scope(suffix, qualifier_terms(suffix, qualifiers.spans))
    # Every governing negation must belong to the completely consumed
    # terminal operator sequence. An unclassified bridge cannot erase it and
    # turn this historical relation into an affirmative observation.
    negation_spans = {
        (token.start(), token.end())
        for token in tokens
        if token.group().casefold() in {"not", "never"}
    }
    bound_negations = {(operator.start, operator.end) for operator in operators}
    return OwnedClause(
        text=text,
        cves=cves,
        attribution="explicit",
        temporal=tuple(prefix_time)
        + tuple(q.temporal for q in qualifiers.spans if q.temporal),
        scopes=(prefix_scope, tail_scope),
        kind="assertion",
        verb="exploited",
        tense="past",
        modal=modal,
        polarity="negative" if operators else "affirmative",
        unsupported=len(frames) != 1
        or len(cves) != 1
        or (has_required_event(prefix) or has_required_event(suffix))
        or not prefix_scope.supported
        or negation_spans != bound_negations
        or not qualifiers.complete,
    )


def _unit(raw):
    if quoted := _quoted_event(raw):
        return quoted
    core, reporting_spans = detach_reporting(raw)
    core_start = 0
    reporting = tuple(q.text for q in reporting_spans)
    reporter_time = tuple(q.temporal for q in reporting_spans if q.temporal)
    if intrusion := _intrusion(core):
        return replace(
            intrusion,
            text=raw,
            reporting=reporting,
            temporal=intrusion.temporal + reporter_time,
        )
    label = re.match(r"^([^:]+):\s*", core)
    if label and not has_required_event(label[1]):
        core_start += label.end()
        core = core[label.end() :]
    core_start += len(core) - len(core.lstrip())
    unprefixed = core.strip()
    core, modal, negative, prefix_scopes = _prefix(unprefixed)
    core_start += len(unprefixed) - len(core)
    if composed := _closed_composition(core):
        return replace(
            composed,
            text=raw,
            modal=modal or composed.modal,
            polarity="negative" if negative else composed.polarity,
            scopes=prefix_scopes + composed.scopes,
            reporting=reporting,
            temporal=composed.temporal + reporter_time,
        )
    if reported := _reported_event(core):
        return replace(
            reported,
            text=raw,
            actor_participation=_actor_at(reported, raw, core_start),
            modal=modal or reported.modal,
            scopes=prefix_scopes + reported.scopes,
            reporting=reporting,
            temporal=reported.temporal + reporter_time,
        )
    cves = tuple(extract_cve_ids(core))
    base = OwnedClause(
        text=raw,
        cves=cves,
        attribution="explicit" if cves else "unscoped",
        reporting=reporting,
        temporal=reporter_time,
        scopes=prefix_scopes,
        modal=modal,
        polarity="negative" if negative else "affirmative",
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
        rf"\({CVE_LIST}\) (?:have|had) come under (?P<activity>active) exploitation in the wild[.!?]*",
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
            scopes=base.scopes
            + (
                assertion_scope(
                    core,
                    (modifier_term(core, *onset.span("activity")),),
                    event_tense="past",
                ),
            ),
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
    recent = re.fullmatch(
        r"(?P<time>Recent) exploitation activity is concentrated in [^.!?]+[.!?]*",
        nominal,
        re.I,
    )
    if recent:
        return replace(
            base,
            kind="assertion",
            verb="exploitation",
            tense="current",
            scopes=base.scopes
            + (
                assertion_scope(
                    nominal,
                    (ScopeTerm(recent["time"], *recent.span("time"), "time"),),
                    event_tense="current",
                ),
            ),
        )
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
        rf"(?:(?P<qualifier>active|potential|possible) )?exploitation(?: of| for)?(?: {CVE_LIST})?"
        rf"(?P<operators>(?: (?:has|not|been|was|is|{REPORTED_PATTERN}))*)"
        r"(?: (?P<event>confirmed|observed|detected))?(?P<tail>[^.!?]*)[.!?]*",
        nominal,
        re.I,
    )
    if noun:
        tokens = list(
            re.finditer(
                r"\S+", nominal[noun.start("operators") : noun.end("operators")]
            )
        )
        auxiliary_spans = tuple(
            (
                noun.start("operators") + token.start(),
                noun.start("operators") + token.end(),
            )
            for token in tokens
            if token.group().casefold() not in REPORTED_MODIFIERS
        )
        auxiliary = " ".join(
            nominal[start:end].lower() for start, end in auxiliary_spans
        )
        modifiers = tuple(
            modifier_term(
                nominal,
                noun.start("operators") + token.start(),
                noun.start("operators") + token.end(),
                owner="evidence",
            )
            for token in tokens
            if token.group().casefold() in REPORTED_MODIFIERS
        )
        certainty = (noun["qualifier"] or "").lower()
        qualifiers = bind_qualifiers(noun["tail"])
        unknown_tail = not qualifiers.complete
        operation = (
            EvidenceOperation(
                noun["event"].lower(),
                auxiliary,
                "negative" if auxiliary == "has not been" else "affirmative",
                nominal,
                (
                    (auxiliary_spans[0][0], auxiliary_spans[-1][1])
                    if auxiliary
                    else (0, 0)
                ),
                noun.span("event"),
                tuple(q.temporal for q in qualifiers.spans if q.temporal),
                absence=negative,
                auxiliary_spans=auxiliary_spans if modifiers else (),
            )
            if noun["event"]
            else None
        )
        terms = modifiers + qualifier_terms(
            nominal,
            qualifiers.spans,
            offset=noun.start("tail"),
            owner="evidence" if operation else "event",
        )
        if certainty:
            terms = (modifier_term(nominal, *noun.span("qualifier")), *terms)
        operators = ()
        if auxiliary == "has not been":
            start = auxiliary_spans[1][0]
            operators = (
                ScopeOperator(
                    nominal[start : start + 3],
                    start,
                    start + 3,
                    "evidence_negation",
                    "evidence",
                ),
            )
        scope = assertion_scope(nominal, terms, operators)
        return replace(
            base,
            kind="assertion",
            verb="exploitation",
            temporal=base.temporal
            + (
                ()
                if operation
                else tuple(q.temporal for q in qualifiers.spans if q.temporal)
            ),
            evidence_operation=operation,
            scopes=base.scopes + (scope,),
            modal=modal
            or ("possible" if certainty in {"potential", "possible"} else ""),
            polarity="negative" if negative and not operation else "affirmative",
            tense=(
                "current"
                if certainty == "active"
                and auxiliary not in {"was", "has been", "has not been"}
                else (
                    "unspecified"
                    if operation
                    else "past" if auxiliary in {"was", "has been"} else "current"
                )
            ),
            unsupported=unknown_tail
            or auxiliary not in {"", "is", "was", "has been", "has not been"}
            or not scope.supported
            or bool(modifiers and operation is None)
            or not (negative or auxiliary or certainty or noun["event"]),
        )
    # The legacy negative envelope must still own a complete event. Its
    # existing nominal gerund frame has no finite auxiliary to borrow; every
    # other event proceeds through the canonical subject/predicate owner.
    absence_subject = _bind_subject(core) if negative else None
    if absence_subject and absence_subject.kind != "vulnerability":
        absence_subject = None
    implicit_absence = (
        re.match(r"^(the (?:flaw|issue|vulnerability))\s+", core, re.I)
        if negative
        else None
    )
    absence_end = (
        absence_subject.end
        if absence_subject
        else implicit_absence.end() if implicit_absence else 0
    )
    absent_nominal = (
        re.match(r"being (?P<event>weaponized|exploited)\b", core[absence_end:], re.I)
        if absence_end
        else None
    )
    if absent_nominal:
        tail = core[absence_end + absent_nominal.end() :]
        qualifiers = bind_qualifiers(tail)
        return replace(
            base,
            kind="assertion",
            subject=core[:absence_end].strip(),
            verb=absent_nominal["event"],
            polarity="negative",
            scopes=base.scopes
            + (assertion_scope(tail, qualifier_terms(tail, qualifiers.spans)),),
            modal=modal,
            object_text=tail,
            temporal=base.temporal
            + tuple(q.temporal for q in qualifiers.spans if q.temporal),
            unsupported=not qualifiers.complete,
        )
    # CVE subjects and actor/object frames are distinct productions. An opaque
    # new subject cannot inherit a previous vulnerability's predicate.
    body = re.sub(r"^Although\s+", "", core, flags=re.I)
    subject_start = core_start + len(core) - len(body)
    owner = _bind_subject(body)
    if owner:
        base = replace(base, subject=owner.text)
        body = body[owner.end :]
    elif cves:
        # Direct ownership without a supported subject/argument production.
        return replace(
            base,
            kind="assertion" if has_required_event(core) else "context",
            unsupported=has_required_event(core),
        )
    frame = bind_predicate(
        body,
        voice=owner.kind if owner else "unscoped",
        modal=modal,
        negative=negative,
        subject=owner,
    )
    owned_cves = (
        frame.target.cves
        if owner and owner.kind == "actor" and frame.target.kind == "explicit"
        else tuple(extract_cve_ids(owner.text)) if owner else base.cves
    )
    participant = None
    if frame.supported and frame.kind == "assertion":
        if owner and owner.kind == "actor":
            participant = ActorParticipation(
                owner,
                "subject",
                raw,
                (subject_start, subject_start + len(owner.text)),
            )
        else:
            agents = [
                term
                for term in frame.scope.terms
                if term.kind == "agent" and term.owner == "event"
            ]
            if len(agents) == 1:
                # This term was admitted by the shared subject production.
                # Keep its literal binding; do not recognize names again.
                agent = agents[0]
                nominal = agent.text[3:]
                start = subject_start + (owner.end if owner else 0) + agent.start + 3
                participant = ActorParticipation(
                    SubjectBinding("actor", nominal, len(nominal)),
                    "agent",
                    raw,
                    (start, start + len(nominal)),
                )
    return replace(
        base,
        cves=owned_cves if frame.supported else base.cves,
        kind=frame.kind,
        context_role=(
            "capability" if frame.verb == "exploitable" and frame.supported else ""
        ),
        verb=frame.verb,
        modal=frame.modal,
        polarity=frame.polarity,
        scopes=base.scopes
        + (frame.scope,)
        + (
            (frame.observation.observation_scope,)
            if frame.observation and frame.observation.observation_scope
            else ()
        ),
        tense=frame.tense,
        aspect=frame.aspect,
        temporal=base.temporal + frame.temporal,
        observation=frame.observation,
        object_text=body[slice(*frame.adjunct_span)],
        unsupported=not frame.supported and not frame.requires_inheritance,
        finite=frame.finite,
        correlative=frame.correlative,
        actor_participation=participant,
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
    """Finalize every assertion through the same owned semantic projection."""
    results = [
        (
            replace(item, unsupported=True)
            if item.kind == "assertion" and item.assertion_status is None
            else item
        )
        for item in _parse_assertions(sentence)
    ]
    # An incomplete statement cannot supply presentation participants from a
    # partially admitted branch, even when that branch has a lexical subject.
    if any(item.unsupported for item in results):
        return [replace(item, actor_participation=None) for item in results]
    return results


def _parse_assertions(sentence):
    """Resolve coordination using each parsed relation's owned qualifiers once."""
    if qualification := source_qualification(sentence):
        return [qualification]
    if envelope := reporting_envelope(sentence):
        return [
            replace(
                clause,
                text=sentence,
                actor_participation=_actor_at(clause, sentence, 1),
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
    leading = leading_assertion_condition(sentence)
    if leading:
        relations = parse_assertions(leading["event"])
        return [
            replace(
                item,
                actor_participation=_actor_at(item, sentence, leading.start("event")),
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
    # An observation owns its whole nominal, including rejected residuals.
    # A lexical event noun after a comma is not a new finite relation. Preserve
    # true independent subjects/finite predicates and the existing conditions.
    boundaries = list(BOUNDARY.finditer(sentence))
    for begin in [0, *(boundary.end() for boundary in boundaries)]:
        candidate = sentence[begin:].lstrip()
        offset = len(sentence) - len(candidate)
        owner = _bind_subject(candidate)
        body_start = owner.end if owner else 0
        frame = bind_predicate(
            candidate[body_start:],
            voice=owner.kind if owner else "unscoped",
            subject=owner,
        )
        event = frame.event_binding
        if event and event.descriptor and event.descriptor.complement:
            start, end = event.complement_span
            protected.append((offset + body_start + start, offset + body_start + end))
        if frame.observation is None:
            continue
        nominal_start = offset + body_start + frame.observation.predicate_span[1]
        for boundary in boundaries:
            if boundary.start() < nominal_start:
                continue
            right = sentence[boundary.end() :].strip()
            if (
                boundary.group().strip() == ";"
                or _bind_subject(right)
                or bind_predicate(right).starts_relation
                or REQUIRED_ADJUNCT.match(right)
            ):
                break
            protected.append((boundary.start(), boundary.end()))
    parts = bind_condition_boundaries(
        sentence,
        boundary=BOUNDARY,
        condition=REQUIRED_ADJUNCT,
        starts_relation=lambda right: bool(
            _bind_subject(right)
            or has_required_event(BOUNDARY.split(right, maxsplit=1)[0])
            or bind_predicate(right).starts_relation
            # Closed reporter/composition productions retain their own typed
            # finite boundary. Ordinary verbal parsing still has one owner.
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
            actor_participation=_actor_at(clause, sentence, part.start),
            conditions=clause.conditions + part.conditions,
            unsupported=clause.unsupported
            or part.unsupported
            or any(not CONDITION.match(value) for value in part.conditions),
        )
        frame = bind_predicate(part.predicate)
        inherited_subject = (
            relation in {"additive", "adversative", "correlative"}
            and frame.inherits_subject
            and len(previous.cves) == 1
        )
        if not clause.cves and inherited_subject:
            clause = replace(clause, cves=previous.cves, attribution="coordinated")
        modal = clause.modal
        negative = clause.polarity == "negative"
        scopes = clause.scopes
        if group is not None:
            modal = group[0] or modal
            negative |= group[1] == "negative"
            if (
                any(t.kind == "reported" for s in group[2] for t in s.terms)
                or group[1] == "negative"
                or (
                    inherited_subject
                    and not clause.finite
                    and any(s.knowledge_negative for s in group[2])
                )
            ):
                scopes = group[2] + scopes
        elif relation == "additive":
            if previous.modal == "unknown":
                modal = "unknown"
            elif inherited_subject and not clause.finite:
                modal = previous.modal or modal
            if inherited_subject and not clause.finite:
                negative |= previous.polarity == "negative"
                if (
                    previous.polarity == "negative"
                    or previous.knowledge_negative
                    or previous.reported_proposition
                ):
                    scopes = previous.scopes + scopes
        if (
            relation == "adversative"
            and inherited_subject
            and not clause.finite
            and (
                previous.knowledge_negative
                or (
                    previous.polarity == "negative"
                    and any(scope.restrictions for scope in previous.scopes)
                )
            )
        ):
            # An elided branch supplies no new current finite. Neither the
            # legacy weaponized default nor guessed past scope can settle it.
            modal = "unknown"
        clause = replace(
            clause,
            relation=relation,
            modal=modal,
            polarity="negative" if negative else "affirmative",
            scopes=scopes,
        )
        if (
            inherited_subject
            and not clause.finite
            and clause.tense == "unspecified"
            and previous.tense in {"current", "past"}
        ):
            clause = replace(clause, tense=previous.tense, aspect=previous.aspect)
        if clause.correlative is not None:
            governing_scopes = []
            for scope in clause.scopes:
                markers = [o.start for o in scope.operators if o.kind == "correlative"]
                boundary_start = min(markers) if markers else len(scope.text)
                governing_scopes.append(
                    assertion_scope(
                        scope.text,
                        tuple(t for t in scope.terms if t.end <= boundary_start),
                        tuple(o for o in scope.operators if o.end <= boundary_start),
                        event_tense=scope.event_tense,
                    )
                )
            groups.append(
                (
                    clause.correlative[0]
                    or (previous.modal if relation == "additive" else ""),
                    clause.correlative[1],
                    tuple(governing_scopes),
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
