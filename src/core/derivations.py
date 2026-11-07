"""Run-scoped memoization of pure source derivations.

Detail context, version scopes and span partitions are pure functions of the
retained source content. One run re-derives them for the same catalog many
times: source review at filter, analysis and generation time, the eligible
subset check, and once per finding during publication validation. Within one
derivation scope each result is computed once per exact input and reused.

Keys are the complete inputs (frozen ``ReportingSource`` values in catalog
order, or the exact content string and CVE tuple), so a changed byte, order or
field is a different key. Nothing is cached outside an active scope, results
never outlive the outermost scope, and a derivation that raises is not cached.
Callers receive values that cannot alias the cached copy.
"""

from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any, Callable, Hashable, Iterator, TypeVar

T = TypeVar("T")

_ACTIVE: ContextVar[dict[Hashable, Any] | None] = ContextVar(
    "sentryinsight_derivations", default=None
)


@contextmanager
def derivation_scope() -> Iterator[None]:
    """Share derivations until the outermost scope exits; nested scopes reuse it."""
    if _ACTIVE.get() is not None:
        yield
        return
    token = _ACTIVE.set({})
    try:
        yield
    finally:
        _ACTIVE.reset(token)


def memoized(
    kind: str,
    key: Hashable,
    compute: Callable[[], T],
    copy: Callable[[T], T] | None = None,
) -> T:
    """Return ``compute()`` once per ``(kind, key)`` within the active scope."""
    cache = _ACTIVE.get()
    if cache is None:
        return compute()
    entry = (kind, key)
    try:
        hash(entry)
    except TypeError:  # an unhashable caller-supplied value is never cached
        return compute()
    if entry in cache:
        value = cache[entry]
    else:
        value = cache[entry] = compute()
    return copy(value) if copy is not None else value
