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

## Retained report candidates

After successful generation, the workflow retains a separate
`report-candidate-<run>-<attempt>` artifact for seven days before browser checks.
It contains only exact `index.md` bytes and a small manifest bound to the run,
attempt, checked-out source revision, review-plan identity and report SHA-256.
The completed generation receipt must agree with the schema-5 report. Reports
are limited to 2 MiB; nonregular files, hard links, symlink paths and existing
output directories are refused. The manifest is finalized only after the report
has been written, and upload requires successful export.

This artifact contains generated report text for offline replay. It excludes
article snapshots, prompts, model reasoning, logs, environment and credentials.
It is an unpublished candidate with no publication authority; a failed browser
check still prevents commit and publication. Export does not request another
model response, release a reservation or authorize a retry. Diagnose and validate
the retained candidate against its recorded source revision before any separate
publication decision.

## Request budget

Production uses the existing `publication-admission` compare-and-set store. Every
HTTP attempt reserves a slot before transmission, including the initial request
and internal client retries. The limit remains three total attempts per original
request episode. Reservations
bind the admission/run identity, source revision and a hash of the exact request
(including prompt, model, routing and token limit). A different request, revision,
limit or owner cannot reuse that episode. These operational records persist on
the admission branch independently of expiring Actions diagnostic artifacts;
they contain hashes, identifiers and fixed states, never request/answer content.

Generation runs share one queue. Main runs check out current main when they
start; other refs retain the triggering revision. The recorded checkout SHA is
passed as `SENTRYINSIGHT_SOURCE_REVISION` to the request budget and diagnostics,
and identifies the trace's service version. Older callers without that variable
retain their `GITHUB_SHA` identity; an invalid explicit revision cannot fall back
to it. Before pushing a report, both the fetched main tip and the report commit's
parent must match the recorded checkout. A main change during generation stops
publication and preserves the remote report, including when rebase would apply
cleanly or drop an already-applied report patch. There is no automatic
regeneration after that failure.

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

## Informed repair

Once the original request episode records `response_received`, it accepts no
further send. A draft that then fails validation may receive a separate,
bounded repair, which never reopens that episode:

- A classifier maps every failure to one class. `repairable`: a named contract,
  validation or grounding rule. `transient`: a timeout, 408, 429, 5xx or
  network error, already retried inside the original episode. `fail_fast`:
  authentication, quota, configuration, model identity, source or Reporting
  identity, site safety, integrity, the output-token limit, and anything
  unrecognized. Only `repairable` failures are repaired.
- Each repair request reserves its own slot in the same `publication-admission`
  store, under `repair_reserved`/`repair_finished` records distinct from the
  original episode's, bound to its own `request_sha256`. The store refuses a
  repair slot unless the original episode's latest completion is
  `response_received`, while another repair slot is unfinished, after six slots
  in the admitted run, or when the run holds a paid-verification reservation.
  Paid verification never repairs.
- A finding-level failure regenerates only that finding's block. The request
  carries the rule code, the field, the offending draft value (at most 400
  characters), fixed guidance for a valid value, and only the material from
  the original request for the sources that finding already cited. A repaired
  block may keep or narrow its own citations, never add one. A failure
  outside findings repairs its section; a report-level failure such as a
  repeated section gets one full regeneration. Limits: three rounds per finding
  or section, one full regeneration, six repair requests and 20 minutes of
  repair requests per run.
- After every splice or drop, the complete validation and grounding pipeline
  runs again at its unchanged bar.
- A finding that still fails after its rounds, or once the run's repair
  requests are spent, is omitted. The omission is disclosed in the generation
  receipt and in host-owned source coverage; sources cited only by omitted
  findings show as not represented, never as cited. The report publishes only
  while at least `analysis.min_findings` (default 1) findings remain.
  Identity, integrity and site-safety failures always block the whole report.
- Every attempt (original, repair or omission) adds one bounded line to the
  generation receipt, the step summary and the report-history projection:
  attempt number, kind, class, rule, finding number, field, outcome and request
  digest. Lines carry no candidate, prompt or source text. Deploy the history
  Worker's projection validator before a producer that sends these lines; an
  older Worker refuses the projection, which the workflow reports as a warning.

## Decisions

| Observation | Behavior |
| --- | --- |
| Connection failure established before sending | Retry only within the shared remaining budget |
| Explicit transient error envelope without completion/usage evidence | Bounded retry honoring Retry-After; all attempts consume the same cap |
| Wait exceeds 30 seconds | Defer for review; no early retry or automatic restart |
| Read/write timeout, interrupted response, bare transient status, malformed HTTP 200, conflicting response metadata | Hold for reconciliation; no automatic replay |
| Authentication/payment/configuration error or wrong resolved model | Stop for repair; no provider, credential or price fallback |
| Output limit (`finish_reason=length`) | Reject partial output; allow at most one bounded recovery attempt (raising `max_tokens` to the free route's 131,072 ceiling without tightening reasoning) within the same three-attempt and wall-clock budgets, then preserve last-good output and advise `repair_required` |
| Repairable evidence, content or artifact validation failure | Informed repair as above, then full revalidation; omit and disclose a finding that stays invalid when at least `min_findings` remain, otherwise preserve last-good output |
| Identity, integrity or site-safety failure | Fail fast without repair or omission; preserve last-good output |
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

## Large source metadata

Source-review packets preserve every source link, including links after the
former 512-item per-source limit. The existing 1 MiB canonical-JSON packet bound
still applies. URLs, evidence identities, CVE cohorts and source dispositions
are validated without truncation or weakened grounding. A real packet overflow
fails before generation with `review_packet_size_limit_exceeded`, which the
bounded diagnostic receipt preserves.

Completed-run history projections likewise preserve full metadata lists within
their existing per-item, 320 KiB escaped-record and 8 MiB request limits.
Ordinary admissions and scheduled bundles retain their 64-item list cap. Update
the existing history Worker's projection validator before the Python producer:
both sides must use the same bounds. Snapshot omissions now log only fixed
reason categories and counts, never source content or URLs.

Validate large-input repairs offline with saved triage decisions before an
authorized fresh run. A passing preflight is not proof of report generation or
publication; verify the resulting diagnostic receipt, history projection and
served release separately. Existing request budgets and uncertain-run holds
remain unchanged.
