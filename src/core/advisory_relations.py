"""Compose a declared rating, product argument and owned capability relation."""

from dataclasses import dataclass

from .assertion_bindings import bind_product, ProductBinding, bind_subject
from .assertion_predicates import (
    BOUNDARY,
    CONDITION,
    REQUIRED_ADJUNCT,
    PredicateFrame,
    bind_predicate,
)
from .condition_boundaries import bind_condition_boundaries, leading_assertion_condition
from .source_document import ADVISORY_DECLARATION


@dataclass(frozen=True)
class AdvisoryRelation:
    text: str
    severity: str
    product_span: tuple[int, int]
    predicate_span: tuple[int, int]
    product: ProductBinding | None = None
    frame: PredicateFrame | None = None
    declaration_conditions: tuple[str, ...] = ()
    relative_conditions: tuple[str, ...] = ()
    complete: bool = False


def bind_advisory(text):
    """Unknown tails are retained; only complete modal capabilities are context.

    Document/list ownership remains with source_document. Actual relative
    events are outside this declaration composition and fail closed rather
    than losing event semantics through a capability label.
    """
    leading = leading_assertion_condition(text)
    body = leading["event"] if leading else text
    offset = leading.start("event") if leading else 0
    declaration = ADVISORY_DECLARATION.match(body)
    if declaration is None:
        return None
    start = offset + declaration.end()
    product_text, separator, predicate = text[start:].partition(" that ")
    product = bind_product(product_text)
    predicate_start = start + len(product_text) + len(separator)
    parts = (
        bind_condition_boundaries(
            predicate,
            boundary=BOUNDARY,
            condition=REQUIRED_ADJUNCT,
            starts_relation=lambda right: bool(
                bind_subject(right) or bind_predicate(right).starts_relation
            ),
        )
        if separator
        else ()
    )
    part = parts[0] if len(parts) == 1 else None
    frame = bind_predicate(part.predicate, voice="vulnerability") if part else None
    conditions = part.conditions if part else ()
    complete = bool(
        product
        and frame
        and frame.capability
        and part
        and not part.unsupported
        and all(CONDITION.match(value) for value in conditions)
    )
    return AdvisoryRelation(
        text,
        declaration["severity"],
        (start, start + len(product_text)),
        (predicate_start, predicate_start + len(part.predicate) if part else len(text)),
        product,
        frame,
        (leading["condition"],) if leading else (),
        conditions,
        complete,
    )
