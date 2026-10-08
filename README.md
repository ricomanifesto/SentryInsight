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

Before publication, finding status and rendered claims are checked against the retained sources. Conflicting evidence and ambiguous CVE attribution cannot establish confirmed exploitation. Explicit CVE-bound past intrusion reports and recognized past-tense confirmation predicates establish observed exploitation, independent of time-adverb wording. They do not establish ongoing activity. Tense belongs to the exploitation predicate: an incidental past confirmation does not turn a current exploitation statement into a historical one, and a current confirmation does not make past exploitation ongoing. Historical-only findings cannot promote their badge, narrative or summary to active exploitation; negatives and conflicts remain part of the assessment. Assertion and directive qualifiers belong to parsed source relations. Explicitly unknown source claims remain distinct from required relations that the bounded grammar cannot interpret: those relations fail with `unsupported_evidence_relation`. Unrelated article prose does not require a semantic interpretation. A failed validation preserves the previous report and fingerprint. Passing these checks does not establish general English comprehension or independently verify every source claim.

Generation uses immutable finding records built from the publication gate's shared assessment and detail collector. The model returns a closed JSON plan containing finding and excerpt references only; it cannot supply badges, factual prose, source identities or version values. A deterministic renderer retains complete version constraints, exceptions and recommendation blocks, including negative and conflicting evidence. Joint scopes are grouped when needed to preserve jointly owned assertions or details, avoiding duplicate singleton findings. Intersecting joint assertions, including negative and unsupported relations, survive selection before assessment; a joint predicate cannot be silently reduced to independent singleton claims. Missing, duplicate, foreign or unsupported plan references fail closed before publication. Finding membership uses the established exploitation-relevance rule, including negative or unknown activity, and explicitly high/critical risks with recognized impact or attack details. Required positive-activity CVE coverage is unchanged. Routine context does not become a mandatory finding; selecting a CVE still retains every supplied supporting, contrary and contextual source for that CVE. Jointly owned details remain complete. If no eligible scope exists, generation fails before a model call and preserves the previous report. The rendered report still passes the same evidence, content and artifact gates.

Optional narrative excerpts require an explicitly attributed CVE paragraph or section, exclude page furniture, and pass whole-finding evidence checks. Source link labels and their original paragraphs are retained separately from the unchanged article text; only explicitly labeled, owned advisory references become vendor links. Bare URLs do not establish advisory roles, and repeated indistinguishable advisory paragraphs fail closed rather than sharing links across CVE sections. Metadata-only CVEs retain identity coverage with an explicit attribution limit; metadata cannot confirm exploitation or manufacture body-detail ownership. Explicit scoped severity ratings are retained; unrecognized, qualified or conflicting ratings remain unknown. Action badges require unqualified affirmative source recommendations. Recommendation interpretation produces source-owned directives with modality, polarity, conditions and coordinated verb/object clauses before badge selection. Explicit audience advice is distinct from a bounded whole-object imperative grammar, so action-looking nouns do not establish instructions. Bounded audience noun qualifiers retain modal ownership; recognized reported or epistemic clauses retain their qualification, while unsupported audience bridges block publication. Conditions and polarity belong to their directive or coordinated clause. Independent action targets survive unrelated qualifications, while same-target prohibitions/conflicts still constrain the badge. Continuation references bind only within their retained source block; unresolved references remain conservative. Alternatives and unrecognized targets cannot inherit an unconditional badge from the first verb. The same parsed representation supplies recommendation roles and badge projection. A required unclassified directive blocks publication instead of silently becoming an unknown or no-action badge. Prohibitions and conditional directives remain intact without becoming unconditional actions. The single badge prioritizes patch, mitigate, investigate, then monitor; recognized qualified guidance remains complete with an explicit context note and no unconditional badge. Source excerpts also populate the product, technique and actor sections. These bounded eligibility rules do not guarantee that a model selects the most useful excerpt or that all source phrasings are recognized. The complete article context remains available, and both the source and combined prompt must fit the input budget without truncation.

Grounding failures emit bounded JSON diagnostics in the workflow logs: a stable assertion code, affected field, finding position, CVEs, source identities and coverage kind, and SHA-256 fingerprints of the candidate, finding and source content. Expected/observed comparisons contain only allowlisted exploitation states, booleans (required versus present/supported), or bounded entry counts; unavailable comparisons are null and unrecognized values are labeled invalid. Cited sources take priority within the diagnostic size limit. Raw candidate text, source bodies, titles, URLs and exception messages are excluded from those diagnostics. These fingerprints identify the rejected inputs but do not store a replayable source snapshot.

Source roles are nonexclusive: a paragraph containing both descriptive facts and recommendations remains available as complete narrative context and complete guidance. Recommendation statements retain ordered explicit and referential clauses. A reference cannot erase an earlier explicit instruction; its conditions or prohibition constrain its supported antecedent. Unparsed intervening statements break reference ownership. Supported noun quantifiers retain audience scope and polarity. These boundaries are exercised together through the offline publication pipeline, including joint CVE scopes and mixed paragraph roles.

Action inference uses a closed verb/argument contract. Installing or applying patches, patching systems or identified flaws, and upgrading/updating systems or numbered releases can establish patch guidance. Upgrade/update destinations use `to version <number>`, with an optional system object. Applying workarounds or mitigating identified risks establishes mitigation; investigating evidence or reviewing logs establishes investigation; monitoring recognized evidence, systems or advisories establishes monitoring. Consult/contact/advisory-review guidance stays complete without a remediation badge. Named cumulative-update and affected-release arguments reuse identities and qualifiers parsed by the existing version owner; its role grammar does not establish directive modality. Prohibited or conditional implicit targets constrain action projection without asserting an unconditional positive action. Unsupported required verb/target combinations block publication: updating an advisory does not imply patching a system. Conjunctive clauses share their governing polarity until an explicit audience/modal or adversative `but` branch establishes a new scope. Alternatives remain qualified, and sequential clauses retain their source order. Object coordination, destinations, conjunctions, conditions and reference limits are tested together; this finite grammar does not claim to interpret every English instruction.

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
