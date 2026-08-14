# SentryInsight

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-lockup-dark.png">
    <img src="assets/logo-lockup-light.png" alt="SentryInsight" width="440">
  </picture>
</div>

SentryInsight turns security RSS feeds into exploitation-focused threat reports, with CVE correlation, affected systems, attack vectors, and executive summaries ready for review.

[![Latest Exploitation Report](https://img.shields.io/badge/View-Latest%20Report-blue)](https://ricomanifesto.github.io/SentryInsight/)

## What It Does

SentryInsight monitors security feeds for exploitation activity, extracts relevant vulnerability signals, and generates a published report for review. The reports are shaped for fast triage: what is being exploited, what systems are affected, how the attack works, and what threat activity is visible.

## Report Coverage

Generated reports can include:

- executive summaries
- CVE extraction and correlation
- affected systems and technologies
- attack vectors
- threat actor activity
- exploitation context from monitored feeds

## Relationship to SentryDigest

SentryInsight can be triggered by updates from [SentryDigest](https://github.com/ricomanifesto/SentryDigest), using the security-news feed as an input for exploitation-focused analysis. Digest incident handoffs can use stable `#cve-YYYY-NNNN` fragments: the static page lands near that CVE without JavaScript, while the enhanced reader focuses the matching finding or reports an honest current-report fallback. Reporting-card fragments follow SentryDigest's versioned `contracts/reporting-identity-v1.json` vectors; CI executes a byte-identical copy of the owner-maintained verifier and rejects drift in either the verifier or contract. SentryDigest's [reporting identity runbook](https://github.com/ricomanifesto/SentryDigest/blob/main/contracts/README.md) defines ownership, immutable revisions, consumer adoption order, and the family gate inventory.

## Architecture

- **LangGraph** orchestrates workflow state and conditional logic.
- **Model access** calls OpenRouter directly when `OPENROUTER_API_KEY` is set. Local development can route through an OpenCode gateway.
- **A versioned Markdown artifact** owns report dates, complete CVE IDs, and triage metadata.
- **A deterministic static builder** publishes the latest report and immutable dated history from one canonical template tree.
- **An allowlisted Pages artifact** exposes only finished report, archive, and asset files after validation succeeds.

## Setup

Install dependencies:

```bash
uv sync --group dev
```

Provide model access with OpenRouter:

```bash
export OPENROUTER_API_KEY=...
```

Or run a local OpenCode server:

```bash
opencode serve --port 4096
```

Configure feeds, output paths, and the default model in `config/config.json`. Model IDs use `provider/model` format.

Override the model for one environment:

```bash
export SENTRYINSIGHT_MODEL=openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
```

If OpenCode is not listening on `http://127.0.0.1:4096`, set:

```bash
export OPENCODE_BASE_URL=http://127.0.0.1:4096
```

## Usage

```bash
uv run python main.py
```

This fetches articles, filters for exploitation content, analyzes threats, and stages a complete static publication rooted at `index.md` and `index.html`. Each schema-version 2 finding must cite one or more input-owned reporting keys; publication resolves those keys to original publisher links and the matching dated SentryDigest context. When the report date advances, the previous artifact is archived under `reports/`.

## Validation

Validate a generated report before publishing:

```bash
bash scripts/local_validation.sh
```

The validation gate checks Python behavior and formatting, artifact integrity, generated-site drift, the packaged Pages tree, bundled frontend dependencies, accessibility interactions, responsive layouts, and light/dark browser screenshots. The validation and generation workflows link the screenshot artifact from their run summaries for visual review.
