# Report control plane (local, D1-first)

A Cloudflare Worker that admits report requests, records product state in D1, hands work to a generic execution service through a Queue, verifies and stores accepted report artifacts in R2, and publishes them through a fenced publisher while keeping the last-good revision.

This directory is a local slice. Nothing here is deployed, and no account, route, remote binding or credential is used.

## Authorities

| Store | Owns |
|---|---|
| D1 | operations, article revisions, artifacts, publications, targets, schedules and the audit of events |
| R2 | immutable bytes: admitted snapshots at `snapshots/<sha256>`, and verified artifacts with their manifests at `artifacts/<sha256>/` |
| The execution service | runs, attempts, leases and execution retries; its contract is `contracts/execution-service.md` |
| The publisher | the published revision and its receipts; its contract is `contracts/publisher.md` |

The Worker is the only writer of D1 and R2, and completion is pulled from the execution service. No transaction spans two stores, so every handoff records durable intent first and is repaired by a single retry owner:

| What needs repair | Owner |
|---|---|
| Unconfirmed sends | the sweeper |
| Enqueued deliveries | the Queue |
| Execution | the execution service |
| Completion of submitted work | the sweeper's status pull |
| Publications | the target claim and the publisher's fence |

## Layout

| Path | Contents |
|---|---|
| `src/` | Worker modules: routes, authentication, identities, strict JSON, admission, delivery, completion, publication and the sweeper |
| `migrations/0001_init.sql` | the D1 schema |
| `contracts/` | product API, execution service and publisher |
| `cli/report-control.mjs` | a command-line client; `artifact` downloads and verifies an accepted artifact |
| `local/stack.mjs`, `local/serve.mjs` | the local stack on the installed Miniflare/workerd API, plus a runner with a read-only inspection endpoint |
| `tests/` | `node:test` suites against the real local D1, R2 and Queue bindings, a fake execution service and a durable fake publisher (`tests/support/`) |
| `wrangler.toml` | the deployment-shaped declaration of the same bindings; it is not used locally |

## Running locally

The local stack loads the installed Miniflare module by absolute path. Nothing is downloaded or installed.

```bash
MINIFLARE_MODULE=/path/to/miniflare/dist/src/index.js node --test --test-concurrency=1 'tests/*.test.mjs'
```

`--test-concurrency=1` runs one disposable stack at a time.

For a long-running stack, copy `local/config.example.json` to `local/config.local.json`, fill in absolute paths and synthetic tokens, and run:

```bash
node local/serve.mjs --config local/config.local.json
```

It writes a ready file with the Worker URL and the inspection URL. On SIGTERM the engine's own exit hook disposes the workerd runtime and the process exits with status 143 (128 + SIGTERM); that status is the engine's convention, not an application success code, so a caller that owns the process should also confirm that the engine's child processes are gone.

### Queue names

| Variable | Default | Names |
|---|---|---|
| `ADMISSIONS_QUEUE_NAME` | `report-admissions` | the admission queue: the producer behind the `ADMISSIONS` binding and its consumer |
| `DEAD_LETTER_QUEUE_NAME` | `report-admissions-dead` | the admission queue's dead-letter queue and its consumer |

- **One mapping:** `queueNames` in `src/config.js` decides the effective names. The Worker's queue dispatch, the settings every entry point reads, the local stack's producer, consumers and dead-letter link, and the runner's `/queue-dispatch` inspection guard all use it, so they cannot disagree.
- **Grammar:** 1 to 63 lowercase letters, digits and hyphens, starting and ending with a letter or digit. The two names must differ, including when one is set to the other's default. This is a deliberately narrow subset of the platform's naming rule: a padded, upper-case or punctuated name is refused rather than compared.
- **Invalid names fail closed:** every authenticated route answers `503 config_invalid`, the scheduled handler admits nothing, a queue batch is retried without being handled, and the local stack and runner refuse to start. Nothing is written or sent.
- **Unknown queue:** a batch from a queue that is neither effective name is never acknowledged and never handled. A message naming a known operation records one `queue_unknown` event (no queue name, body or other value is stored), and the batch is retried with `QUEUE_RETRY_DELAY_S`, so the Queue's own retry bound still applies. The durable row and the sweeper's bounded re-send recover the operation once the configuration is corrected.
- **Deployment:** `wrangler.toml` declares the default queue topology literally and sets both variables to the defaults. A deployment with other names must change both together; nothing here deploys.

The CLI reads `REPORT_CONTROL_URL` and `REPORT_CONTROL_TOKEN_FILE`:

```bash
node cli/report-control.mjs status <operation_id>
```

## Guarantees that the tests check against stored state

**Admission:**
- Identical requests are one operation, and conflicting reuse of a source revision is refused.
- A failed admission batch rolls back every row, including article metadata and the sequence number.

**Delivery:**
- The consumer calls the execution service only after winning a durable claim.
- A late write from an expired claim changes nothing.
- Delayed or dead-lettered messages from an earlier delivery generation are stale.
- Unconfirmed sends are bounded, and their exhaustion is recorded.

**Completion:**
- An operation completes only after every artifact part is fetched, length- and hash-checked, stored immutably, and its digest recomputed.
- Wrong, missing, reordered, oversized or stale artifacts are rejected.

**Publication:**
- One claim wins per target, and a stale candidate is refused.
- An ambiguous effect is settled by observation.
- Settlement is one D1 batch whose target and publication statements are coupled in SQL, so both apply or neither does.

## Limits

- **Local emulation only:** local Miniflare/workerd is evidence about the D1, R2 and Queue APIs, not about a production account's consistency, latency or scale.
- **Queue concurrency and persistence:** local Queue consumer concurrency is not emulated; concurrent deliveries are exercised by dispatching to the handler directly. In one local test, a message still pending when the local engine restarted was not observed to be delivered before the sweeper's staleness re-send, and the re-send recovered the operation. That observation is narrower than proof that the message was permanently lost, and it says nothing about the durability of a deployed Queue.
- **Queue names:** the name grammar is checked only against the installed local engine; a deployment's queue declarations are not derived from the variables (see Queue names).
- **Publisher fence:** a real publisher that cannot enforce a candidate sequence keeps only the expected-remote fence.
- **Fakes:** the fake execution service and the durable fake publisher in `tests/support/` are test doubles; no real model or publication is called.
