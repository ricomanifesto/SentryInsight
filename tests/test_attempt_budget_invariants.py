"""Exhaustive reachable-state checks of the local attempt budget and retry policy.

Every operation sequence over two request identities, every limit (including
invalid ones), and current, stale and forged finishes is explored until no new
budget state appears. The invariants are the recovery guarantees: at most
``limit <= 3`` sends per episode, a reservation blocks further sends until
finished, a terminal disposition holds the episode, a bound identity never
changes, and a delay above the retry budget never schedules a retry.
"""

import asyncio
import copy
import itertools

from src.core.attempt_budget import AttemptBudgetError, MemoryAttemptBudget
from src.core.retry_policy import (
    DISPOSITIONS,
    MAX_ATTEMPTS,
    MAX_RETRY_DELAY,
    REQUEST_STATES,
    retry_decision,
)

HASHES = ("a" * 64, "b" * 64)
LIMITS = (0, 1, 2, 3, 4)
SENDABLE = {"not_sent", "retryable_rejection"}
FINISH_DISPOSITIONS = sorted(DISPOSITIONS) + ["reserved", "unknown"]


def _key(budget):
    return (budget.identity, budget.attempt, budget.disposition)


def _reserve(budget, request_sha256, limit):
    try:
        return asyncio.run(budget.reserve(request_sha256, limit))
    except AttemptBudgetError:
        return None


def _finish(budget, reservation, disposition):
    try:
        asyncio.run(budget.finish(reservation, disposition))
        return True
    except AttemptBudgetError:
        return False


def _reachable():
    """Breadth-first over reachable budgets, recording each transition."""
    start = MemoryAttemptBudget()
    seen = {_key(start): start}
    frontier = [(start, None)]
    transitions = []
    while frontier:
        next_frontier = []
        for budget, reservation in frontier:
            for request_sha256, limit in itertools.product(HASHES, LIMITS):
                after = copy.deepcopy(budget)
                granted = _reserve(after, request_sha256, limit)
                transitions.append(("reserve", budget, after, granted))
                if _key(after) not in seen:
                    seen[_key(after)] = after
                    next_frontier.append((after, granted))
            candidates = [reservation] if reservation else []
            if reservation:
                candidates += [
                    {**reservation, "attempt": reservation["attempt"] - 1},
                    {**reservation, "request_sha256": HASHES[1]},
                    {**reservation, "limit": reservation["limit"] + 1},
                ]
            for held, disposition in itertools.product(candidates, FINISH_DISPOSITIONS):
                after = copy.deepcopy(budget)
                finished = _finish(after, held, disposition)
                transitions.append(("finish", budget, after, (held, finished)))
                if _key(after) not in seen:
                    seen[_key(after)] = after
                    next_frontier.append((after, None))
        frontier = next_frontier
    return seen, transitions


SEEN, TRANSITIONS = _reachable()


def test_the_exploration_covers_every_disposition_and_attempt():
    dispositions = {state[2] for state in SEEN}
    assert dispositions == set(REQUEST_STATES)
    assert {state[1] for state in SEEN} == set(range(MAX_ATTEMPTS + 1))


def test_no_episode_sends_more_than_its_bound_limit():
    for identity, attempt, _ in SEEN:
        bound = identity[1] if identity else 0
        assert attempt <= bound <= MAX_ATTEMPTS


def test_a_bound_identity_never_changes():
    for operation, before, after, _ in TRANSITIONS:
        if before.identity is not None:
            assert after.identity == before.identity, operation


def test_a_reservation_blocks_every_further_send_until_finished():
    for operation, before, after, granted in TRANSITIONS:
        if operation == "reserve" and before.disposition == "reserved":
            assert granted is None and _key(after) == _key(before)


def test_terminal_dispositions_hold_the_episode():
    for operation, before, after, outcome in TRANSITIONS:
        if before.disposition not in SENDABLE | {"reserved"}:
            assert _key(after) == _key(before), operation
            assert (outcome if operation == "reserve" else outcome[1]) in (
                None,
                False,
            )


def test_a_stale_or_foreign_finish_is_refused():
    for operation, before, after, outcome in TRANSITIONS:
        if operation != "finish":
            continue
        held, finished = outcome
        current = (held["request_sha256"], held["limit"]) == before.identity and held[
            "attempt"
        ] == before.attempt
        if not current:
            assert not finished and _key(after) == _key(before)


def test_a_different_identity_never_opens_a_new_episode_on_a_bound_budget():
    for operation, before, _, granted in TRANSITIONS:
        if operation == "reserve" and before.identity is not None and granted:
            assert (granted["request_sha256"], granted["limit"]) == before.identity


def test_retry_is_scheduled_only_within_the_attempt_and_delay_budgets():
    delays = (0, 1, MAX_RETRY_DELAY, MAX_RETRY_DELAY + 0.001, 3600, -1, float("inf"))
    for state, attempts, limit, delay in itertools.product(
        sorted(REQUEST_STATES) + ["bogus"], range(-1, 5), range(0, 5), delays
    ):
        decision = retry_decision(state, attempts=attempts, limit=limit, delay=delay)
        if decision["action"] == "retry_after":
            assert state in SENDABLE
            assert 0 <= attempts < limit <= MAX_ATTEMPTS
            assert 0 <= delay <= MAX_RETRY_DELAY
            assert decision["delay_seconds"] == delay
        if delay > MAX_RETRY_DELAY:
            assert decision["action"] != "retry_after"
        coherent = (
            state in REQUEST_STATES
            and 1 <= limit <= MAX_ATTEMPTS
            and 0 <= attempts <= limit
            and 0 <= delay < float("inf")
        )
        if not coherent:
            assert decision["action"] == "reconcile"
            assert decision["remaining_attempts"] == 0
