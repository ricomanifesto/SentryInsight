# Proposed closed Sentry full-feed canary

This temporary execution route is prepared for review. The committed manifest is
**disabled**, with no active pilot, opening liability, billing basis, data grant
or operational-metadata audience approval. It cannot read a provider key or send
an inference in that state. This is separate from ordinary model activation:
selected application clients remain OFFLINE and mock-only.

The existing registered `verify-nemotron.yml` path is intentionally rewritten on
the canary branch for this Sentry-only case.
The branch has a `vercel.json` Git-deployment guard. That local guard alone is not
fresh verification of the hosting integration. Do not merge the temporary
workflow, canary manifest or hosting guard into production main.

## Authority and exact request

The closed job requires the exact reviewed commit and manifest digest, the fixed
owner/repository, manual event, first run attempt, canary ref, clean source tree,
unchanged production-main head and both serving report hashes. The source
candidate is intentionally different from production main. The one-day manifest
expires before key lookup/send when the UTC date changes; it cannot relabel an
old answer. A report receives the real host generation timestamp.

Only the frozen 30-entry feed packet is permitted. All bytes are source-bound;
25 eligible entries enter the actual prompt, five held entries stay in host
coverage metadata. Model context contains eligible titles, publishers, URLs,
normalized complete available feed content, reporting keys, supplied CVEs,
source-link/coverage labels, source-owned detail/version reference scopes and
exploitation assessments, plus the existing public system and Markdown report
instructions. It contains no held source bodies, synthetic calibration answer,
telemetry, private material, fetched article bodies or search/tool results.
There are no article-URL, provider-account or key-management requests.

The exact prepared JSON request body is 54,033 bytes: SHA256
`a260b0a92a35926c8201e80c9b44fd4edbeb84c00b05f600c1856de57a4ca440`.
Its decoded canonical JSON SHA256 is
`93de9d2adc4d7bbbaa12759a54291b750e9e8d47c22c75d3de1c14ad06a40649`.
These hashes exclude HTTP headers and TLS framing. The source-pack SHA256 is
`b74eb002a01d5676653ea06f4336e968f2fb012f3e78555b33ebaa5ce6808ce9`.
The source review is 25 eligible/5 held; the cl100k estimate is 12,128 message
tokens. That estimator is not a provider-token or billing guarantee.

One POST goes to OpenRouter chat completions, exact Kimi K3.1 Pro with only
`moonshotai/mxfp4`, standard requested tier, low/excluded reasoning, no fallback,
no data collection, ZDR required, and text prices at most $2/$10 per million plus
zero request fee. Output is at most 32,000 combined completion/reasoning tokens.
No retry, repair, alternate route, premium tier or filter relaxation exists.
HTTP, transport, accounting and permission uncertainty stops the operation.

## Persistent financial and physical ownership

The job reuses the admission/daily/spending implementation over the fixed
`publication-admission` Git CAS branch. Existing persisted financial history is
not assumed. A separately approved [one-time initialization](../publication/INITIALIZED_ADMISSION.md)
must precede the first paid run; the sender cannot create or re-seed this branch.
Every paid read and CAS retry requires its stable first marker and hosting guard.
Missing, unavailable, foreign or recreated unmarked state stops before a token or
model-key access. The initialization marker grants no money, day or send allowance.
The registered manual workflow has a separate `initialize_ledger=true` job using
only checkout Git authority, without a model key or artifact. It is mutually
exclusive with the default canary job. These are two separately approved manual
dispatches, with acknowledged root/marker read-only verification between them;
initialization never automatically starts inference. Its bounded stdout is kept
in ordinary Actions logs, not the canary's seven-day artifact.
The real pilot activation and opening remain absent in source. Once separately
approved, the Sentry quota is $20 per UTC month; one daily claim and the whole
$7.251456 hold are atomic. The SAME original physical token is acknowledged
before the one POST, with limit one. The ordinary three-slot full hold is kept;
there is no undisclosed smaller canary policy. A model-context/rate assumption
bounds one physical request at $2.417152; it is not an external billing warranty.

Readmission, new workflow runs, cancellation and source revisions cannot reset
the day or mint another token. Unknown writes/sends remain held, block automatic
replay and can block rollover. A trusted reconciliation is separate. The existing
Sentry key is unchanged; its current limit and available credits are unverified; no purchase, top-up, key change or account lookup is
performed. A 401/402/404 does not authorize another attempt or imply zero cost.

Settlement requires complete coherent model/usage/cost within the fixed limits,
a separately established credit-only billing basis, and explicit
`usage.is_byok: false`. OpenRouter cost alone is not proof of all upstream spend.
Absent/true BYOK status or incomplete accounting keeps the full hold and refuses
promotion. Returned null/missing provider/tier is unavailable attestation, not
fabricated standard-tier proof; explicit contradictory values refuse. Financial
settlement occurs once before admission completion, independently of whether
host quality passes. No caller supplies a refund amount or reopens slots.

## Key, artifacts and output fate

The existing Sentry Actions key is injected only into the sender step. Every
source/date/report/context fence and the persistent token acknowledgement precede
key lookup and real transport construction. Child Git/Node processes receive an
explicit environment without the model key, AWS credentials, proxies or tracing
secrets. The existing ephemeral Actions checkout Git credential is used for CAS;
no new credential is created. The prepared workflow requests `contents: write`,
which needs explicit approval along with the public financial-metadata audience.
Policy, day and bounded usage records on the Git branch are public and durable.

Credentials have process-lifetime memory only, with no cryptographic zeroization
guarantee. The same response is replayed in memory through the actual host using the
original token, with no second external call. Complete source/version grounding,
coverage, rendering and Pages packaging must pass. Failed raw bodies, prompts,
answers, reasoning, headers and exceptions are never logs or artifacts. Only the
explicit allowlisted JSON receipt is uploaded for seven days. Raw duplicate JSON
keys are refused before accounting, host replay, settlement or promotion. A
receipt-output failure emits only the safe in-memory result with emission marked
unknown, exits nonzero and never retries the metadata or ledger mutation. Sanitized stdout
also enters ordinary Actions logs under repository-configured retention; there
is no claim that logs share the seven-day artifact period.

Default fate is **nonpublish**: scratch output is removed, and any later live
report needs a new separately authorized request. An explicitly approved
`conditional_publish` fate rechecks main and both old serving hashes, then makes
one report-only fast-forward main commit from the exact validated scratch tree.
No application source/workflow is merged. A failed/unknown push is never retried,
rebased or rolled back automatically. A push using the checkout GITHUB_TOKEN normally does not trigger on:push
workflows. The coordinator must separately run the already-existing manual Pages
deployment under explicit approval, verify its actual checkout SHA, and verify
Vercel through its existing publication route separately. This sender adds no
actions:write permission, workflow dispatch or second credential. A pushed
commit is not yet verified serving publication; the receipt retains that
distinction. Public valid report/archive
retention is normal publication retention, not the diagnostic seven-day period.

## Future commands; execution approval is still required

After exact source, manifest values, data/privacy, billing, audience, permission
and output-fate review, the supported dispatch shape is:

```sh
gh workflow run verify-nemotron.yml \
  --ref canary/sentry-full-feed-20261105 \
  -f expected_commit=REVIEWED_FULL_SHA \
  -f expected_manifest=REVIEWED_MANIFEST_SHA256
```

Do not execute this preparation command while the required grants are absent.
The main workflow file is already registered; the reviewed branch version can
be dispatched without merging this temporary route into main. Dependency setup
uses the existing frozen Python lock, Node24 and public tokenizer data before
secret injection. The secret-free preparation fetches only the fixed public
feed; control fences read the two fixed public report endpoints and existing Git
metadata. No AWS operation, scheduling change or production resumption is part
of this route.

The GitHub token trigger rule is documented in [GitHub Actions triggering rules](https://docs.github.com/actions/using-workflows/triggering-a-workflow).

Synthetic acceptance uses the existing pinned environment, OS/network denial,
mock issuer/client/publisher adapters and the actual offline host. It proves the
closed sequencing and failure behavior, not live Git authentication, account
billing, provider eligibility or a fresh serving report.
