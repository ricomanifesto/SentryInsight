"""Paid readiness: reviewed facts in, acknowledged IDs back, host-rendered report.

One manual, first-attempt-only paid request. The model sees only the required
CVE IDs and returns a closed JSON acknowledgement; it supplies no prose, links
or values to the report. The host renders the defensive report from a
repository-owned, reviewer-approved fact manifest pinned by commit and digest,
reusing the vendor-link ownership gate, Reporting resolution, Critical-first
order and the artifact parser.

Every check that can fail before money is committed runs before the key is
used: dispatch identity, checkout, manifest, legacy publication surface,
output location, request size and the paid profile bound. Any refusal yields
one categorical receipt; no model text, answers or raw response is retained.
The rendered candidate is written only to a fresh directory outside the
repository and is never promoted, uploaded or published here.
"""

from __future__ import annotations

import asyncio
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from decimal import ROUND_CEILING, Decimal, InvalidOperation
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
from types import MappingProxyType
from typing import Any, Callable, Mapping, cast

import httpx

from .attempt_budget import AdmissionAttemptBudget, AttemptBudgetError
from .paid_verification import EVIDENCE, FLAG as VERIFICATION_FLAG, READINESS_FLAG
from .publication_transaction import COMPLETED_DIRECTORY, CORE, JOURNAL_DIRECTORY
from .public_site import emitted_origin
from .report_artifact import (
    REVIEWED_FACTS_MODE,
    ReportArtifactError,
    parse_report_artifact,
)
from .report_validation import ReportPreparationError, order_active_findings
from .reporting import (
    ReportingGroundingError,
    ReportingSource,
    normalize_reporting_url,
    reporting_key,
    resolve_reporting_keys,
)
from .finding_evidence import EvidenceError
from .source_review import SourceReviewError
from .vendor_link_references import (
    STRAY_LINK_ID_PATTERN,
    link_id,
    resolve_vendor_link_ids,
)

FLAG = READINESS_FLAG
MANIFEST_DIGEST = "SENTRYINSIGHT_FACT_MANIFEST_SHA256"
SURFACE_DIGEST = "SENTRYINSIGHT_SURFACE_APPROVAL_SHA256"
MANIFEST_PATH = "config/paid-readiness-facts.json"
SURFACE_PATH = "config/paid-readiness-surface.json"
MANIFEST_SCHEMA = "sentryinsight/paid-readiness-facts/v1"
SURFACE_SCHEMA = "sentryinsight/paid-readiness-surface/v1"
RECEIPT_SCHEMA = "sentryinsight/paid-readiness-receipt/v1"
API_ROOT = "https://openrouter.ai/api/v1/"
ROOT = Path(__file__).resolve().parents[2]

# Mirrors publication/kit/verification-budget.js READINESS_PROFILE exactly;
# both sides pin the same canonical digest and bound independently.
READINESS_PROFILE: Mapping[str, Any] = MappingProxyType(
    {
        "id": "kimi-moonshot-readiness-20261121",
        "model": "moonshotai/kimi-k3.1-pro",
        "provider": "moonshotai/mxfp4",
        "reportAttempts": 1,
        "reportContext": 1048576,
        "reportOutput": 32000,
        "reportPromptPrice": "2",
        "reportCompletionPrice": "10",
        "triageRequests": 0,
        "reserveMicrousd": 2417152,
        "limitMicrousd": 2420000,
        "periodMicrousd": 20000000,
        "periodStart": "2026-11-01T00:00:00.000Z",
        "periodEnd": "2026-12-01T00:00:00.000Z",
    }
)
READINESS_PROFILE_SHA256 = (
    "b892d97a1df2c76e5547a078a8c81bb9d622bf4d2aba688facbcd802bab5c951"
)
HARD_CAP_MICROUSD = 2420000

SEVERITIES = ("critical", "high", "medium", "low")
# The reviewed exploitation exposure, in the artifact's status vocabulary.
EXPOSURES = ("active", "observed", "potential", "not_observed", "unknown")
REMEDIATIONS = ("patch", "mitigate", "investigate", "monitor")
RECOMMENDATIONS = MappingProxyType(
    {
        "patch": "Apply the reviewed fix from the linked remediation reference.",
        "mitigate": (
            "Apply the reviewed mitigation from the linked remediation reference "
            "until a fix is deployed."
        ),
        "investigate": (
            "Confirm whether the product is deployed, then follow the linked "
            "remediation reference."
        ),
        "monitor": "Track the linked remediation reference for updates.",
    }
)
ABSENT = "Not stated in supplied sources."
PUBLISHER = "Reviewed advisory facts"
MAX_MANIFEST_BYTES = 65536
MAX_ADVISORIES = 32
MAX_REFERENCES = 4
MAX_RESPONSE_BYTES = 262144
MAX_CONTENT_BYTES = 4096
# Bytes bound tokens from above; the margin covers the chat template.
TEMPLATE_MARGIN = 4096

_HEX64 = re.compile(r"[a-f0-9]{64}")
_REVISION = re.compile(r"[a-f0-9]{40}")
_CVE = re.compile(r"CVE-\d{4}-\d{4,7}")
_PRODUCT = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9 .+_-]{0,62}[A-Za-z0-9+])?")
_REVIEWER = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,38}[a-z0-9])?")
_COMMIT = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
_REPOSITORY = re.compile(
    r"[A-Za-z0-9][A-Za-z0-9-]{0,38}/[A-Za-z0-9_][A-Za-z0-9_.-]{0,99}"
)
# Reviewed URLs never contain ";" or ",", the Markdown field separators.
_URL = re.compile(r"https?://[^\s\"'<>()\\;,]+", re.IGNORECASE)
_PROTOCOL_RELATIVE = re.compile(r"""(?:href|src|action)\s*=\s*["']?//""", re.IGNORECASE)

# Commit pages whose path names exactly one immutable commit object.
PROVIDERS: Mapping[str, tuple[str, str]] = MappingProxyType(
    {
        "github": ("github.com", "/{repository}/commit/{commit}"),
        "gitlab": ("gitlab.com", "/{repository}/-/commit/{commit}"),
    }
)
# Repository-owned site identity links the page template always carries.
SITE_IDENTITY_LINKS = frozenset(
    {"https://github.com/ricomanifesto/SentryInsight", "https://ricomanifesto.com/"}
)
NVD_DETAIL = "https://nvd.nist.gov/vuln/detail/"
# Vocabulary identifiers (JSON-LD context, sitemap namespace), never rendered as links.
VOCABULARY_IDENTIFIERS = frozenset(
    {"https://schema.org", "http://www.sitemaps.org/schemas/sitemap/0.9"}
)
_DATED = re.compile(r"\d{4}-\d{2}-\d{2}\.(?:md|html)|index\.(?:html|json)")

SYSTEM_PROMPT = (
    "You confirm receipt of a fixed list of identifiers. Reply with one JSON "
    'object and nothing else. It must have exactly two keys: "acknowledged", '
    'set to true, and "ids", an array that contains every identifier from the '
    "list exactly once. Do not add keys, commentary, code fences or any other text."
)

STAGES = frozenset(
    {
        "preflight",
        "checkout",
        "manifest",
        "surface",
        "output",
        "request",
        "profile",
        "credential",
        "metadata",
        "reservation",
        "send",
        "response",
        "acknowledgement",
        "render",
        "complete",
    }
)
CODES = frozenset(
    {
        "not_requested",
        "exclusive_route_conflict",
        "dispatch_invalid",
        "fact_manifest_unpinned",
        "checkout_mismatch",
        "fact_manifest_unavailable",
        "fact_manifest_invalid",
        "fact_manifest_unapproved",
        "publication_recovery_pending",
        "legacy_surface_unapproved",
        "legacy_surface_mismatch",
        "output_unsafe",
        "context_overflow",
        "profile_invalid",
        "bound_exceeds_cap",
        "credential_missing",
        "billing_evidence_invalid",
        "metadata_unavailable",
        "billing_scope_mismatch",
        "capability_unestablished",
        "pricing_unbounded",
        "reservation_refused",
        "reservation_expired",
        "claim_refused",
        "send_uncertain",
        "http_status_not_ok",
        "response_invalid",
        "model_mismatch",
        "provider_mismatch",
        "output_length",
        "output_incomplete",
        "output_unsafe",
        "model_refused",
        "usage_invalid",
        "cost_exceeds_bound",
        "acknowledgement_invalid",
        "render_invalid",
        "output_write_failed",
        "internal_error",
        "rendered",
    }
)


class ReadinessRefusal(Exception):
    def __init__(self, stage: str, code: str):
        assert stage in STAGES and code in CODES
        super().__init__(f"{stage}:{code}")
        self.stage = stage
        self.code = code


def _require(condition: bool, stage: str, code: str) -> None:
    if not condition:
        raise ReadinessRefusal(stage, code)


def canonical_bytes(value: Any) -> bytes:
    """The publication kit's canonicalJson: sorted keys, two spaces, newline."""
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def _reject_constant(_: str) -> Any:
    raise ValueError("non-finite number")


def strict_json(text: str) -> Any:
    return json.loads(
        text, object_pairs_hook=_no_duplicates, parse_constant=_reject_constant
    )


# Profile and bound


def readiness_bound_microusd(profile: Mapping[str, Any]) -> int:
    """One full input context plus the full output allowance, rounded up."""
    try:
        prompt = Decimal(profile["reportPromptPrice"])
        completion = Decimal(profile["reportCompletionPrice"])
    except (InvalidOperation, KeyError, TypeError):
        raise ReadinessRefusal("profile", "profile_invalid") from None
    attempts, context, output = (
        profile.get("reportAttempts"),
        profile.get("reportContext"),
        profile.get("reportOutput"),
    )
    _require(
        all(type(value) is int and value > 0 for value in (attempts, context, output))
        and prompt.is_finite()
        and completion.is_finite()
        and prompt >= 0
        and completion >= 0,
        "profile",
        "profile_invalid",
    )
    # The check above proves three positive ints; name that for typing.
    attempts, context, output = (
        cast(int, value) for value in (attempts, context, output)
    )
    total = attempts * (context * prompt + output * completion)
    return int(total.to_integral_value(rounding=ROUND_CEILING))


def verify_readiness_profile(exported: Any) -> Mapping[str, Any]:
    """Node's exported profile must be this exact profile, bound and digest."""
    _require(
        type(exported) is dict and set(exported) == {"profile", "sha256"},
        "profile",
        "profile_invalid",
    )
    profile, digest = exported["profile"], exported["sha256"]
    _require(type(profile) is dict, "profile", "profile_invalid")
    bound = readiness_bound_microusd(profile)
    _require(
        bound == profile.get("reserveMicrousd")
        and type(profile.get("limitMicrousd")) is int
        and bound <= profile["limitMicrousd"] <= HARD_CAP_MICROUSD,
        "profile",
        "bound_exceeds_cap",
    )
    _require(
        profile.get("reportAttempts") == 1 and profile.get("triageRequests") == 0,
        "profile",
        "profile_invalid",
    )
    _require(
        profile == dict(READINESS_PROFILE)
        and digest == _sha256(canonical_bytes(profile))
        and digest == READINESS_PROFILE_SHA256,
        "profile",
        "profile_invalid",
    )
    return MappingProxyType(dict(profile))


# Fact manifest


@dataclass(frozen=True)
class Advisory:
    cve: str
    product: str
    severity: str
    exposure: str
    remediation: str
    references: tuple[str, ...]


@dataclass(frozen=True)
class FactManifest:
    sha256: str
    advisories: tuple[Advisory, ...]

    @property
    def required_ids(self) -> tuple[str, ...]:
        return tuple(advisory.cve for advisory in self.advisories)


def _reference(value: Any) -> str:
    """One reviewed commit at an allowlisted provider; the host builds the URL.

    The manifest names a provider, a repository and the reviewed commit
    digest, never a free-form link, so the only path served is that
    provider's commit page for exactly that commit: no branch, tag, blob,
    query, fragment, port, credentials or redirect parameter can appear.
    """
    _require(
        type(value) is dict and set(value) == {"commit", "provider", "repository"},
        "manifest",
        "fact_manifest_invalid",
    )
    provider, repository, commit = (
        value["provider"],
        value["repository"],
        value["commit"],
    )
    _require(
        type(provider) is str
        and provider in PROVIDERS
        and type(repository) is str
        and _REPOSITORY.fullmatch(repository) is not None
        and not repository.casefold().endswith(".git")
        and type(commit) is str
        and _COMMIT.fullmatch(commit) is not None,
        "manifest",
        "fact_manifest_invalid",
    )
    host, path = PROVIDERS[provider]
    url = f"https://{host}{path.format(repository=repository, commit=commit)}"
    try:
        normalized = normalize_reporting_url(url)
    except ReportingGroundingError:
        raise ReadinessRefusal("manifest", "fact_manifest_invalid") from None
    _require(normalized == url, "manifest", "fact_manifest_invalid")
    return url


def _product(value: Any) -> str:
    _require(
        type(value) is str
        and _PRODUCT.fullmatch(value) is not None
        and " ".join(value.split()) == value
        and "cve" not in value.casefold()
        and STRAY_LINK_ID_PATTERN.search(value) is None,
        "manifest",
        "fact_manifest_invalid",
    )
    return value


def _advisory(value: Any) -> Advisory:
    _require(
        type(value) is dict
        and set(value)
        == {"cve", "exposure", "product", "references", "remediation", "severity"},
        "manifest",
        "fact_manifest_invalid",
    )
    references = value["references"]
    _require(
        type(value["cve"]) is str
        and _CVE.fullmatch(value["cve"]) is not None
        and value["severity"] in SEVERITIES
        and value["exposure"] in EXPOSURES
        and value["remediation"] in REMEDIATIONS
        and type(references) is list
        and 1 <= len(references) <= MAX_REFERENCES,
        "manifest",
        "fact_manifest_invalid",
    )
    return Advisory(
        cve=value["cve"],
        product=_product(value["product"]),
        severity=value["severity"],
        exposure=value["exposure"],
        remediation=value["remediation"],
        references=tuple(_reference(reference) for reference in references),
    )


def load_fact_manifest(raw: bytes | None, pinned_sha256: str) -> FactManifest:
    """Exact pinned bytes, canonical encoding, closed schema, approved state."""
    _require(raw is not None, "manifest", "fact_manifest_unavailable")
    assert raw is not None
    _require(
        len(raw) <= MAX_MANIFEST_BYTES and _sha256(raw) == pinned_sha256,
        "manifest",
        "fact_manifest_invalid",
    )
    try:
        value = strict_json(raw.decode("ascii"))
    except (UnicodeDecodeError, ValueError):
        raise ReadinessRefusal("manifest", "fact_manifest_invalid") from None
    _require(
        canonical_bytes(value) == raw
        and type(value) is dict
        and set(value) == {"advisories", "approval", "schema"}
        and value["schema"] == MANIFEST_SCHEMA
        and type(value["approval"]) is dict
        and set(value["approval"]) == {"reviewed_by", "state"}
        and type(value["approval"]["reviewed_by"]) is str
        and _REVIEWER.fullmatch(value["approval"]["reviewed_by"]) is not None
        and type(value["advisories"]) is list
        and 1 <= len(value["advisories"]) <= MAX_ADVISORIES,
        "manifest",
        "fact_manifest_invalid",
    )
    _require(
        value["approval"]["state"] == "approved",
        "manifest",
        "fact_manifest_unapproved",
    )
    advisories = tuple(_advisory(item) for item in value["advisories"])
    cves = [advisory.cve for advisory in advisories]
    references = [url for advisory in advisories for url in advisory.references]
    _require(
        cves == sorted(set(cves)) and len(references) == len(set(references)),
        "manifest",
        "fact_manifest_invalid",
    )
    return FactManifest(sha256=pinned_sha256, advisories=advisories)


# Legacy publication surface


def _surface_names(root: Path) -> list[str]:
    """Names that publication could re-serve; stat only, no content read."""
    for name in (JOURNAL_DIRECTORY, COMPLETED_DIRECTORY):
        journal = root / name
        _require(
            not (journal.exists() or journal.is_symlink()),
            "surface",
            "publication_recovery_pending",
        )
    names = []
    for name in sorted(CORE):
        path = root / name
        if path.is_symlink() or path.exists():
            _require(
                path.is_file() and not path.is_symlink(),
                "surface",
                "legacy_surface_mismatch",
            )
            names.append(name)
    reports = root / "reports"
    if reports.is_symlink() or reports.exists():
        _require(
            reports.is_dir() and not reports.is_symlink(),
            "surface",
            "legacy_surface_mismatch",
        )
        for child in sorted(reports.iterdir()):
            _require(
                child.is_file()
                and not child.is_symlink()
                and _DATED.fullmatch(child.name) is not None,
                "surface",
                "legacy_surface_mismatch",
            )
            names.append(f"reports/{child.name}")
    return names


def check_publication_surface(
    root: Path, approval_raw: bytes | None, pinned_sha256: str
) -> None:
    """Old archives or pending recovery never ride along unapproved.

    With no legacy surface there is nothing to re-export. Otherwise only an
    owner approval committed at the pinned revision, pinned by digest, stating
    that publication is idle and binding every re-servable file by digest,
    lets the paid success path advance. Files are hashed only then.
    """
    names = _surface_names(root)
    if not names:
        return
    _require(
        approval_raw is not None and _HEX64.fullmatch(pinned_sha256) is not None,
        "surface",
        "legacy_surface_unapproved",
    )
    assert approval_raw is not None
    try:
        value = strict_json(approval_raw.decode("ascii"))
    except (UnicodeDecodeError, ValueError):
        raise ReadinessRefusal("surface", "legacy_surface_unapproved") from None
    _require(
        _sha256(approval_raw) == pinned_sha256
        and canonical_bytes(value) == approval_raw
        and type(value) is dict
        and set(value) == {"publication_idle", "reviewed_by", "schema", "served"}
        and value["schema"] == SURFACE_SCHEMA
        and value["publication_idle"] is True
        and type(value["reviewed_by"]) is str
        and _REVIEWER.fullmatch(value["reviewed_by"]) is not None
        and type(value["served"]) is dict
        and all(
            type(digest) is str and _HEX64.fullmatch(digest) is not None
            for digest in value["served"].values()
        ),
        "surface",
        "legacy_surface_unapproved",
    )
    _require(set(value["served"]) == set(names), "surface", "legacy_surface_mismatch")
    for name in names:
        _require(
            _sha256((root / name).read_bytes()) == value["served"][name],
            "surface",
            "legacy_surface_mismatch",
        )


# Request and response


def build_request(manifest: FactManifest) -> tuple[dict, bytes]:
    """Acknowledgement only: CVE IDs, no facts, links, enrichment or tools."""
    profile = READINESS_PROFILE
    user = "Identifiers:\n" + json.dumps(
        list(manifest.required_ids), separators=(",", ":")
    )
    payload = {
        "model": profile["model"],
        "max_tokens": profile["reportOutput"],
        "stream": False,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
        "provider": {
            "only": [profile["provider"]],
            "order": [profile["provider"]],
            "allow_fallbacks": False,
            "require_parameters": True,
            "max_price": {
                "prompt": profile["reportPromptPrice"],
                "completion": profile["reportCompletionPrice"],
                "request": "0",
            },
        },
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    _require(
        len(raw) + TEMPLATE_MARGIN <= profile["reportContext"],
        "request",
        "context_overflow",
    )
    return payload, raw


def _bounded_int(value: Any, low: int, high: int) -> bool:
    return type(value) is int and low <= value <= high


def check_response(response: httpx.Response, provider_name: str) -> dict:
    """Accept one complete, exact-route, tool-free text completion."""
    _require(response.status_code == 200, "response", "http_status_not_ok")
    _require(
        len(response.content) <= MAX_RESPONSE_BYTES, "response", "response_invalid"
    )
    try:
        body = strict_json(response.content.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise ReadinessRefusal("response", "response_invalid") from None
    _require(type(body) is dict and "error" not in body, "response", "response_invalid")
    _require(
        body.get("model") == READINESS_PROFILE["model"], "response", "model_mismatch"
    )
    _require(body.get("provider") == provider_name, "response", "provider_mismatch")
    choices = body.get("choices")
    _require(
        type(choices) is list and len(choices) == 1 and type(choices[0]) is dict,
        "response",
        "response_invalid",
    )
    choice = choices[0]
    finish = choice.get("finish_reason")
    _require(finish != "length", "response", "output_length")
    _require(finish == "stop", "response", "output_incomplete")
    message = choice.get("message")
    _require(
        type(message) is dict and message.get("role") == "assistant",
        "response",
        "response_invalid",
    )
    _require(
        not message.get("tool_calls") and not message.get("function_call"),
        "response",
        "output_unsafe",
    )
    _require(not message.get("refusal"), "response", "model_refused")
    content = message.get("content")
    _require(
        type(content) is str and len(content.encode()) <= MAX_CONTENT_BYTES,
        "response",
        "response_invalid",
    )
    usage = body.get("usage")
    _require(type(usage) is dict, "response", "usage_invalid")
    output = READINESS_PROFILE["reportOutput"]
    prompt_tokens = usage.get("prompt_tokens")
    completion_tokens = usage.get("completion_tokens")
    _require(
        _bounded_int(prompt_tokens, 1, READINESS_PROFILE["reportContext"])
        and _bounded_int(completion_tokens, 1, output),
        "response",
        "usage_invalid",
    )
    details = usage.get("completion_tokens_details")
    reasoning = 0
    if details is not None:
        _require(type(details) is dict, "response", "usage_invalid")
        reasoning = details.get("reasoning_tokens", 0)
        _require(
            _bounded_int(reasoning, 0, completion_tokens), "response", "usage_invalid"
        )
    cost = usage.get("cost")
    if cost is not None:
        _require(
            type(cost) in (int, float) and math.isfinite(cost) and cost >= 0,
            "response",
            "usage_invalid",
        )
        microusd = Decimal(str(cost)) * 1000000
        _require(
            microusd <= READINESS_PROFILE["reserveMicrousd"],
            "response",
            "cost_exceeds_bound",
        )
    return {
        "content": content,
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "reasoning_tokens": reasoning,
        },
    }


def check_acknowledgement(content: str, required: tuple[str, ...]) -> None:
    """Closed JSON naming exactly the required IDs, each once, nothing more."""
    try:
        value = strict_json(content.strip(" \t\r\n"))
    except ValueError:
        raise ReadinessRefusal("acknowledgement", "acknowledgement_invalid") from None
    _require(
        type(value) is dict
        and set(value) == {"acknowledged", "ids"}
        and value["acknowledged"] is True
        and type(value["ids"]) is list
        and all(type(item) is str for item in value["ids"])
        and len(value["ids"]) == len(set(value["ids"])) == len(required)
        and set(value["ids"]) == set(required),
        "acknowledgement",
        "acknowledgement_invalid",
    )


# Deterministic rendering


@dataclass(frozen=True)
class RenderedReport:
    source: str
    sha256: str
    finding_count: int


def _catalog(manifest: FactManifest) -> dict[str, ReportingSource]:
    catalog = {}
    for advisory in manifest.advisories:
        url = advisory.references[0]
        key = reporting_key(url)
        _require(key not in catalog, "render", "render_invalid")
        catalog[key] = ReportingSource(
            key=key,
            publisher=PUBLISHER,
            title=f"{advisory.product} {advisory.cve}",
            url=url,
            content=canonical_bytes(asdict(advisory)).decode(),
            content_kind="reviewed_facts",
            links=advisory.references,
        )
    return catalog


def _finding(advisory: Advisory, key: str, source: ReportingSource) -> str:
    links = "; ".join(link_id(key, source.content, url) for url in advisory.references)
    return (
        f"### {advisory.product} {advisory.cve}\n"
        f"- **Description**: Reviewed advisory facts record {advisory.cve} in "
        f"{advisory.product}.\n"
        f"- **Severity**: {advisory.severity}\n"
        f"- **Exploitation Status**: {advisory.exposure}\n"
        f"- **Action**: {advisory.remediation}\n"
        f"- **CVE IDs**: {advisory.cve}\n"
        f"- **Reporting**: {key}\n"
        f"- **Affected Versions**: {ABSENT}\n"
        f"- **Exceptions**: {ABSENT}\n"
        f"- **Recommended Actions**: {RECOMMENDATIONS[advisory.remediation]}\n"
        f"- **Vendor Links**: {links}\n\n"
    )


def render_report(manifest: FactManifest, generated_at: datetime) -> RenderedReport:
    """Host-only Markdown from approved facts; no model text is involved."""
    catalog = _catalog(manifest)
    keys = list(catalog)
    critical = sum(item.severity == "critical" for item in manifest.advisories)
    products = sorted({item.product for item in manifest.advisories})
    body = (
        "# Exploitation Report\n\n## Executive Summary\n\n"
        f"This report lists {len(manifest.advisories)} reviewed advisories "
        f"({critical} critical) from an approved fact manifest. Critical "
        "findings appear first.\n\n"
        "Each finding links only to reviewed, commit-addressed remediation "
        "references.\n\n"
        "## Active Exploitation Details\n\n"
        + "".join(
            _finding(advisory, key, catalog[key])
            for advisory, key in zip(manifest.advisories, keys, strict=True)
        )
        + "## Affected Systems and Products\n\n"
        + "".join(f"- {product}\n" for product in products)
        + "\n## Attack Vectors and Techniques\n\n"
        "- Not covered: this report carries no attack-method detail.\n\n"
        "## Threat Actor Activities\n\n"
        "- Not covered by the reviewed advisory facts.\n"
    )
    try:
        body = resolve_vendor_link_ids(body, catalog)
        body = resolve_reporting_keys(body, catalog)
        body = order_active_findings(body)
        moment = generated_at.astimezone(timezone.utc).replace(microsecond=0)
        source = (
            "---\nschema_version: 1\n"
            f"render_mode: {REVIEWED_FACTS_MODE}\n"
            f"report_date: {moment.date().isoformat()}\n"
            f"generated_at: {moment.isoformat().replace('+00:00', 'Z')}\n---\n" + body
        )
        artifact = parse_report_artifact(source)
    except (
        EvidenceError,
        ReportingGroundingError,
        ReportPreparationError,
        ReportArtifactError,
        SourceReviewError,
    ):
        raise ReadinessRefusal("render", "render_invalid") from None
    expected = sorted(manifest.advisories, key=lambda item: item.severity != "critical")
    _require(
        [finding.cve_ids for finding in artifact.findings]
        == [(item.cve,) for item in expected]
        and [finding.vendor_links for finding in artifact.findings]
        == [item.references for item in expected]
        and [finding.severity.value for finding in artifact.findings]
        == [item.severity for item in expected]
        and [finding.exploitation_status.value for finding in artifact.findings]
        == [item.exposure for item in expected]
        and [finding.action.value for finding in artifact.findings]
        == [item.remediation for item in expected]
        and artifact.render_mode == REVIEWED_FACTS_MODE
        and artifact.digest_issue_url is None
        and STRAY_LINK_ID_PATTERN.search(source) is None,
        "render",
        "render_invalid",
    )
    return RenderedReport(source, _sha256(source.encode()), len(artifact.findings))


def check_candidate_links(directory: Path, manifest: FactManifest) -> None:
    """Every outward URL in the rendered pair is reviewed or site-owned.

    Allowed: the manifest's commit references, the NVD record of each
    manifest CVE, the site's own production origin and its fixed identity
    links. Anything else, a digest link included, refuses the candidate.
    Copied stylesheet and script assets are repository code, not render output.
    """
    allowed = {url for item in manifest.advisories for url in item.references}
    allowed |= {NVD_DETAIL + item.cve for item in manifest.advisories}
    allowed |= SITE_IDENTITY_LINKS | VOCABULARY_IDENTIFIERS
    site = emitted_origin("SentryInsight")
    for path in sorted(directory.rglob("*")):
        if path.suffix not in {".html", ".json", ".xml", ".md"} or not path.is_file():
            continue
        text = path.read_text()
        _require(_PROTOCOL_RELATIVE.search(text) is None, "render", "render_invalid")
        for url in _URL.findall(text):
            _require(url in allowed or url.startswith(site), "render", "render_invalid")


# Orchestration


def _default_git(root: Path) -> Callable[[list[str]], bytes | None]:
    def run(arguments: list[str]) -> bytes | None:
        env = {k: os.environ[k] for k in ("PATH", "HOME") if k in os.environ}
        try:
            completed = subprocess.run(
                ["git", *arguments],
                cwd=root,
                env=env,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=30,
                check=True,
            )
        except (OSError, subprocess.SubprocessError):
            return None
        return completed.stdout

    return run


def _now_ms() -> float:
    return time.time() * 1000


class _Run:
    def __init__(self, environ, root, output, bridge, transport, git, clock):
        self.environ = environ
        self.root = Path(root)
        self.output = Path(output)
        self.bridge = bridge
        self.transport = transport
        self.git = git or _default_git(self.root)
        self.clock = clock or _now_ms
        self.receipt: dict[str, Any] = {
            "schema": RECEIPT_SCHEMA,
            "outcome": "refused",
            "stage": "preflight",
            "code": "internal_error",
            "profile_sha256": READINESS_PROFILE_SHA256,
            "fact_manifest_sha256": None,
            "source_revision": None,
            "sent": False,
            "request_sha256": None,
            "usage": None,
            "report_sha256": None,
            "finding_count": None,
        }
        self.valid_until = 0
        self.manifest: FactManifest | None = None

    def _invoke(self, command: str, arguments: list[str], stage: str, code: str):
        try:
            return self.bridge._invoke(command, ["--run-attempt", "1", *arguments])
        except AttemptBudgetError:
            raise ReadinessRefusal(stage, code) from None

    def _deadline(self, stage: str) -> None:
        current = self.clock()
        _require(
            math.isfinite(current) and current < self.valid_until,
            stage,
            "reservation_expired",
        )

    def preflight(self) -> tuple[str, str]:
        env = self.environ
        _require(bool(env.get(FLAG, "")), "preflight", "not_requested")
        _require(env[FLAG] == READINESS_PROFILE["id"], "preflight", "dispatch_invalid")
        _require(
            not env.get(VERIFICATION_FLAG, ""),
            "preflight",
            "exclusive_route_conflict",
        )
        revision = env.get("SENTRYINSIGHT_SOURCE_REVISION", "")
        run_id = env.get("GITHUB_RUN_ID", "")
        _require(
            env.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
            and env.get("GITHUB_REF") == "refs/heads/main"
            and env.get("GITHUB_RUN_ATTEMPT") == "1"
            and env.get("SENTRYINSIGHT_ATTEMPT_STORE") == "admission"
            and _REVISION.fullmatch(revision) is not None
            and re.fullmatch(r"[0-9]{1,20}", run_id) is not None
            and env.get("SENTRYINSIGHT_ADMISSION_KEY") == f"run:{run_id}",
            "preflight",
            "dispatch_invalid",
        )
        pinned = env.get(MANIFEST_DIGEST, "")
        _require(
            _HEX64.fullmatch(pinned) is not None,
            "preflight",
            "fact_manifest_unpinned",
        )
        self.receipt.update(source_revision=revision, fact_manifest_sha256=pinned)
        if self.bridge is None:
            try:
                self.bridge = AdmissionAttemptBudget(
                    key=env["SENTRYINSIGHT_ADMISSION_KEY"],
                    run_id=run_id,
                    revision=revision,
                    run_attempt="1",
                )
            except AttemptBudgetError:
                raise ReadinessRefusal("preflight", "dispatch_invalid") from None
        return revision, pinned

    def checkout(self, revision: str, pinned: str) -> FactManifest:
        head = self.git(["rev-parse", "HEAD"])
        _require(
            head is not None and head.decode(errors="replace").strip() == revision,
            "checkout",
            "checkout_mismatch",
        )
        raw = self.git(["show", f"{revision}:{MANIFEST_PATH}"])
        manifest = load_fact_manifest(raw, pinned)
        approval = self.git(["show", f"{revision}:{SURFACE_PATH}"])
        check_publication_surface(
            self.root, approval, self.environ.get(SURFACE_DIGEST, "")
        )
        return manifest

    def check_output(self) -> None:
        output = self.output
        try:
            resolved_root = self.root.resolve()
            parent = output.parent.resolve()
        except OSError:
            raise ReadinessRefusal("output", "output_unsafe") from None
        _require(
            output.is_absolute()
            and not output.exists()
            and not output.is_symlink()
            and parent.is_dir()
            and parent != resolved_root
            and resolved_root not in parent.parents,
            "output",
            "output_unsafe",
        )

    def credential(self) -> tuple[str, Path, dict]:
        key = self.environ.get("OPENROUTER_API_KEY", "").strip()
        proof = self.environ.get(EVIDENCE, "")
        _require(bool(key) and bool(proof), "credential", "credential_missing")
        path = Path(proof)
        try:
            _require(
                not path.is_symlink() and path.stat().st_size <= 4096,
                "credential",
                "billing_evidence_invalid",
            )
            evidence = strict_json(path.read_text())
        except (OSError, ValueError, UnicodeDecodeError):
            raise ReadinessRefusal("credential", "billing_evidence_invalid") from None
        _require(
            type(evidence) is dict
            and type(evidence.get("actualMicrousd")) is int
            and evidence.get("keySha256") == _sha256(key.encode()),
            "credential",
            "billing_evidence_invalid",
        )
        return key, path, evidence

    async def metadata(self, key: str, evidence: dict) -> str:
        profile = READINESS_PROFILE
        async with httpx.AsyncClient(
            timeout=15, transport=self.transport, follow_redirects=False
        ) as client:

            async def read(path: str, authorized: bool) -> dict:
                try:
                    response = await client.get(
                        API_ROOT + path,
                        headers=(
                            {"Authorization": "Bearer " + key} if authorized else {}
                        ),
                    )
                    _require(
                        response.status_code == 200 and len(response.content) <= 524288,
                        "metadata",
                        "metadata_unavailable",
                    )
                    value = strict_json(response.content.decode("utf-8"))
                except (httpx.HTTPError, ValueError, UnicodeDecodeError):
                    raise ReadinessRefusal("metadata", "metadata_unavailable") from None
                _require(
                    type(value) is dict and type(value.get("data")) is dict,
                    "metadata",
                    "metadata_unavailable",
                )
                return value["data"]

            account = await read("key", True)
            workspace = account.get("workspace_id")
            try:
                usage = Decimal(str(account.get("usage_monthly")))
                byok = Decimal(str(account.get("byok_usage_monthly")))
            except InvalidOperation:
                raise ReadinessRefusal("metadata", "billing_scope_mismatch") from None
            _require(
                type(workspace) is str
                and bool(workspace)
                and evidence.get("scopeSha256")
                == _sha256(("workspace:" + workspace).encode())
                and type(account.get("usage_monthly")) in (int, float, str)
                and type(account.get("byok_usage_monthly")) in (int, float, str)
                and usage.is_finite()
                and byok.is_finite()
                and byok == 0
                and 0 <= usage * 1000000 <= evidence["actualMicrousd"],
                "metadata",
                "billing_scope_mismatch",
            )
            data = await read(f"models/{profile['model']}/endpoints", False)
        _require(
            data.get("id") == profile["model"] and type(data.get("endpoints")) is list,
            "metadata",
            "capability_unestablished",
        )
        endpoints = [
            row
            for row in data["endpoints"]
            if type(row) is dict and row.get("tag") == profile["provider"]
        ]
        _require(len(endpoints) == 1, "metadata", "capability_unestablished")
        endpoint = endpoints[0]
        provider_name = endpoint.get("provider_name")
        context = endpoint.get("context_length")
        completion = endpoint.get("max_completion_tokens")
        supported = endpoint.get("supported_parameters")
        _require(
            type(provider_name) is str
            and 0 < len(provider_name) <= 128
            and _bounded_int(context, 1, profile["reportContext"])
            and type(completion) is int
            and completion >= profile["reportOutput"]
            and type(supported) is list
            and "max_tokens" in supported,
            "metadata",
            "capability_unestablished",
        )
        pricing = endpoint.get("pricing")
        _require(type(pricing) is dict, "metadata", "pricing_unbounded")
        ceilings = {
            "prompt": Decimal(profile["reportPromptPrice"]),
            "completion": Decimal(profile["reportCompletionPrice"]),
        }
        _require(set(ceilings) <= set(pricing), "metadata", "pricing_unbounded")
        for field, value in pricing.items():
            try:
                _require(
                    type(value) in (int, float, str), "metadata", "pricing_unbounded"
                )
                amount = Decimal(str(value))
            except InvalidOperation:
                raise ReadinessRefusal("metadata", "pricing_unbounded") from None
            ceiling = ceilings.get(field, Decimal(0))
            _require(
                amount.is_finite() and 0 <= amount * 1000000 <= ceiling,
                "metadata",
                "pricing_unbounded",
            )
        return provider_name

    async def reserve(self, proof: Path, evidence: dict, pinned: str) -> None:
        digest = _sha256(canonical_bytes(evidence))
        reserved = self._invoke(
            "readiness-reserve",
            [
                "--billing-evidence",
                str(proof),
                "--evidence-sha256",
                digest,
                "--fact-manifest-sha256",
                pinned,
            ],
            "reservation",
            "reservation_refused",
        )
        current = self.clock()
        _require(
            type(reserved) is dict
            and set(reserved)
            == {"reservedMicrousd", "profileSha256", "factManifestSha256", "validUntil"}
            and reserved["reservedMicrousd"] == READINESS_PROFILE["reserveMicrousd"]
            and reserved["profileSha256"] == READINESS_PROFILE_SHA256
            and reserved["factManifestSha256"] == pinned
            and type(reserved["validUntil"]) is int
            and reserved["validUntil"] <= current + 3600000,
            "reservation",
            "reservation_refused",
        )
        self.valid_until = reserved["validUntil"]
        self._deadline("reservation")

    async def send(self, key: str, raw: bytes, request_sha256: str, pinned: str):
        claimed = self._invoke(
            "readiness-report",
            ["--request-sha256", request_sha256, "--fact-manifest-sha256", pinned],
            "send",
            "claim_refused",
        )
        _require(claimed == {"claimed": True}, "send", "claim_refused")
        self._deadline("send")
        self.receipt["sent"] = True
        try:
            async with httpx.AsyncClient(
                timeout=httpx.Timeout(900, connect=15),
                transport=self.transport,
                follow_redirects=False,
            ) as client:
                return await client.post(
                    API_ROOT + "chat/completions",
                    content=raw,
                    headers={
                        "Authorization": "Bearer " + key,
                        "Content-Type": "application/json",
                    },
                )
        except httpx.HTTPError:
            raise ReadinessRefusal("send", "send_uncertain") from None

    def write_output(self, rendered: RenderedReport) -> None:
        # Imported here: the site builder is needed only for a rendered result.
        from scripts.build_site import SiteBuildError, build_site

        staging = Path(
            tempfile.mkdtemp(prefix=".paid-readiness-", dir=self.output.parent)
        )
        try:
            report_path = staging / "index.md"
            report_path.write_text(rendered.source)
            build_site(
                report_path=report_path,
                output_path=staging,
                template_path=ROOT / "site",
            )
            assert self.manifest is not None
            check_candidate_links(staging, self.manifest)
            final = dict(self.receipt, outcome="rendered", stage="complete")
            final["code"] = "rendered"
            (staging / "receipt.json").write_bytes(canonical_bytes(final))
            os.rename(staging, self.output)
        except ReadinessRefusal:
            shutil.rmtree(staging, ignore_errors=True)
            raise
        except (OSError, SiteBuildError, UnicodeDecodeError):
            shutil.rmtree(staging, ignore_errors=True)
            raise ReadinessRefusal("render", "output_write_failed") from None

    async def run(self) -> dict:
        revision, pinned = self.preflight()
        manifest = self.checkout(revision, pinned)
        self.manifest = manifest
        self.check_output()
        _, raw = build_request(manifest)
        request_sha256 = _sha256(raw)
        self.receipt["request_sha256"] = request_sha256
        verify_readiness_profile(
            self._invoke("readiness-profile", [], "profile", "profile_invalid")
        )
        key, proof, evidence = self.credential()
        provider_name = await self.metadata(key, evidence)
        await self.reserve(proof, evidence, pinned)
        response = await self.send(key, raw, request_sha256, pinned)
        checked = check_response(response, provider_name)
        self.receipt["usage"] = checked["usage"]
        check_acknowledgement(checked["content"], manifest.required_ids)
        moment = datetime.fromtimestamp(self.clock() / 1000, tz=timezone.utc)
        rendered = render_report(manifest, moment)
        self.receipt.update(
            report_sha256=rendered.sha256, finding_count=rendered.finding_count
        )
        self.write_output(rendered)
        self.receipt.update(outcome="rendered", stage="complete", code="rendered")
        return self.receipt


async def run_paid_readiness(
    *,
    environ: Mapping[str, str],
    output: Path,
    root: Path = ROOT,
    bridge: Any = None,
    transport: httpx.AsyncBaseTransport | None = None,
    git: Callable[[list[str]], bytes | None] | None = None,
    clock: Callable[[], float] | None = None,
) -> dict:
    """Run the paid readiness route once; always return one bounded receipt."""
    run = _Run(dict(environ), root, output, bridge, transport, git, clock)
    try:
        return await run.run()
    except ReadinessRefusal as refusal:
        run.receipt.update(outcome="refused", stage=refusal.stage, code=refusal.code)
    except asyncio.CancelledError:
        raise
    except Exception:
        # Never echo an unexpected exception: it may carry response content.
        run.receipt.update(outcome="refused", code="internal_error")
    return run.receipt
