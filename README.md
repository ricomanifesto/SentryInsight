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

Analysis retains article-owned text and links, or the complete available feed content when article extraction fails. It rejects inputs that exceed the model budget rather than truncating source qualifications. Newly generated reports use schema 3 and require affected versions, exceptions, recommended actions, and vendor links, with explicit absent values. Existing schema 1 and 2 reports remain readable.

Before publication, finding status and rendered claims are checked against the retained sources. Conflicting evidence and ambiguous CVE attribution cannot establish confirmed exploitation. These checks use a bounded recognition grammar: unrecognized source phrasing can remain unknown and block publication. A failed validation preserves the previous report and fingerprint. Passing these checks does not establish general English comprehension or independently verify every source claim.

Generation receives a per-CVE detail view built by the same source-scoping function as the publication gate, alongside complete article text. It must not copy unscoped version rows from multi-CVE articles, treat fixed releases as affected releases, or infer earlier affected ranges. The combined prompt remains subject to the input budget; sources are never truncated to fit. Grounding failures emit bounded JSON diagnostics in the workflow logs: the check code, finding position, CVEs, source identities and coverage kind, and SHA-256 fingerprints of the candidate, finding and source content. Raw candidate text, source bodies, titles, URLs and exception messages are excluded from those diagnostics. These fingerprints identify the rejected inputs but do not store a replayable source snapshot.

Finding details can inherit an explicit CVE section, including nested headings; sibling CVE sections stay separate. Unowned general text is excluded when explicit CVE sections exist; findings covering multiple CVEs retain each matching section. Headings guide parsing but cannot serve as factual detail values or establish active exploitation. All retained sources naming the CVE contribute detail evidence. Exceptions and recommendations are grounded in their respective source roles. Every recognized recommendation must retain its original paragraph or list-item wording, including abbreviations, wrapped lines, nested list qualifications and internal semicolons, and cannot be omitted by citing another source; parsed version exclusions must be preserved as complete entries in Exceptions. Recognized multiline range qualifiers stay attached to their version constraint. Cumulative-update lists require every listed release; an update named only by a recommendation does not establish an affected-version list or ground an affected-version claim. List detection and constraint collection share complete clause classification. Explicit affected and unaffected assertions take precedence over recommendation context, while descriptive qualifiers remain part of the advice. After complete clause classification, remaining affected/impacted/vulnerable/unaffected language fails closed regardless of its verb chain. Advice and information may end with supported prepositional descriptions such as “on affected systems”; terminal punctuation is allowed, but following details are not exempted. A terminal advice description leaves a pending cue: following release rows activate list validation, while unrelated content and source or section boundaries end that context. A terminal description alone does not introduce an empty list. Explicit affected-version and affected-release list introductions retain their constraints, including following release lines. CVE tags on scoped release rows are attribution metadata and do not erase version constraints; foreign-CVE rows remain excluded. Complete parsed constraints are compared after attribution normalization, retaining qualifiers before or after a CVE tag, including a shared parenthesized or bracketed group. Delimiters inside balanced qualifier groups remain part of one constraint; only top-level delimiters separate release entries. Grouped CVE metadata is removed as an attribution member, retaining the remaining qualifier text, connectors and original connector spacing. Unrecognized mixed attribution fails closed. Other unrecognized descriptive phrasing can conservatively block publication. Recommendation/information clauses also reject structural separators left unclassified by the clause parser; ordered statement context retains wrapped advice without applying later advice to earlier release rows. HTML5 tree construction through `html5lib` handles omitted end tags before article selection and evidence extraction. HTML outer list items retain their nested qualifications and entry boundaries, including repeated soft line breaks. Repeated breaks outside list items retain paragraph separation.

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

## Validation

Install Chromium once, then run the full local gate:

```bash
npm ci
npx playwright install chromium
bash scripts/local_validation.sh
```

The script installs locked Python and Node dependencies, runs linting, formatting, type checks, and tests, verifies the report and packaged Pages files, and exercises the current and archived pages in Chromium. Browser checks cover accessibility, responsive layouts, stable CVE links, and light and dark themes.

## Publishing

- `.github/workflows/generate-report.yml` runs after a SentryDigest update, once daily as a backup, or by manual trigger.
- `.github/workflows/validate.yml` checks pull requests and pushes to `main`.
- `.github/workflows/deploy-pages.yml` automatically publishes the validated `main` commit. A manual dispatch can publish the selected branch or tag without first checking Validate.

The public Pages package contains only the finished report, archive, assets, sitemap, and the versioned reporting contract.
