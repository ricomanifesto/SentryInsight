# Private synthetic-answer review

This optional route replaces public plaintext artifacts with single-recipient
[age](https://github.com/FiloSottile/age) encryption. It changes neither the six
request plan nor the model/provider policy, answer oracle or production promotion
boundary. The existing no-answer-retention mode remains the default.

## Recipient and access

Only one canonical native X25519 `age1...` public recipient is supported. SSH,
plugins, multiple recipients, recipient files, passphrases and private identities
are rejected as recipient input. The installer contains a hardcoded
`APPROVED_REVIEW_RECIPIENT_SHA256`; it is deliberately empty in this candidate.
The dispatch input cannot replace that pin. Missing or mismatched approval fails
before setup or the inference secret is made available. Native age validates the
recipient checksum before the first model request.

Before enabling capture, the owner must provide an **existing public recipient**,
approve its exact SHA-256 over canonical UTF-8 bytes with no newline, and
demonstrate local decryption of a synthetic challenge. Never provide the private
identity to GitHub, the model service, an agent or a chat. If no suitable identity
exists, creating one is a separate owner decision; setup does not create keys.
No repository access, GitHub secrets, account permissions or provider keys need
to change. Committing the approved public fingerprint is a separate reviewed
configuration/release action, and execution remains separately authorized.

The GitHub runner and model services necessarily process plaintext in memory.
The encryption subprocess receives only the answer on stdin and public recipient
on its argument list. It receives no API key, home/config, proxy or agent
environment. Hash-pinned age v1.3.2 binaries are used on Ubuntu x86-64 and macOS
arm64; archives and extracted binaries are both checked. Only the `age` binary
is extracted; no key-generation program is installed by this helper. Binary
distribution is trusted through pinned official GitHub release hashes; no
independent Sigsum signature verification is claimed.

Each complete transport answer is encrypted before shared grounding/oracle
evaluation. The envelope binds the exact candidate SHA, workflow run ID, first
attempt, case, request SHA-256, recipient fingerprint, creation and expiry times.
An answer that subsequently fails validation can therefore be privately reviewed.
Encryption or file-write failure stops further model requests; partial output is
removed without replacing an existing result. Raw provider errors and exceptions
are not retained. Reasoning traces are not saved.

GitHub receives only final `encrypted-review/*.age` files, at most six. Each
answer is at most 512 KiB; the JSON envelope adds at most 4 KiB, and ciphertext
has another 4-KiB bound. No plaintext answer files or raw answer upload steps
exist. Ciphertext files have owner-only local permissions.
Public metadata retains ciphertext digests, case, recipient fingerprint,
timestamps and existing evaluation metadata; it contains no answer.

Anyone with public-repository artifact access can download ciphertext. They
cannot read its contents without the matching private identity under age's
cryptographic assumptions. This does not protect against a compromised runner,
reviewer device, private identity, or provider internals. Public recipient and
metadata are not secrets. Changing the recipient requires another explicit
approval; it is not an automatic fallback.

## One-day retention and its limits

The encrypted-answer artifact uses `retention-days: 1`; safe metadata remains
seven days. Verify actual artifact expiry after an eventual approved upload.
There is no remote artifact or expiry timestamp to verify during local tests.
Each answer also has an exact 86,400-second window from creation. The local reader
checks it before releasing plaintext and rejects future-created, expired or
malformed windows. A long six-case run gives different case expiry times.
The reader depends on a correct local clock.

GitHub retention is a deletion policy, not guaranteed instantaneous erasure.
Encryption cannot revoke downloaded copies or make a retained private key stop
working after a day. An owner can still decrypt with native age after expiry;
the helper's expiry is an application policy, not cryptographic destruction.
Runner temporary files last until hosted-runner disposal; memory/swap erasure is
not guaranteed. Local decrypted copies, terminal scrollback, backups and shared
screenshots are outside artifact retention. The owner must approve and follow a
separate local-copy retention policy before reviewing real model answers.

## Local reader

Install the pinned tool without an inference credential in the environment:

```sh
uv run python -m evals.xing_synthetic.private_review setup --age-binary /tmp/xing-age
```

From the **verified GitHub run and metadata receipt**, obtain the expected
ciphertext digest, candidate, run, case, request and approved recipient hash.
Verify the downloaded artifact's origin and GitHub digest first. Do not trust
metadata supplied only alongside an untrusted ciphertext: anyone with the public
recipient can encrypt a forged answer. age authenticates ciphertext integrity;
it does not authenticate its sender.

The human reviewer can run locally, substituting their existing native identity
file and those independently trusted values:

```sh
uv run python -m evals.xing_synthetic.private_review open \
  --age-binary /tmp/xing-age --file /path/to/case.age \
  --identity-file /private/path/to/existing-identity \
  --ciphertext-sha256 VERIFIED_CIPHERTEXT_SHA256 \
  --recipient-sha256 APPROVED_RECIPIENT_SHA256 \
  --candidate-sha VERIFIED_CANDIDATE_SHA --run-id VERIFIED_RUN_ID \
  --case VERIFIED_CASE --request-sha256 VERIFIED_REQUEST_SHA256
```

The reader refuses to operate in Actions or with an inference key in its
environment. It requires a single native identity file owned by the current
user and inaccessible to group/others. The open file descriptor is passed to
age; the identity pathname is not reopened in the subprocess. Complete bounded
decryption/authentication, context and expiry checks finish before any answer is
returned. The CLI prints one JSON object locally, escaping terminal control
characters. It creates no plaintext file and uploads nothing. Neither successful
decryption nor automated grading sets human review to complete.

Review narrative and field claims against the frozen synthetic sources and
answer key. Do not rely only on the automated grade. Provider terms, human review,
publication and production suitability remain distinct decisions.

## Offline tests

Tests use identities already published in upstream age test vectors, never real
user credentials or key generation. Native integration requires a verified tool
path; without it those tests are explicitly skipped.

```sh
XING_TEST_AGE_BINARY=/tmp/xing-age uv run python -W error -m pytest \
  tests/test_xing_synthetic.py tests/test_xing_private_review.py -q
```

Checks cover matching/wrong identity, ciphertext tampering, approved recipient
pin, alternate recipient types, context substitution, expiry, bounded subprocess
output, identity permissions, partial-write cleanup, existing file preservation,
and six mocked model answers through encryption and local decryption. Network
and live model calls are forbidden in those tests.
