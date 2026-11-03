# Xing synthetic evaluation

This is a bounded evaluation of `xingchen-agi/xing4.0-29b-a4b:free` through
OpenRouter's Phala endpoint. It is not a production model setting, publication
path, or claim of unattended production suitability. Even six passing trials
leave `production_ready: false` and `human_review: not_performed`.

## Data and checks

Six frozen, hash-checked fictional source fixtures use only `example.invalid`
URLs. No feeds, public article bodies, private documents, repository source code,
credentials, or answer keys enter the model messages. The production prompt and
source preflight run locally against those fixtures; only their resulting system
and user messages are submitted. These messages include synthetic source text,
source identifiers and constraints. The API key goes only in the authentication
header to `https://openrouter.ai/api/v1/chat/completions`.

The separate answer file checks complete version constraints, qualifiers,
product/CVE/source ownership, exploitation status, remediation and source
coverage. The same reviewed-report resolver used by the application checks the
whole answer. Joint-CVE ambiguity and a numbered botnet name are held by local
source preflight; the tests check their exclusion and coverage disclosure. They
do not test whether a model can resolve evidence that the application withholds.
The long fixture places known facts at the beginning, middle and end of three
sources among repetitive synthetic background. This is a bounded retrieval
stress test, not representative evidence of real-world report quality.

Calibration uses independently specified fields from `answers.json` and local
reference-formatted reports. It proves the fixtures are accepted by the shared
gate, not that the remote model produces correct reports. A live trial must also
match those answer fields. Semantically equivalent paraphrases can fail this
strict oracle; failures require review rather than relaxed validation or retry.

## Request policy

- Exactly six planned trials, sequential, at most one POST per trial; stop at the
  first HTTP, routing, completion, validation or oracle failure. No retries,
  redirects, alternate models or provider fallback. Starts are at least 60 seconds
  apart. Each inference has a 1,600-second total deadline; public policy checks
  have a 60-second total deadline.
- Immediately before each POST, unauthenticated public metadata must identify
  one active free Phala endpoint, adequate context/output limits and required
  parameters, plus a matching ZDR entry with `safety_retention: false`.
- Every POST specifies `only: [phala]`, `allow_fallbacks: false`,
  `require_parameters: true`, `data_collection: deny`, `zdr: true`, and zero
  maximum prompt/completion/request/image prices. Returned model/provider must
  match. Any reported nonzero cost fails and stops. Missing usage remains null;
  it does not become a verified zero-dollar bill.
- At most 200,000 input tokens counted with the pinned author SentencePiece
  tokenizer plus a 2,048-token framing reserve; 32,000 output tokens including
  reasoning. Reasoning is enabled and excluded from the requested response.
  The unpublished provider chat template means the local count is an estimate,
  with a further 30,144 tokens of context headroom. Returned usage over either
  limit fails without a retry. `finish_reason` must be `stop`.
- Response bodies are bounded to 512 KiB. No tools, plugins, model routers,
  streaming, production promotion, credential management or usage endpoint calls.

Tokenizer data is fetched from the fixed Hugging Face commit in `policy.py` and
SHA-256 verified before loading. No remote Python or model weights are executed
or downloaded. Setup rejects an API key in its environment.

## Offline use

```sh
uv sync --group dev --frozen
uv run python -m evals.xing_synthetic tokenizer --tokenizer /tmp/xing-tokenizer.model
uv run python -m evals.xing_synthetic calibrate --tokenizer /tmp/xing-tokenizer.model
uv run python -W error -m pytest tests/test_xing_synthetic.py -q
```

The tokenizer command makes a public data download; calibration and tests make
zero model requests. Tests use a fake credential and HTTP mock transport with
network connections forbidden. Live mode requires explicit flags, a clean exact
candidate commit and the first attempt of a manual workflow dispatched from
`ricomanifesto/SentryInsight` main. Outputs must be in the disposable runner's
temporary directory, outside the repository. These guards do not themselves
grant permission to install or dispatch a workflow. A separate manual dispatch
can start another run; operator authorization must enforce the run allowance.

## Retention and human review

Default: model answer text is processed in memory and is never written to logs,
summaries or artifacts. Metadata contains only fixed case identifiers, request
hashes, counts, booleans, elapsed time, safe error codes, a constrained response
ID, and numeric usage/cost when reported. A proposed installer uploads this
metadata with `retention-days: 7`.

The optional [private review route](PRIVATE_REVIEW.md) encrypts at most six
512-KiB answers directly in memory to one approved native age recipient. It saves
only ciphertext, including an answer that later fails grounding. Truncated,
wrong-provider, malformed and secret-echoing responses are not retained. Its
ciphertext artifact uses one-day retention, and its local reader rejects an
answer outside its 24-hour review window. No plaintext answer file is created
by the harness. Capturing or decrypting never marks human review complete.

The installer defaults to no answer retention. Its approved-recipient SHA-256
pin is deliberately empty, so requesting encrypted retention currently fails
before setup or credential access. Enabling it requires approval of the exact
public recipient and verification that the human reviewer can decrypt locally;
no real identity is generated, accessed or stored by setup. The public artifact
proposal is replaced by recipient-encrypted delivery, not public plaintext.
The [provider terms, section 21](https://redpill.ai/terms) still require human
review before using or sharing outputs; technical encryption is not a provider
terms approval or an unattended-production qualification.

The seven-day metadata artifact is also public to signed-in readers. GitHub
retention is a service deletion policy, not a guarantee of immediate erasure or
deletion of downloaded copies. Runner temporary files last until the hosted
runner is disposed. Workflow logs retain commands/status under the repository's
existing log-retention setting; the installer redirects CLI results to temporary
files and does not print answer text or usage receipts.

These local controls do not establish the broker's effective account privacy
settings or remove legal/abuse-retention exceptions. Public ZDR metadata and
requested routing are checked, not independently audited. Provider terms and
current free-tier availability must be reviewed before execution. The provider's
human-review requirement prevents treating this pilot as approval for unattended
production use. No credential rotation, top-up or cap change is part of it.
