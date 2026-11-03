# One unpublished Nemotron trial

This is a small functional screen of the real report prompt, OpenRouter client,
source review and whole-candidate validators. It is not a benchmark, human answer
review or proof of production suitability. It never writes or publishes a report
and cannot enable the production generation workflow.

`case.json` is the complete, hash-pinned synthetic fixture. It contains one
fictional Example Gateway advisory and one independent source with an ambiguous
version assertion. Preflight must classify the first source as eligible and hold
the second. Only the eligible source, the existing public report prompt and the
host-derived evidence contracts enter the model request. No URL in this fixture
is fetched. The handwritten `calibration_response` is used only by an in-memory
mock transport; it is never sent to the model and is not a generated answer.

The runner uses the existing `VerificationClient` and adds a transport boundary
that allows only one POST to `https://openrouter.ai/api/v1/chat/completions`.
It pins `nvidia/nemotron-3-ultra-550b-a55b:free` to provider `nvidia`, with no
fallbacks, retries, tools or plugins, and zero prompt/completion/request/image
price ceilings. It checks the live request against the calibrated request hash.
The fixed input must fit 16,000 estimated tokens including a 256-token reserve;
output retains the report pipeline's 32,000-token allowance. No production model
or token configuration is changed.

## Offline preparation

Use the frozen project environment. Set `TIKTOKEN_CACHE_DIR` to a cache containing
the hash-verified `cl100k_base` file. Setup may download that public tokenizer
without inference credentials; the runner itself refuses a missing or changed
cache rather than fetching it implicitly.

```sh
python scripts/verify_nemotron_once.py --output /path/to/new-calibration.json
```

The calibration exercises the actual prompt and validators with a mock response.
Its receipt records source dispositions, request/input hashes and estimated token
count. It makes no provider request and does not read an inference credential.

## Manual trial

The manual-only `Verify Nemotron Without Publication` workflow requires the exact
reviewed `main` commit as `expected_commit`. Its job refuses a different revision,
branch, repository, event or rerun attempt. The runner also checks the checkout
and rejects a dirty tree or an already-used output path. The workflow has only
`contents: read`; checkout credentials are not persisted. The existing
`OPENROUTER_API_KEY` Actions secret is supplied only to the trial step, after
credential-free setup and calibration. No key is created, extracted or changed.

Each separately authorized dispatch permits at most one network attempt. An HTTP
error, timeout or unknown outcome does not authorize another dispatch. The job
guards reject reruns of the same workflow run; this is not a persistent global
ledger preventing a maintainer from starting another new dispatch.

Answers remain in process memory. The application exports only sanitized JSON
metadata for seven days: source/prompt fingerprints, counts, outcome, bounded
provider usage/cost fields when available and a validated-report hash. It does
not export generated text, prompts, source bodies or credentials. Temporary source
review metadata is removed on ordinary exit; runner teardown handles interrupted
execution. Setup logs and generic outcome messages use the repository's existing
Actions log retention. Artifacts are on the public repository under GitHub's
existing access rules; they are not private answer-review artifacts.

On report-validation failure, `validation_diagnostic` adds a fixed stage name,
allowlisted error codes, an allowlisted field name and a bounded finding number
when available. At most eight report-content issues are inspected; a flag marks
truncation and repeated codes are collapsed. Unknown codes and unexpected errors
produce fixed fallback labels. Legacy reporting/artifact exceptions without codes
receive a category rather than an inferred message. No exception message, class
name, traceback, title, URL, CVE, source identifier or candidate/source hash is
added by this diagnostic. Existing receipt fingerprints are unchanged. These
categories can locate a future rejection but cannot recover a discarded answer.
Validation rules, retry limits and seven-day artifact retention are unchanged.

A passing trial requires one attempt, HTTP 200, the exact resolved model, a
complete response, all current evidence/content/artifact validators and the
expected partial source coverage. The `published` and `production_ready` fields
remain false even on success. Raw answers are discarded, so this screen does not
establish independent human quality review or justify resuming generation.

## Provider data and terms

The [free model notice](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free)
says NVIDIA logs use for security and product improvement and excludes personal
or confidential inputs. This synthetic case contains neither. The linked
[NVIDIA trial terms](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)
distinguish internal testing from production use. This workflow is an unpublished
internal trial; it does not establish a production-use entitlement.

[OpenRouter's policy](https://openrouter.ai/docs/guides/privacy/data-collection)
also applies. Account opt-ins and provider retention are not verified by this
runner, and zero data retention is not claimed. Zero-price routing is enforced,
but availability and remaining account quota are unknown until a request; stop
on 429. Do not infer a zero charge from missing usage data. No top-up, subscription
or key-cap change is part of this workflow.
