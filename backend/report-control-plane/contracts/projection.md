# Projection: recording runs the producer completed

A projection pipeline records report runs after the authoritative producer has completed them. The producer, the report workflow, still generates every report and publishes every deployment. This store keeps an immutable, queryable history of what it decided and exports it (`contracts/export.md`). Nothing here generates, retries or publishes a report. If this store is unavailable, the producer's own run and deployment are unaffected.

The caller holds a principal whose only role is `project`. With that role it can upload bytes, record runs and record observed deployments. It cannot admit, publish, operate, read status or read the export.

## Pipeline

`PUT /v1/pipelines/{pipeline}` with `"mode": "project"` (role `operate`) makes a projection pipeline.

- **Admission refused:** `POST /v1/operations` refuses it with `422 pipeline_projection_only`.
- **Publishing refused:** a projected run can't be published through this store (`409 projection_not_publishable`).
- **Execution pipelines unaffected:** without `mode`, a pipeline is `execute`, as before.

## `PUT /v1/projections/blobs/{sha256}`

The body is the raw bytes, at most 8 MiB. They are stored once under their own digest.

| Response | Meaning |
|---|---|
| `201` | stored |
| `200` | already stored |
| `422 blob_digest_mismatch` | the bytes do not hash to the path |
| `409 blob_conflict` | an object under that digest holds other bytes |

## `POST /v1/projections`

The body is strict JSON, at most 64 KiB:

```json
{
  "schema": "report-control-plane/projection/1",
  "pipeline": "reports",
  "policy_id": "production",
  "source_revision": "actions:<run id>:<attempt>",
  "snapshot_sha256": "<an uploaded blob>",
  "run": {
    "execution_id": "actions-run-<run id>-<attempt>",
    "source_commit": "<40 hex> | null",
    "outcome": "succeeded | failed",
    "reason": "<token> | null",
    "source_outcomes": {"<link>": "executed | filtered | review_required | source_rejected", "…": "…"} | null
  },
  "artifact": {"files": [{"path": "index.md", "sha256": "<an uploaded blob>", "bytes": 1234}]} | null
}
```

**The snapshot:**
- It is an admission body (`report-control-plane/admission/1`) naming the same pipeline, policy and source revision.
- It is parsed with projection bounds: 1 to 100 articles, at most 256 KiB of content each, at most 8 MiB in total.
- Articles may carry `published_at`, the producer's own publication time in UTC RFC 3339.
- As with an admission, `operation_id = sha256("report-control-plane/1\n" + pipeline + "\n" + policy_id + "\n" + snapshot_sha256)`.

**The run:**
- A `succeeded` run names its `source_commit` and an artifact, and has no `reason`.
- A `failed` run names a `reason`, has no artifact and reports no source outcomes.
- `source_outcomes`, when reported, names every snapshot link exactly once: `executed` when the source was given to the model, otherwise the reason it was not (`filtered`, `review_required`, `source_rejected`). `null` means the producer did not establish them, and the export then says `not_reported`.
- No run-completion time is accepted. The store records when it recorded the run; it does not claim when the producer's run completed.

**The artifact:** the listing follows the artifact rules in `contracts/execution-service.md`: path grammar, segment order, sizes and the digest over path, NUL, file digest and newline. Every part must be an uploaded blob of the listed length.

**Processing:**
1. The Worker re-verifies the snapshot and every part.
2. It stores them immutably at `snapshots/<sha256>` and `artifacts/<digest>/`.
3. It writes the run, its articles and outcomes, its artifact row and an audit event in one D1 batch.

**Responses:**

| Response | Meaning |
|---|---|
| `201` | recorded |
| `200` | the same run was already recorded; nothing changes |
| `409 projection_conflict` | the operation exists with another fact record |
| `409 source_revision_conflict` | the label names other bytes. The refusal is recorded as an identity conflict on the existing run |
| `409 blob_missing`, `409 blob_mismatch` | an uploaded blob is missing or does not match |
| `422 <reason>` | the request or the snapshot is invalid. A snapshot refusal is prefixed `snapshot_` |

**Retry:** an interrupted projection is retried with the same request. Uploaded blobs are reused, and the batch either recorded the run or did not.

**Run identity:** the strictly parsed request is the run's complete fact record. Every object in it is checked for exact keys, so nothing else can be accepted. The store keeps `facts_sha256 = sha256("report-control-plane/projection-facts/1\n" + canonical JSON of the request)`, with object keys sorted at every level and arrays in their validated order. A repeated projection is the same run only when this digest is equal; any difference in any field, including a reason or one source's outcome, is `409 projection_conflict`. A field added to the request later is in the digest by construction.

## `POST /v1/projections/publications`

```json
{"schema": "report-control-plane/publication-observation/1", "pipeline": "reports", "source_commit": "<40 hex>", "target": "production", "observed_at": "<RFC 3339>"}
```

This records that the producer's deployment of a source commit completed.

- **Kept once:** the first observation of each `(pipeline, source_commit, target)` is kept.
- **Attached in either order:** it attaches a `published` publication to every completed projected run of that commit, whichever of the two arrives second. Each run gets its own publication, identified by target and operation.
- **Scoped to its run:** an observation is never shared through an artifact. A run of another commit with identical report bytes does not become published by it, and its record does not change.
- **Responses:** `200` when it attached to at least one run; `202` when it is stored and waiting for its run.
- **Commits without a report:** a deployment of such a commit stays an unattached observation.

## SentryInsight producer

The report workflow runs `python -m src.control_plane.projection` with `CONTROL_PLANE_URL` and `CONTROL_PLANE_TOKEN`. Without them every command skips and exits 0.

| Command | Where it runs | What it does |
|---|---|---|
| `run` | `generate-report`, after the outcome is recorded | `main.py` writes a run-local snapshot (`SENTRYINSIGHT_PROJECTION_SNAPSHOT`) holding every eligible article it read, with its full text and feed publication time, and each source's outcome. Outcomes come from the source-review plan the model used, matched to sources by the product's reporting URL identity, and only when the run generated its report: report generation refuses to proceed unless that plan equals the analysis's plan and one rebuilt from the filtered articles. A plan alone is not evidence, because analysis can stop after building it and before calling the model; such runs report `null`. The snapshot stays in the runner. A `published` run records the committed report: `index.md`, `current-findings.json` and the dated `reports/<date>.md`. `failed` and `cancelled` record a failure with its reason. Other outcomes record nothing |
| `observe-serving` | `record-report-history.yml`, after Publish Production succeeds and daily, with read-only repository access | reads the release descriptor the production origin serves (`_release/descriptor.json`), checks that it names this repository and origin, and records its source commit for the target `production` |
| `rebuild --commit <sha>` | operator replay | re-projects a report commit whose `Admission-Feed` trailer names a commit-addressed feed snapshot. Evidence is feed level (`content_kind: feed`): each source's text is the feed item's content, else its description, the same fallback the report's own enrichment uses. The executed set is unreported. A commit without a retained feed is refused (`feed_not_retained`) and stays a coverage gap |

Every upload is content-addressed and every write idempotent, so a repeated command changes nothing.
