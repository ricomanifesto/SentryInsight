# Execution service contract

The control plane hands an admitted operation to an execution service and later pulls its outcome. The control plane never writes to the service's stores, and the service never writes to the control plane's. Every call carries `Authorization: Bearer <token>`, and every response is bounded and parsed strictly; an unknown or malformed field fails closed.

## `POST /executions`

Body: the snapshot bytes exactly as admitted. A record may carry `published_at`, the producer's own publication time in RFC 3339 UTC. The service may use it or ignore it, but it must not refuse a snapshot because of it. Headers:

| Header | Value |
|---|---|
| `X-Operation-Id` | the 64-hex operation id |
| `X-Snapshot-Sha256` | SHA-256 of the body |
| `X-Binding-Id` | the operation's 64-hex pipeline binding |

The call is idempotent per operation and binding, including when an earlier call for the same operation is still in progress. The service admits at most one execution per immutable operation, and repeats return the same identifiers. Byte-identical source records under one binding may converge on one execution.

- **`2xx`:** `{"operation_id", "execution_id", "run_id", "binding_id", "state"}`, where `binding_id` echoes the request.
- **Terminal refusal:** a `4xx` with `{"reason": "<token>", "terminal": true}`. Reasons include `binding_mismatch`, for a binding the service does not serve; `snapshot_invalid`; `empty_source_set`; and `effective_config_invalid`. No execution is created.
- **Anything else:** transient. The control plane releases its claim and retries the delivery later. A timeout does not prove that no execution was created; idempotency makes the retry safe.

## `GET /executions/{operation_id}`

The read carries `X-Snapshot-Sha256` and `X-Binding-Id`, the operation's recorded snapshot digest and binding, so a service that lost its own operation mapping can rebuild it from bytes it already received, without creating an execution. The control plane still requires the receipt's `execution_id` and `binding_id` to equal its own recorded values.

The execution receipt, `200`, or `404` when the operation is unknown:

```json
{
  "schema": "execution-receipt/1",
  "operation_id": "<64 hex>",
  "execution_id": "<id>",
  "binding_id": "<64 hex>",
  "state": "queued | running | waiting_retry | succeeded | failed | unknown",
  "reason": null,
  "attempts": {"used": 1, "limit": 3},
  "budget": {"reserved": 1, "limit": 3},
  "articles": {"admitted_count": 2, "executed": [{"article_key": "<link>", "content_sha256": "<64 hex>"}]},
  "artifact": null
}
```

`artifact` stays `null` until the service has itself verified the accepted output. Then it is:

```json
{
  "accepted_output_sha256": "<the digest the execution authority recorded as the run's output>",
  "sha256": "<recomputed by the service from the files>",
  "file_count": 3,
  "total_bytes": 1234,
  "files": [{"path": "a/b.md", "sha256": "<64 hex>", "bytes": 10}]
}
```

**The artifact digest:** SHA-256 over `path`, NUL, the file's hex digest and a newline, for each file in canonical order. Canonical order compares paths segment by segment, which differs from whole-string order; for example, `a/b` comes before `a-c`.

**Path grammar:**
- relative ASCII paths of at most 200 characters, with segments `[A-Za-z0-9._-]+`, none `.` or `..`;
- at most 64 files, at most 4 MiB per file and 8 MiB in total.

**Article keys:** `article_key` is an article's `link` and `content_sha256` is the SHA-256 of its `content` string's UTF-8 bytes, the same terms the control plane records at admission. The executed set is a non-empty subset of the admitted set; the service may exclude records by policy.

## `GET /executions/{operation_id}/artifact/{path}`

Returns the raw bytes of one listed file, or `404`.

## Control-plane verification before completion

The control plane completes an operation only after these checks pass:
1. **Receipt identity:** the receipt's `execution_id` and `binding_id` equal its own recorded values.
2. **Articles:** the executed articles are within the admitted set.
3. **Listing:** counts, sizes, path grammar, uniqueness and canonical order hold, and `accepted_output_sha256` equals `sha256`.
4. **Parts:** every part is fetched, and its length and SHA-256 match its listing.
5. **Digest:** the artifact digest recomputed from the fetched parts equals the receipt's.
6. **Storage:** the parts and a manifest are stored immutably.

Any structural or digest mismatch on a receipt that reports success is a terminal `artifact_rejected`, and so is `succeeded` with a `null` artifact (token `receipt_success_without_artifact`): the artifact is carried exactly when the service has accepted it, so that combination is contradictory, not pending. A transport failure while fetching parts is retried by the next sweep.
