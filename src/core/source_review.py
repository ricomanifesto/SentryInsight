"""Source-owned quarantine before generation; no failed claim is repaired here."""

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile
from typing import Any, Mapping, Sequence

from .cve import extract_cve_ids
from .report_validation import markdown_plain_text, markdown_references
from .article_prompt import canonical_source_article, format_article_summary
from .finding_evidence import build_finding_detail_context
from .reporting import (
    ReportingGroundingError,
    ReportingSource,
    build_reporting_catalog,
    normalize_reporting_url,
    reporting_key,
)
from .version_references import _scopes

POLICY_VERSION = 1
# Advisory grounding admits sources held only for soft version-evidence
# reasons. Their unresolved versions render as unresolved after generation;
# hard reasons still reject. The packet records the policy it was planned
# under, so archived strict packets keep validating unchanged.
ADVISORY_POLICY_VERSION = 2
POLICY_VERSIONS = frozenset({POLICY_VERSION, ADVISORY_POLICY_VERSION})
PLAN_KEY = "source_review_plan"
SOFT_REASONS = frozenset(
    {"unowned_version_evidence", "unresolved_version_assertion", "version_clause_error"}
)
HARD_REASONS = frozenset(
    {
        "version_collection_error",
        "empty_version_list",
        "contradictory_version_constraints",
        "unresolved_scope_not_eligible",
    }
)
STATES = {"eligible": 0, "review_required": 1, "source_rejected": 2}
HEX = re.compile(r"[0-9a-f]{64}")
MAX_SOURCES = 512
MAX_PACKET_BYTES = 1024 * 1024


class SourceReviewError(ValueError):
    """Fixed codes/messages only; never includes source or candidate values."""

    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def _require(condition: bool, code: str = "invalid_review_packet") -> None:
    if not condition:
        raise SourceReviewError(code)


def _cve_list(values: Any) -> list[str]:
    _require(isinstance(values, (list, tuple)), "invalid_source_metadata")
    _require(
        all(
            isinstance(value, str)
            and re.fullmatch(r"CVE-\d{4}-\d{4,}", value.strip(), re.I)
            for value in values
        ),
        "invalid_source_metadata",
    )
    return sorted({value.strip().upper() for value in values})


def _scope_state(
    state: str, reasons: Sequence[str], policy_version: int = POLICY_VERSION
) -> str:
    _require(set(reasons) <= SOFT_REASONS | HARD_REASONS, "unknown_review_reason")
    held = (
        "eligible" if policy_version == ADVISORY_POLICY_VERSION else "review_required"
    )
    if state == "blocked":
        _require(bool(reasons), "invalid_review_scope")
        return "source_rejected" if set(reasons) & HARD_REASONS else held
    _require(not reasons and state in {"supported", "not_stated", "unresolved"})
    return held if state == "unresolved" else "eligible"


def _cohorts(rows: Sequence[Mapping[str, Any]]) -> list[list[str]]:
    by_key = {row["key"]: row for row in rows}
    pending = set(by_key)
    groups = []
    while pending:
        seed = min(pending)
        members = {seed}
        cves = set(by_key[seed]["cves"])
        while added := {
            key for key in pending - members if cves & set(by_key[key]["cves"])
        }:
            members |= added
            cves |= {cve for key in added for cve in by_key[key]["cves"]}
        pending -= members
        groups.append(sorted(members))
    return groups


def _apply_dispositions(
    rows: list[dict[str, Any]],
    scopes: list[dict[str, Any]],
    policy_version: int = POLICY_VERSION,
) -> None:
    for row in rows:
        owned = [scope for scope in scopes if row["key"] in scope["source_keys"]]
        _require(bool(owned), "missing_review_scope")
        row["scope_ids"] = sorted(scope["id"] for scope in owned)
        row["direct_state"] = max(
            (
                _scope_state(scope["state"], scope["reason_codes"], policy_version)
                for scope in owned
            ),
            key=STATES.__getitem__,
        )
        row["reason_codes"] = sorted(
            {
                reason
                for scope in owned
                for reason in (
                    scope["reason_codes"]
                    if scope["state"] != "unresolved"
                    else ["unresolved_version_evidence"]
                )
            }
        )
    by_key = {row["key"]: row for row in rows}
    for cohort in _cohorts(rows):
        state = max(
            (by_key[key]["direct_state"] for key in cohort), key=STATES.__getitem__
        )
        origins = [key for key in cohort if by_key[key]["direct_state"] != "eligible"]
        for key in cohort:
            by_key[key].update(state=state, origin_keys=origins, cohort_keys=cohort)


def validate_review_packet(packet: Any) -> dict[str, Any]:
    """Validate bounded metadata and its internal relationships, not source truth."""
    _require(isinstance(packet, dict))
    _require(
        set(packet)
        == {"schema_version", "policy_version", "plan_id", "sources", "scopes"}
    )
    _require(type(packet["schema_version"]) is int and packet["schema_version"] == 1)
    _require(
        type(packet["policy_version"]) is int
        and packet["policy_version"] in POLICY_VERSIONS
    )
    _require(
        isinstance(packet["sources"], list) and len(packet["sources"]) <= MAX_SOURCES
    )
    _require(
        isinstance(packet["scopes"], list) and len(packet["scopes"]) <= MAX_SOURCES * 16
    )
    _require(len(canonical_json(packet).encode()) <= MAX_PACKET_BYTES)
    source_fields = {
        "key",
        "publisher",
        "title",
        "url",
        "content_sha256",
        "detail_evidence_sha256",
        "content_kind",
        "links",
        "metadata_cves",
        "cves",
        "scope_ids",
        "direct_state",
        "state",
        "reason_codes",
        "origin_keys",
        "cohort_keys",
    }
    rows = []
    for original in packet["sources"]:
        _require(isinstance(original, dict) and set(original) == source_fields)
        row = dict(original)
        for field in (
            "key",
            "publisher",
            "title",
            "url",
            "content_sha256",
            "content_kind",
        ):
            _require(
                isinstance(row[field], str)
                and bool(row[field])
                and len(row[field]) <= 8192
            )
        _require(bool(HEX.fullmatch(row["content_sha256"])))
        _require(
            isinstance(row["detail_evidence_sha256"], str)
            and bool(HEX.fullmatch(row["detail_evidence_sha256"]))
        )
        _require(row["content_kind"] in {"article", "feed"})
        try:
            _require(row["url"] == normalize_reporting_url(row["url"]))
            _require(row["key"] == reporting_key(row["url"]))
            _require(isinstance(row["links"], list) and len(row["links"]) <= 512)
            _require(
                all(
                    isinstance(link, str) and link == normalize_reporting_url(link)
                    for link in row["links"]
                )
            )
        except ReportingGroundingError:
            raise SourceReviewError("invalid_review_packet") from None
        for field in ("metadata_cves", "cves"):
            _require(row[field] == _cve_list(row[field]))
        _require(set(row["metadata_cves"]) <= set(row["cves"]))
        rows.append(row)
    keys = [row["key"] for row in rows]
    _require(keys == sorted(set(keys)))
    scopes = packet["scopes"]
    ids = []
    for scope in scopes:
        _require(
            isinstance(scope, dict)
            and set(scope)
            == {"id", "cves", "source_keys", "state", "reason_codes", "evidence_sha256"}
        )
        _require(scope["cves"] == _cve_list(scope["cves"]))
        _require(isinstance(scope["source_keys"], list) and bool(scope["source_keys"]))
        _require(all(isinstance(key, str) for key in scope["source_keys"]))
        _require(scope["source_keys"] == sorted(set(scope["source_keys"])))
        _require(set(scope["source_keys"]) <= set(keys))
        _require(
            isinstance(scope["reason_codes"], list)
            and all(isinstance(r, str) for r in scope["reason_codes"])
        )
        _require(scope["reason_codes"] == sorted(set(scope["reason_codes"])))
        _require(isinstance(scope["state"], str))
        _scope_state(scope["state"], scope["reason_codes"], packet["policy_version"])
        _require(
            isinstance(scope["evidence_sha256"], str)
            and bool(HEX.fullmatch(scope["evidence_sha256"]))
        )
        _require(scope["id"] == digest({k: v for k, v in scope.items() if k != "id"}))
        ids.append(scope["id"])
    _require(ids == sorted(set(ids)))
    _apply_dispositions(rows, scopes, packet["policy_version"])
    _require(rows == packet["sources"])
    _require(
        packet["plan_id"] == digest({k: v for k, v in packet.items() if k != "plan_id"})
    )
    return packet


@dataclass(frozen=True)
class SourceReviewPlan:
    catalog: dict[str, ReportingSource]
    packet: dict[str, Any]

    @property
    def eligible_keys(self) -> tuple[str, ...]:
        return tuple(
            row["key"] for row in self.packet["sources"] if row["state"] == "eligible"
        )

    @property
    def eligible_catalog(self) -> dict[str, ReportingSource]:
        return {key: self.catalog[key] for key in self.eligible_keys}


def review_articles(
    plan: SourceReviewPlan, *, eligible_only: bool = True
) -> list[dict[str, Any]]:
    """Canonical prompt inputs; preserve complete bodies and normalize metadata."""
    validate_review_packet(plan.packet)
    metadata = {row["key"]: row["metadata_cves"] for row in plan.packet["sources"]}
    catalog = plan.eligible_catalog if eligible_only else plan.catalog
    return [
        canonical_source_article(source, metadata[key])
        for key, source in catalog.items()
    ]


def _source_cve_identities(
    catalog: Mapping[str, ReportingSource], metadata_cves: Mapping[str, Sequence[str]]
) -> dict[str, list[str]]:
    """Bound each identity to a field under shared and isolated prompt context.

    CommonMark references may be defined by another source. Use the exact shared
    presentation to find those definitions, but never concatenate fields while
    extracting identities. Also retain each source's isolated interpretation so
    an unrelated unclosed block cannot hide its own definitions.
    """
    summaries = {
        key: format_article_summary(
            canonical_source_article(source, metadata_cves[key])
        )
        for key, source in catalog.items()
    }
    shared_references = markdown_references("".join(summaries.values()))
    local_references = {
        key: markdown_references(summary) for key, summary in summaries.items()
    }
    # An unrelated open block must not hide a valid definition supplied by a
    # different source. Retain that conservative interpretation as well, using
    # only definitions recognized in actual shared or isolated source contexts.
    available_references = dict(shared_references)
    for references in local_references.values():
        for label, definition in references.items():
            available_references.setdefault(label, definition)
    identities = {}
    for key, source in catalog.items():
        contexts = [shared_references]
        for references in (local_references[key], available_references):
            if references not in contexts:
                contexts.append(references)
        fields = [(source.content, False)] + [
            (field, True)
            for field in (
                source.title,
                source.publisher,
                source.url,
                *source.links,
                *metadata_cves[key],
            )
        ]
        cves = set()
        for field, inline in fields:
            cves.update(extract_cve_ids(field))
            for references in contexts:
                cves.update(
                    extract_cve_ids(
                        markdown_plain_text(field, inline=inline, references=references)
                    )
                )
        identities[key] = sorted(cves)
    return identities


def plan_reporting_catalog(
    catalog: Mapping[str, ReportingSource],
    metadata_cves: Mapping[str, Sequence[str]],
    *,
    advisory: bool = False,
) -> SourceReviewPlan:
    """Recompute from retained source bodies; never accept a cached disposition.

    ``advisory`` admits sources held only for soft version-evidence reasons.
    """
    policy_version = ADVISORY_POLICY_VERSION if advisory else POLICY_VERSION
    _require(set(catalog) == set(metadata_cves), "invalid_source_metadata")
    _require(len(catalog) <= MAX_SOURCES, "review_input_limit_exceeded")
    ordered = {key: catalog[key] for key in sorted(catalog)}
    full_context = build_finding_detail_context(ordered)
    normalized_metadata = {key: _cve_list(metadata_cves[key]) for key in ordered}
    identities = _source_cve_identities(ordered, normalized_metadata)
    rows = []
    for key, source in ordered.items():
        extra = normalized_metadata[key]
        _require(bool(source.content.strip()), "missing_source_content")
        _require(source.content_kind in {"article", "feed"}, "invalid_source_metadata")
        rows.append(
            {
                "key": key,
                "publisher": source.publisher,
                "title": source.title,
                "url": source.url,
                "content_sha256": hashlib.sha256(source.content.encode()).hexdigest(),
                "detail_evidence_sha256": digest(
                    [item for item in full_context if item["source_key"] == key]
                ),
                "content_kind": source.content_kind,
                "links": list(source.links),
                "metadata_cves": extra,
                "cves": identities[key],
            }
        )
    full_scopes = _scopes(ordered)
    decisions = []
    for scope in full_scopes:
        item = {
            "cves": list(scope.cves),
            "source_keys": sorted(scope.source_keys),
            "state": scope.state,
            "reason_codes": list(scope.failure_reasons),
            "evidence_sha256": digest(scope.context()),
        }
        item["id"] = digest(item)
        decisions.append(item)
    decisions.sort(key=lambda item: item["id"])
    _apply_dispositions(rows, decisions, policy_version)
    packet: dict[str, Any] = {
        "schema_version": 1,
        "policy_version": policy_version,
        "sources": rows,
        "scopes": decisions,
    }
    packet["plan_id"] = digest(packet)
    validate_review_packet(packet)
    plan = SourceReviewPlan(ordered, packet)
    eligible = set(plan.eligible_keys)
    # Removing a definition/context provider must not change a retained identity.
    _require(
        _source_cve_identities(plan.eligible_catalog, normalized_metadata)
        == {key: identities[key] for key in plan.eligible_keys},
        "review_selection_changed_evidence",
    )
    # Exclusion must not strengthen a retained interpretation or lose a peer.
    _require(
        all(
            not (set(scope.source_keys) & eligible)
            or set(scope.source_keys) <= eligible
            for scope in full_scopes
        ),
        "review_cohort_incomplete",
    )
    expected_scopes = [
        scope.context() for scope in full_scopes if set(scope.source_keys) <= eligible
    ]
    selected_scopes = [scope.context() for scope in _scopes(plan.eligible_catalog)]
    _require(
        sorted(map(canonical_json, expected_scopes))
        == sorted(map(canonical_json, selected_scopes)),
        "review_selection_changed_evidence",
    )
    expected_context = [item for item in full_context if item["source_key"] in eligible]
    selected_context = build_finding_detail_context(plan.eligible_catalog)
    _require(
        sorted(map(canonical_json, expected_context))
        == sorted(map(canonical_json, selected_context)),
        "review_selection_changed_evidence",
    )
    return plan


def prepare_source_review(
    articles: Sequence[Mapping[str, Any]], *, advisory: bool = False
) -> SourceReviewPlan:
    _require(
        isinstance(articles, (list, tuple))
        and all(isinstance(article, Mapping) for article in articles),
        "invalid_review_input_catalog",
    )
    try:
        catalog = build_reporting_catalog(articles)
        metadata = {}
        for article in articles:
            key = reporting_key(article.get("link"))
            values = _cve_list(article.get("cves", []))
            _require(
                key not in metadata or metadata[key] == values,
                "conflicting_source_metadata",
            )
            metadata[key] = values
        return plan_reporting_catalog(catalog, metadata, advisory=advisory)
    except ReportingGroundingError:
        raise SourceReviewError("invalid_source_identity") from None


def packet_bytes(packet: dict[str, Any]) -> bytes:
    validate_review_packet(packet)
    return (canonical_json(packet) + "\n").encode()


def _verify_existing_packet(path: Path, data: bytes) -> None:
    _require(not path.is_symlink(), "review_packet_path_invalid")
    descriptor = os.open(path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW)
    with os.fdopen(descriptor, "rb") as stream:
        metadata = os.fstat(stream.fileno())
        _require(stat.S_ISREG(metadata.st_mode), "review_packet_path_invalid")
        _require(
            stat.S_IMODE(metadata.st_mode) == 0o600, "review_packet_permissions_invalid"
        )
        _require(stream.read(MAX_PACKET_BYTES + 1) == data, "review_packet_conflict")
        os.fsync(stream.fileno())


def write_review_packet(packet: dict[str, Any], directory: Path) -> Path:
    """Durably create an immutable, mode-0600 metadata packet, never overwrite."""
    data = packet_bytes(packet)
    path = directory / (packet["plan_id"] + ".json")
    temporary: Path | None = None
    try:
        _require(not directory.is_symlink(), "review_packet_path_invalid")
        directory.mkdir(parents=True, exist_ok=True)
        _require(not path.is_symlink(), "review_packet_path_invalid")
        if path.exists():
            _verify_existing_packet(path, data)
            descriptor = os.open(directory, os.O_RDONLY)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
            return path
        with tempfile.NamedTemporaryFile(
            dir=directory, prefix=".packet-", delete=False
        ) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            _verify_existing_packet(path, data)
        descriptor = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return path
    except OSError:
        raise SourceReviewError("review_packet_persistence_failed") from None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
