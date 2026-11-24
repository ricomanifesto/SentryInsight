# Retained admission capacity

D1 owns capacity for manual, event and scheduled execute admissions and their
staged source bundles. The fixed limits in `src/admission.js` are aggregate
across principals and execute pipelines:

| Retained resource | Limit |
| --- | --- |
| Admission identities, including conflicts and interrupted attempts | 10,000 |
| Unique admission or staged snapshot digests | 10,000 |
| Reserved snapshot bytes | 256 MiB |
| Principal/reason refusal diagnostic cells | 256, plus one overflow cell |

The existing 1 MiB request and 100 article limits still apply. At maximum body
size, the byte ceiling permits 256 snapshots; smaller daily bundles permit
more until an identity ceiling is reached. These are storage backpressure
limits, not time-window rates or per-principal fair shares. Output artifacts
keep their separate per-operation limits; this is not a whole-bucket byte cap.
Projection blob uploads, projected runs, publication records, and background
reconciliation diagnostics are outside this admission-specific policy.

## Ordering and retries

Before any new snapshot put, one D1 transaction reserves its identity and byte
charge. Execute admission reserves its operation identity in the same batch.
Capacity checks are part of the conditional inserts, so concurrent callers
cannot spend the same final slot or bytes. A refused new reservation returns
`429 admission_capacity_exhausted` before R2, article metadata, operation intent,
or Queue delivery changes. Only its bounded diagnostic cell may change.

A reservation survives an R2 error or a later D1 failure. Its `reserved` state,
principal, source revision, fingerprint and timestamp identify an unfinished
attempt. Retry the exact request; it reuses capacity. A successful operation
marks its reservation `admitted`; a source-label conflict marks it
`identity_conflict`. Already retained operations and conflicts return their
usual `200` or `409` at full capacity without creating another snapshot or
spending another slot. Shared snapshots are charged once, including bundles
staged before cron admission. Changing a pending bundle does not release its
old immutable bytes or reservation.

The operation, article rows and admitted event still commit together after
storage. A failed admission batch cannot partially write those rows. The
reservation intentionally belongs to an earlier transaction: it accounts for
bytes even when their operation never commits. Reservations are not expiry
leases and must never be cleared by a timer or an unsuccessful caller.

## Authenticated diagnostics

New conflict rows and their append-once conflict events have a dedicated
`principal` field naming the first authenticated observer. Repeated refusals
also update aggregate `admission_refusals` cells keyed by principal and fixed
reason. These contain counts, first/last times, and the latest operation id or
schedule id when available. They contain no request bodies or bearer tokens.
At most 256 distinct cells are retained; later combinations share one overflow
cell with a total count and the most recent principal/reason. This summary is
not a per-attempt audit trail. Returning a previous conflict never replaces its
first observer, but the later caller remains attributable in the summary.

Source staging records the latest authenticated actor, staging time and count
on its existing schedule row (`staged_by`, `staged_at`, `staging_count`), rather
than appending an event on every replay. Historical staging events remain.
Configuration failures and unauthenticated/unauthorized requests write nothing.
Validation and capacity refusal diagnostics are best effort: an unavailable
audit store preserves the original refusal. Unexpected storage failures remain
failures, with any committed reservation available for diagnosis and retry.

## Upgrade and operation at capacity

This upgrade requires a quiesced write boundary. Applying the one-time backfill
while an old Worker can still admit or stage sources can leave later writes
permanently uncharged; deploying the new Worker afterward does not repair them.
Use this order:

1. Quiesce manual/event admission producers, scheduled admission triggers and
   source-bundle staging producers. Fence their HTTP/cron entry points against
   new work; stopping producers alone does not cancel requests already running.
2. Drain or fence all in-flight old admission/staging handlers and their pending
   retries, including snapshot puts and D1 batches. Confirm no old Worker can
   finish or start such a write before beginning inventory or backfill. Keep
   that fence in place through migration, deployment and verification.
3. Inventory the now-stable D1 references and R2 objects. Reconcile historical
   orphans and conflicts attached to project-origin operations when a pipeline
   has mixed project/execute history, as described below. Preserve the inventory
   and the agreed retained baseline; the SQL migration does not discover or
   automatically charge those omitted admission bytes/identities.
4. Apply `0005_admission_capacity.sql`, then
   `0006_delivery_revision_bounds.sql`, in that order, and verify both migration
   receipts. Both are required before serving this updated Worker.
5. Deploy the updated Worker against the same inventoried D1/R2 pair while
   producers remain fenced. Verify its active version, schema and backfilled
   reservation counts/bytes against the inventory, then verify retained replays
   and reservation-before-storage behavior with controlled rollout checks.
6. Resume admission, scheduled triggers and staging only after verification and
   after confirming old Worker revisions can no longer write. If verification
   fails or rollback restores an old writer, keep producers fenced; do not rely
   on the quota bound while an old writer remains writable.

Migration `0005` keeps all existing rows and backfills execute-origin operations
and conflicts whose existing operation has execute origin.
It uses known snapshot lengths where recorded; legacy conflicts and staged
bundles without lengths are conservatively charged at the full 1 MiB request
limit. Known historical principals are retained on operation reservations;
unknown legacy conflict/event attribution stays `NULL`. Existing totals above
a limit are preserved and block new capacity, while retained identities remain
replayable. No destructive backfill or automatic pruning occurs.

Historical R2 orphans without D1 references cannot be discovered by this SQL
migration. The fenced inventory/reconciliation step above is required; the new
limits bound additional admission retention, not unknown historical bytes. The
migration itself never accesses or deletes R2.

A pipeline can change between project and execute mode. The existing operation's
origin therefore does not prove the path that created a refused conflict. In
mixed-mode history, an execute admission may have conflicted with a project-origin
operation; `0005` does not charge that conflict or its snapshot through that
relationship. The fenced inventory must review these project-origin conflict
references alongside orphan R2 objects, reconcile any execute-admission usage,
and record unresolved attribution and the retained baseline explicitly. Do not
claim the migration counted this ambiguous history, or charge all project
retention to this admission policy merely because attribution is unavailable.

There is no online release/reset API. Monitor the counts and summed bytes in
`admission_reservations` and `admission_snapshots`, and investigate `reserved`
rows and refusal summaries. At capacity, operators can review a deliberate
code-limit increase or rotate to a new, inventoried D1-and-R2 pair after
preserving the old pair for its export/retention obligations. Rotation requires
quiescing producers, draining/fencing old deliveries, moving bindings together,
and explicitly deciding how the old history remains available. It is a separate
operational change, not an automatic action performed by this implementation.
Clearing D1 reservations while keeping their R2 objects would defeat the bound.
