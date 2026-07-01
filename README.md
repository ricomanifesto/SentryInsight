# SentryInsight

<div align="center">
  <img src="assets/logo.png" alt="SentryInsight Logo" width="400"/>
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

SentryInsight can be triggered by updates from [SentryDigest](https://github.com/ricomanifesto/SentryDigest), using the security-news feed as an input for exploitation-focused analysis.

## Architecture

- **LangGraph** orchestrates workflow state and conditional logic.
- **FastMCP** organizes RSS tooling with decorators.
- **Model access** calls OpenRouter directly when `OPENROUTER_API_KEY` is set. Local development can route through an OpenCode gateway.

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

This fetches articles, filters for exploitation content, analyzes threats, and saves reports to `index.md`.

## Validation

Validate a generated report before publishing:

```bash
bash scripts/local_validation.sh
```
