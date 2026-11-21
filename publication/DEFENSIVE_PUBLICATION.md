# Defensive publication gate

SentryInsight publishes only one thing: the defensive package rendered by
`scripts/package_defensive.py` (`src/core/defensive_package.py`) from pinned
inputs at one exact commit. Production (the artifact branch, through
`publication/cli.js publish`) and the optional GitHub Pages mirror use the
same packager and require the approved bytes.

## What the package contains

The packager reads exactly these paths as committed blobs at the pinned head,
and no other tree entry:

- `config/paid-readiness-facts.json`: the canonical, owner-reviewed fact
  manifest (closed schema, approved state, commit-addressed references at an
  allowlisted provider);
- `site/` templates, the static assets listed in `scripts/package_pages.py`,
  and `contracts/reporting-identity-v1.json`.

It renders Markdown with the host-only renderer, stages a clean temporary
tree, builds the pages with `scripts/build_site.py`, checks every outward URL
against the reviewed set, applies the Pages package shape and the static
artifact public-path policy, and refuses any dated report file. Every
verification boundary (packager build, `verify`, and the Node publisher)
checks names before reading bytes, refusing control characters (newline
included), backslashes and dot segments, and requires the closed generated
path inventory exactly (`closed_inventory()` in Python, `CLOSED_PATHS` in
`publication/kit/defensive.js`, kept equal by test). The legacy
root `index.md`, `index.html` and `reports/` are never listed, read or copied,
even when present. The timestamp is the pinned commit's committer time unless
`--generated-at` pins one explicitly, so the same inputs give the same bytes.

## The approval triple

1. `head`: the exact 40-hex main commit;
2. `facts_sha256`: SHA-256 of the committed `config/paid-readiness-facts.json`
   bytes at that head;
3. `package_sha256`: the package inventory digest, the publication kit's
   `inventoryDigest` (SHA-256 over `<sha256>  <path>` lines sorted bytewise,
   `publication/kit/canonical.js`). It is the descriptor's `payload_digest`.

The publisher verifies all three before it reads the artifact branch, resumes
anything, writes a state record or pushes a ref, and re-verifies immediately
before the push. Pages re-verifies immediately before its upload. An approved
build, and the direct Node publisher, also refuse unless the actual checkout
`HEAD` is the approved head.

## Release sequence

1. Merge the reviewed code-only pull request after the merge checks below.
   The main push runs synthetic Validate and Workflow Lint. Leave Pages
   disabled and confirm the existing release is still serving.
2. Merge the canonical, owner-reviewed `config/paid-readiness-facts.json` in a
   separate review-only pull request under the same merge checks. Use a
   real owner-reviewed manifest and attestation.
3. After the facts merge, pin the exact 40-hex current `main` SHA as `head`.
   Set `package_dir` to a new directory outside the repository.

       python3 -B scripts/package_defensive.py build --revision "$head" \
         --output "$package_dir"

   Omit `--generated-at` so the package uses that commit's committer timestamp.
   An independent rebuild from the same SHA must reproduce both digests.
   Obtain owner approval of that exact SHA, facts digest and package digest.
   If `main` advances, rebuild and obtain approval for the new triple.
4. For an authorized Vercel-only promotion, complete the promotion checks
   below, then dispatch **Publish Production** manually on `main`, first
   attempt, with the approved triple. Confirm the live descriptor matches the
   approved source SHA and package digest. Keep Pages disabled.
5. A Pages promotion is optional and requires separate authorization and the
   Pages checks below. Dispatch **Deploy GitHub Pages** manually on `main`,
   first attempt, with the same approved triple for the current head.
6. Only if the paid evidence is needed: one manual **Generate Exploitation
   Report** paid readiness dispatch (one Kimi attempt, hard cap $2.42). Its
   acknowledgment is outside this $0 package gate and changes no package
   bytes.

## Held legacy paths and owner hold

- Rollback is held. `publication/cli.js resume` and `rollback` are refused
  before any configuration, Git or network access, and the publisher holds
  them too, before extraction or ref writes. Promotion accepts only the exact
  current `main` head, so an earlier head cannot be re-promoted either.
  Restoring earlier content means a new review-only pull request that
  recommits the earlier reviewed facts at a new head, a new local proposal,
  independent review and a new approved triple; until then the owner hold
  below applies.
- A defensive publish never resumes the legacy tip. An unproved tip holds the
  promotion; the safe owner hold is to leave the artifact branch and prior
  live site as they are, inspect the state records read-only, and record a
  provider failure with `publication/cli.js resolve` only when it is real.
- The hosted legacy generator is held: Generate Exploitation Report has only
  the manual paid readiness job, reached solely by `paid_verification`, with
  no schedule, SentryDigest dispatch, legacy checkout, model run, artifact or
  screenshot upload, report commit, push or resume. The paid job checks out
  the exact head sparsely, without the legacy report, pages or archives, and
  needs no surface approval. `main.py` remains for offline/local use.
- Validate checks out sparsely without the current report and pages, dated
  archives, correction exchanges, `config/paid-readiness-facts.json` or the
  surface approval, proves they are absent, and only then runs
  `scripts/validate_synthetic.sh`.
- `scripts/build_static_artifact.py`, `scripts/package_pages.py` and
  `scripts/local_validation.sh` stay as offline/local helpers; no workflow
  publishes their output.

## Read-only checks before merging

- Confirm Vercel is connected to `ricomanifesto/SentryInsight`. The production
  branch is `vercel-production` and the Root Directory is the repository root.
  The project's Ignored Build Step allows only `vercel-production` to build.
  Source branches also set `git.deploymentEnabled: false` in their root
  `vercel.json`.
- Confirm GitHub Pages is off, **Deploy GitHub Pages** is disabled, and the
  existing production release is serving. A code-only merge changes neither
  host's settings and authorizes no promotion.

## Read-only checks before promotion

- Vercel builds the artifact branch with `node _publication/build.js`. The
  adapter writes Build Output API files to `.vercel/output`. The dashboard
  Output Directory override is off.
- Artifact-branch writer exclusivity is unverified. Hold Vercel promotion
  until the owner confirms from effective branch rules and integration
  permissions that only the approved publisher can write
  `vercel-production`.
- For a separately authorized Pages promotion, verify GitHub Pages uses
  GitHub Actions as its source and that only **Deploy GitHub Pages** can deploy
  it. Verify the environment and integration permissions before dispatch.
