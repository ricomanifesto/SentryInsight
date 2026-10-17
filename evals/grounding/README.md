# Frozen-source report evaluation

This pilot compares the existing report prompt (`baseline`) with the same prompt
plus an evidence checklist (`checklist`). It uses `pydantic_evals` to execute and
grade 12 synthetic article cases: eight development cases and four held-out cases.
It calls the real `analyze_exploitation` prompt builder through an injected model
client. It never fetches feeds, writes the public report, or deploys pages.

## Run

Install the locked development dependencies with `uv sync --group dev --frozen`.
Run from the repository root in a fresh process:

```sh
# No model calls: replay answer-derived reference reports to calibrate checks.
uv run python -m evals.grounding calibrate --split all --output test-results/eval-calibration

# Six smoke trials: three development cases, both prompts, one repetition.
# Supply OPENROUTER_API_KEY through the environment. Unset SENTRYINSIGHT_MODEL.
uv run python -m evals.grounding run --live \
  --model openrouter/nvidia/nemotron-3-ultra-550b-a55b:free \
  --split development --limit 3 --repetitions 1 --output test-results/eval-smoke

# After inspecting the smoke results: 12 cases × 2 prompts × 3 repetitions.
uv run python -m evals.grounding run --live \
  --model openrouter/nvidia/nemotron-3-ultra-550b-a55b:free \
  --split all --repetitions 3 --concurrency 2 --output test-results/eval-comparison
```

Use a new output directory for every run. The runner refuses to overwrite prior
results. Explicit `:free` OpenRouter models are required; routing sets all price
ceilings to zero and disables provider fallback. Unavailable free capacity is an
execution error. There is one attempt per trial, at most two concurrent requests,
a maximum of three repetitions, 8,000 output tokens per request, temperature 1,
and a 240-second trial timeout (180-second HTTP timeout). No paid fallback or
LLM judge is used. Free-service quotas can prevent a complete run.

The CLI disables OpenTelemetry and Logfire export before SDK/application imports
and does not configure application telemetry. Use the CLI in a fresh ordinary
Python process, not an already instrumented notebook. Live model runs send the
synthetic source material and report prompts to the named provider. Raw reports
stay in the local output directory; they are not uploaded to Logfire.

## Dataset and answer ownership

`evals/grounding/data/sources.json` owns the articles, stable case identities and
split. `answers.json` separately owns expected fields, supporting source quotes,
rationales, review status and source-byte digests. A separate source-only review
checked every label before model execution and corrected two ambiguous fixtures:
a question heading is not confirmation, and hypothetical exploitation is potential.
These labels have independent automated review, **not human review**.

The model receives articles and production-generated evidence context. Case names,
categories, splits, gold fields and rationales are withheld; article URLs use
neutral identities. The production evidence recognizer remains part of the prompt
under evaluation. It is deliberately not the grading oracle.

The cases cover direct confirmation, explicit denial, likelihood-only reporting,
conflicting sources, a question heading, sibling-CVE ownership, fixed versus
affected releases, hypothetical exploitation, qualified recommendations, degree
negation, source instruction injection, and platform-specific version exceptions.
Vendor links mean supplied source links, not the article's reporting identity.
Conflict maps to `unknown`; explicit denial maps to `not_observed`. The benchmark
checks fidelity to supplied claims, not whether those claims are true in the world.

Keep the four holdouts out of prompt tuning. Freeze prompt, dataset and grading
policy before running them. Once their model failures influence a revision, they
are development examples; create fresh holdouts for the next comparison. Repeated
trials measure variability on these same 12 cases, not 72 independent examples.

## What the grades establish

The independent grader checks required finding structure, finding coverage, CVE
identity, exact exploitation status, affected versions, exceptions, recommended
actions, vendor links and citation sets. Whitespace is normalized; one terminal full stop is also normalized for version,
exception and recommendation phrases. Status values and URL punctuation remain
exact. Internal punctuation and qualifiers remain significant. Code blocks and
HTML markup cannot provide report structure and are rejected by the pilot. Required
scored fields must occupy one line. Wrapped continuations fail structure rather
than being silently ignored. Severity and Action have schema checks only; their
semantic correctness is not scored.

The test suite calibrates positive reference controls against deliberate wrong
statuses, omissions, duplicate fields, fenced pseudo-reports, conflicting field
continuations, lost qualifiers, exchanged CVE versions, unsupported links and
bad citations. References are generated from answer keys: their pass rate is a
**calibration result**, not evidence of model quality.

An exact-field pass does not prove arbitrary descriptions or summary prose are
correct. An exact-field failure can be harmless paraphrasing. Review raw reports
before treating either as a semantic verdict. Gate acceptance/rejection
**disagreements** compare these checks to a replay of the current evidence,
reporting-identity, content and artifact validators. This replay uses the workflow
normalizers and source-derived expected-CVE check, but omits fetching, publication,
and runtime site behavior. It is not a
production execution receipt. Neither disagreement count proves an unsafe
acceptance or unnecessary rejection without manual adjudication.

## Run evidence

- `manifest.json`: planned trial IDs, Git commit and dirty flag, source-file
  hashes, dataset hash, dependencies, Python version, timing and completion flag.
  A source change during execution leaves the run incomplete.
- `trials.jsonl`: each completed trial is saved immediately, including elapsed
  time, exact output, input hash and sanitized error type.
- `model-receipts.jsonl`: request hash, selected/reported model, provider, request
  policy, output limit, finish reason and provider-reported usage/cost. Missing
  usage is unknown, not zero. Credentials and raw provider errors are excluded.
- `graded.json`: per-trial field checks and validation-gate outcomes.
- `summary.json`: complete/error counts and each check's denominator, split by
  prompt and development/holdout. Errors do not disappear from planned totals.

The command exits with code 2 for execution errors. Quality failures remain
experiment results, not a CI approval signal. An incomplete manifest is never a
finished experiment. No live model-quality score is checked into this pilot.

## Versioned regrading of saved runs

The original commands and `grading.py` retain the v1 contract. To diagnose an
existing completed run under `grounding-fields-v2`, use a fresh process and a
new output directory outside the original run:

```sh
uv run python -m evals.grounding.regrade \
  --input test-results/eval-comparison \
  --output test-results/eval-comparison-grading-v2
```

This command makes no model requests, runs no production validation gate, and
disables telemetry export. It verifies the frozen source/key/grader hashes,
dataset and input digests, complete trial identities, raw reports and original
v1 grades before writing. A checksum records identity, not independent approval
or protection against coordinated tampering. Incomplete or inconsistent runs
are rejected; existing destinations are never overwritten. Results retain every
original graded record, report hash and the original gate receipt. The new
manifest records input and grading-code hashes and marks completion only after
a final source/input check.

V2 deliberately changes three grading policies:

- A structural failure leaves dependent checks `not_evaluated`, with a reason.
  Missing expected findings also prevent dependent field comparison. Summaries
  show pass, fail and not-evaluated counts against the full planned denominator;
  model execution errors remain visible.
- One redundant `Affected versions:` prefix is ignored in that field. Values,
  internal punctuation and qualifiers still have to match the answer key.
- CVE ownership is scoped to each finding's title and structured fields. Extra
  identifiers elsewhere are listed for narrative review; neither rejection nor
  affirmation of those identifiers is automatically classified as factual.

Prerequisites remain distinct from unaffected-environment exceptions. Placing a
source-exact prerequisite in Exceptions is a field-role mismatch, not evidence
of fabrication. The v1 conditional case rationale said it checked status only,
although the implementation checked every field. V2 explicitly grades all
listed fields and retains that strict role policy; it does not change the old
answer file or retrospectively relabel the old score.

Every returned report has a separate `narrative_review: not_evaluated` result.
Review titles, descriptions, summaries and other prose against the sources.
`data/narrative_review_pairs.json` supplies development anchors for polarity,
component attribution, prerequisites versus mechanisms, affected versus attacked
versions, and prevalence versus likelihood. These are agent-authored review
anchors requiring human review, not a trained classifier or an LLM judge.
Both sides intentionally pass field grading in tests, proving that field-pass
does not certify prose. Preserve the positive and negative sides when proposing
validator changes; accepting a supported denial must not admit an unsupported
affirmative claim.

Regrading changes the measurement, not the model or product behavior. Do not
compare v1 and v2 scores as a product improvement. Previously inspected holdouts
are development evidence for subsequent tuning. A new prompt or production-path
claim needs a frozen rubric, fresh held-out sources and a separate experiment.
