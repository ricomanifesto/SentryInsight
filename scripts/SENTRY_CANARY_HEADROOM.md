# Closed receive-window recovery preparation

This is local preparation, not a renewed request grant. The November 5 source,
request, manifest, financial records and failed run remain immutable. The old
request's exact local exception and final charge remain unknown. It has no report;
its original token/day remain consumed and the entire $7.251456 hold stays counted.
Ordinary selected clients remain OFFLINE and recurring generation stays paused.

## One clock and owned work

The registered manual workflow still requires the exact canary branch/head,
repository, actor, event and first attempt. Before dependency setup or secrets,
`anchor_canary_clock.py` makes one anonymous GET of that exact public GitHub run.
The fixed workflow ID, run ID, head, branch, actor, repository, event, attempt,
status and nonfuture creation time must agree. The entire GET is a bounded owned
child, including headers, body and close. No GitHub/provider key is read.

The public run's creation time is conservative: queue time only reduces the
40-minute allowance. Monotonic time is sampled before UTC wall time so a sampling
pause cannot extend it. One exclusive 0600 regular file in RUNNER_TEMP binds that
anchor to the context. Loads refuse symlinks, FIFOs, extra links, foreign owners,
permissions, oversized/duplicate JSON and inconsistent arithmetic. This assumes
the reviewed runner, its UTC/default-loop monotonic clocks and owned temporary
filesystem are trusted; the file is not an approval certificate or spend grant.
Reloading it never creates a new deadline.

The enforced profile is:

| Boundary | Ceiling |
| --- | --- |
| Workflow job | 2400 seconds / 40 minutes |
| Before whole money/day/original-token reservation | at least 2300 seconds remain in both job and UTC day |
| After known ACK, before key and again before send | at least 2280 seconds remain in both |
| Setup source/capture/calibration/Git fence | original run origin +120 seconds; no new phase on reload |
| HTTPX inactivity/per-phase timeout | 1600 seconds |
| Owned total receive window | at most 1600 seconds, also preserving the complete tail |
| Post-response host/ledger/fence/promotion work | one fixed window at most 600 seconds |
| Owned client/process/scratch/receipt cleanup | one fixed window at most 20 seconds |
| Standard pinned artifact upload | step timeout one minute, gated on at least 60 seconds remaining |

The final split is 600 seconds post work plus 80 seconds tail, within the original
680-second combined reserve. It retains the 2300/2280 gates and uses the supported
standard uploader, not a replacement uploader or dependency. The uploader is an
Actions step, not part of Python's private process group. Runner step transitions,
checkout post-actions and job termination remain GitHub orchestration; the job's
40-minute timeout is the platform backstop. A skipped, timed-out or failed upload
is never evidence of a retained artifact. Metadata also has ordinary Actions-log
retention, distinct from the seven-day artifact setting.

Setup actions/installations run without the provider key. Slow setup cannot gain
admission: the fixed setup deadline and 2300-second check refuse before money.
The public feed GET and both report GETs bound headers, complete body and close.
Preparation, actual host replay/render/package, Git fences and the single
publisher attempt run in owned process groups with bounded private pipes and
absolute phase expiry. Timeout/cancellation terminates only those groups and
boundedly reaps them. A spawn acknowledgement race is cleaned up before returning.
Each phase object is retained; relative waits cannot recharge it. Node admission
exchanges have a 20-second ACK ceiling under the same phase; an unknown exchange
latches and cannot be repeated. Killing a local Git process does not prove that
a remote write did not occur. Unknown writes require read-only reconciliation.

Only the parent reads the existing provider key, after all fences and the original
durable permit. Workers receive no provider/AWS keys, Python startup overrides,
proxies, tracing secrets or persistent credentials. The response, prompt and
source pack remain memory/private-pipe data. Only validated public report files
and allowlisted operational metadata may reach disk. No exception text, raw
stderr, headers or model content enters diagnostics. Original status/read errors
retain precedence over cleanup errors; uncertainty preserves the full hold and
never authorizes retry.

1600 matches the existing 32,000-output/20-tokens-per-second heuristic. It is a
local ceiling, not a provider throughput, completion or billing guarantee. The
output cap, requested model/provider/tier, source bytes, prices, reasoning/privacy
request controls, one physical send and financial policy are unchanged here.
Requested `zdr:true` and `data_collection:deny` remain unchanged. OpenRouter's
provider/endpoint and account Safety Retention policy, plus legal/CSAM exceptions,
qualify what those controls establish; catalog membership alone is not proof of
a strict endpoint retention tier. No account setting is inspected or changed.

## Separately gated fixed NO-MODEL action

`config/original-canary-readmission.json` is disabled with no approval-scope hash.
Its only possible target is the original invocation `42022367409`, with the exact
original owner and frozen ten-record journal history. It uses the existing
`readmitted` stage and existing initialized ledger; it creates no new wallet,
marker, opening, token, day, financial record or operator invocation.

Every CAS decision, including a store retry, rechecks the full history digest,
original admitted/invoked owner and absence of unrelated active invocations.
Changed history refuses. A failed write ACK stops without the generic Git
adapter's remote-adoption readback or retry. Malformed ACKs latch. The only
permitted append is one standard `readmitted` row; the returned prefix must be
byte-identical to the original records. This does not classify or refund the old
charge, supply a report, reset November 5, or make its old token usable.

The workflow's readmission job is mutually exclusive with initialization and the
canary, receives no provider secret and produces no artifact. Its filtered
Node/Git child is bounded to 90 seconds, using existing ephemeral checkout
authentication and no desktop credential helper. Sanitized stdout uses ordinary
Actions retention. It requires a separate exact operator grant and read-only
verification of the resulting row/prefix before a fresh canary is considered.
An unknown ACK is reconciled read-only, never dispatched again automatically.

## Pending bundle, no executable grant

The intended source release is a normal fast-forward of the existing historical
branch `canary/sentry-full-feed-20261105` and its draft PR191. Do not merge the
temporary application/workflow branch into main. A separate local child must
rederive November 6 date-dependent prompt/wire/source bindings and remain inert
until exact approval. It is a fresh generation of the same fixed public
30-source snapshot (25 eligible, five held), not a claim to newest news.

The November pilot start/opening/marker and $20 cap remain unchanged. The old full
hold plus a fresh identical hold would total $14.502912, absent other liabilities;
that arithmetic is not permission. No same-day extra allowance or financial
reconciliation is implemented. Earliest ordinary fresh day is November 6 UTC,
after a separately approved readmission and all exact context/date/source gates.

Future coordinator-owned commands, with exact approved hashes substituted, are:

```sh
# Separate NO-MODEL action; verify exact new row and unchanged old prefix afterward.
gh workflow run verify-nemotron.yml --ref canary/sentry-full-feed-20261105 \
  -f expected_commit=APPROVED_SOURCE_SHA -f readmit_original=true \
  -f expected_readmission=APPROVED_READMISSION_MANIFEST_SHA256
# Separate fresh one-shot; never initialize or readmit during this action.
gh workflow run verify-nemotron.yml --ref canary/sentry-full-feed-20261105 \
  -f expected_commit=APPROVED_SOURCE_SHA -f expected_manifest=APPROVED_NOV6_MANIFEST_SHA256
```

Both are proposals, not instructions to execute now. No source publication,
readmission, request, account operation, scheduling or deployment occurred during
this local preparation. Exact source/manifest/ref/date, public payload and metadata
audience, retention, conditional output fate and normal CI/runner effects require
the parent approval bundle.

A conditional report-only main push must still be based on verified `5fc6821`.
The checkout GITHUB_TOKEN push normally suppresses push workflows. Inspect actual
matching jobs; otherwise the separately approved existing manual routes are:

```sh
gh workflow run deploy-pages.yml --ref main -f expected_commit=EXACT_REPORT_SHA
gh workflow run publish-production.yml --ref main \
  -f invocation=publish -f source_sha=EXACT_REPORT_SHA
```

The latter runs the repository gate before publishing. Verify actual checkout,
descriptor/receipt and both serving surfaces; green or skipped jobs alone are
insufficient. Stop on an intervening main change or publication uncertainty. No
publication failure authorizes another inference, and recurring generation stays
paused. This sender adds no actions:write permission or dispatch credential.
