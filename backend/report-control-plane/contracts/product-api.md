# Product API, `v1` (local use; the version may change before any consumer)

Every route except `/healthz` takes `Authorization: Bearer <token>`. Callers are verified against SHA-256 digests before any storage or queue call.

**Roles:**
- `admit`: submit, retry and stage sources;
- `read`: status, targets and artifacts;
- `publish`: publish operations;
- `operate`: set pipelines and schedules, and run the sweeper;
- `export`: the research export only (`contracts/export.md`);
- `project`: projection uploads, runs and observations only (`contracts/projection.md`).

**Responses:** refusals are `{"error": "<token>"}`. Status responses carry states, versions, ids, digests, counts and fixed reason tokens, never paths, hosts or upstream messages.

| Route | Role | Effect |
|---|---|---|
| `POST /v1/operations` | admit | admit a request (below); `201` new, `200` identical repeat, `409 source_revision_conflict`, `422 <reason>`, `413` |
| `GET /v1/operations/{id}` | read | operation, its publications and their targets' last-good |
| `POST /v1/operations/{id}/publish` | publish | body `{"target"}`; `200` published, `202` in progress or unresolved, `409` refused or held |
| `POST /v1/operations/{id}/retry` | admit | from `dead_letter` only: a new delivery generation, at most 3 rounds |
| `POST /v1/reconcile` | operate | run the sweeper once |
| `GET /v1/targets/{target}` | read | last-good publication of a target |
| `GET /v1/artifacts/{sha256}` | read | the verified artifact manifest |
| `GET /v1/artifacts/{sha256}/files/{path}` | read | one verified artifact file |
| `PUT /v1/pipelines/{pipeline}` | operate | `{"policy_id", "binding_id", "state": "active" or "retired", "mode": "execute" (default) or "project"}` |
| `PUT /v1/schedules/{id}` | operate | `{"pipeline", "policy_id", "state": "active" or "paused"}` |
| `PUT /v1/schedules/{id}/sources` | admit | stage a source bundle for the next scheduled admission |
| `PUT /v1/projections/blobs/{sha256}` | project | upload immutable bytes |
| `POST /v1/projections` | project | record a completed run |
| `POST /v1/projections/publications` | project | record an observed deployment |
| `GET /v1/export` | export | a page of the research export, `?after=<cursor>&limit=<1..25>` |
| `GET /v1/export/sources/{snapshot}/{position}` | export | one retained article's text, re-verified |

## Configuration

`EXECUTION_URL` with `EXECUTION_TOKEN`, and `PUBLISHER_URL` with `PUBLISHER_TOKEN`, are optional pairs.

- **Unset pair:** with neither variable set, that dependency is unconfigured. Admission into an execution pipeline and manual retry answer `503 execution_unconfigured`, and publishing answers `503 publisher_unconfigured`, before any write. The sweeper skips sends, pulls and publication repair. Projection, reads and the export serve.
- **Half-set pair:** one variable of a pair without the other is invalid (`503 config_invalid`).

The admission queue and its dead-letter queue are named by `ADMISSIONS_QUEUE_NAME` (default `report-admissions`) and `DEAD_LETTER_QUEUE_NAME` (default `report-admissions-dead`). Each must be 1 to 63 lowercase letters, digits and hyphens, starting and ending with a letter or digit, and the two must differ. With an invalid name, every authenticated route answers `503 config_invalid` before any write, and no Queue or scheduled work is done. Messages are dispatched by these names only; a batch from any other queue is retried, never handled.

## Admission request

At most 1 MiB, strict JSON. Duplicate keys and unknown fields are refused, and so is any string that is not valid Unicode text, such as an escaped unpaired surrogate (`\ud800`): such a string has no UTF-8 encoding, so it could not be hashed or forwarded without rewriting it.

```json
{
  "schema": "report-control-plane/admission/1",
  "pipeline": "reports",
  "policy_id": "standard",
  "source_revision": "caller-label-1",
  "articles": [{"title": "...", "link": "https://...", "source": "...", "content": "..."}]
}
```

**Article bounds:**
- 1 to 100 articles;
- `link` (the article key): `http(s)`, at most 2,048 characters, unique within a request;
- `title`: at most 512 characters;
- `source`: at most 256 characters;
- `content`: at most 64 KiB;
- each record's ASCII-escaped JSON encoding: at most 64 KiB;
- optional fields: `summary`, `content_kind`, `source_links`, `cves` and `published_at` (the producer's publication time, RFC 3339 UTC, for example `2026-11-08T15:43:08Z`).

**Identities:**
- **Snapshot:** `fingerprint = sha256(request bytes)`. The bytes are stored once at `snapshots/<fingerprint>`.
- **Operation:** `operation_id = sha256("report-control-plane/1\n" + pipeline + "\n" + policy_id + "\n" + fingerprint)`. Identical bytes are one operation.
- **Source revision:** a label reused with different bytes is a conflict. The refusal records one `identity_conflicts` row per distinct refused snapshot, plus one `identity_conflict` event on the existing operation; the refused bytes stay in R2 and the existing operation is unchanged.
- **Article metadata:** written in the same batch as the operation. `article_revisions(article_key, content_sha256)` rows are immutable and keep the record's `content_kind` (`feed`, `article`, `other` or absent) and content length. When an operation completes, each of its articles is marked executed or excluded as the execution receipt reports.

## Scheduled admission

A source bundle is `{"schema": "report-control-plane/source-bundle/1", "articles": [...]}`. When the cron fires, each active schedule with a newly staged bundle is admitted through the same path with principal `scheduler`, source revision `schedule:<id>:<bundle sha256>` and fingerprint = the bundle's SHA-256. A refire is the same operation. Each sweep reads at most 20 schedules, resuming after the last one it read and wrapping to the start (the cursor is stored in D1), so schedules whose admission keeps failing cannot starve a newer one; the status pull and publication repair rotate the same way. One staged bundle may be admitted by several schedules on different pipelines: the snapshot row and object are shared, and each pipeline gets its own operation and binding.

## Operation states

`admitted` → `enqueued` → `submitting` (a durable claim) → `submitted` → `completed` or `failed`.

An `admitted`, `enqueued` or `submitting` operation can also move to `dead_letter`, and a manual retry returns it to `admitted`.

Messages carry `{operation_id, generation}`. A message whose generation is not the row's current one is acknowledged as stale.
