# Findings export: accepted reports and the findings they state

`python -m src.control_plane.findings_export --after <cursor> --out <file>` writes one JSON document, schema `sentryinsight-findings-export/1`. It is read-only. It runs with `CONTROL_PLANE_URL` and an **export-role** token in `CONTROL_PLANE_TOKEN`, the same principal that reads the research export (`contracts/export.md`).

An example built from real staging history is in `fixtures/findings-export/staging-2026-11-09.json`.

## What it reads, and what it proves

For every run in the research export after `after`:

1. It keeps each run record's highest `record_version`.
2. For a `succeeded` run with an artifact:
   - it reads `GET /v1/export/artifacts/{artifact}`;
   - it recomputes the artifact digest (path, NUL, file SHA-256 and newline per file) and requires it to equal the run's `artifact.sha256`;
   - it reads `index.md` and requires its SHA-256 to equal the manifest's entry.

   Any mismatch stops the export; no unverified content is written.
3. It parses `index.md` with the report's own artifact parser. That is the same parser and grammar the report's validation used before the report was committed.

Nothing is generated, fetched from elsewhere or inferred. A run without an accepted artifact has no findings.

## Document

```json
{
  "schema": "sentryinsight-findings-export/1",
  "product": "sentryinsight",
  "history": {"page_schema": "sentryinsight-export-page/1", "after": 0, "next_cursor": 12},
  "basis": "generated_report_finding",
  "verification": "not_individually_verified",
  "entries": [ /* one per terminal run, in admission order */ ],
  "skipped_in_progress": 0,
  "export_sha256": "<64 hex>"
}
```

### Entry (one per run)

| Field | Meaning |
|---|---|
| `entry_key` | `sentryinsight:report-entry:<operation_id>`; one per run |
| `run_record_id`, `run_record_version`, `run_record_sha256` | the research-export run record this entry was built from |
| `operation_id`, `admission_seq`, `origin`, `source_revision`, `source_commit` | as in the run record |
| `outcome`, `reason` | `succeeded` or `failed`/`incomplete`, with the run's reason |
| `report_published`, `publications` | copied from the run record. A succeeded run is not published until a publication says so |
| `acceptance` | `committed_report_passed_validation` for a succeeded run with an artifact; otherwise `null` |
| `report` | `artifact_sha256`, `file`, `file_sha256`, `report_schema_version`, `report_date`, `generated_at`, `digest_issue_url`, `finding_count`, and `source_coverage` (`coverage_id`, `counts`) for schema-5 reports. `null` without parsed findings |
| `findings_status` | see below |
| `findings_note` | why findings are `unavailable` or `unparseable`; otherwise `null` |
| `findings` | the report's findings in report order; `[]` unless `parsed`. They are artifact-level: identical for every run that recorded this artifact |
| `evidence` | this run's link for every citation of every finding, described below; `[]` unless `parsed` |
| `entry_sha256` | SHA-256 of the entry's canonical JSON without this field |

`findings_status` values:

| Value | Meaning |
|---|---|
| `parsed` | findings were read from the verified artifact |
| `no_accepted_artifact` | the run did not succeed, or recorded no artifact. Nothing is supplied for it |
| `unavailable` | the verified artifact has no `index.md` |
| `unparseable` | `index.md` is not a valid versioned report. The note gives the parser's reason |

### Finding

| Field | Meaning |
|---|---|
| `finding_key` | `sentryinsight:finding:<artifact_sha256>:<slug>`. A finding is a statement in one accepted report; runs that share an artifact share its findings with identical digests |
| `position`, `title`, `slug` | as in the report |
| `basis` | `generated_report_finding`: the report's model-generated content, which passed the report's validation and grounding gate before commit |
| `verification` | `not_individually_verified`: no claim in it was separately verified |
| `description`, `impact`, `status` | the finding's own text fields, verbatim; `null` when absent |
| `severity`, `exploitation_status`, `action`, `cve_ids` | parsed values |
| `affected_versions`, `affected_versions_status`, `exceptions`, `recommended_actions`, `vendor_links` | parsed values |
| `citations` | one per Reporting citation: `publisher`, `title`, `url`, `reporting_fragment` |
| `text_sha256` | SHA-256 of the finding's exact text in `index.md` |
| `finding_sha256` | SHA-256 of the finding's canonical JSON without this field |

### Evidence (per run)

Links belong to the run, not the finding. Runs that share an artifact can retain different revisions of a cited source (a rebuild retains a feed excerpt where the original run fetched the article), or not retain it at all. So links sit on the entry and stay outside `finding_sha256`.

Each evidence entry has:
- `finding_key` and `citation`, the citation's index in that finding's `citations`;
- `reporting_fragment`;
- `link`:
  - `run_source`: a source of this same run, matched by the reporting URL identity. `source_record_id`, `article_key_sha256` and `content_sha256` name its research-export source revision.
  - `not_in_run_sources`: the run did not retain the cited source, for example one its projection bounds dropped. Those three fields are then `null`. A source revision from another run is never substituted.

## Semantics consumers can rely on

- **Identical replay:** the same history gives the same bytes. The document carries no wall-clock time.
- **Changed revision:** a run record whose version advances changes its entry's `run_record_version` and `entry_sha256`. That happens, for example, when a deployment is observed. The run's findings do not change, because the artifact is immutable.
- **Failure and non-publication:** failed runs appear, with no findings. `report_published` is false until a publication is recorded.
- **Conflicting identity:** a `finding_key` names one artifact and one slug, and its `finding_sha256` depends only on that artifact. Runs that share the artifact give identical finding records even when their evidence links differ. Two different `finding_sha256` values for one key would mean the producer's derivation changed; treat that as a conflict, not a new revision.
- **Cursor:** `history.next_cursor` is the research-export cursor. Re-running with `--after` reads only runs changed since. Entries are cumulative per run, so a consumer upserts by `entry_key` and `run_record_version`.
