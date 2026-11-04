# Fixed fictional GRC workflow verification

This temporary branch prepares a manual, nonpublishing test. Publishing or
dispatching it requires separate approval of the exact executor, source and data
scope. It does not activate an ordinary paid model route. Do not merge the test
workflow or branch hosting guard into main.

The registered `verify-nemotron.yml` workflow accepts only an exact reviewed
commit on `test/selected-model-fixtures-20261104`, the repository owner, manual
dispatch and first attempt. Public workflow-history checks refuse a second run at
that head; an exclusive private claim refuses reuse within a run. Concurrency
alone does not provide exactly-once execution. An operator must inspect any
uncertain or stopped run before a separately approved action. No automatic retry,
fallback, repair or claim reset exists.

The existing Sentry Actions OpenRouter secret enters only the outer sender step.
It never enters the GRC checkout, worker, dependency setup, command arguments or
artifacts. No AWS credential, account/key-status call, publisher or database is
used. The source is fixed to the deployed GRC commit and tree in the manifest.
Ordinary selected routes still require OFFLINE activation, an exact MockTransport
and a synthetic key.

Before secret access, the actual host workflow prepares both calibration requests
in a secret-free child with socket and real HTTP transports denied. Source and
fixture hashes, the first request and calibration second request hashes must
match. Handwritten fixture answers are test inputs; captured provider answers
are never saved. Both financial reservations ($0.096 and $0.128) are made durable
upfront. The claim fsyncs a sending marker before each of at most two POSTs.

The first POST sends only two fictional notices and the public legacy TEXT
analysis prompt. The recognized-analysis gate requires an exact source-bound
supplier row and refuses the parser's fallback-to-all behavior. Bullet/Markdown
or unrecognized rows fail this closed compatibility test; they are not normalized
into a claimed original-parser success. The first prompt and production parser
are unchanged. This is a known legacy-format limitation.

The actual parser and workflow derive the second prompt. Only the reconciled
GRC-relevant count (1 or 2) and six closed regulation names may vary from the
frozen calibration prompt. All source evidence, dates, links, system prompt,
selection schema and request policy must remain identical. No raw first answer
is inserted into the plan prompt. The new second-body hash is recorded before
its single POST; its live hash cannot be promised from a mock first answer.
The secret-free child uses a replaced environment and fixed Python hash seed so
set-based parser ordering repeats across processes. It disables user site and
implicit working-directory imports. The secret-bearing outer process stays in
Python isolated mode; that mode would ignore the child's hash-seed setting.

Both requests use `google/gemini-4-argon` only through `google-vertex/global`,
default tier, low/excluded reasoning, text-only input, no fallback, data collection
denied and ZDR filtering, with $2/M input, $10/M combined output and zero request
price ceilings. Vertex SafetyRetention may retain flagged prompts up to 90 days
for safety without training; ZDR filtering does not mean zero retention. No
account privacy option is changed or filter relaxed. Input reserves are 8k/24k
complete-input units, each output cap is 8k. The $0.224 admission estimate is not
actual cost or execution permission. All prior trial allowances are consumed.

Responses must be complete and model/known provider/tier consistent, with finite,
complete and coherent cost/token accounting within both reservations. Null or
missing tier/provider metadata remains explicitly unverified and alone does not
fail host quality or stop continuation. Missing cost or uncertain accounting
stops and retains the reservation. Authentication, HTTP, parser, worker, output,
grounding or transport failure stops the sequence without repair. Compressed or
oversized response bodies are refused; each request and child has a deadline.

Both real responses are replayed privately through the same analysis, evidence,
strict JSON selection, grounding and host renderer. Success requires a grounded
supplier control and deliberate primary-regulatory abstention. No report is
written or published; tracked local and remote report blobs are fenced. No URL
fetch, tools, search, multimodal input or optional relevance pilot runs.

Raw prompts, model bodies, answers and reasoning remain only in memory/private
pipes. Only fixed diagnostics, hashes, counts, requested/resolved identity and
validated numeric usage/cost enter the three allowlisted artifacts, retained for
seven days. The public repository's Actions logs and artifact visibility still
apply; ordinary log retention is repository-configured. No account or key-status
diagnostic is logged. The local Vercel branch guard disables Git deployments in
source, but does not attest to current remote hosting configuration.

With source/interpreter paths supplied as documented by the release handoff,
`tests/test_grc_full_trial.py` exercises only synthetic transports and private
workers. The future sender command, run only by the guarded manual job, is:

```sh
sources/grc/agent/.venv/bin/python -I -B executor/scripts/verify_grc_workflow_once.py \
  --expected-commit "$EXPECTED_COMMIT"
```

This is test preparation, not proof of recurring production readiness. Recurring
paid generation still needs server-owned admission, aggregate spending policy,
real-source retention approval and separate publication/schedule decisions.

## Future diagnostic output

New trial receipts use `schema_version: 2`; diagnostic records have their own
`version: 1`. Each record contains only fixed `stage`, `phase` and `code` enums.
The receipt separates the last observation, first failure and at most three
secondary cleanup/persistence failures from authoritative request states. It
tracks the latest observation independently of the capped secondary list and
preserves it through wrapped failures; reaching the cap cannot make `last`
revert to the first failure or an older retained cleanup record. The first
failure and retained secondary order remain unchanged.
records owned boundaries before risky work where possible: response validation
and close, worker launch/I/O/protocol, derived-body validation, plan binding,
replay/host validation, and source/report fences. Unknown exceptions remain
`unknown_failure`; their text, class, traceback, headers and bodies are discarded.

Worker success and error envelopes have exact, disjoint key sets and versioned,
allowlisted records. Malformed, mixed, oversized, duplicate-field or unknown
envelopes are protocol failures, not evidence of a recognition cause. A
`worker_recognition_gate` refusal describes this test's stricter closed gate;
it does not prove that the production parser itself fell back or that a model's
answer was semantically incompatible.

Response close, sender-client exit and child reap are bounded to five seconds. An earlier failure
stays primary if cleanup also fails; a close-only failure after valid metadata
stops before derivation. Cancellation/timeout preserves sending/uncertain holds.
Scratch-directory, claim-descriptor and outer control-client cleanup failures
also retain the first failure rather than replacing it. A returned receipt keeps
its operation/state evidence if client exit later fails. The independent trial
artifact is written only once, after control-client cleanup, so a late close
cannot replace a precise receipt with an empty generic fallback.
A claim save failure latches persistence as unknown: the runner never retries
that save through diagnostic recording, finish, binding or cleanup. Its trial
`states` become null with `claim_persistence: unknown`, because partially written
or mutated in-memory values are not durable-state proof. A safe independent
metadata write may preserve the failure; if the output directory is unsafe or
unavailable, only the fixed stop message remains. No claim is reset or rearmed.

Historical schema-1 receipts and their null/unknown costs remain unchanged.
Absent diagnostic fields mean unavailable evidence, not a default recognition
or formatting cause. The original stopped run cannot be classified after its
discarded answer merely because future diagnostics are more precise. Any new
request still needs a fresh exact grant; this diagnostic change adds no retry,
inference, payload or production activation authority.
