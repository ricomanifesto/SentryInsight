# Failure receipts and bounded recovery

Generation records a separate, schema-validated diagnostic receipt before the
workflow starts and finalizes it on ordinary exit. The receipt preserves fixed
failure stages, reason codes, optional field/finding identifiers, bounded provider
status/usage, the observed request state and an advisory recovery decision. It
does not contain exception messages, source bodies, prompts or generated answers.
Unknown usage remains unknown. A successful model response is not a valid report;
all existing evidence and content checks still apply.

The generation workflow exports this metadata as `generation-diagnostics-<run>`
with seven-day artifact retention. The existing source-review artifact retains
its separate 90-day contract. Neither artifact is part of the served report.
Missing or malformed diagnostics do not authorize a retry. The verification
workflow continues to allow only its single request and retains its existing
receipt format.

## Request budget

Production uses the existing `publication-admission` compare-and-set store. Every
HTTP attempt reserves a slot before transmission, including the initial request
and internal client retries. The limit remains three total attempts. Reservations
bind the admission/run identity, source revision and a hash of the exact request
(including prompt, model, routing and token limit). A different request, revision,
limit or owner cannot reuse that episode. These operational records persist on
the admission branch independently of expiring Actions diagnostic artifacts;
they contain hashes, identifiers and fixed states, never request/answer content.

A reserved attempt with no trustworthy completion remains held. A timeout or lost
acknowledgement while updating the ledger is not retried. Concurrent processes
cannot both reserve the same next attempt. Recorded retry delays are checked by
the store as well as the client, so a restart cannot skip the wait. Local callers
without production admission use a shared in-process budget; this is not a claim
of durable, cross-process protection for local development.

The CI entrypoint refuses to generate without the durable admission route. A new
workflow run does not release an uncertain prior invocation. Existing admission
recovery and explicit readmission rules remain unchanged. A trusted operator
readmission can create a new admitted episode, retaining all older reservations;
ordinary restarts cannot. Diagnostic advice alone
cannot bypass them. There is no additional workflow retry loop or scheduled
recovery controller.

## Decisions

| Observation | Behavior |
| --- | --- |
| Connection failure established before sending | Retry only within the shared remaining budget |
| Explicit transient error envelope without completion/usage evidence | Bounded retry honoring Retry-After; all attempts consume the same cap |
| Wait exceeds 30 seconds | Defer for review; no early retry or automatic restart |
| Read/write timeout, interrupted response, bare transient status, malformed HTTP 200, conflicting response metadata | Hold for reconciliation; no automatic replay |
| Authentication/payment/configuration error or wrong resolved model | Stop for repair; no provider, credential or price fallback |
| Output limit or evidence/content validation failure | Preserve last-good output; correct the cause offline before another authorized request |
| Ambiguous source evidence | Preserve the existing explicit source-review state and coverage |
| Publication failure after validation | Investigate/recover existing artifacts through the publisher; do not regenerate |

An explicit error envelope permits a bounded policy decision; it is not proof
that the provider performed no work. This mechanism limits sends and preserves
uncertainty; it does not claim exactly-once execution inside a provider.
The free-model price ceilings and no-fallback guard remain unchanged. Automatic
generation, new evaluation requests, token/cost changes and deployment remain
separate operational decisions.

`retry.action` is advisory and uses fixed values: `stop`, `repair_required`,
`review_required`, `reconcile`, `retry_after`, or `recover_publication`. A report
validation rejection does not silently become a conclusive publication success;
the admission workflow retains its conservative failure mapping. No output is
published merely because a receipt exists or a provider returned HTTP 200.
