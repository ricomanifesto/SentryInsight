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

SentryInsight can be triggered by updates from [SentryDigest](https://github.com/ricomanifesto/SentryDigest), using the security-news feed as an input for exploitation-focused analysis.

## Architecture

- **LangGraph** orchestrates workflow state and conditional logic.
- **FastMCP** organizes RSS tooling with decorators.
- **Model access** uses the official OpenAI SDK and Responses API.

## Setup

Install dependencies:

```bash
uv sync --group dev
```

Provide OpenAI model access:

```bash
export OPENAI_API_KEY=...
```

Configure feeds, output paths, and the default model in `config/config.json`.

Override the model for one environment:

```bash
export SENTRYINSIGHT_MODEL=gpt-5.6-sol
export OPENAI_REASONING_EFFORT=xhigh
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
