# Publisher contract

Every call carries `Authorization: Bearer <token>`.

**Publication id:** `publication_id = sha256("report-control-plane/publication/1\n" + target + "\n" + artifact_sha256)`.

## `GET /publications/{publication_id}`

Returns the receipt (`200`), or `404` if no effect was ever applied for this id. The control plane uses this observation to repair an ambiguous outcome. Observation is not the fence.

## `POST /publications/{publication_id}`

Body: `{"target", "artifact_sha256", "expected_remote", "candidate_seq"}`.

The publisher applies the effect atomically, and only when all of these hold:
- no receipt exists for this id, so a repeat returns the existing receipt with `200` and no effect;
- `expected_remote` equals the target's current remote version;
- `candidate_seq` is greater than the target's current candidate sequence.

When `expected_remote` or the sequence condition fails, the call returns `409 {"error": "remote_changed" | "stale_candidate"}` with no effect. A slow old call that arrives after a newer publication therefore fails its condition and changes nothing, and the published revision never moves backward.

A new effect returns `201` with:

```json
{"publication_id": "...", "receipt_id": "...", "target": "...", "artifact_sha256": "...", "remote_version": 2, "candidate_seq": 7}
```

## Limits

A real publisher that cannot enforce a candidate sequence has only `expected_remote` as its fence. Only a local durable fake implements this contract here: `tests/support/durable-publisher.mjs`. It keeps its state in one atomically replaced file and has test controls to drop the acknowledgement after an effect or to hold a request before its effect.
