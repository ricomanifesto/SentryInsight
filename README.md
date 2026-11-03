# SentryInsight

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-lockup-dark.png">
    <img src="assets/logo-lockup-light.png" alt="SentryInsight" width="440">
  </picture>
</div>

SentryInsight reads security news and publishes a report about vulnerabilities that are being exploited or need urgent review.

**[Read the latest exploitation report](https://ricomanifesto.github.io/SentryInsight/)**

## What the Report Answers

- What is being exploited?
- Which products and systems are affected?
- How does the attack work?
- Which CVEs and source articles support the finding?
- What should a defender review next?

Each published report is available as a web page and Markdown file. Older reports remain in the [dated archive](https://ricomanifesto.github.io/SentryInsight/reports/).

Contents links and direct finding links open collapsed findings and focus their disclosure controls, including when revisiting the same finding.

## How It Works

1. SentryInsight reads the RSS feed from [SentryDigest](https://github.com/ricomanifesto/SentryDigest).
2. It filters for exploitation-related articles and builds a report with LangGraph.
3. It uses OpenRouter when `OPENROUTER_API_KEY` is set. Local development can use an OpenCode server instead.
4. It writes the canonical report to `index.md`, builds the matching static pages, and archives the previous report when the report date changes.
5. A successful Validate run for a push to `main` starts the automatic GitHub Pages deployment. A maintainer can also dispatch the Pages workflow for a selected branch or tag; that manual path deploys the selected commit without requiring Validate to pass first.

Every current finding cites one or more SentryDigest article identities. Those identities follow SentryDigest's [reporting identity contract](https://github.com/ricomanifesto/SentryDigest/blob/main/contracts/README.md), which keeps links stable across all three reporting projects.

Analysis retains article-owned text and links, or the complete available feed content when article extraction fails. It rejects inputs that exceed the model budget rather than truncating source qualifications. Newly generated reports use schema 4 and require affected versions, their evidence status, exceptions, recommended actions, and vendor links. Existing schema 1–3 reports remain readable without rewriting or reclassifying their evidence.

Before publication, finding status and rendered claims are checked against the retained sources. Conflicting evidence and ambiguous CVE attribution cannot establish confirmed exploitation. These checks use a bounded recognition grammar: unrecognized source phrasing can remain unknown and block publication. A failed validation preserves the previous report and fingerprint. Passing these checks does not establish general English comprehension or independently verify every source claim.

Live generation selects source-owned references for Affected Versions instead of composing version ranges. Each reference binds a complete recognized constraint, including its qualifiers, to a source content hash and exact CVE scope. Internal reference protocol 2 also offers source-bound unresolved references under the narrow eligibility below. The application resolves references to schema-4 text and a host-owned Affected Versions Status before the existing grounding and publication checks; the evaluation adapter uses the same resolver and preparation order. Both reject blocked promotions before removing Source Attribution and normalizing the summary, then resolve references. Free-text claims, stale or wrong-scope references, omitted constraints, parsed contradictions and ineligible unresolved evidence fail closed. Explicit absence is allowed only by the supplied scope contract and is never substituted for an unsupported claim. Integer-only affected-version assertions still require clause classification; an unrecognized assertion cannot authorize absence or disappear behind another source constraint. Fixed releases and severity scores do not establish affected ranges.

Schema 4 defines three affected-version evidence states:

| Status | Meaning and rendered value |
| --- | --- |
| `supported` | Every required recognized source constraint and qualifier is retained. |
| `not_stated` | The scope permits the exact value `Not stated in supplied sources.` |
| `unresolved` | Eligible source evidence remains unclassified; the value is exactly `Unresolved from supplied sources.` |

The unresolved state is limited to findings without CVEs whose cited sources have no recognized affected or excluded version constraints, no explicit version list, and only unclassified numeric prose. It does not classify a number as a campaign name or establish that versions are not applicable. Every unresolved reference binds its source key, content hash, span hash and reason. The model must select all offered unresolved references for its cited sources; it cannot supply the status or turn a rejected claim into uncertainty. The grounding gate recomputes eligibility from those sources. CVE-scoped uncertainty, contradictory constraints, incomplete version lists, ambiguous affected-state assertions and parser failures remain blocked, as does a mixture of known constraints and unresolved evidence. All other detail and exploitation checks still apply.

The initial numeric-prose recognizer is deliberately narrow: a temporal clause describing an attributed event, followed by a counted-device observation. It does not infer prose from a verb anywhere in a paragraph. Release rows, conditional qualifiers, structural lists and other unclassified sentence forms stay blocked. This is a bounded evidence grammar, not general English understanding or campaign-name recognition.

An unresolved finding displays a review notice beside its reporting links. Report metadata and the run log include its count, and the report shows a visible count notice. The `current-findings.json` schema-1 summary remains unchanged. Synthetic offline tests cover the new contract, including the shared production/evaluation adapters; the existing CVE-focused evaluation dataset does not measure no-CVE coverage. This conservative protocol can still block unfamiliar source wording. It does not change source retention, model routing, token allowances or raw diagnostic logging.

Generation receives single and jointly attributed CVE detail scopes built by the same source-scoping function as the publication gate, alongside complete article text and the gate's exploitation assessment across retained sources. It must preserve unknown, negative and conflicting assessments in badges, finding prose and the executive summary, and must not copy unscoped version rows from multi-CVE articles, treat fixed releases as affected releases, or infer earlier affected ranges. Joint version attribution alone does not confirm exploitation. The combined prompt remains subject to the input budget; sources are never truncated to fit. Grounding failures emit bounded JSON diagnostics in the workflow logs: a stable assertion code, affected field, finding position, CVEs, source identities and coverage kind, and SHA-256 fingerprints of the candidate, finding and source content. Expected/observed comparisons contain only allowlisted exploitation states, booleans (required versus present/supported), or bounded entry counts; unavailable comparisons are null and unrecognized values are labeled invalid. Cited sources take priority within the diagnostic size limit. Raw candidate text, source bodies, titles, URLs and exception messages are excluded from those diagnostics. These fingerprints identify the rejected inputs but do not store a replayable source snapshot.

Finding details can inherit an explicit CVE section, including nested headings; sibling CVE sections stay separate. Unowned general text is excluded when explicit CVE sections exist; findings covering multiple CVEs retain each matching section. Headings guide parsing but cannot serve as factual detail values or establish active exploitation. All retained sources naming the CVE contribute detail evidence. Exceptions and recommendations are grounded in their respective source roles. Every recognized recommendation must retain its original paragraph or list-item wording, including abbreviations, wrapped lines, nested list qualifications and internal semicolons, and cannot be omitted by citing another source; parsed version exclusions must be preserved as complete entries in Exceptions. Recognized multiline range qualifiers stay attached to their version constraint. Cumulative-update lists require every listed release; an update named only by a recommendation does not establish an affected-version list or ground an affected-version claim. List detection and constraint collection share complete clause classification. Explicit affected and unaffected assertions take precedence over recommendation context, while descriptive qualifiers remain part of the advice. After complete clause classification, remaining affected/impacted/vulnerable/unaffected language fails closed regardless of its verb chain. Advice and information may end with supported prepositional descriptions such as “on affected systems”; terminal punctuation is allowed, but following details are not exempted. A terminal advice description leaves a pending cue: following release rows activate list validation, while unrelated content and source or section boundaries end that context. A terminal description alone does not introduce an empty list. Explicit affected-version and affected-release list introductions retain their constraints, including following release lines. CVE tags on scoped release rows are attribution metadata and do not erase version constraints; foreign-CVE rows remain excluded. Complete parsed constraints are compared after attribution normalization, retaining qualifiers before or after a CVE tag, including a shared parenthesized or bracketed group. Delimiters inside balanced qualifier groups remain part of one constraint; only top-level delimiters separate release entries. Grouped CVE metadata is removed as an attribution member, retaining the remaining qualifier text, connectors and original connector spacing. Unrecognized mixed attribution fails closed. Other unrecognized descriptive phrasing can conservatively block publication. Recommendation/information clauses also reject structural separators left unclassified by the clause parser; ordered statement context retains wrapped advice without applying later advice to earlier release rows. HTML5 tree construction through `html5lib` handles omitted end tags before article selection and evidence extraction. HTML outer list items retain their nested qualifications and entry boundaries, including repeated soft line breaks. Repeated breaks outside list items retain paragraph separation.

Version assessment also retains a separate view of evidence whose CVE ownership is unknown, overlapping or conflicting. Recognizable version evidence in that view blocks absence. Any unaccounted context blocks an otherwise recognized constraint or exclusion, because a separate paragraph or peer source may qualify it. An explicit, consistent foreign-CVE section can establish disjoint ownership; outside such a section, only a complete simple foreign-CVE/product/release assertion does so. A foreign identifier mentioned in a comparison or a sentence prefix is insufficient. The complete source catalog determines scope groups and peer sources even when a caller supplies a partial detail-context cache. This rejection-only guard adds no new extraction rule or unresolved eligibility, leaves no-CVE behavior unchanged, and may conservatively block additional CVE scopes.

## Run It Locally

SentryInsight requires Python 3.11 and [`uv`](https://docs.astral.sh/uv/):

```bash
uv sync --group dev --frozen
```

For direct OpenRouter access:

```bash
export OPENROUTER_API_KEY=...
export SENTRYINSIGHT_MODEL=openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
uv run python main.py
```

The default model is set in `config/config.json`. `SENTRYINSIGHT_MODEL` overrides it for one environment.

`analysis.max_input_tokens` caps the estimated analysis prompt at 200,000 tokens,
leaving headroom for complete articles and scoped evidence in the default
[Nemotron 3 Ultra free model's 1,000,000-token context](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free).
The estimate uses `cl100k_base`, so it is an application limit rather than an exact
provider token count. When changing models, keep this cap plus `max_tokens`
comfortably below the new model's context limit. Inputs over the cap fail without truncating source
evidence or replacing the published report.

`analysis.max_tokens` allows up to 32,000 output tokens, including reasoning
tokens counted by the provider. OpenRouter responses that reach this limit fail
with `model_output_limit_exceeded` before report validation, without an automatic
retry or replacing the published report. A complete response must still pass
source-grounding and report validation before publication.

To use a local OpenCode server instead, leave `OPENROUTER_API_KEY` unset. Start the server in one terminal:

```bash
opencode serve --port 4096
```

Then run SentryInsight from the repository root in another terminal:

```bash
uv run python main.py
```

Set `OPENCODE_BASE_URL` if the server is not listening on `http://127.0.0.1:4096`.

Report generation fetches live feeds and calls the configured model service. Local validation does neither.

Set `LOGFIRE_TOKEN` to send a trace of each generation run to [Pydantic Logfire](https://logfire.pydantic.dev/docs/). The trace has one span per workflow stage, with counts, outcomes and failure codes. Without the token nothing is exported. Spans never include article text or titles, prompts, model output or validation messages, and recorded exceptions keep only their type. In GitHub Actions the run span also records the workflow run ID, attempt and triggering event, the commit is reported as the service version, and a failed model call records a fixed error class with its HTTP status, provider code and attempt count. The report workflow reads the optional `LOGFIRE_TOKEN` repository secret in the generation step only.

## Validation

Install Chromium once, then run the full local gate:

```bash
npm ci
npx playwright install chromium
bash scripts/local_validation.sh
```

The script installs locked Python and Node dependencies, runs linting, formatting, type checks, and tests, verifies the report and packaged Pages files, and exercises the current and archived pages in Chromium. Browser checks cover accessibility, responsive layouts, stable CVE links, and light and dark themes.

## Report Evaluations

The [frozen-source evaluation pilot](evals/grounding/README.md) compares two prompts
on synthetic article cases, with independent field checks, held-out cases and
complete trial accounting. Calibration runs make no model calls; live runs require
an explicit free model route. Evaluation outputs do not publish reports.
Completed runs can be regraded offline under a separate v2 field contract, with
original grades preserved and skipped checks distinguished from failures. Narrative
claims always require separate source review; regrading is not a model improvement.

## Publishing

- `.github/workflows/generate-report.yml` runs after a SentryDigest update, once daily as a backup, or by manual trigger.
- `.github/workflows/validate.yml` checks pull requests and pushes to `main`.
- `.github/workflows/deploy-pages.yml` automatically publishes the validated `main` commit. A manual dispatch can publish the selected branch or tag without first checking Validate.

The public Pages package contains only the finished report, archive, assets, sitemap, and the versioned reporting contract.

### Source review and partial coverage

New generation performs source review before contacting the model or deciding
that inputs are unchanged. Every retained source is classified as eligible,
review required, or source rejected. A source with ambiguous version ownership
requires review. Contradictory or incomplete version collections remain source
failures. Sources sharing a CVE are held together, including otherwise valid
sources, so removing negative or conflicting evidence cannot change a finding's
assessment. The eligible subset must reproduce the full-catalog evidence
assessments exactly.

Only eligible sources enter the model prompt. Every generated finding must pass
all existing reference, grounding, content, and artifact checks. A failed finding
fails the whole candidate; the application never removes it to obtain a passing
report. If all sources are held, no model is called and the last-good report and
fingerprint stay in place. A valid partial report records every retained source,
including eligible sources the model did not cite. Those uncited sources are
labelled **not represented**, not resolved or irrelevant.

Live reports use schema 5 with host-owned `source_coverage` metadata and a
prominent coverage notice and source disposition table. Review rows are not
findings and do not contribute to finding or CVE counts. Historical schemas 1–4
remain readable; their existing unresolved-version state has not been broadened.
The finding-only `current-findings.json` contract remains schema 1. Static parsing
verifies coverage structure and digests; it cannot re-establish source semantics
without the original source bodies. This coverage is not a complete advisory.

Immutable review packets live in `.sentryinsight-review/<plan_id>.json` with mode
0600. They contain source identity, titles, URLs, source-content hashes, evidence
decision hashes, CVE cohorts, fixed reason codes, and dispositions. They contain
no source bodies or model responses. Local packets remain until explicitly
cleaned up. CI exports only strictly validated metadata, including a terminal
outcome receipt, and requires a valid review-artifact link before committing a
new report. CI artifacts are retained for **90 days**; expiry does not mean a
review item was resolved. Coverage of successful reports also remains in the
dated report history. There is no automatic review approval command.

Offline tools (none contacts a model):

```bash
# Input is a complete JSON array of normalized article objects.
python scripts/review_sources.py preflight articles.json --root /path/to/review
python scripts/review_sources.py inspect /path/to/review/.sentryinsight-review/PLAN_ID.json
python scripts/review_sources.py package --root /path/to/review --output /path/to/new-package
```

Canonical report files, archives, generated site files, and the input fingerprint
are staged and promoted together using a rollback journal. A pre-commit copy
failure restores the prior files. If restoration fails or an intervening edit is
detected, the journal blocks further generation and preserves the available
recovery material. Do not delete it. After all verified copies and directory
syncs succeed, an atomic journal rename records the local commit point. A cleanup
failure after that point keeps the valid new report and a completed manifest;
it blocks the next generation until cleanup succeeds. Recovery verifies hashes
and refuses to overwrite intervening edits or deletions:

```bash
python scripts/review_sources.py recover --root /path/to/report
```

Recovery restores a pending promotion or finishes cleanup of an already committed
or restored promotion. It does not publish to GitHub. If CI review-artifact upload
fails, commit/push is blocked: the disposable runner may contain a validated new
local report while the public last-good report remains unchanged.

Model-backed evaluation retains its full-case denominator. Any held or rejected
source causes an explicit `SourceReviewRequired` abstention before a provider
request is reserved. All-eligible cases pass the same whole-candidate gate as
production. Existing historical fixture grading remains full-case grading; these
abstentions do not measure the quality of partial reports.
