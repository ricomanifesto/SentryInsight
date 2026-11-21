"""Paid readiness route: synthetic facts, mocked transport and ledger only.

Every manifest, product label and link here is fictional (example.test). No
case sends a request, reads a credential, an advisory, a report or an
archive. Live provider honoring of the route is a later acceptance check.
"""

import asyncio
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

import httpx
import pytest

from src.core import paid_readiness as readiness
from src.core import paid_verification
from src.core.attempt_budget import AttemptBudgetError
from src.core.paid_verification import PaidVerificationError, initialize_verification
from src.core.report_findings import report_findings

ROOT = Path(__file__).resolve().parents[1]
REVISION = "c" * 40
COMMIT = "0123456789abcdef0123456789abcdef01234567"
KEY = "test-only-key"
PROVIDER_NAME = "Synthetic Provider"
CHECKED_AT = "2026-11-21T08:55:00.000Z"
NOW_MS = datetime(2026, 11, 21, 9, tzinfo=timezone.utc).timestamp() * 1000
VALID_UNTIL = int(datetime(2026, 11, 21, 9, 55, tzinfo=timezone.utc).timestamp() * 1000)


COMMIT_TWO = "fedcba9876543210fedcba9876543210fedcba98"
SYNTHETIC_HOST = "code.example.test"


@pytest.fixture(autouse=True)
def synthetic_provider(monkeypatch):
    """Inert control: a fictional provider beside the production allowlist."""
    providers = dict(readiness.PROVIDERS)
    providers["synthetic"] = (SYNTHETIC_HOST, "/{repository}/commit/{commit}")
    monkeypatch.setattr(readiness, "PROVIDERS", providers)


def ref(name, commit=COMMIT, provider="synthetic"):
    return {"provider": provider, "repository": f"vendor/{name}", "commit": commit}


def url_of(reference):
    return (
        f"https://{SYNTHETIC_HOST}/{reference['repository']}"
        f"/commit/{reference['commit']}"
    )


def advisory(cve, product, severity, **extra):
    return {
        "cve": cve,
        "product": product,
        "severity": severity,
        "exposure": "unknown",
        "remediation": "patch",
        "references": [ref(product.split()[-1].lower())],
        **extra,
    }


EIGHT = [
    advisory("CVE-2026-0101", "Gateway Alpha", "high"),
    advisory("CVE-2026-0102", "Gateway Bravo", "critical", exposure="active"),
    advisory("CVE-2026-0103", "Gateway Charlie", "medium"),
    advisory("CVE-2026-0104", "Gateway Delta", "critical"),
    advisory("CVE-2026-0105", "Gateway Echo", "low", remediation="monitor"),
    advisory(
        "CVE-2026-0106",
        "Gateway Foxtrot",
        "critical",
        remediation="mitigate",
        references=[ref("foxtrot"), ref("foxtrot", COMMIT_TWO)],
    ),
    advisory("CVE-2026-0107", "Gateway Golf", "high", remediation="investigate"),
    advisory("CVE-2026-0108", "Gateway Hotel", "critical", exposure="observed"),
]
EXPECTED_ORDER = ["0102", "0104", "0106", "0108", "0101", "0103", "0105", "0107"]


def manifest_value(advisories=None, **overrides):
    value = {
        "schema": readiness.MANIFEST_SCHEMA,
        "approval": {"reviewed_by": "owner-review", "state": "approved"},
        "advisories": EIGHT if advisories is None else advisories,
    }
    value.update(overrides)
    return value


def encode(value):
    return readiness.canonical_bytes(value)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


@pytest.fixture(scope="module")
def exported():
    return json.loads(
        subprocess.check_output(
            [
                "node",
                "-e",
                "const p=require('./publication/kit/verification-budget');"
                "console.log(JSON.stringify({profile:p.READINESS_PROFILE,"
                "sha256:p.READINESS_PROFILE_SHA256}))",
            ],
            cwd=ROOT,
            text=True,
        )
    )


def ok_completion(content=None, **changes):
    ids = [item["cve"] for item in EIGHT]
    body = {
        "model": readiness.READINESS_PROFILE["model"],
        "provider": PROVIDER_NAME,
        "choices": [
            {
                "finish_reason": "stop",
                "message": {
                    "role": "assistant",
                    "content": (
                        json.dumps({"acknowledged": True, "ids": ids[::-1]})
                        if content is None
                        else content
                    ),
                },
            }
        ],
        "usage": {
            "prompt_tokens": 180,
            "completion_tokens": 900,
            "completion_tokens_details": {"reasoning_tokens": 700},
            "cost": 0.00936,
        },
    }
    body.update(changes)
    return body


class World:
    def __init__(self, tmp_path, exported, *, manifest=None, completion=None):
        self.root = tmp_path / "repository"
        self.root.mkdir()
        (tmp_path / "candidates").mkdir()
        self.output = tmp_path / "candidates" / "readiness"
        self.manifest = encode(manifest_value()) if manifest is None else manifest
        self.approval = None
        self.exported = exported
        self.calls = []
        self.requests = []
        self.posts = []
        self.completion = completion or (
            lambda: httpx.Response(200, json=ok_completion())
        )
        self.endpoint = {
            "tag": readiness.READINESS_PROFILE["provider"],
            "provider_name": PROVIDER_NAME,
            "context_length": 1048576,
            "max_completion_tokens": 32000,
            "supported_parameters": ["max_tokens", "reasoning"],
            "pricing": {"prompt": "0.000002", "completion": "0.00001", "request": "0"},
        }
        evidence = {
            "billing": "credits-no-applicable-byok",
            "coverage": "all-applicable-ci-keys",
            "periodStart": "2026-11-01T00:00:00.000Z",
            "periodEnd": "2026-12-01T00:00:00.000Z",
            "actualMicrousd": 1400000,
            "checkedAt": CHECKED_AT,
            "scopeSha256": digest(b"workspace:synthetic-workspace"),
            "keySha256": digest(KEY.encode()),
        }
        self.evidence = tmp_path / "billing.json"
        self.evidence.write_text(json.dumps(evidence))
        self.env = {
            readiness.FLAG: readiness.READINESS_PROFILE["id"],
            readiness.MANIFEST_DIGEST: digest(self.manifest),
            "SENTRYINSIGHT_BILLING_EVIDENCE": str(self.evidence),
            "GITHUB_EVENT_NAME": "workflow_dispatch",
            "GITHUB_REF": "refs/heads/main",
            "GITHUB_RUN_ID": "100",
            "GITHUB_RUN_ATTEMPT": "1",
            "SENTRYINSIGHT_SOURCE_REVISION": REVISION,
            "SENTRYINSIGHT_ADMISSION_KEY": "run:100",
            "SENTRYINSIGHT_ATTEMPT_STORE": "admission",
            "OPENROUTER_API_KEY": KEY,
        }
        self.reserve_result = None

    def git(self, arguments):
        self.calls.append(("git", tuple(arguments)))
        if arguments == ["rev-parse", "HEAD"]:
            return (REVISION + "\n").encode()
        if arguments == ["show", f"{REVISION}:{readiness.MANIFEST_PATH}"]:
            return self.manifest
        if arguments == ["show", f"{REVISION}:{readiness.SURFACE_PATH}"]:
            return self.approval
        return None

    def _invoke(self, command, arguments):
        self.calls.append((command, tuple(arguments)))
        assert arguments[:2] == ["--run-attempt", "1"]
        if command == "readiness-profile":
            return self.exported
        if command == "readiness-reserve":
            return self.reserve_result or {
                "reservedMicrousd": 2417152,
                "profileSha256": readiness.READINESS_PROFILE_SHA256,
                "factManifestSha256": self.env[readiness.MANIFEST_DIGEST],
                "validUntil": VALID_UNTIL,
            }
        if command == "readiness-report":
            return {"claimed": True}
        raise AssertionError(f"unexpected ledger command {command}")

    def handler(self, request):
        self.requests.append(request)
        if request.method == "GET" and request.url.path.endswith("/key"):
            assert request.headers["authorization"] == f"Bearer {KEY}"
            return httpx.Response(
                200,
                json={
                    "data": {
                        "workspace_id": "synthetic-workspace",
                        "byok_usage_monthly": 0,
                        "usage_monthly": 0.25,
                    }
                },
            )
        if request.method == "GET":
            assert "authorization" not in request.headers
            return httpx.Response(
                200,
                json={
                    "data": {
                        "id": readiness.READINESS_PROFILE["model"],
                        "endpoints": [self.endpoint],
                    }
                },
            )
        assert request.method == "POST"
        self.posts.append(request)
        response = self.completion()
        if isinstance(response, Exception):
            raise response
        return response

    def run(self, clock=None):
        return asyncio.run(
            readiness.run_paid_readiness(
                environ=self.env,
                output=self.output,
                root=self.root,
                bridge=self,
                transport=httpx.MockTransport(self.handler),
                git=self.git,
                clock=clock or (lambda: NOW_MS),
            )
        )

    def commands(self):
        return [call[0] for call in self.calls if call[0] != "git"]


@pytest.fixture
def world(tmp_path, exported):
    return World(tmp_path, exported)


def refused(receipt, stage, code):
    assert receipt["outcome"] == "refused"
    assert (receipt["stage"], receipt["code"]) == (stage, code)


class Titles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles, self._open = [], False

    def handle_starttag(self, tag, attrs):
        if tag == "span" and "finding-title" in (dict(attrs).get("class") or ""):
            self._open = True
            self.titles.append("")

    def handle_endtag(self, tag):
        if tag == "span":
            self._open = False

    def handle_data(self, data):
        if self._open:
            self.titles[-1] += data


# Profile and bound


def test_node_and_python_pin_the_same_narrow_profile_and_bound(exported):
    profile = readiness.verify_readiness_profile(exported)
    assert exported["sha256"] == readiness.READINESS_PROFILE_SHA256
    assert readiness.readiness_bound_microusd(profile) == 2417152
    assert 1048576 * 2 + 32000 * 10 == 2417152
    assert profile["reserveMicrousd"] == 2417152 <= profile["limitMicrousd"] <= 2420000
    assert profile["reportAttempts"] == 1 and profile["triageRequests"] == 0
    assert profile["model"] == "moonshotai/kimi-k3.1-pro"
    assert profile["provider"] == "moonshotai/mxfp4"


@pytest.mark.parametrize(
    ("change", "code"),
    [
        ({"reportContext": 1048577}, "bound_exceeds_cap"),
        ({"reportPromptPrice": "2.01"}, "bound_exceeds_cap"),
        ({"reportCompletionPrice": "10.1"}, "bound_exceeds_cap"),
        ({"reportAttempts": 2}, "bound_exceeds_cap"),
        ({"limitMicrousd": 2420001}, "bound_exceeds_cap"),
        ({"reserveMicrousd": 2417151}, "bound_exceeds_cap"),
        ({"reportPromptPrice": "NaN"}, "profile_invalid"),
        ({"reportOutput": "32000"}, "profile_invalid"),
        ({"triageRequests": 1}, "profile_invalid"),
        ({"provider": "other/provider"}, "profile_invalid"),
    ],
)
def test_any_profile_drift_or_overflow_is_refused(exported, change, code):
    profile = dict(exported["profile"], **change)
    tampered = {
        "profile": profile,
        "sha256": digest(readiness.canonical_bytes(profile)),
    }
    with pytest.raises(readiness.ReadinessRefusal) as caught:
        readiness.verify_readiness_profile(tampered)
    assert caught.value.code == code


def test_profile_drift_refuses_before_any_credential_use_or_ledger_write(world):
    world.exported = dict(world.exported, sha256="0" * 64)
    refused(world.run(), "profile", "profile_invalid")
    assert world.requests == []
    assert world.commands() == ["readiness-profile"]


# Manifest


def test_absent_manifest_fails_closed_before_any_send(world):
    world.manifest = None
    refused(world.run(), "manifest", "fact_manifest_unavailable")
    assert world.requests == [] and world.commands() == []


def _mutations():
    good = manifest_value()
    first = dict(EIGHT[0])
    yield "digest-mismatch", None, "fact_manifest_invalid"
    yield "noncanonical", json.dumps(good).encode(), "fact_manifest_invalid"
    yield "unknown-top-key", encode(dict(good, notes="x")), "fact_manifest_invalid"
    yield (
        "unapproved",
        encode(dict(good, approval={"reviewed_by": "owner-review", "state": "draft"})),
        "fact_manifest_unapproved",
    )
    yield "wrong-schema", encode(dict(good, schema="other")), "fact_manifest_invalid"
    yield "empty", encode(manifest_value([])), "fact_manifest_invalid"
    yield "unsorted", encode(manifest_value(EIGHT[::-1])), "fact_manifest_invalid"
    yield (
        "duplicate-cve",
        encode(manifest_value([first, dict(EIGHT[1], cve=first["cve"])])),
        "fact_manifest_invalid",
    )
    yield (
        "duplicate-reference",
        encode(manifest_value([first, dict(EIGHT[1], references=first["references"])])),
        "fact_manifest_invalid",
    )
    for field, value in [
        ("severity", "unknown"),
        ("exposure", "widespread"),
        ("remediation", "ignore"),
        ("cve", "CVE-26-1"),
        ("product", "[label](https://code.example.test/x)"),
        ("product", "Gateway CVE-2026-1"),
        ("product", "Gateway  Alpha"),
        ("product", "Gateway link-0123456789abcdef"),
        ("product", "x" * 65),
        ("extra", "value"),
    ]:
        yield f"{field}={value}", encode(
            manifest_value([dict(first, **{field: value})])
        ), "fact_manifest_invalid"
    good_ref = ref("alpha")
    for name, reference in [
        ("free-form-url", url_of(good_ref)),
        ("unknown-provider", dict(good_ref, provider="mirror")),
        ("provider-case", dict(good_ref, provider="GitHub")),
        ("branch-not-commit", dict(good_ref, commit="main")),
        ("short-commit", dict(good_ref, commit=COMMIT[:39])),
        ("upper-commit", dict(good_ref, commit=COMMIT.upper())),
        ("commit-query", dict(good_ref, commit=COMMIT + "?redirect=1")),
        ("commit-path", dict(good_ref, commit=COMMIT + "/x")),
        ("nested-repository", dict(good_ref, repository="a/b/c")),
        ("dot-repository", dict(good_ref, repository="vendor/..")),
        ("git-suffix", dict(good_ref, repository="vendor/alpha.git")),
        ("repository-host", dict(good_ref, repository="evil.example.test/x")),
        ("repository-query", dict(good_ref, repository="vendor/alpha?x=1")),
        ("missing-commit", {"provider": "synthetic", "repository": "vendor/a"}),
        ("extra-url", dict(good_ref, url=url_of(good_ref))),
    ]:
        yield f"reference-{name}", encode(
            manifest_value([dict(first, references=[reference])])
        ), "fact_manifest_invalid"
    yield (
        "too-many-references",
        encode(
            manifest_value([dict(first, references=[ref(f"r{n}") for n in range(5)])])
        ),
        "fact_manifest_invalid",
    )


@pytest.mark.parametrize(
    ("raw", "code"),
    [(raw, code) for _, raw, code in _mutations()],
    ids=[name for name, _, _ in _mutations()],
)
def test_malformed_noncanonical_or_unapproved_manifest_is_refused(world, raw, code):
    if raw is None:
        world.env[readiness.MANIFEST_DIGEST] = "f" * 64
    else:
        world.manifest = raw
        world.env[readiness.MANIFEST_DIGEST] = digest(raw)
    refused(world.run(), "manifest", code)
    assert world.requests == [] and world.commands() == []


# Preflight, checkout, surface and output: all before credentials or ledger


@pytest.mark.parametrize(
    ("change", "code"),
    [
        ({readiness.FLAG: ""}, "not_requested"),
        ({readiness.FLAG: "other-profile"}, "dispatch_invalid"),
        (
            {paid_verification.FLAG: paid_verification.PROFILE_ID},
            "exclusive_route_conflict",
        ),
        ({"GITHUB_RUN_ATTEMPT": "2"}, "dispatch_invalid"),
        ({"GITHUB_EVENT_NAME": "schedule"}, "dispatch_invalid"),
        ({"GITHUB_REF": "refs/heads/feature"}, "dispatch_invalid"),
        ({"SENTRYINSIGHT_ATTEMPT_STORE": "memory"}, "dispatch_invalid"),
        ({"SENTRYINSIGHT_ADMISSION_KEY": "digest:" + "a" * 40}, "dispatch_invalid"),
        ({readiness.MANIFEST_DIGEST: ""}, "fact_manifest_unpinned"),
    ],
)
def test_invalid_dispatch_is_refused_before_any_outward_step(world, change, code):
    world.env.update(change)
    refused(world.run(), "preflight", code)
    assert world.requests == [] and world.calls == []


def test_changed_checkout_is_refused(world):
    world.env["SENTRYINSIGHT_SOURCE_REVISION"] = "d" * 40
    refused(world.run(), "checkout", "checkout_mismatch")
    assert world.requests == [] and world.commands() == []


def test_legacy_surface_without_owner_approval_blocks_the_paid_path(world):
    (world.root / "reports").mkdir()
    (world.root / "reports" / "2026-11-01.md").write_text("synthetic legacy bytes\n")
    refused(world.run(), "surface", "legacy_surface_unapproved")
    assert world.requests == [] and world.commands() == []


def test_pending_publication_recovery_blocks_the_paid_path(world):
    (world.root / ".sentryinsight-publication").mkdir()
    refused(world.run(), "surface", "publication_recovery_pending")
    assert world.requests == [] and world.commands() == []


def _approve(world, served):
    approval = encode(
        {
            "schema": readiness.SURFACE_SCHEMA,
            "reviewed_by": "owner-review",
            "publication_idle": True,
            "served": served,
        }
    )
    world.approval = approval
    world.env[readiness.SURFACE_DIGEST] = digest(approval)


def test_digest_bound_owner_approval_admits_an_exactly_matching_surface(world):
    (world.root / "index.md").write_text("synthetic serving bytes\n")
    _approve(world, {"index.md": digest(b"synthetic serving bytes\n")})
    assert world.run()["outcome"] == "rendered"
    assert (world.root / "index.md").read_text() == "synthetic serving bytes\n"


@pytest.mark.parametrize("drift", ["bytes", "extra-file", "not-idle", "unpinned"])
def test_surface_approval_that_does_not_bind_exactly_is_refused(world, drift):
    (world.root / "index.md").write_text("synthetic serving bytes\n")
    _approve(world, {"index.md": digest(b"approved other bytes\n")})
    expected = "legacy_surface_mismatch"
    if drift != "bytes":
        _approve(world, {"index.md": digest(b"synthetic serving bytes\n")})
    if drift == "extra-file":
        (world.root / "sitemap.xml").write_text("synthetic\n")
    if drift == "not-idle":
        value = json.loads(world.approval)
        value["publication_idle"] = False
        world.approval = encode(value)
        world.env[readiness.SURFACE_DIGEST] = digest(world.approval)
        expected = "legacy_surface_unapproved"
    if drift == "unpinned":
        world.env[readiness.SURFACE_DIGEST] = "0" * 64
        expected = "legacy_surface_unapproved"
    refused(world.run(), "surface", expected)
    assert world.requests == [] and world.commands() == []


@pytest.mark.parametrize("where", ["existing", "inside-repository", "relative"])
def test_unsafe_output_location_is_refused_before_credentials(world, where):
    if where == "existing":
        world.output.mkdir()
    if where == "inside-repository":
        world.output = world.root / "candidate"
    if where == "relative":
        world.output = Path("candidate")
    refused(world.run(), "output", "output_unsafe")
    assert world.requests == [] and world.commands() == []


def test_oversized_request_is_refused_as_context_overflow(world, monkeypatch):
    monkeypatch.setattr(readiness, "TEMPLATE_MARGIN", 1048576)
    refused(world.run(), "request", "context_overflow")
    assert world.requests == [] and world.commands() == []


# Metadata, billing and reservation


@pytest.mark.parametrize(
    ("change", "code"),
    [
        ({"context_length": 1048577}, "capability_unestablished"),
        ({"max_completion_tokens": 31999}, "capability_unestablished"),
        ({"supported_parameters": ["temperature"]}, "capability_unestablished"),
        ({"provider_name": None}, "capability_unestablished"),
        ({"tag": "other/provider"}, "capability_unestablished"),
        ({"pricing": {"prompt": "0.000002"}}, "pricing_unbounded"),
        ({"pricing": None}, "pricing_unbounded"),
        (
            {"pricing": {"prompt": "0.000003", "completion": "0.00001"}},
            "pricing_unbounded",
        ),
        (
            {
                "pricing": {
                    "prompt": "0.000002",
                    "completion": "0.00001",
                    "image": "0.1",
                }
            },
            "pricing_unbounded",
        ),
        (
            {
                "pricing": {
                    "prompt": "0.000002",
                    "completion": "0.00001",
                    "request": "0.01",
                }
            },
            "pricing_unbounded",
        ),
    ],
)
def test_missing_capability_or_unbounded_pricing_refuses_before_reservation(
    world, change, code
):
    world.endpoint.update(change)
    refused(world.run(), "metadata", code)
    assert world.posts == []
    assert "readiness-reserve" not in world.commands()


def test_key_evidence_mismatch_refuses_before_metadata(world):
    world.env["OPENROUTER_API_KEY"] = "another-test-only-key"
    refused(world.run(), "credential", "billing_evidence_invalid")
    assert world.requests == []


def test_refused_reservation_never_sends(world):
    def refuse(command, arguments):
        if command == "readiness-reserve":
            world.calls.append((command, tuple(arguments)))
            raise AttemptBudgetError()
        return World._invoke(world, command, arguments)

    world._invoke = refuse
    refused(world.run(), "reservation", "reservation_refused")
    assert world.posts == [] and "readiness-report" not in world.commands()


def test_expired_reservation_never_claims_or_sends(world):
    refused(world.run(clock=lambda: VALID_UNTIL), "reservation", "reservation_expired")
    assert world.posts == [] and "readiness-report" not in world.commands()


# One attempt, zero triage, strict acknowledgement


def test_success_sends_once_and_renders_critical_first_markdown_and_html(world):
    receipt = world.run()
    assert receipt["outcome"] == "rendered"
    assert world.commands() == [
        "readiness-profile",
        "readiness-reserve",
        "readiness-report",
    ]
    [post] = world.posts
    raw = post.content
    assert receipt["request_sha256"] == digest(raw)
    claim = dict(zip(*[iter(world.calls[-1][1][2:])] * 2))
    assert claim["--request-sha256"] == digest(raw)
    payload = json.loads(raw)
    assert set(payload) == {"model", "max_tokens", "stream", "messages", "provider"}
    assert payload["model"] == "moonshotai/kimi-k3.1-pro"
    assert payload["max_tokens"] == 32000 and payload["stream"] is False
    assert payload["provider"] == {
        "only": ["moonshotai/mxfp4"],
        "order": ["moonshotai/mxfp4"],
        "allow_fallbacks": False,
        "require_parameters": True,
        "max_price": {"prompt": "2", "completion": "10", "request": "0"},
    }
    prompt = json.dumps(payload["messages"])
    for item in EIGHT:
        assert item["cve"] in prompt
        assert item["product"] not in prompt
        assert all(url_of(ref) not in prompt for ref in item["references"])
    assert "example.test" not in prompt
    assert set(post.headers) >= {"authorization", "content-type"}
    assert not any(name.startswith("x-") for name in post.headers)

    # Bounded categorical receipt: no model text or answers.
    assert set(receipt) == {
        "schema",
        "outcome",
        "stage",
        "code",
        "profile_sha256",
        "fact_manifest_sha256",
        "source_revision",
        "sent",
        "request_sha256",
        "usage",
        "report_sha256",
        "finding_count",
    }
    assert receipt["usage"] == {
        "prompt_tokens": 180,
        "completion_tokens": 900,
        "reasoning_tokens": 700,
    }
    assert "acknowledged" not in json.dumps(receipt)
    stored = json.loads((world.output / "receipt.json").read_text())
    assert stored == receipt

    source = (world.output / "index.md").read_text()
    assert receipt["report_sha256"] == digest(source.encode())
    rows = report_findings(source).rows
    assert [row.title.rsplit("-", 1)[1] for row in rows] == EXPECTED_ORDER
    assert "link-" not in source and "acknowledged" not in source
    by_cve = {item["cve"]: item for item in EIGHT}
    from src.core.report_artifact import parse_report_artifact

    artifact = parse_report_artifact(source)
    for finding in artifact.findings:
        [cve] = finding.cve_ids
        assert finding.vendor_links == tuple(
            url_of(ref) for ref in by_cve[cve]["references"]
        )
        assert finding.severity.value == by_cve[cve]["severity"]
    page = Titles()
    page.feed((world.output / "index.html").read_text())
    assert [title.rsplit("-", 1)[1] for title in page.titles] == EXPECTED_ORDER
    # The actual outward URL inventory: reviewed references, NVD records for
    # the manifest CVEs and the site's own fixed links; never a digest.
    html_text = (world.output / "index.html").read_text()
    outward = set(re.findall(r"https?://[^\s\"'<>()]+", html_text))
    references = {url_of(r) for item in EIGHT for r in item["references"]}
    nvd = {readiness.NVD_DETAIL + item["cve"] for item in EIGHT}
    site = readiness.emitted_origin("SentryInsight")
    assert references <= outward
    assert {
        url
        for url in outward
        if url
        not in references
        | nvd
        | readiness.SITE_IDENTITY_LINKS
        | readiness.VOCABULARY_IDENTIFIERS
        and not url.startswith(site)
    } == set()
    assert readiness.emitted_origin("SentryDigest") not in html_text
    assert "sentrydigest" not in html_text.casefold()
    assert "Reviewed advisory facts." in html_text
    assert "render_mode: reviewed_facts" in source
    # Nothing was written into the repository or its publication surface.
    assert list(world.root.iterdir()) == []


@pytest.mark.parametrize(
    "response",
    [
        lambda: httpx.Response(503, json={"error": {"code": 503}}),
        lambda: httpx.Response(429, json={"error": {"code": 429}}),
        lambda: httpx.ReadTimeout("synthetic"),
        lambda: httpx.ConnectError("synthetic"),
    ],
    ids=["unavailable", "rate-limited", "read-timeout", "connect-error"],
)
def test_any_failed_send_is_terminal_with_no_retry_or_triage(world, response):
    world.completion = response
    receipt = world.run()
    assert receipt["outcome"] == "refused" and receipt["sent"] is True
    assert receipt["code"] in {"http_status_not_ok", "send_uncertain"}
    assert len(world.posts) == 1
    assert world.commands().count("readiness-report") == 1
    assert not any("triage" in command for command in world.commands())
    assert not world.output.exists()


def _ack(ids, **extra):
    return json.dumps({"acknowledged": True, "ids": ids, **extra})


IDS = [item["cve"] for item in EIGHT]


@pytest.mark.parametrize(
    "content",
    [
        _ack(IDS[:-1]),
        _ack(IDS + ["CVE-2026-9999"]),
        _ack(IDS + IDS[:1]),
        _ack(IDS, note="extra"),
        json.dumps({"acknowledged": "true", "ids": IDS}),
        json.dumps({"acknowledged": False, "ids": IDS}),
        json.dumps({"ids": IDS}),
        "```json\n" + _ack(IDS) + "\n```",
        "Acknowledged: " + _ack(IDS),
        '{"acknowledged": true, "acknowledged": true, "ids": []}',
        "",
    ],
    ids=[
        "missing-id",
        "unknown-id",
        "duplicate-id",
        "extra-key",
        "string-true",
        "false",
        "missing-key",
        "fenced",
        "prose",
        "duplicate-key",
        "empty",
    ],
)
def test_acknowledgement_must_name_exactly_the_required_ids(world, content):
    world.completion = lambda: httpx.Response(200, json=ok_completion(content))
    refused(world.run(), "acknowledgement", "acknowledgement_invalid")
    assert len(world.posts) == 1 and not world.output.exists()


def _choice(**changes):
    choice = ok_completion()["choices"][0]
    choice.update(changes)
    return [choice]


@pytest.mark.parametrize(
    ("changes", "code"),
    [
        ({"choices": _choice(finish_reason="length")}, "output_length"),
        ({"choices": _choice(finish_reason="content_filter")}, "output_incomplete"),
        ({"choices": _choice(finish_reason=None)}, "output_incomplete"),
        (
            {
                "choices": _choice(
                    message={
                        "role": "assistant",
                        "content": "",
                        "tool_calls": [{"id": "x"}],
                    }
                )
            },
            "output_unsafe",
        ),
        (
            {
                "choices": _choice(
                    message={"role": "assistant", "content": "", "refusal": "no"}
                )
            },
            "model_refused",
        ),
        ({"choices": _choice() * 2}, "response_invalid"),
        ({"model": "moonshotai/kimi-k3.1"}, "model_mismatch"),
        ({"provider": "Other Provider"}, "provider_mismatch"),
        (
            {"usage": {"prompt_tokens": 180, "completion_tokens": 32001}},
            "usage_invalid",
        ),
        ({"usage": None}, "usage_invalid"),
        (
            {"usage": {"prompt_tokens": 180, "completion_tokens": 900, "cost": 2.5}},
            "cost_exceeds_bound",
        ),
    ],
    ids=[
        "length",
        "filtered",
        "no-finish",
        "tool-call",
        "refusal",
        "two-choices",
        "wrong-model",
        "wrong-provider",
        "over-output",
        "missing-usage",
        "over-cost",
    ],
)
def test_uncertain_or_off_route_output_refuses_before_any_output(world, changes, code):
    world.completion = lambda: httpx.Response(200, json=ok_completion(**changes))
    refused(world.run(), "response", code)
    assert len(world.posts) == 1 and not world.output.exists()


def test_unexpected_failure_never_echoes_response_content(world, monkeypatch):
    def explode(*_):
        raise RuntimeError("SECRETMARKER")

    monkeypatch.setattr(readiness, "render_report", explode)
    receipt = world.run()
    assert (receipt["outcome"], receipt["code"]) == ("refused", "internal_error")
    assert "SECRETMARKER" not in json.dumps(receipt)
    assert not world.output.exists()


# Exclusivity and import boundary


def test_legacy_pipeline_refuses_to_start_beside_a_readiness_dispatch(monkeypatch):
    monkeypatch.setenv(readiness.FLAG, readiness.READINESS_PROFILE["id"])
    with pytest.raises(PaidVerificationError):
        asyncio.run(initialize_verification({}))


def test_entry_point_import_loads_no_tracing():
    loaded = subprocess.check_output(
        [
            sys.executable,
            "-B",
            "-c",
            "import sys; import scripts.paid_readiness_report;"
            "print(sorted(m for m in ('logfire', 'langgraph') if m in sys.modules))",
        ],
        cwd=ROOT,
        text=True,
    )
    assert loaded.strip() == "[]"


# Provider allowlist


def test_production_allowlist_builds_only_canonical_commit_pages():
    production = {
        name: value
        for name, value in readiness.PROVIDERS.items()
        if name != "synthetic"
    }
    assert production == {
        "github": ("github.com", "/{repository}/commit/{commit}"),
        "gitlab": ("gitlab.com", "/{repository}/-/commit/{commit}"),
    }
    # String construction only; fictional repository, never fetched.
    repository = "example-owner/example-repo"
    assert readiness._reference(
        ref("x", provider="github") | {"repository": repository}
    ) == (f"https://github.com/{repository}/commit/{COMMIT}")
    assert readiness._reference(
        ref("x", provider="gitlab") | {"repository": repository}
    ) == (f"https://gitlab.com/{repository}/-/commit/{COMMIT}")


# One guard for every consumer that rebuilds reviewed-facts HTML


def _paid_source(day):
    raw = encode(manifest_value(EIGHT[:2]))
    manifest = readiness.load_fact_manifest(raw, digest(raw))
    moment = datetime(2026, 11, day, 9, tzinfo=timezone.utc)
    return readiness.render_report(manifest, moment).source


def _outward(directory):
    found = set()
    for page in directory.rglob("*.html"):
        found |= set(re.findall(r"https?://[^\s\"'<>()]+", page.read_text()))
    return found


def test_site_builder_rebuild_of_current_and_archived_paid_reports_links_no_digest(
    tmp_path,
):
    from scripts.build_site import build_site

    (tmp_path / "reports").mkdir()
    (tmp_path / "reports" / "2026-11-20.md").write_text(_paid_source(20))
    (tmp_path / "index.md").write_text(_paid_source(21))
    build_site(
        report_path=tmp_path / "index.md",
        output_path=tmp_path,
        template_path=ROOT / "site",
    )
    assert (tmp_path / "reports" / "2026-11-20.html").exists()
    outward = _outward(tmp_path)
    assert not any("sentrydigest" in url.casefold() for url in outward)
    assert url_of(EIGHT[0]["references"][0]) in outward


def test_pages_package_rebuild_of_paid_report_links_no_digest(tmp_path):
    from scripts.package_pages import STATIC_ASSETS, package_pages

    repo = tmp_path / "repository"
    repo.mkdir()
    # Repository code only: templates and the public contract.
    for name in ("site", "contracts"):
        shutil.copytree(ROOT / name, repo / name)
    # Inert placeholders: only the packager's presence check reads them.
    (repo / "assets").mkdir()
    for name in STATIC_ASSETS:
        (repo / "assets" / name).write_bytes(b"synthetic placeholder\n")
    (repo / "reports").mkdir()
    (repo / "reports" / "2026-11-20.md").write_text(_paid_source(20))
    (repo / "index.md").write_text(_paid_source(21))
    package_pages(repo_root=repo, output_path=tmp_path / "pages" / "site")
    outward = _outward(tmp_path / "pages" / "site")
    assert outward and not any("sentrydigest" in url.casefold() for url in outward)


def test_legacy_reports_keep_their_digest_method_link(tmp_path):
    from scripts.build_site import build_site

    legacy = _paid_source(21).replace("render_mode: reviewed_facts\n", "")
    (tmp_path / "index.md").write_text(legacy)
    build_site(
        report_path=tmp_path / "index.md",
        output_path=tmp_path,
        template_path=ROOT / "site",
    )
    assert readiness.emitted_origin("SentryDigest") in _outward(tmp_path)


@pytest.mark.parametrize(
    "change",
    [
        lambda text: text.replace("render_mode: reviewed_facts", "render_mode: other"),
        lambda text: text.replace("schema_version: 1", "schema_version: 2"),
    ],
    ids=["unknown-mode", "mode-with-digest-schema"],
)
def test_render_mode_drift_is_refused_by_parser_and_site_builder(tmp_path, change):
    from scripts.build_site import build_site
    from src.core.report_artifact import ReportArtifactError, parse_report_artifact

    source = change(_paid_source(21))
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(source)
    (tmp_path / "index.md").write_text(source)
    with pytest.raises(Exception):
        build_site(
            report_path=tmp_path / "index.md",
            output_path=tmp_path,
            template_path=ROOT / "site",
        )
    assert not (tmp_path / "index.html").exists()


@pytest.mark.parametrize(
    "extra",
    [
        '<a href="https://tracker.example.test/x">x</a>',
        '<a href="//tracker.example.test/x">x</a>',
        '<a href="https://sentrydigest.ricomanifesto.com/archive/2026-11-21/">d</a>',
    ],
    ids=["unknown-host", "protocol-relative", "digest-link"],
)
def test_candidate_link_inventory_refuses_any_unreviewed_outward_url(tmp_path, extra):
    raw = encode(manifest_value(EIGHT[:2]))
    manifest = readiness.load_fact_manifest(raw, digest(raw))
    (tmp_path / "index.html").write_text("<p>" + extra + "</p>")
    with pytest.raises(readiness.ReadinessRefusal) as caught:
        readiness.check_candidate_links(tmp_path, manifest)
    assert (caught.value.stage, caught.value.code) == ("render", "render_invalid")


def test_inventory_failure_after_send_leaves_no_candidate(world, monkeypatch):
    monkeypatch.setattr(readiness, "SITE_IDENTITY_LINKS", frozenset())
    refused(world.run(), "render", "render_invalid")
    assert len(world.posts) == 1 and not world.output.exists()
    assert not list(world.output.parent.iterdir())


# The actual Generate Report wiring


def _workflow():
    import yaml

    text = (ROOT / ".github/workflows/generate-report.yml").read_text()
    return text, yaml.safe_load(text)


def test_paid_option_runs_only_the_one_send_job_and_never_resumes():
    text, workflow = _workflow()
    jobs = workflow["jobs"]
    paid = "github.event.inputs.paid_verification"
    assert jobs["paid-readiness"]["if"] == (
        f"github.event_name == 'workflow_dispatch' && {paid} == 'true'"
    )
    # The hosted legacy generator is held: the paid job is the only job.
    assert set(jobs) == {"paid-readiness"}
    # Publication is never resumed from this workflow.
    assert "resume-publication" not in jobs
    assert "SENTRYINSIGHT_PAID_VERIFICATION" not in text
    assert "kimi-moonshot-verification-20261117" not in text
    inputs = workflow[True]["workflow_dispatch"]["inputs"]
    for name in ("expected_head", "fact_manifest_sha256", "surface_approval_sha256"):
        assert inputs[name]["default"] == ""


def test_paid_job_uses_only_scoped_secrets_and_no_legacy_side_effects():
    text, workflow = _workflow()
    job = workflow["jobs"]["paid-readiness"]
    section = text[text.index("  paid-readiness:") : len(text)]
    # Executable configuration only; explanatory comments may name what is absent.
    job_text = "\n".join(
        line for line in section.splitlines() if not line.lstrip().startswith("#")
    )
    assert set(re.findall(r"secrets\.([A-Z_]+)", job_text)) == {
        "PAT_GITHUB",
        "OPENROUTER_API_KEY",
    }
    for forbidden in (
        "main.py",
        "LOGFIRE",
        "VT_",
        "GOOGLE_TI",
        "projection",
        "publish-production",
        "git push",
        "git commit",
        "triage",
        "continue-on-error",
        "--readmit true",
        "retry",
        "export_report_candidate",
        "review_sources",
    ):
        assert forbidden not in job_text, forbidden
    assert job["permissions"] == {"contents": "read"}
    steps = {step["name"]: step for step in job["steps"]}
    admit = steps["Admit paid readiness without readmission"]["run"]
    assert "--readmit false" in admit
    run = steps["Run the one-send paid readiness route"]
    assert (
        run["env"]["SENTRYINSIGHT_PAID_READINESS"] == readiness.READINESS_PROFILE["id"]
    )
    assert "scripts/paid_readiness_report.py" in run["run"]
    uploads = [
        step for step in job["steps"] if "upload-artifact" in step.get("uses", "")
    ]
    assert len(uploads) == 1
    assert uploads[0]["if"] == "success() && steps.readiness.outcome == 'success'"
    assert uploads[0]["with"]["path"] == "${{ runner.temp }}/paid-readiness/candidate"
    outcome = steps["Record paid readiness outcome"]
    assert outcome["if"].startswith("always()")
    assert "OUTCOME=not-published" in outcome["run"]
    assert "OUTCOME=failed" in outcome["run"]
