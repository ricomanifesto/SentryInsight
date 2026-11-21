# Defensive publication gate

SentryInsight publishes only one thing: the defensive package rendered by
`scripts/package_defensive.py` (`src/core/defensive_package.py`) from pinned
inputs at one exact commit. Production (the artifact branch, through
`publication/cli.js publish`) and the GitHub Pages mirror both build that
package with the same packager and refuse anything but the approved bytes.

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

1. Commit the canonical, owner-reviewed `config/paid-readiness-facts.json` in a
   review-only pull request. This repository carries no production manifest
   and no owner attestation; none may be invented.
2. Local $0 proposal, with no approval, credentials or remote side effect:

       python3 -B scripts/package_defensive.py build --revision <head> \
         --output <new directory outside the repository>

   It prints the proposed triple. Independent review rebuilds it at the same
   head and must obtain the same `package_sha256`.
3. Merge the review-only pull request. Validate is synthetic-only and nothing
   chains from it, so the code-only head merges without repackaging a prior
   release.
4. Separately authorized pure promotion: dispatch **Publish Production** and
   then **Deploy GitHub Pages** manually on `main`, first attempt, with the
   reviewed triple. Any other event, ref, attempt or digest refuses.
5. Only if the paid evidence is needed: one manual **Generate Exploitation
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

## Checks the owner makes read-only before any push

These cannot be proved from the repository:

- Vercel project: the effective Production Branch is the artifact branch,
  Root Directory is the repository root of that branch, and the Build and
  Output settings are overridden by the artifact's own `vercel.json`. Source
  branches carry the root `vercel.json` with `git.deploymentEnabled: false`,
  so commits on them create no preview deployment; confirm the project honors
  it (deployment list shows no source-branch builds).
- GitHub Pages: the source is "GitHub Actions", so only the
  **Deploy GitHub Pages** workflow deploys.
- No other workflow, app or integration can push the artifact branch or
  deploy Pages (branch protection, environments, installed apps).
