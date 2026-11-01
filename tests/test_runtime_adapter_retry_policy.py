"""Default-off delay-policy seam, adapter jitter, retry disposition and the
closed failure mapping."""

import asyncio
import inspect

import httpx
import pytest

from src.core import model_client
from src.core.analyze import analyze_exploitation
from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import (
    MAX_RETRY_DELAY,
    OpenRouterClient,
    OpenRouterError,
)
from src.runtime_adapter import reasons
from src.runtime_adapter.checkpoint import CheckpointStore, ledger_view
from src.runtime_adapter.fakes import (
    FakeModelService,
    Respond,
    SimulatedCrash,
    SyntheticClock,
)
from src.runtime_adapter.send_gate import (
    JitterPolicy,
    Lease,
    ProviderSendGate,
    RetryDispositionRecorder,
)
from src.runtime_adapter.synthetic import (
    FAKE_PROVIDER_KEY,
    SYNTHETIC_MODEL,
    completion_body,
    synthetic_articles,
    synthetic_config,
)

JOB = "a" * 64
OK = Respond(200, completion_body("Synthetic model answer"))


def unavailable(retry_after=None):
    headers = {"Retry-After": retry_after} if retry_after is not None else None
    return Respond(503, {"error": {"code": 503}}, headers)


class Recorded(list):
    """Recorded in-call delays plus the synthetic clocks they advance."""


@pytest.fixture
def sleeps(monkeypatch):
    recorded = Recorded()
    clocks = []

    async def sleep(delay, *_args, **_kwargs):
        recorded.append(delay)
        for clock in clocks:
            clock.advance(delay)

    monkeypatch.setattr(asyncio, "sleep", sleep)
    recorded.clocks = clocks
    return recorded


@pytest.fixture
def world(tmp_path, sleeps):
    class World:
        def __init__(self):
            self.clock = SyntheticClock(tmp_path / "clock.json")
            sleeps.clocks.append(self.clock)
            self.store = CheckpointStore(tmp_path / "store")
            self.store.create_job(JOB, "key")
            self.store.record_run(JOB, "run-1")
            self.store.record_lease(JOB, "run-1", 1, attempt=1, now=self.clock.now())

        def process(self, script, random=lambda: 0.5, sleep_fault=None):
            self.provider = FakeModelService(tmp_path / "provider.json", script)
            gate = ProviderSendGate(
                store=self.store,
                job_id=JOB,
                lease=Lease(run_id="run-1", owner="w", version=1),
                inner=self.provider,
                clock=self.clock.now,
            )
            policy = JitterPolicy(gate, random)
            client = OpenRouterClient(
                api_key=FAKE_PROVIDER_KEY,
                base_url="https://model.example.test/api/v1",
                transport=gate,
                retry_delay_policy=policy,
            )
            return gate, policy, RetryDispositionRecorder(client, gate)

        def view(self):
            return ledger_view(self.store.load(JOB))

    return World()


def call(client):
    return asyncio.run(
        client.generate(
            system_prompt="s",
            user_prompt="u",
            model=parse_model_selection(SYNTHETIC_MODEL),
        )
    )


def legacy_client(responses, policy=None):
    requests = []

    def handler(request):
        requests.append(request)
        return responses[min(len(requests) - 1, len(responses) - 1)]

    kwargs = {} if policy is None else {"retry_delay_policy": policy}
    client = OpenRouterClient(
        api_key=FAKE_PROVIDER_KEY, transport=httpx.MockTransport(handler), **kwargs
    )
    return client, requests


def completion():
    return httpx.Response(200, json=completion_body("ok"))


# Delay-policy seam -----------------------------------------------------------


def test_seam_is_an_optional_keyword_that_defaults_off(monkeypatch, sleeps):
    parameter = inspect.signature(OpenRouterClient).parameters["retry_delay_policy"]
    assert parameter.default is None
    assert parameter.kind is inspect.Parameter.KEYWORD_ONLY

    monkeypatch.setenv("OPENROUTER_API_KEY", FAKE_PROVIDER_KEY)
    built = model_client.build_model_client(timeout=1.0, max_tokens=10)
    assert built.retry_delay_policy is None

    client, requests = legacy_client([httpx.Response(503), httpx.Response(503)])
    with pytest.raises(OpenRouterError):
        call(client)
    assert sleeps == [1.0, 2.0]
    assert len(requests) == 3


@pytest.mark.parametrize(
    "chosen, expected",
    [
        (lambda floor, cap: floor + 0.25, [1.25, 2.25]),
        (lambda floor, cap: 0.0, [1.0, 2.0]),
        (lambda floor, cap: cap + 100, [MAX_RETRY_DELAY, MAX_RETRY_DELAY]),
        (lambda floor, cap: float("nan"), [1.0, 2.0]),
        (lambda floor, cap: float("inf"), [1.0, 2.0]),
    ],
    ids=["within", "below_floor", "above_cap", "nan", "infinite"],
)
def test_client_clamps_policy_delay_between_floor_and_cap(sleeps, chosen, expected):
    calls = []

    def policy(floor, cap):
        calls.append((floor, cap))
        return chosen(floor, cap)

    client, requests = legacy_client(
        [httpx.Response(503), httpx.Response(503), completion()], policy
    )

    assert call(client) == "ok"
    assert calls == [(1.0, MAX_RETRY_DELAY), (2.0, MAX_RETRY_DELAY)]
    assert sleeps == expected
    assert len(requests) == 3


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(400),
        httpx.Response(429, headers={"Retry-After": "31"}),
    ],
    ids=["not_retryable", "floor_above_cap"],
)
def test_policy_is_consulted_only_after_the_existing_stop_test(sleeps, response):
    def policy(floor, cap):
        raise AssertionError("policy must not run when the client stops")

    client, requests = legacy_client([response], policy)
    with pytest.raises(OpenRouterError):
        call(client)

    assert sleeps == []
    assert len(requests) == 1


# Adapter jitter --------------------------------------------------------


@pytest.mark.parametrize("sample", [0.0, 0.5, 1.0])
def test_jitter_stays_within_floor_and_cap_for_min_mid_max(world, sleeps, sample):
    gate, policy, client = world.process(
        [unavailable(), unavailable(), OK], random=lambda: sample
    )

    assert call(client) == "Synthetic model answer"

    view = world.view()
    assert view.reserved == 3
    samples = view.of_type("delay_sample")
    assert [entry["floor"] for entry in samples] == [1.0, 2.0]
    assert [entry["delay"] for entry in samples] == sleeps
    for entry in samples:
        assert entry["floor"] <= entry["delay"] <= entry["cap"] == MAX_RETRY_DELAY
        assert entry["delay"] == entry["floor"] + entry["floor"] * sample


def test_jitter_range_is_visibly_non_constant_where_headroom_exists(world, sleeps):
    delays = []
    for sample in (0.0, 0.5, 1.0):
        policy = JitterPolicy(None, lambda value=sample: value)
        delays.append(policy(4.0, MAX_RETRY_DELAY))
    assert delays == [4.0, 6.0, 8.0]


@pytest.mark.parametrize(
    "retry_after, floor, low, high, zero_headroom",
    [
        ("0", 1.0, 1.0, 2.0, False),
        ("29", 29.0, 29.0, 30.0, False),
        ("30", 30.0, 30.0, 30.0, True),
    ],
    ids=["below_backoff", "just_below_cap", "at_cap"],
)
def test_retry_after_floor_is_never_undercut(
    world, sleeps, retry_after, floor, low, high, zero_headroom
):
    _, _, client = world.process([unavailable(retry_after), OK], random=lambda: 1.0)

    assert call(client) == "Synthetic model answer"

    [entry] = world.view().of_type("delay_sample")
    assert entry["floor"] == floor
    assert low <= entry["delay"] <= high
    assert entry["headroom"] == MAX_RETRY_DELAY - floor
    assert entry["delay"] - floor <= min(entry["headroom"], floor)
    assert (entry["headroom"] == 0.0) is zero_headroom
    assert sleeps == [entry["delay"]]


def test_retry_after_above_cap_stops_and_persists_not_before(world, sleeps):
    start = world.clock.now()
    _, _, client = world.process([unavailable("31"), OK])

    with pytest.raises(OpenRouterError) as raised:
        call(client)

    assert raised.value.retryable is True
    assert sleeps == []
    assert world.view().not_before == int(start) + 31
    assert world.provider.forwards == 1


def test_sampled_delay_survives_a_crash_and_is_reused_on_replay(
    world, sleeps, monkeypatch
):
    _, _, client = world.process([unavailable(), OK], random=lambda: 0.75)

    async def crash_while_waiting(delay, *_args, **_kwargs):
        sleeps.append(delay)
        raise SimulatedCrash("during in-call delay")

    monkeypatch.setattr(asyncio, "sleep", crash_while_waiting)
    with pytest.raises(SimulatedCrash):
        call(client)
    [sample] = world.view().of_type("delay_sample")
    assert sample["delay"] == 1.75

    async def advance(delay, *_args, **_kwargs):
        sleeps.append(delay)
        world.clock.advance(delay)

    monkeypatch.setattr(asyncio, "sleep", advance)
    before = world.clock.now()
    _, _, fresh = world.process([unavailable(), OK], random=lambda: 0.0)
    assert call(fresh) == "Synthetic model answer"

    view = world.view()
    assert sleeps == [1.75, 1.75]
    assert len(view.of_type("delay_sample")) == 1
    assert (view.reserved, view.replays, world.provider.forwards) == (2, 1, 2)
    assert world.clock.now() == before + 1.75


# Retry disposition recorder --------------------------------------------


def test_recorder_passes_success_through_unchanged(world):
    _, _, client = world.process([OK])

    assert call(client) == "Synthetic model answer"
    assert client.disposition is None
    assert world.view().of_type("retry_disposition") == []


def test_recorder_reraises_the_same_exception_after_recording(world):
    _, _, client = world.process([Respond(400, {"error": {"code": 400}})])
    caught = []

    async def run():
        try:
            await client.generate(
                system_prompt="s",
                user_prompt="u",
                model=parse_model_selection(SYNTHETIC_MODEL),
            )
        except OpenRouterError as error:
            caught.append(error)

    asyncio.run(run())

    [error] = caught
    [entry] = world.view().of_type("retry_disposition")
    assert client.disposition == {
        "http_status": 400,
        "provider_code": 400,
        "attempts": 1,
        "retryable": False,
    }
    assert entry["http_status"] == 400 and entry["retryable"] is False
    assert entry["follows"] == world.view().reservations[0]["seq"]
    assert error.http_status == 400


def test_analysis_flattening_is_unchanged_by_the_recorder(world):
    _, _, wrapped = world.process([Respond(400, {"error": {"code": 400}})])
    plain, _ = legacy_client([httpx.Response(400, json={"error": {"code": 400}})])

    with_recorder = asyncio.run(
        analyze_exploitation(
            synthetic_articles(), synthetic_config(), model_client=wrapped
        )
    )
    without = asyncio.run(
        analyze_exploitation(
            synthetic_articles(), synthetic_config(), model_client=plain
        )
    )

    for key in ("error", "error_class", "error_detail", "exploitation_report"):
        assert with_recorder[key] == without[key]
    assert wrapped.disposition["retryable"] is False


AUTH_CASES = [
    Respond(401),
    Respond(403),
    Respond(200, {"error": {"code": 401}}),
    Respond(503, {"error": {"code": 401}}),
]


@pytest.mark.parametrize(
    "step, reason",
    [(step, "model_auth_rejected") for step in AUTH_CASES]
    + [(Respond(400, {"error": {"code": 503}}), "model_response_rejected")],
    ids=["401", "403", "200_provider_401", "503_provider_401", "400_provider_503"],
)
def test_auth_and_precedence_matrix_is_never_retried(world, sleeps, step, reason):
    _, _, client = world.process([step, OK])

    with pytest.raises(OpenRouterError):
        call(client)

    disposition = client.disposition
    assert disposition["retryable"] is False
    assert world.provider.forwards == 1 and sleeps == []
    assert reasons.provider_failure_reason(disposition, reserved=1) == reason


def test_auth_after_earlier_transients_reports_the_actual_reservation_count(
    world, sleeps
):
    _, _, client = world.process([unavailable(), Respond(401), OK])

    with pytest.raises(OpenRouterError):
        call(client)

    reserved = world.view().reserved
    assert reserved == 2
    reason = reasons.provider_failure_reason(client.disposition, reserved=reserved)
    assert reason == "model_auth_rejected"
    summary = reasons.error_summary(reason, reserved=reserved, attempts=2)
    assert summary == "model_auth_rejected reserved=2 attempts=2"


@pytest.mark.parametrize(
    "step",
    [
        Respond(529),
        Respond(200, {"error": {"code": 529}}),
        Respond(200, {"error": {"code": "unrecognized"}}),
        Respond(
            529,
            {
                "error": {
                    "code": 529,
                    "message": "fake-secret-token PROMPT-MARKER source text",
                }
            },
        ),
    ],
    ids=["http_529", "provider_529", "unknown_code", "secret_text"],
)
def test_529_and_unknown_codes_are_not_retried(world, sleeps, step):
    _, _, client = world.process([step, OK])

    with pytest.raises(OpenRouterError):
        call(client)

    assert world.provider.forwards == 1 and sleeps == []
    reason = reasons.provider_failure_reason(client.disposition, reserved=1)
    assert reason == "model_response_rejected"
    summary = reasons.error_summary(
        reason,
        reserved=1,
        **{
            key: value
            for key, value in client.disposition.items()
            if key in ("http_status", "provider_code", "attempts")
        },
    )
    for marker in ("fake-secret", "PROMPT-MARKER", "OpenRouter", "Error"):
        assert marker not in summary


@pytest.mark.parametrize(
    "step",
    [Respond(code) for code in (408, 429, 500, 502, 503, 504)]
    + [Respond(200, []), Respond(200, {}), Respond(200, {"choices": None})],
)
def test_verified_transient_set_is_retryable(world, sleeps, step):
    _, _, client = world.process([step, step, step])

    with pytest.raises(OpenRouterError):
        call(client)

    assert client.disposition["retryable"] is True
    assert world.provider.forwards == 3
    assert reasons.provider_failure_reason(client.disposition, reserved=3) == (
        "provider_budget_exhausted"
    )
    assert reasons.provider_failure_reason(client.disposition, reserved=1) == (
        "provider_transient_response"
    )


def test_missing_text_output_is_not_retryable(world, sleeps):
    _, _, client = world.process([Respond(200, completion_body("")), OK])

    with pytest.raises(OpenRouterError):
        call(client)

    assert client.disposition["retryable"] is False
    assert world.provider.forwards == 1


# Closed mapping ----------------------------------------------


def test_closed_reason_mapping_never_uses_unknown_or_worker_error():
    for reason, mapping in reasons.REASONS.items():
        assert mapping.runtime_code not in ("unknown", "worker_error"), reason
    retry = {r for r, m in reasons.REASONS.items() if m.runtime_code and m.retry}
    assert retry == {
        "provider_transient_response",
        "provider_connect_failed",
        "provider_retry_after_deferred",
    }
    assert reasons.runtime_code("provider_connect_failed", fault="connect_timeout") == (
        "dependency_timeout"
    )
    assert reasons.runtime_code("model_auth_rejected") == "invalid_input"
    assert reasons.runtime_code("provider_intent_unresolved") == "side_effect_conflict"
    assert reasons.runtime_code("worker_unclassified") == "invalid_result"
    assert reasons.runtime_code("lease_lost") is None


def test_error_summary_is_a_fixed_token_with_bounded_integers():
    assert (
        reasons.error_summary(
            "provider_transient_response",
            reserved=1,
            attempts=3,
            http_status=503,
            provider_code=None,
        )
        == "provider_transient_response reserved=1 attempts=3 http_status=503"
    )
    with pytest.raises(ValueError):
        reasons.error_summary("free text reason")
    with pytest.raises(ValueError):
        reasons.error_summary("worker_unclassified", detail=1)
    assert reasons.error_summary("worker_unclassified", reserved="7") == (
        "worker_unclassified"
    )
    assert reasons.reported_reserved("provider_transient_response reserved=2") == 2
    assert reasons.reported_reserved(None) is None


def test_retry_after_deferral_and_pre_send_mapping():
    transient = {"http_status": None, "provider_code": None, "retryable": True}
    assert (
        reasons.provider_failure_reason(
            dict(transient, http_status=429), reserved=1, not_before=200, now=100
        )
        == "provider_retry_after_deferred"
    )
    assert (
        reasons.provider_failure_reason(
            transient, reserved=2, last_fault="connect_error"
        )
        == "provider_connect_failed"
    )
    assert (
        reasons.provider_failure_reason(
            dict(transient, http_status=503), reserved=3, not_before=200, now=100
        )
        == "provider_budget_exhausted"
    )
