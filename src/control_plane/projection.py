"""Project completed report runs into the report history store.

The report workflow and its published commit stay the authority for
generation and publication. This client records what they already decided,
after the fact, through the control plane's ``project`` role:

- ``run`` projects the run that just finished from its run snapshot and the
  report files it committed;
- ``observe`` records that a deployment of a source commit completed;
- ``rebuild`` re-projects an earlier report commit whose feed snapshot was
  retained at a commit-addressed URL, with feed-level evidence only.

Every upload is content-addressed and every write idempotent, so a retry or a
replay of the same run changes nothing. With no store configured the commands
skip and exit successfully; they never change a run's outcome.

    python -m src.control_plane.projection run --snapshot PATH --source-commit SHA \\
        --run-id ID --run-attempt N --outcome published
"""

from __future__ import annotations

import argparse
import asyncio
import dataclasses
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

import httpx

from .admission import (
    PROJECTION_LIMITS,
    AdmissionRefused,
    admission_body,
    expected_identity,
)
from .run_snapshot import SCHEMA as SNAPSHOT_SCHEMA, build_run_snapshot

PROJECTION_SCHEMA = "report-control-plane/projection/1"
OBSERVATION_SCHEMA = "report-control-plane/publication-observation/1"
DEFAULT_PIPELINE = "reports"
DEFAULT_POLICY = "production"
URL_ENV = "CONTROL_PLANE_URL"
TOKEN_ENV = "CONTROL_PLANE_TOKEN"
MAX_FILE_BYTES = 4 * 1024 * 1024
RETRY_DELAYS = (2.0, 8.0)
# Report outcomes from the workflow; only these two leave a run to record.
OUTCOMES = {"published": "succeeded", "failed": "failed", "cancelled": "failed"}


class ProjectionError(Exception):
    """The projection was refused or could not be delivered."""


@dataclasses.dataclass(frozen=True)
class Store:
    url: str
    token: str


def configured_store(environ: Mapping[str, str] = os.environ) -> Store | None:
    url, token = environ.get(URL_ENV, "").strip(), environ.get(TOKEN_ENV, "").strip()
    return Store(url.rstrip("/"), token) if url and token else None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _segments_key(path: str) -> list[str]:
    return path.split("/")


def report_files(root: Path, read: Callable[[str], bytes | None]) -> dict[str, bytes]:
    """The run's report: the canonical report, its machine summary and its dated copy."""
    files: dict[str, bytes] = {}
    for path in ("index.md", "current-findings.json"):
        data = read(path)
        if data is not None:
            files[path] = data
    summary = files.get("current-findings.json")
    if summary is not None:
        date = json.loads(summary).get("report_date")
        if isinstance(date, str) and len(date) == 10:
            dated = read(f"reports/{date}.md")
            if dated is not None:
                files[f"reports/{date}.md"] = dated
    for path, data in files.items():
        if len(data) > MAX_FILE_BYTES:
            raise ProjectionError(f"report file too large: {path}")
    return files


def projection_request(
    *,
    snapshot: bytes,
    files: Mapping[str, bytes] | None,
    pipeline: str,
    policy_id: str,
    source_revision: str,
    execution_id: str,
    source_commit: str | None,
    outcome: str,
    reason: str | None,
    executed_links: Sequence[str] | None,
    completed_at: str | None,
) -> dict[str, Any]:
    listing = None
    if files is not None:
        listing = sorted(
            (
                {"path": path, "sha256": sha256(data), "bytes": len(data)}
                for path, data in files.items()
            ),
            key=lambda f: _segments_key(f["path"]),
        )
    return {
        "schema": PROJECTION_SCHEMA,
        "pipeline": pipeline,
        "policy_id": policy_id,
        "source_revision": source_revision,
        "snapshot_sha256": sha256(snapshot),
        "run": {
            "execution_id": execution_id,
            "source_commit": source_commit,
            "outcome": outcome,
            "reason": reason,
            "executed_links": (
                None if executed_links is None else list(executed_links)
            ),
            "completed_at": completed_at,
        },
        "artifact": None if listing is None else {"files": listing},
    }


class Client:
    """Bearer calls with bounded retries for transient failures only."""

    def __init__(
        self,
        store: Store,
        http: httpx.Client,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.store, self.http, self.sleep = store, http, sleep

    def call(self, method: str, path: str, content: bytes) -> httpx.Response:
        headers = {"authorization": f"Bearer {self.store.token}"}
        for delay in (*RETRY_DELAYS, None):
            try:
                response = self.http.request(
                    method, f"{self.store.url}{path}", content=content, headers=headers
                )
            except httpx.HTTPError:
                response = None
            if response is not None and response.status_code < 500:
                return response
            if delay is None:
                status = "transport" if response is None else response.status_code
                raise ProjectionError(f"store unavailable: {status}")
            self.sleep(delay)
        raise AssertionError("unreachable")

    def upload(self, data: bytes) -> None:
        response = self.call("PUT", f"/v1/projections/blobs/{sha256(data)}", data)
        if response.status_code not in (200, 201):
            raise ProjectionError(f"upload refused: {_reason(response)}")

    def project(
        self, snapshot: bytes, files: Mapping[str, bytes] | None, request: dict
    ) -> dict[str, Any]:
        self.upload(snapshot)
        for data in (files or {}).values():
            self.upload(data)
        body = json.dumps(request, separators=(",", ":")).encode()
        response = self.call("POST", "/v1/projections", body)
        if response.status_code not in (200, 201):
            raise ProjectionError(f"projection refused: {_reason(response)}")
        _, operation_id = expected_identity(
            snapshot, request["pipeline"], request["policy_id"]
        )
        operation = response.json().get("operation", {})
        if operation.get("operation_id") != operation_id:
            raise ProjectionError("projection named another operation")
        return {
            "operation_id": operation_id,
            "created": response.status_code == 201,
            "state": operation.get("state"),
        }

    def observe(
        self, pipeline: str, source_commit: str, target: str, observed_at: str
    ) -> dict[str, Any]:
        body = json.dumps(
            {
                "schema": OBSERVATION_SCHEMA,
                "pipeline": pipeline,
                "source_commit": source_commit,
                "target": target,
                "observed_at": observed_at,
            },
            separators=(",", ":"),
        ).encode()
        response = self.call("POST", "/v1/projections/publications", body)
        if response.status_code not in (200, 202):
            raise ProjectionError(f"observation refused: {_reason(response)}")
        return response.json()


def _reason(response: httpx.Response) -> str:
    try:
        value = response.json()
    except ValueError:
        return f"http_{response.status_code}"
    return str(value.get("error", f"http_{response.status_code}"))


def now_rfc3339() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan_run(
    run_snapshot: Mapping[str, Any],
    *,
    workflow_outcome: str,
    run_id: str,
    run_attempt: str,
    source_commit: str | None,
    files: Mapping[str, bytes] | None,
    pipeline: str = DEFAULT_PIPELINE,
    policy_id: str = DEFAULT_POLICY,
    completed_at: str | None = None,
) -> tuple[bytes, Mapping[str, bytes] | None, dict[str, Any]] | None:
    """The snapshot bytes, files and request for a finished run, or None to skip."""
    if run_snapshot.get("schema") != SNAPSHOT_SCHEMA:
        raise ProjectionError("run snapshot schema unsupported")
    outcome = OUTCOMES.get(workflow_outcome)
    if outcome is None or not run_snapshot.get("articles"):
        return None
    source_revision = f"actions:{run_id}:{run_attempt}"
    try:
        snapshot = admission_body(
            run_snapshot["articles"],
            pipeline=pipeline,
            policy_id=policy_id,
            source_revision=source_revision,
            limits=PROJECTION_LIMITS,
        )
    except AdmissionRefused as error:
        raise ProjectionError(f"snapshot refused: {error.reason}") from error
    succeeded = outcome == "succeeded"
    if succeeded and (not files or not source_commit):
        raise ProjectionError("a published run needs its commit and report files")
    codes = run_snapshot.get("failure_codes") or []
    reason = None
    if not succeeded:
        reason = (
            "generation_cancelled"
            if workflow_outcome == "cancelled"
            else (codes[0] if codes else "generation_failed")
        )
    request = projection_request(
        snapshot=snapshot,
        files=files if succeeded else None,
        pipeline=pipeline,
        policy_id=policy_id,
        source_revision=source_revision,
        execution_id=f"actions-run-{run_id}-{run_attempt}",
        source_commit=source_commit if succeeded else None,
        outcome=outcome,
        reason=reason,
        executed_links=run_snapshot.get("analyzed_links") if succeeded else None,
        completed_at=completed_at,
    )
    return snapshot, files if succeeded else None, request


def feed_from_message(message: str) -> str | None:
    """The commit-addressed feed a report commit was admitted from, if retained."""
    for line in message.splitlines():
        if line.startswith("Admission-Feed: "):
            value = line.removeprefix("Admission-Feed: ").strip()
            return (
                value
                if value.startswith("https://raw.githubusercontent.com/")
                else None
            )
    return None


def _git(root: Path, *args: str) -> bytes | None:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, check=False
    )
    return result.stdout if result.returncode == 0 else None


async def _feed_articles(feed_url: str) -> list[dict[str, Any]]:
    from src.services.article_content import normalize_feed_content
    from src.services.fetch import SentryDigestFeedClient

    articles = await SentryDigestFeedClient(feed_url).fetch_articles()
    for article in articles:
        article["content"] = normalize_feed_content(article.get("content")) or ""
        article["content_kind"] = "feed"
    return articles


def plan_rebuild(
    root: Path, commit: str, feed_articles: Callable[[str], list[dict]]
) -> tuple[bytes, Mapping[str, bytes], dict[str, Any]]:
    message = _git(root, "log", "-1", "--format=%B", commit)
    if message is None:
        raise ProjectionError("commit not found")
    feed = feed_from_message(message.decode())
    if feed is None:
        raise ProjectionError("feed_not_retained")
    full = (_git(root, "rev-parse", commit) or b"").decode().strip()
    files = report_files(root, lambda path: _git(root, "show", f"{full}:{path}"))
    if "index.md" not in files:
        raise ProjectionError("commit has no report")
    snapshot_state = {"articles": feed_articles(feed), "filtered_articles": None}
    run_snapshot = build_run_snapshot(snapshot_state)
    source_revision = f"rebuild:{full}"
    snapshot = admission_body(
        run_snapshot["articles"],
        pipeline=DEFAULT_PIPELINE,
        policy_id=DEFAULT_POLICY,
        source_revision=source_revision,
        limits=PROJECTION_LIMITS,
    )
    request = projection_request(
        snapshot=snapshot,
        files=files,
        pipeline=DEFAULT_PIPELINE,
        policy_id=DEFAULT_POLICY,
        source_revision=source_revision,
        execution_id=f"rebuild-{full[:12]}",
        source_commit=full,
        outcome="succeeded",
        reason=None,
        executed_links=None,
        completed_at=None,
    )
    return snapshot, files, request


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m src.control_plane.projection")
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run", help="Project the run that just finished")
    run.add_argument("--snapshot", type=Path, required=True)
    run.add_argument("--report-root", type=Path, default=Path("."))
    run.add_argument("--source-commit", default=None)
    run.add_argument("--run-id", required=True)
    run.add_argument("--run-attempt", required=True)
    run.add_argument("--outcome", required=True)
    observe = commands.add_parser("observe", help="Record a completed deployment")
    observe.add_argument("--source-commit", required=True)
    observe.add_argument("--target", default="github-pages")
    observe.add_argument("--observed-at", default=None)
    rebuild = commands.add_parser(
        "rebuild", help="Re-project a report commit from its retained feed snapshot"
    )
    rebuild.add_argument("--commit", required=True)
    rebuild.add_argument("--repo", type=Path, default=Path("."))
    args = parser.parse_args(argv)

    store = configured_store()
    if store is None:
        print(json.dumps({"skipped": "history store not configured"}))
        return 0
    try:
        with httpx.Client(timeout=30.0) as http:
            client = Client(store, http)
            if args.command == "observe":
                result = client.observe(
                    DEFAULT_PIPELINE,
                    args.source_commit,
                    args.target,
                    args.observed_at or now_rfc3339(),
                )
            elif args.command == "run":
                if not args.snapshot.is_file():
                    print(json.dumps({"skipped": "no run snapshot"}))
                    return 0
                run_snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
                root = args.report_root

                def read(path: str) -> bytes | None:
                    file = root / path
                    return file.read_bytes() if file.is_file() else None

                files = (
                    report_files(root, read) if args.outcome == "published" else None
                )
                planned = plan_run(
                    run_snapshot,
                    workflow_outcome=args.outcome,
                    run_id=args.run_id,
                    run_attempt=args.run_attempt,
                    source_commit=args.source_commit,
                    files=files,
                    completed_at=now_rfc3339(),
                )
                if planned is None:
                    print(
                        json.dumps(
                            {"skipped": f"nothing to project for {args.outcome}"}
                        )
                    )
                    return 0
                result = client.project(*planned)
                result["dropped_articles"] = run_snapshot.get("dropped_articles", 0)
            else:
                snapshot, files, request = plan_rebuild(
                    args.repo,
                    args.commit,
                    lambda url: asyncio.run(_feed_articles(url)),
                )
                result = client.project(snapshot, files, request)
    except (ProjectionError, AdmissionRefused, OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
