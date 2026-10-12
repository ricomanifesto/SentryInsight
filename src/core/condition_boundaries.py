"""Bind condition spans before consumers interpret coordinated relations.

This operation owns punctuation only. Consumers supply their existing condition
and relation grammars; it neither recognizes semantic states nor guesses actions.
Original text remains intact beside the predicate and its owned qualification.
"""

from dataclasses import dataclass
import re
from typing import Callable, Sequence


@dataclass(frozen=True)
class ConditionSegment:
    text: str
    connector: str
    predicate: str
    conditions: tuple[str, ...]
    unsupported: bool = False


def _nominal_condition_join(text: str, boundary_offset: int) -> bool:
    """Recognize coordination inside one condition's finite nominal subject.

    An unclassified later verb clause cannot silently become condition text.
    This structural production assigns no evidence state or action meaning.
    """
    subject = re.match(
        r"^(?:if|unless|when|until)\s+[A-Za-z][\w-]*"
        r"(?:\s+and\s+[A-Za-z][\w-]*)+\s+"
        r"(?P<finite>is|are|was|were)\b",
        text,
        re.I,
    )
    return bool(subject and boundary_offset < subject.start("finite"))


def bind_condition_boundaries(
    text: str,
    *,
    boundary: re.Pattern[str],
    condition: re.Pattern[str],
    starts_relation: Callable[[str], bool],
    protected: Sequence[tuple[int, int]] = (),
    can_qualify: Callable[[str], bool] = lambda _: True,
) -> tuple[ConditionSegment, ...]:
    """A condition owns internal conjunctions, not an independent later clause.

    A comma cannot detach a trailing adjunct into unowned context. Unknown
    adjuncts stay with the predicate so its consumer can reject them. Semicolons
    still terminate a clause; explicit later predicates retain their own scope.
    """
    spans = []
    start, connector, unresolved = 0, "", False

    def qualification(value, offset):
        position = 0
        while match := condition.search(value, position):
            if not any(
                left <= offset + match.start() < right for left, right in protected
            ) and can_qualify(value[: match.start()].rstrip(" ,")):
                return match
            # Some consumers supply a tail production. Skipping a protected
            # token (e.g. a month in a deadline) must not skip a later qualifier.
            position = match.start() + 1
        return None

    for match in boundary.finditer(text):
        if any(
            left <= match.start() and match.end() <= right for left, right in protected
        ):
            continue
        left, right = text[start : match.start()], text[match.end() :].strip()
        marker = match.group().strip()
        attached = condition.match(right)
        independent = not attached and starts_relation(right)
        if marker == "," and not independent:
            continue
        owned = qualification(left, start)
        if owned and marker != ";" and not independent:
            unresolved |= not _nominal_condition_join(
                text[start + owned.start() :], match.start() - start - owned.start()
            )
            continue
        spans.append(
            (
                connector,
                left.strip(),
                unresolved,
                start + len(left) - len(left.lstrip()),
            )
        )
        start, connector, unresolved = match.end(), marker, False
    tail = text[start:]
    spans.append(
        (connector, tail.strip(), unresolved, start + len(tail) - len(tail.lstrip()))
    )
    result = []
    for connector, raw, unresolved, offset in spans:
        if not raw:
            continue
        qualified = qualification(raw, offset)
        # Leading conditions belong to each consumer's existing leading-form
        # production. Do not turn an unknown subject bridge into a predicate.
        trailing = qualified is not None and qualified.start() > 0
        result.append(
            ConditionSegment(
                raw,
                connector,
                raw[: qualified.start()].rstrip(" ,") if trailing else raw,
                (raw[qualified.start() :].rstrip(".!?"),) if trailing else (),
                unresolved,
            )
        )
    return tuple(result)
