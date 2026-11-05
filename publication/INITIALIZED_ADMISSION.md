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
public metadata audience and first branch creation, the one-time command is:

```sh
node scripts/bootstrap_canary_ledger.cjs \
  --expected-commit REVIEWED_FULL_COMMIT \
  --expected-manifest REVIEWED_MANIFEST_SHA256 \
  --initialize-public-ledger
```

The committed manifest has no pilot/opening or metadata-audience approval, so this
command currently refuses before Git/auth access. It never enables the sender.
The command requires a clean exact checkout, the fixed repository origin and the
manifest's production-main fence. It uses only the checkout's existing authorized
Git authentication; it does not obtain a provider credential or add access. Any
future authenticated job/command and public write remain separately approved.
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

Record the acknowledged root OID and marker SHA privately. The Git branch and
later financial metadata are public and durable; command stdout follows its
chosen execution environment's retention. The marker is provenance, not caller
authentication or protection from an authorized writer deliberately rewriting
history. Initialization does not invoke a model, account/key, publisher or
deployment API. A hosting integration may still observe its public Git push as
described above; no live effect is claimed from local tests.

Synthetic checks use disposable local Git remotes and no credentials:

```sh
node --test --test-concurrency=1 publication/test/initialized-store.test.js \
  publication/test/canary-owner.test.js
```
