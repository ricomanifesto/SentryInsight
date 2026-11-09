"""A read-only export of accepted reports and the findings they state.

The report history store keeps every run's accepted report artifact
immutably, under a digest recorded on the run. This export reads the store
through its export role and, for each succeeded run:

1. reads the artifact's manifest and recomputes the artifact digest from it;
2. reads ``index.md`` and checks its bytes against the manifest;
3. parses it with the report's own artifact parser.

Every finding it emits is therefore one the published report states, tied to
its run, artifact and evidence. Findings are generated report content checked
by the report's validation gate before it was committed, not individually
verified claims, and they are labelled that way. Runs that failed or produced
no artifact are listed with no findings. Nothing is synthesized for them.

    python -m src.control_plane.findings_export --after 0 --out findings.json

``CONTROL_PLANE_URL`` and ``CONTROL_PLANE_TOKEN`` (an export-role token) name
the store. The output is deterministic for the same history: it carries no
wall-clock time.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import quote

import httpx

from src.core.report_artifact import ReportArtifactError, parse_report_artifact
from src.core.report_findings import report_findings
from src.core.reporting import ReportingGroundingError, reporting_fragment

from .projection import Client, ProjectionError, configured_store

SCHEMA = "sentryinsight-findings-export/1"
HISTORY_PAGE = "sentryinsight-export-page/1"
PAGE_LIMIT = 25
MAX_PAGES = 1000
REPORT_FILE = "index.md"
BASIS = "generated_report_finding"
VERIFICATION = "not_individually_verified"
ACCEPTANCE = "committed_report_passed_validation"


class ExportError(Exception):
    """The export cannot be produced truthfully."""


def canonical(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()


def sealed(record: dict[str, Any], field: str) -> dict[str, Any]:
    """The record with ``field`` set to the SHA-256 of the rest of it."""
    return {**record, field: hashlib.sha256(canonical(record)).hexdigest()}


def artifact_digest(files: Sequence[Mapping[str, Any]]) -> str:
    """Path, NUL, file digest and newline per file, in manifest order."""
    text = "".join(f"{f['path']}\0{f['sha256']}\n" for f in files)
    return hashlib.sha256(text.encode()).hexdigest()


def _get(client: Client, path: str) -> httpx.Response:
    response = client.call("GET", path, b"")
    if response.status_code != 200:
        raise ExportError(f"store refused {path.split('?')[0]}: {response.status_code}")
    return response


def history(client: Client, after: int) -> tuple[dict[str, dict], dict[str, dict], int]:
    """The latest version of every run record after ``after``, and the sources."""
    runs: dict[str, dict] = {}
    sources: dict[str, dict] = {}
    cursor = after
    for _ in range(MAX_PAGES):
        page = _get(client, f"/v1/export?after={cursor}&limit={PAGE_LIMIT}").json()
        if page.get("schema") != HISTORY_PAGE:
            raise ExportError("unsupported history page schema")
        for record in page["records"]:
            if record["record_type"] == "source_revision":
                sources[record["record_id"]] = record
            elif record["record_type"] == "run":
                known = runs.get(record["record_id"])
                if known is None or record["record_version"] >= known["record_version"]:
                    runs[record["record_id"]] = record
        cursor = page["next_cursor"]
        if not page["has_more"]:
            return runs, sources, cursor
    raise ExportError("history did not end within the page bound")


def accepted_report(client: Client, artifact_sha: str) -> tuple[str, str]:
    """The artifact's ``index.md`` text and digest, verified against the run."""
    manifest = _get(client, f"/v1/export/artifacts/{artifact_sha}").json()
    files = manifest.get("files") or []
    if (
        manifest.get("artifact_sha256") != artifact_sha
        or artifact_digest(files) != artifact_sha
    ):
        raise ExportError(
            f"artifact {artifact_sha[:12]} manifest does not match its digest"
        )
    listed = {f["path"]: f["sha256"] for f in files}
    if REPORT_FILE not in listed:
        raise LookupError(f"artifact has no {REPORT_FILE}")
    data = _get(
        client, f"/v1/export/artifacts/{artifact_sha}/files/{quote(REPORT_FILE)}"
    ).content
    file_sha = hashlib.sha256(data).hexdigest()
    if file_sha != listed[REPORT_FILE]:
        raise ExportError(
            f"artifact {artifact_sha[:12]} {REPORT_FILE} does not match its manifest"
        )
    return data.decode("utf-8"), file_sha


def _fragment(url: Any) -> str | None:
    try:
        return reporting_fragment(url)
    except ReportingGroundingError:
        return None


def findings(
    text: str, artifact_sha: str
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """The report's own facts and findings: artifact-level, the same for every
    run that recorded this artifact."""
    artifact = parse_report_artifact(text)
    rows = report_findings(text).rows
    if [r.title for r in rows] != [f.title for f in artifact.findings]:
        raise ReportArtifactError("finding table and artifact disagree")
    records = []
    for position, (finding, row) in enumerate(zip(artifact.findings, rows)):
        fields = row.fields()
        citations = [
            {
                "publisher": ref.publisher,
                "title": ref.title,
                "url": ref.url,
                "reporting_fragment": ref.digest_fragment,
            }
            for ref in finding.reporting
        ]
        status = finding.affected_versions_status
        records.append(
            sealed(
                {
                    "finding_key": f"sentryinsight:finding:{artifact_sha}:{finding.slug}",
                    "position": position,
                    "title": finding.title,
                    "slug": finding.slug,
                    "basis": BASIS,
                    "verification": VERIFICATION,
                    "description": fields.get("Description"),
                    "impact": fields.get("Impact"),
                    "status": fields.get("Status"),
                    "severity": finding.severity.value,
                    "exploitation_status": finding.exploitation_status.value,
                    "action": finding.action.value,
                    "cve_ids": list(finding.cve_ids),
                    "affected_versions": finding.affected_versions,
                    "affected_versions_status": status and status.value,
                    "exceptions": finding.exceptions,
                    "recommended_actions": finding.recommended_actions,
                    "vendor_links": list(finding.vendor_links),
                    "citations": citations,
                    "text_sha256": row.sha256,
                },
                "finding_sha256",
            )
        )
    coverage = artifact.source_coverage
    report = {
        "report_schema_version": artifact.schema_version,
        "report_date": artifact.report_date.isoformat(),
        "generated_at": artifact.generated_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "digest_issue_url": artifact.digest_issue_url,
        "finding_count": len(records),
        "source_coverage": (
            None
            if coverage is None
            else {"coverage_id": coverage["coverage_id"], "counts": coverage["counts"]}
        ),
    }
    return report, records


def evidence_links(
    records: Sequence[Mapping[str, Any]], run_sources: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    """This run's link for every citation: its own retained source, or none.

    Links belong to the run, not the finding: runs sharing an artifact can
    retain different revisions of a cited source, or not retain it at all.
    """
    by_fragment = {_fragment(s["canonical_url"]): s for s in run_sources}
    by_fragment.pop(None, None)
    links = []
    for record in records:
        for index, citation in enumerate(record["citations"]):
            source = by_fragment.get(citation["reporting_fragment"])
            links.append(
                {
                    "finding_key": record["finding_key"],
                    "citation": index,
                    "reporting_fragment": citation["reporting_fragment"],
                    "link": "run_source" if source else "not_in_run_sources",
                    "source_record_id": source and source["record_id"],
                    "article_key_sha256": source and source["article_key_sha256"],
                    "content_sha256": source and source["content_sha256"],
                }
            )
    return links


def entry(
    client: Client, run: dict, sources: Mapping[str, dict]
) -> dict[str, Any] | None:
    """One run's export entry, or None for a run still in progress."""
    body = run["run"]
    if body["outcome"] == "in_progress":
        return None
    run_sources = [
        sources[s["source_record_id"]]
        for s in run["sources"]
        if s["source_record_id"] in sources
    ]
    value: dict[str, Any] = {
        "entry_key": f"sentryinsight:report-entry:{body['operation_id']}",
        "run_record_id": run["record_id"],
        "run_record_version": run["record_version"],
        "run_record_sha256": run["record_sha256"],
        "operation_id": body["operation_id"],
        "admission_seq": body["admission_seq"],
        "origin": body["origin"],
        "source_revision": body["source_revision"],
        "source_commit": body["source_commit"],
        "outcome": body["outcome"],
        "reason": body["reason"],
        # Publication is the run's own record: observed or published
        # deployments only. A succeeded run is not thereby published.
        "report_published": run["report_published"],
        "publications": run["publications"],
        "acceptance": None,
        "report": None,
        "findings": [],
        "evidence": [],
        "findings_status": "no_accepted_artifact",
        "findings_note": None,
    }
    artifact = run.get("artifact")
    if body["outcome"] == "succeeded" and artifact:
        value["acceptance"] = ACCEPTANCE
        try:
            text, file_sha = accepted_report(client, artifact["sha256"])
            report, records = findings(text, artifact["sha256"])
        except LookupError as error:
            value["findings_status"], value["findings_note"] = "unavailable", str(error)
        except ReportArtifactError as error:
            value["findings_status"] = "unparseable"
            value["findings_note"] = str(error)[:200]
        else:
            value["report"] = {
                "artifact_sha256": artifact["sha256"],
                "file": REPORT_FILE,
                "file_sha256": file_sha,
                **report,
            }
            value["findings"] = records
            value["evidence"] = evidence_links(records, run_sources)
            value["findings_status"] = "parsed"
    return sealed(value, "entry_sha256")


def build(client: Client, after: int = 0) -> dict[str, Any]:
    runs, sources, cursor = history(client, after)
    ordered = sorted(runs.values(), key=lambda r: r["run"]["admission_seq"])
    entries = [e for e in (entry(client, r, sources) for r in ordered) if e is not None]
    return sealed(
        {
            "schema": SCHEMA,
            "product": "sentryinsight",
            "history": {
                "page_schema": HISTORY_PAGE,
                "after": after,
                "next_cursor": cursor,
            },
            "basis": BASIS,
            "verification": VERIFICATION,
            "entries": entries,
            "skipped_in_progress": len(ordered) - len(entries),
        },
        "export_sha256",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m src.control_plane.findings_export")
    parser.add_argument("--after", type=int, default=0)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    store = configured_store()
    if store is None:
        print(json.dumps({"error": "history store not configured"}), file=sys.stderr)
        return 1
    try:
        with httpx.Client(timeout=30.0) as http:
            document = build(Client(store, http), args.after)
    except (ExportError, ProjectionError, ValueError, KeyError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 1
    args.out.write_bytes(canonical(document) + b"\n")
    print(
        json.dumps(
            {
                "export_sha256": document["export_sha256"],
                "entries": len(document["entries"]),
                "findings": sum(len(e["findings"]) for e in document["entries"]),
                "next_cursor": document["history"]["next_cursor"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
