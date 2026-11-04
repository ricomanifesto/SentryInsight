# Offline report rehearsal

Run the complete production graph against the existing hash-pinned synthetic
case, using an already installed development environment and tokenizer cache:

```sh
python -B scripts/rehearse_report_offline.py \
  --offline-only --tokenizer-cache "$TIKTOKEN_CACHE_DIR"
```

The cache must already contain the verified `cl100k_base` data used by
`verify_nemotron_once.py`. Missing or changed data fails without downloading.
There is no live option, provider credential, workflow, dispatch, or publication
operation. The command writes one bounded JSON receipt to stdout and exits
nonzero on a failed rehearsal invariant. Dependency installation is separate.

The graph, analyzer, prompt builder, OpenRouter client, response checks, source
and finding validators, HTML renderer, manifest builder, fingerprint writer and
transactional artifact promotion are the production implementations. Only the
feed retrieval/enrichment boundary and client transport/budget are substituted.
The real production model-client factory selects the actual OpenRouter client
using a synthetic credential, with `httpx.MockTransport` and the fixture response;
the clock is fixed for deterministic hashes. The
request model, 32,000 output-token setting and zero-price/no-fallback policy
must match the current production configuration.

Each scenario runs admission through the unchanged Node CLI in disposable Git
repositories with a local file remote. The CLI itself creates a valid manual
admission and invocation. The actual Python admission bridge then calls that
CLI for every request reservation and completion. A new client and graph
invocation must respect the same durable history. This exercises the existing
authority and compare-and-set implementation without contacting a repository
service. No production admission branch or checkout remote is used.

Ten scenarios cover a valid report with explicit partial source coverage,
all-held sources with no request, unsupported evidence, an unsupported version
reference, truncated output, a mismatched resolved model, transient rejection followed by success, shared
three-attempt exhaustion, uncertain transport and a simulated lost completion
acknowledgement after the durable completion commits. Failure scenarios retain
a valid scratch site's public artifacts and fingerprint byte-for-byte. Every
run also hashes the checkout's tracked public artifacts before and after. Valid
reports are passed through the existing Pages packager in scratch, comparing
its report, HTML, manifest and generated assets with the promoted files.

Reports, answers, source-review packets, reservation handles and Git history
exist only in automatically removed temporary directories. The retained receipt
contains counts, hashes, fixed stages/diagnostics, mock request disposition,
model identity, fixture/source hashes, checkout commit and finish outcome. It
contains no prompt, source body, answer,
exception text, credentials or scratch paths. Inherited environment settings
are discarded; a scratch HOME isolates Git configuration and credentials.
Python sockets and normal HTTP transports, Node network APIs and all Git
protocols except local file transport are denied. Observability is unconfigured
and tracing/export environment settings are disabled.

This proves local integration with synthetic responses. It does not prove live
provider behavior, quality on the frozen source corpus, GitHub authentication,
branch permissions, CI secret availability, deployment or public serving. The
`publish_results` graph node only marks local readiness; external workflow
publication is outside this command. Forced process termination can leave OS
temporary files for normal OS cleanup; ordinary success and failure remove them.

The metadata-only `verify_report_generation.py` remains useful for unpublished
candidate validation. This command reuses the graph to add actual writing,
rendering, promotion and durable admission checks, without creating a second
report pipeline or changing production defaults.

## Free model selection parity

No production selection change is needed. At the inspected SentryInsight commit
`1e8e9d082b29f4d64d5f75138d360cc894a33032` and GRCInsight commit
`f9a22d23dfee3a0ce22b2981d331bda4411e7836`, the configured workflow defaults
select `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`. Both direct clients
disable fallbacks and set prompt, completion, request and image price ceilings
to zero. Neither production route pins a provider. The rehearsal asserts that
actual production factory and payload contract through its mock transport.

GRC's report workflow requests 8,000 output tokens, while its settings/API
defaults are 16,000. Sentry retains its 200,000 input budget and 32,000 output
allowance, along with exact resolved-ID acceptance, complete-output rejection,
grounding, source coverage and durable request-budget checks. Matching the
selected model does not require changing those report-specific limits or checks.
The separate existing NVIDIA verifier has its own provider pin; this rehearsal
uses the production route and performs no inference request.

Reference sources: GRC's pinned
[workflow](https://github.com/ricomanifesto/GRCInsight/blob/f9a22d23dfee3a0ce22b2981d331bda4411e7836/.github/workflows/lambda-report-generation.yml),
[settings](https://github.com/ricomanifesto/GRCInsight/blob/f9a22d23dfee3a0ce22b2981d331bda4411e7836/agent/config/settings.py),
and [direct client](https://github.com/ricomanifesto/GRCInsight/blob/f9a22d23dfee3a0ce22b2981d331bda4411e7836/agent/services/openrouter_client.py).

Focused regression checks:

```sh
TIKTOKEN_CACHE_DIR="$TIKTOKEN_CACHE_DIR" python -B -m pytest \
  tests/test_offline_report_rehearsal.py -q -p no:cacheprovider
```
