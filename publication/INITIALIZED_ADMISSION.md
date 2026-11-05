# Explicit first initialization

The closed Sentry canary requires the fixed `publication-admission` branch to
exist before paid admission. The ordinary free/default store retains its earlier
first-use behavior. Branch presence alone is insufficient: every paid store read,
including every CAS retry, requires exactly one first `admission_store_initialized`
record and the fixed hosting guard. A free writer recreating a deleted branch
without that marker cannot create a fresh paid wallet.

The marker has exact fields `stage`, `schema_version: 1`, `site: SentryInsight`,
`scope_sha256`, `initialization_id` and canonical UTC `at`. Its identity is derived
from the site and the approved canary pilot's existing `opening.basisSha256`.
It contains no request, run, source revision, day, cap or grant. Normal later
generations keep the same marker. A different opening scope refuses; it never
creates a new branch or erases older costs/holds. This closed one-day adapter does
not define a later production month's opening or a new initialization policy.

The root `state.json` is canonical JSON with `schema_version: 1`,
`site: SentryInsight` and `records: [marker]`. There is no opening charge, daily
claim, request token or financial reservation at initialization. The second root
file is fixed `vercel.json` with `git.deploymentEnabled: false`. Every append to a
marked history retains that file, including a legacy free append, because the Git
tree builder does not otherwise retain parent files. Paid reads also verify its
exact bytes. This is a branch-local hosting guard, not live hosting verification:
integration/root-directory behavior and possible build/preview attempts must be
disclosed or checked before a public push. No Vercel setting is changed here.

After separately approving the exact source/manifest, opening-scope assertion,
public metadata audience and first branch creation, the concrete operator route
is TWO separate manual dispatches of the existing registered workflow. First:

```sh
gh workflow run verify-nemotron.yml --repo ricomanifesto/SentryInsight \
  --ref canary/sentry-full-feed-20261105 \
  -f expected_commit=REVIEWED_FULL_COMMIT \
  -f expected_manifest=REVIEWED_MANIFEST_SHA256 -f initialize_ledger=true
```

Only the initializer job is eligible. It requires the fixed owner/repository,
canary ref, exact head, first attempt and non-debug steps. Its fixed command also
refuses outside the manifest's execution date. The job uses the pinned checkout's
existing ephemeral `GITHUB_TOKEN` Git configuration and Node24. It has no provider
key, Python/model/dependency/source-fetch step or artifact upload. Checkout removes
its credential at job end. No credential is exported, copied into this program,
added to global configuration or persisted by the initializer. Its minimal child
environment still permits repository-local conditional includes used by checkout;
synthetic tests qualify the [pinned checkout's local-include mechanism](https://github.com/actions/checkout/blob/3d3c42e5aac5ba805825da76410c181273ba90b1/src/git-auth-helper.ts#L330-L348),
not actual GitHub write permission.
Desktop global credential helpers are not assumed to work.

The command executed inside that authenticated checkout is:

```sh
node scripts/bootstrap_canary_ledger.cjs \
  --expected-commit REVIEWED_FULL_COMMIT \
  --expected-manifest REVIEWED_MANIFEST_SHA256 \
  --initialize-public-ledger
```

This section preserves the historical November 5 first-use route and its $20
November Sentry pilot, prospective zero opening and public metadata audience.
The ledger is already initialized. The separately prepared November 6 fixed-snapshot
scope must reuse that same marker/opening and must NOT initialize again or choose
a new namespace. Its only proposed operator step is the fixed NO-MODEL readmission
described in [the recovery guide](../scripts/SENTRY_CANARY_HEADROOM.md).
The initializer below is not a November 6 release instruction.
The registered job enforces the fixed owner, ref, head, first attempt and nondebug
context. The command additionally requires the exact manifest digest, current UTC
date, clean checkout, fixed repository origin and production main at
`5fc68212f1a9772ab56872ad20ad94ccc8322f3e`; an existing target ref refuses.
It uses only the checkout's existing authorized Git authentication, without a
provider credential or added access, and never starts the separate sender job.
Child Git processes receive fixed minimal controls, no model/AWS key, proxy,
arbitrary Git environment, HOME override or interactive credential prompt.

The command creates one root commit and performs one expected-absent CAS push to
that branch. This uses an empty expected ref lease solely to refuse an existing
branch, never to replace one. Any existing ref, including an identical marker,
refuses without adoption. A rejected/lost push acknowledgement stops without
write retry or automatic readback/adoption. Only fixed status and root/marker
identity metadata reach stdout. `initialization_unknown` may include *proposed*
root/marker hashes; these do not assert remote success. Preserve that result and
perform separately authorized read-only reconciliation of the exact candidate
before any operator decision. Do not repeat initialization, change namespaces or
treat an uncertain outcome as permission.

After an acknowledged result, the operator must separately verify the exact
remote root and marker read-only and record their identity privately. Only then,
under its separate inference/output approval, dispatch the same reviewed workflow
with `initialize_ledger=false` (the default). Only the canary job is then eligible;
it performs the existing checks before its one possible POST. There is no job
dependency, initialize-on-missing path or automatic progression from initialization
to inference. Unknown initialization stops this sequence without another dispatch
or write until separately reconciled.

The Git branch and later financial metadata are public and durable. Initializer
stdout is allowlisted root/marker/status metadata in ordinary GitHub Actions logs
under repository-configured retention; it has no seven-day artifact. The canary's
existing sanitized artifact policy is separate. The marker is provenance, not caller
authentication or protection from an authorized writer deliberately rewriting
history. Initialization does not invoke a model, account/key, publisher or
deployment API. A hosting integration may still observe its public Git push as
described above; no live effect is claimed from local tests.

Synthetic checks use disposable local Git remotes and no credentials:

```sh
node --test --test-concurrency=1 publication/test/initialized-store.test.js \
  publication/test/canary-owner.test.js publication/test/bootstrap-auth.test.js
```
