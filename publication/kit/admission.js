// Consumer admission for SentryDigest release events, used by the downstream
// report generators before any paid generation starts.
//
// Admission keys:
//   digest:<Digest source revision>  repository_dispatch, both payload shapes,
//                                    so a legacy and a new event for the same
//                                    Digest commit contend for one claim
//   run:<workflow run id>            scheduled and manual runs (new intent)
//
// Order for a new-shape event: identity validation, the uncertain-invocation
// guard, admission-key and content deduplication, staleness and identity
// against the serving descriptor and build receipt, input binding against
// the commit-addressed feed snapshot, then an atomic compare-and-set claim
// that decides the key and content checks again. Scheduled and manual runs
// skip identity, binding and content checks but are still subject to the
// uncertain-invocation guard.
//
// Per key: admitted -> invoked -> completed, or admitted -> abandoned when the
// run stopped before invoking (no paid work, so the claim is released). An
// invoked key whose outcome is not conclusive stays invoked (an "unresolved"
// record notes the outcome) until a report is recovered, a report handle is
// re-attached, or an operator readmits it explicitly.
//
// The generator receives the commit-addressed snapshot URL, never the mutable
// public feed, so a feed that advances after admission cannot change the
// analyzed input. This binds the feed bytes only; third-party article
// enrichment is outside the binding.
const { sha256 } = require('./canonical');
const { createGit } = require('./git');
const { LAYOUT, SHA1, SHA256, releaseKeyOf } = require('./release');
const { createStore } = require('./store');
const { createRequestBudget } = require('./request-budget');

const DIGEST_REPOSITORY = 'ricomanifesto/SentryDigest';
const SNAPSHOT_FEED_PATH = `${LAYOUT.payloadPrefix}feed.xml`;
const NEW_SHAPE_FIELDS = [
  'digest_content_digest', 'feed_sha256', 'news_data_sha256', 'payload_digest', 'release_key',
  'release_ref', 'schema', 'site', 'source_revision',
];
const KEY_STAGES = new Set(['admitted', 'invoked', 'completed', 'readmitted', 'abandoned']);
const ACTIVE_STAGES = new Set(['admitted', 'invoked', 'completed']);
const IN_FLIGHT_STAGES = new Set(['admitted', 'invoked']);
// Outcomes that settle an invoked generation: the generator finished, so a
// report was published, retained, found unchanged or refused by validation.
// Cancellation, failure or anything else may leave paid work outstanding.
const CONCLUSIVE_OUTCOMES = new Set(['published', 'unchanged', 'not-published', 'retained', 'recovered']);

function snapshotFeedUrl(releaseRef) {
  if (!SHA1.test(releaseRef || '')) throw new Error('snapshot requires a full artifact commit id');
  return `https://raw.githubusercontent.com/${DIGEST_REPOSITORY}/${releaseRef}/${SNAPSHOT_FEED_PATH}`;
}

function validateNewShape(payload) {
  const keys = Object.keys(payload).sort();
  if (keys.join(',') !== NEW_SHAPE_FIELDS.join(',')) return 'unexpected or missing fields';
  if (payload.schema !== 'sentrydigest-release/v1' || payload.site !== 'SentryDigest') return 'not a SentryDigest release event';
  for (const field of ['release_key', 'payload_digest', 'digest_content_digest', 'feed_sha256', 'news_data_sha256']) {
    if (!SHA256.test(payload[field])) return `${field} is not a SHA-256 digest`;
  }
  for (const field of ['release_ref', 'source_revision']) {
    if (!SHA1.test(payload[field])) return `${field} is not a full commit id`;
  }
  return null;
}

function classify({ eventName, payload, runId }) {
  if (eventName === 'schedule' || eventName === 'workflow_dispatch') {
    return { kind: 'intent', key: `run:${runId}` };
  }
  if (eventName !== 'repository_dispatch') return { invalid: `event ${eventName} cannot request generation` };
  if (!payload || typeof payload !== 'object') return { invalid: 'missing client payload' };
  if ('release_key' in payload || 'schema' in payload) {
    const problem = validateNewShape(payload);
    if (problem) return { invalid: problem };
    return { kind: 'release', key: `digest:${payload.source_revision}` };
  }
  if (Object.keys(payload).sort().join(',') === 'ref,sha' && SHA1.test(payload.sha || '')) {
    return { kind: 'legacy', key: `digest:${payload.sha}` };
  }
  return { invalid: 'payload is neither the release shape nor the legacy shape' };
}

// Every field of the event must agree with the release the origin serves:
// the descriptor (source, payload and content identity) and the adapter's
// build receipt (the artifact commit the provider built).
function identityMismatches(payload, descriptor, receipt, artifactBranch) {
  const identity = descriptor.content_identity || {};
  const pairs = [
    ['descriptor site', descriptor.site, 'SentryDigest'],
    ['descriptor kind', descriptor.kind, 'release'],
    ['descriptor release_key', descriptor.release_key, releaseKeyOf({
      site: descriptor.site, kind: descriptor.kind, sourceRevision: descriptor.source_revision, payloadDigest: descriptor.payload_digest, rollbackOf: descriptor.rollback_of,
    })],
    ['source_revision', payload.source_revision, descriptor.source_revision],
    ['payload_digest', payload.payload_digest, descriptor.payload_digest],
    ['digest_content_digest', payload.digest_content_digest, identity.digest_content_digest],
    ['feed_sha256', payload.feed_sha256, identity.feed_sha256],
    ['news_data_sha256', payload.news_data_sha256, identity.news_data_sha256],
    ['receipt release_key', receipt.release_key, payload.release_key],
    ['receipt git_commit_sha', receipt.git_commit_sha, payload.release_ref],
    ['receipt repository', receipt.repository, DIGEST_REPOSITORY],
    ['receipt git_ref', receipt.git_ref, artifactBranch],
    ['receipt environment', receipt.environment, 'production'],
  ];
  return pairs.filter(([, actual, expected]) => actual !== expected).map(([name]) => `${name} differs from the serving release`);
}

// The newest report commit on ref that changed reportPath and carries exactly
// this admission key and feed binding as trailers, or null.
function findAdmissionReport({ git, ref, key, feedUrl, reportPath }) {
  const format = '%H%x1f%(trailers:key=Admission-Key,valueonly,separator=%x1d)%x1f%(trailers:key=Admission-Feed,valueonly,separator=%x1d)%x1e';
  const output = git.run(['log', ref, `--format=${format}`, '--', reportPath]);
  for (const chunk of output.split('\x1e')) {
    const [commit, keys, feeds] = chunk.trim().split('\x1f');
    if (commit && keys === key && feeds === (feedUrl || 'none')) return commit;
  }
  return null;
}

function latestByKey(records) {
  const latest = new Map();
  for (const r of records) {
    if (r.admission_key && KEY_STAGES.has(r.stage)) latest.set(r.admission_key, r);
  }
  return latest;
}

const lastOf = (records, key, stage) => records.findLast((r) => r.admission_key === key && r.stage === stage);

// A conclusive completion keeps the admitted release, content and binding
// identity, so the last-analyzed-content check sees it however it ended.
function completedRecord(admitted, { key, run, outcome, binding }) {
  return {
    stage: 'completed',
    admission_key: key,
    run_id: run,
    outcome,
    binding: binding || admitted.binding,
    release_key: admitted.release_key,
    digest_content_digest: admitted.digest_content_digest,
  };
}

function createAdmission({
  repoRoot,
  remote,
  config,
  consumer,
  fetchUrl,
  findRecoveredReport = async () => false,
  stateBranch = 'publication-admission',
  bindingAttempts = 5,
  bindingBaseDelayMs = 5000,
  sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms)),
  now = () => new Date(),
  gitEnv = process.env,
  hooks = {},
}) {
  if (consumer !== config.site || consumer === 'SentryDigest') throw new Error(`${consumer} is not this consumer site`);
  const git = createGit(repoRoot, { env: gitEnv });
  const store = createStore({ git, remote, branch: stateBranch, site: consumer, now, message: 'Record generation admission' });
  const digestOrigin = config.origins.SentryDigest.production;

  async function skip(base, decision, extra = {}) {
    await store.append(() => [{ stage: 'skipped', decision, ...base, ...extra }]);
    return { decision, admission_key: base.admission_key, exit_code: 0, ...extra };
  }

  async function reject(base, decision, reason) {
    await store.append(() => [{ stage: 'rejected', decision, reason, ...base }]);
    return { decision, reason, exit_code: 1 };
  }

  // Resolves invoked-without-completion records before any new invocation.
  // An explicit readmission releases the key even when it saved a report
  // handle; without one a handle is re-attached and never dropped.
  async function guardUncertain(records, { runId, readmit }) {
    for (const [key, latest] of latestByKey(records)) {
      if (latest.stage !== 'invoked') continue;
      const admitted = lastOf(records, key, 'admitted') || {};
      if (latest.handle && !readmit) {
        return { decision: 'reattach', admission_key: key, reattach_handle: latest.handle, feed_url: admitted.feed_url, binding: admitted.binding, exit_code: 0 };
      }
      const stillInvoked = (current) => latestByKey(current).get(key)?.stage === 'invoked';
      if (await findRecoveredReport(key, admitted)) {
        await store.append((current) => (stillInvoked(current) ? [completedRecord(admitted, { key, run: runId, outcome: 'recovered' })] : []));
        continue;
      }
      if (readmit) {
        await store.append((current) => (stillInvoked(current)
          ? [{ stage: 'readmitted', admission_key: key, run_id: runId, abandoned_handle: latest.handle }]
          : []));
        continue;
      }
      return { decision: 'uncertain', uncertain_key: key, exit_code: 0 };
    }
    return null;
  }

  async function fetchBytes(url) {
    const response = await fetchUrl(url);
    if (response.status !== 200) throw new Error(`${url} returned ${response.status}`);
    return Buffer.isBuffer(response.body) ? response.body : Buffer.from(response.body ?? '');
  }

  async function fetchJson(url) {
    return JSON.parse((await fetchBytes(url)).toString('utf8'));
  }

  async function bindRelease(payload) {
    let descriptor;
    let receipt;
    try {
      descriptor = await fetchJson(`${digestOrigin}${LAYOUT.descriptor}`);
    } catch (error) {
      return { decision: 'binding-unavailable', reason: error.message };
    }
    if (descriptor.release_key !== payload.release_key) return { decision: 'superseded-by-origin', served_release_key: descriptor.release_key };
    try {
      receipt = await fetchJson(`${digestOrigin}${LAYOUT.receipt}`);
    } catch (error) {
      return { decision: 'binding-unavailable', reason: error.message };
    }
    const mismatches = identityMismatches(payload, descriptor, receipt, config.artifact_branch);
    if (mismatches.length > 0) return { decision: 'rejected-inconsistent', reason: mismatches.join('; ') };
    const url = snapshotFeedUrl(payload.release_ref);
    let last = 'not fetched';
    for (let attempt = 1; attempt <= bindingAttempts; attempt += 1) {
      try {
        const bytes = await fetchBytes(url);
        if (sha256(bytes) === payload.feed_sha256) return { decision: 'bound', feed_url: url };
        last = 'snapshot bytes differ from feed_sha256';
      } catch (error) {
        last = error.message;
      }
      if (attempt < bindingAttempts) await sleep(bindingBaseDelayMs * attempt);
    }
    return { decision: 'binding-failed', reason: last };
  }

  async function admit({ eventName, payload, runId, runAttempt, readmit = false }) {
    const classified = classify({ eventName, payload, runId });
    const run = String(runId);
    const base = { run_id: run, run_attempt: String(runAttempt), event: eventName };
    if (classified.invalid) return reject(base, 'rejected-invalid', classified.invalid);
    const key = classified.key;
    const keyed = { ...base, admission_key: key };

    let { records } = await store.read();
    const guarded = await guardUncertain(records, { runId: run, readmit });
    if (guarded) {
      if (guarded.decision === 'uncertain') await skip(keyed, 'uncertain', { uncertain_key: guarded.uncertain_key });
      return guarded;
    }
    ({ records } = await store.read());

    // Only a claim this run made before invoking is resumable; any other
    // in-flight or completed claim on the key, or in-flight or last-analyzed
    // identical content, is a duplicate.
    const own = latestByKey(records).get(key);
    if (own && own.stage === 'admitted' && own.run_id === run) {
      return { decision: 'admitted', admission_key: key, resumed: true, feed_url: own.feed_url, binding: own.binding, exit_code: 0 };
    }
    const conflict = (current) => {
      const latest = latestByKey(current);
      if (ACTIVE_STAGES.has(latest.get(key)?.stage)) return 'skipped-duplicate';
      if (classified.kind !== 'release') return null;
      const content = payload.digest_content_digest;
      for (const [other, record] of latest) {
        if (other !== key && IN_FLIGHT_STAGES.has(record.stage) && lastOf(current, other, 'admitted')?.digest_content_digest === content) {
          return 'skipped-duplicate-content';
        }
      }
      const lastEvent = current.findLast((r) => r.stage === 'completed' && r.digest_content_digest);
      return lastEvent?.digest_content_digest === content ? 'skipped-duplicate-content' : null;
    };
    const early = conflict(records);
    if (early) return skip(keyed, early, classified.kind === 'release' ? { release_key: payload.release_key } : {});

    let claim = { ...keyed, stage: 'admitted', binding: 'none' };
    if (classified.kind === 'release') {
      const bound = await bindRelease(payload);
      if (bound.decision === 'rejected-inconsistent') return reject({ ...keyed, release_key: payload.release_key }, bound.decision, bound.reason);
      if (bound.decision !== 'bound') {
        const { decision, ...detail } = bound;
        return skip(keyed, decision, { release_key: payload.release_key, ...detail });
      }
      claim = {
        ...claim,
        binding: 'feed-bytes',
        feed_url: bound.feed_url,
        release_key: payload.release_key,
        release_ref: payload.release_ref,
        source_revision: payload.source_revision,
        digest_content_digest: payload.digest_content_digest,
        feed_sha256: payload.feed_sha256,
      };
    }

    const { value } = await store.append(async (current) => {
      if (hooks.beforeClaim) await hooks.beforeClaim();
      const decided = conflict(current);
      return decided
        ? { append: [{ stage: 'skipped', decision: decided, ...keyed }], value: decided }
        : { append: [claim], value: 'admitted' };
    });
    if (value !== 'admitted') return { decision: value, admission_key: key, exit_code: 0 };
    return { decision: 'admitted', admission_key: key, feed_url: claim.feed_url, binding: claim.binding, exit_code: 0 };
  }

  // The generation boundary: only the run that holds the claim may start (or
  // record a report handle for) the generator, decided at the compare-and-set.
  // A claim admitted earlier still may not start while another invocation's
  // outcome is unresolved, whatever its entry point; the refused claim is
  // released, since no paid work started under it.
  async function invoked({ admissionKey, runId, handle }) {
    const run = String(runId);
    const { value } = await store.append((current) => {
      const latest = latestByKey(current).get(admissionKey);
      if (!latest || !IN_FLIGHT_STAGES.has(latest.stage) || latest.run_id !== run) {
        throw new Error(`${admissionKey} is not claimed by run ${run}; generation must not start`);
      }
      if (latest.stage === 'admitted') {
        for (const [other, record] of latestByKey(current)) {
          if (other !== admissionKey && record.stage === 'invoked') {
            return {
              append: [{ stage: 'abandoned', admission_key: admissionKey, run_id: run, outcome: 'blocked-by-unresolved', blocked_by: other }],
              value: other,
            };
          }
        }
      }
      return [{ stage: 'invoked', admission_key: admissionKey, run_id: run, handle: handle || undefined }];
    });
    if (value) throw new Error(`${value} has an unresolved invocation; generation must not start`);
  }

  // Records how an in-flight claim ended and returns the recorded stage.
  async function complete({ admissionKey, runId, outcome, binding }) {
    const run = String(runId);
    const { appended } = await store.append((current) => {
      const latest = latestByKey(current).get(admissionKey);
      const admitted = lastOf(current, admissionKey, 'admitted');
      if (!admitted || !latest || !IN_FLIGHT_STAGES.has(latest.stage) || (latest.stage === 'admitted' && latest.run_id !== run)) {
        throw new Error(`${admissionKey} is not in flight`);
      }
      const ended = { admission_key: admissionKey, run_id: run, outcome };
      if (latest.stage === 'admitted') return [{ stage: 'abandoned', ...ended }];
      if (!CONCLUSIVE_OUTCOMES.has(outcome)) return [{ stage: 'unresolved', ...ended }];
      return [completedRecord(admitted, { key: admissionKey, run, outcome, binding })];
    });
    return appended[0].stage;
  }

  const requests = createRequestBudget({ store, now, requireOwner(records, key, run) {
    const latest = latestByKey(records).get(key);
    if (!latest || latest.stage !== 'invoked' || latest.run_id !== run) throw new Error('request admission not owned');
    const admittedIndex = records.findLastIndex((r) => r.admission_key === key && r.stage === 'admitted');
    if (admittedIndex < 0 || records[admittedIndex].run_id !== run) throw new Error('request episode not owned');
    return admittedIndex;
  } });
  return { admit, complete, invoked, ...requests, readState: () => store.read() };
}

module.exports = { CONCLUSIVE_OUTCOMES, DIGEST_REPOSITORY, SNAPSHOT_FEED_PATH, createAdmission, findAdmissionReport, snapshotFeedUrl };
