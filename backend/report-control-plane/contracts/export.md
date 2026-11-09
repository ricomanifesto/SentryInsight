# Research export, `sentryinsight-export/1`

A bounded, read-only change feed over this store's history, for downstream consumers such as a newsletter backend. The export never writes. Its consumer holds a principal whose only role is `export`, so it can read the export and nothing else: it cannot admit, publish, operate, or read operation status or artifacts.

The export reports history. It is not a publication, and it is not a sent newsletter. A run whose artifact was verified is `succeeded`. It is a published report only when one of its publications is `published`.

## Routes

| Route | Effect |
|---|---|
| `GET /v1/export?after=<cursor>&limit=<runs>` | the next page of records after `cursor` |
| `GET /v1/export/sources/{snapshot_sha256}/{position}` | one retained article's text from an admitted snapshot |

**Query bounds:**
- `after` is a non-negative integer, `0` by default.
- `limit` is 1 to 25 runs, 10 by default.
- Any other parameter, a repeated parameter, or a non-decimal value is refused with `422 export_query_invalid`, before any read.

**Bearer token:** both routes require it. A missing or unknown token is `401`, and another role is `403`.

## Paging and the cursor

The cursor is an id in the store's change log. Database triggers write a change row in the same statement as every change a run record reflects: its operation, its publications, its identity conflicts and its per-article outcomes. A change therefore cannot be committed without moving past every earlier cursor. A page names the runs changed after `after`, in change order, up to `limit` runs. It scans at most 2,000 changes. `next_cursor` is the last change it accounted for, and `has_more` says whether to call again. `after=0` is a deliberate full backfill. A later cursor gives a bounded incremental read.

A page carries the source records of each run it names, then the run record. A source record already sent in the same page is not repeated. A record from an earlier page may be sent again.

```json
{
  "schema": "sentryinsight-export-page/1",
  "product": "sentryinsight",
  "after": 0,
  "next_cursor": 42,
  "has_more": false,
  "coverage": {
    "earliest_admitted_at": "2026-11-08T00:00:00.000Z",
    "gaps": [{"kind": "before_first_admission", "until": "2026-11-08T00:00:00.000Z", "detail": "history before this store's first admission is not captured"}]
  },
  "records": []
}
```

No snapshot is invented for history before the first admission. That gap is declared on every page.

## Consumer rules

- **Upsert by `record_id`.** A record with a `record_sha256` you already hold is a replay: change nothing.
- **Source records are immutable.** One `record_id` always carries the same content.
- **Run records are versioned.** Each run is read in one D1 batch, a single transaction. `record_version` is the newest change id for that run, and every change to its content writes a new one atomically. Equal versions therefore carry equal content. Never replace a run with a lower `record_version`. A version can also advance without visible change, for example on an internal retry.

## `source_revision` record

One admitted article revision. A change to the article's content under the same URL is a new record, which names its predecessor. Revision order is commit order, not the Worker clock, so a record's `revision` and `independence` never change after it is written.

```json
{
  "schema": "sentryinsight-export/1",
  "record_type": "source_revision",
  "record_id": "sentryinsight:source:<sha256(url)>:<content sha256>",
  "product": "sentryinsight",
  "canonical_url": "https://…",
  "article_key_sha256": "<sha256(url)>",
  "publisher": "Example Vendor",
  "title": "…",
  "content_sha256": "<sha256 of the content's UTF-8 bytes>",
  "revision": {"index": 2, "previous_content_sha256": "<64 hex> | null"},
  "evidence": {
    "kind": "full_text | excerpt | metadata_only | unspecified",
    "content_kind": "article | feed | other | null",
    "content_bytes": 61,
    "retained": {"snapshot_sha256": "<64 hex>", "position": 0, "fetch": "/v1/export/sources/<64 hex>/0"}
  },
  "times": {"published_at": null, "captured_at": "2026-11-08T00:00:00.000Z"},
  "first_seen_run_id": "sentryinsight:run:<operation id>",
  "independence": {"status": "first_seen | duplicate_content | not_applicable", "same_content_first_url": "https://… | null"},
  "record_sha256": "<sha256 of this record without record_sha256>"
}
```

**`evidence.kind`:**

| Kind | Meaning |
|---|---|
| `full_text` | the product labelled the record `article`, a fetched page |
| `excerpt` | labelled `feed`, the feed's own text |
| `metadata_only` | the content was empty; `retained` is `null` |
| `unspecified` | no known label. The text is still retained; nothing is guessed |

**Retained text:** `retained` locates the text in an admitted snapshot. A digest alone is not the text. The text is read with the `fetch` route.

**Times:** `published_at` is the producer's own publication time for the article, in UTC RFC 3339, when the producer supplied one, and `null` otherwise. For SentryInsight runs it is the source feed's item date; nothing fills a missing time. `captured_at` is when this store first recorded the revision.

**Independence:** identical text under another URL is `duplicate_content` and names the first URL seen with it. Such a copy is one source seen twice, not corroboration. Paraphrased syndication is not detected. Metadata-only records carry no text, so they are `not_applicable`.

## `run` record

One admitted operation: a report run over an immutable snapshot of source records.

```json
{
  "schema": "sentryinsight-export/1",
  "record_type": "run",
  "record_id": "sentryinsight:run:<operation id>",
  "record_version": 37,
  "product": "sentryinsight",
  "pipeline": "reports",
  "policy_id": "standard",
  "run": {
    "operation_id": "<64 hex>",
    "origin": "execute | project",
    "source_commit": "<40 hex> | null",
    "admission_seq": 3,
    "source_revision": "caller-label-1",
    "snapshot_sha256": "<64 hex>",
    "admitted_at": "2026-11-08T00:00:00.000Z",
    "outcome": "in_progress | succeeded | failed | incomplete",
    "reason": "<fixed token> | null",
    "execution": {"execution_id": "…", "run_id": "…", "run_state": "succeeded | failed | null", "run_reason": null, "attempts": {"used": 1, "limit": 3}}
  },
  "sources": [{"source_record_id": "sentryinsight:source:…", "position": 0, "outcome": "executed | excluded | not_reported"}],
  "artifact": {"sha256": "<64 hex>", "manifest_sha256": "<64 hex>", "file_count": 3, "total_bytes": 1234, "verified_at": "…"},
  "publications": [{"target": "site", "publication_id": "<64 hex>", "state": "pending | uncertain | published | refused | refused_by_publisher", "reason": null, "observed_at": "<RFC 3339> | null"}],
  "report_published": true,
  "identity_conflicts": [{"source_revision": "caller-label-1", "refused_snapshot_sha256": "<64 hex>", "observed_at": "…"}],
  "derived_claims": {"status": "not_exported", "reason": "artifact_not_interpreted"},
  "record_sha256": "<64 hex>"
}
```

**`run.outcome`:**

| Outcome | Meaning |
|---|---|
| `succeeded` | a verified artifact is stored. It is not by itself a published report |
| `failed` | terminal. `reason` names it, for example `snapshot_unavailable`, `artifact_rejected` or the execution side's own token |
| `incomplete` | delivery was exhausted before execution. An operator may retry it |
| `in_progress` | anything before a terminal state |

**`run.origin`:** `execute` runs were handed to the execution service by this store. `project` runs were completed by the authoritative producer and recorded afterwards (`contracts/projection.md`). For those, `source_commit` is the report commit the producer published, and `execution.execution_id` names the producer's own run.

**`run.execution`:** `run_state`, `run_reason` and `attempts` are given only once the run is terminal.

**`sources[].outcome`:** `excluded` means the execution side left the record out by its policy. `not_reported` applies to any run that did not succeed, and to a run that completed before migration `0003` recorded per-article outcomes.

**`publications`:**
- Only this operation's own publications are listed. Operations that converge on one artifact share its publications, which belong to the first operation that published it. A consumer can join runs by `artifact.sha256`.
- An intent that was never claimed is not listed.
- `uncertain` means the effect has not been observed yet.
- `observed_at` is set for a projected run's publication: the time its producer's deployment was observed to complete. A publication made through this store's publisher has `null`.
- Which publication is a target's current last-good depends on other runs, so it is not part of this record. Among a target's published runs, the higher `admission_seq` is the newer.

**`identity_conflicts`:** a later admission that reused this run's `source_revision` label with different bytes. It was refused, and its bytes are retained under `refused_snapshot_sha256`, readable with the `fetch` route. When the label was reused under another policy, the refused snapshot can equal this run's own. At most 50 are listed.

**`derived_claims`:** generated findings live inside the report artifact, which this store verifies by digest but does not interpret. Claim-level provenance is not exported in v1.

**Excluded from every record:** principals, tokens, claim tokens, publisher receipts, bindings, upstream messages and operational telemetry. The store holds no subscriber identities or private messages.

## `GET /v1/export/sources/{snapshot}/{position}`

The snapshot, either an admitted one or the refused bytes of a recorded identity conflict, is read from R2. Its digest is recomputed before any byte is returned. `content_kind` is normalized the same way as at admission.

| Response | Meaning |
|---|---|
| `200` | `{"schema": "sentryinsight-export-source/1", "snapshot_sha256", "position", "canonical_url", "content_sha256", "content_kind", "content"}` |
| `404 not_found` | unknown snapshot or position |
| `404 retained_content_unavailable` | the snapshot row exists but its object is missing |
| `409 retained_content_mismatch` | the object's bytes do not match its digest |
| `409 retained_content_malformed` | the object is not a snapshot |
