# Production publication

This directory holds the publisher that moves accepted static content to the
production artifact branch, the hosting adapter that branch carries, and the
admission checks the report generators use for SentryDigest release events.
The library, adapter and tests are identical in SentryDigest, SentryInsight
and GRCInsight; only `site.json` differs.

## Configuration: `site.json`

- `origins`: each site's legacy Pages root, its production origin, and which
  of the two its pages currently emit. Validators accept either configured
  origin; emitted URLs change only when `emitted` is switched.
- `publication`: `mode` and `proof`, read at each source revision. The legal
  states, in order, are `disabled/off`, `prepare/off`, `prepare/on` and
  `active/on`. In `disabled` the publisher builds and validates without
  writing any branch.
- `payload_builder`: the repository's static builder, which produces the
  accepted public payload from a pinned commit.

## Release flow

1. The publisher builds the payload for an exact source commit and writes a
   release descriptor (`_release/descriptor.json`) with the payload digest,
   source revision, content identity and expected origin and repository.
2. It commits the payload under `site/`, the descriptor, the adapter and
   `vercel.json` to the `vercel-production` branch with compare-and-set, only
   past a terminal tip: none, pre-boundary, proved serving, or a provider
   failure attested by an operator. Otherwise the new source is held. Status
   belongs to the exact artifact commit, so a later commit that repeats a
   release key (a second rollback to the same target) is proved on its own.
3. The provider builds that branch with `node _publication/build.js`. The
   adapter refuses a release with proof off, a payload that differs from its
   descriptor, or a build that is not the production build of
   `vercel-production` for the expected repository and host. It then serves
   the payload, the descriptor, a build receipt and
   `_release/served-inventory.txt`.
4. With proof on, the publisher proves the production origin serves exactly
   that release: listing, descriptor, receipt fields, sampled bytes, and a 404
   for the adapter and `vercel.json`.
5. SentryDigest then notifies each downstream site whose last delivered
   content differs, only when publication is `active` both in the release
   and at the current `main` head. Before every send it checks again that
   the release is still the artifact tip, still proved at the production
   origin, and that `main` is still `active`; otherwise delivery is held and
   the next run sends only the consumers still missing.

State records live on the `publication-state` branch; nothing operational
is served. Every run first resumes what the current release still needs.

A rollback targets a release commit that was proved serving and never
attested as a provider failure. Repeating a rollback that is already the tip
is a no-op.

## Generation admission

The report generators record admission on the `publication-admission`
branch around every generation run, whatever the publisher mode, so that
branch is written from the first generation run after these workflows land.
A run is admitted once per Digest commit (`digest:<sha>`) or per scheduled or
manual run (`run:<id>`). A release event must match the descriptor and build
receipt the SentryDigest origin serves, and its generator reads the
commit-addressed feed snapshot. Identical content already in flight or last
analyzed is skipped, including content of a recovered report. Only the run
holding a claim may start the generator, and not while another generation's
outcome is unresolved; a refused claim is released. A run that stops before
invoking releases its claim. A generation that was
cancelled or failed after invoking stays uncertain, and blocks new runs until
its report is recovered (a report commit with the exact `Admission-Key` and
`Admission-Feed` trailers), its saved report handle is re-attached, or an
operator re-admits it with the `readmit` input.

## Commands

```bash
node publication/cli.js publish --source <commit>
node publication/cli.js resume
node publication/cli.js rollback --target <release_key> --reason <text>
node publication/cli.js resolve --release <release_key> --attestation <text>
```

SentryDigest also has `seed` for the activation seed. The report generators
use `admit`, `invoked` and `complete` around each generation.

## Tests

```bash
node --test --test-concurrency=1 publication/test/*.test.js
```

The tests use temporary local repositories and a file-transport remote; they
make no network calls.
