// Append-only operational records on a dedicated branch that the provider
// never builds. Each append re-reads the branch, lets the caller decide what
// to add from the current records, and pushes a child commit with
// compare-and-set; a lost race re-reads and decides again. Records are
// non-secret and separate from report evidence and the served payload.
const { canonicalJson, sha256 } = require('./canonical');
const { CompareAndSetLost } = require('./git');

const STATE_FILE = 'state.json';
const MAX_ATTEMPTS = 8;
const INITIALIZED = 'admission_store_initialized';
const INITIALIZED_GUARD = canonicalJson({ git: { deploymentEnabled: false } });

function stateFiles(site, records) {
  const files = new Map([[STATE_FILE, Buffer.from(canonicalJson({ schema_version: 1, site, records }))]]);
  // commitFiles creates a fresh tree, so every subsequent writer must retain
  // the branch-local hosting guard, including the legacy free writer.
  if (records.some((row) => row?.stage === INITIALIZED)) files.set('vercel.json', Buffer.from(INITIALIZED_GUARD));
  return files;
}

function initializationIdentity(site, scopeSha256) {
  if (typeof site !== 'string' || !/^[A-Za-z][A-Za-z0-9]{0,63}$/.test(site)
      || typeof scopeSha256 !== 'string' || !/^[a-f0-9]{64}$/.test(scopeSha256)) {
    throw new Error('Admission initialization unavailable');
  }
  const value = { stage: INITIALIZED, schema_version: 1, site, scope_sha256: scopeSha256 };
  return Object.freeze({ ...value, initialization_id: sha256(canonicalJson(value)) });
}

function checkedInitialization(identity, site) {
  const expected = initializationIdentity(site, identity?.scope_sha256);
  if (canonicalJson(identity) !== canonicalJson(expected)) throw new Error('Admission initialization unavailable');
  return expected;
}

function requireMarker(records, identity) {
  const first = records[0];
  const { at, ...value } = first || {};
  if (canonicalJson(value) !== canonicalJson(identity)
      || typeof at !== 'string' || !Number.isFinite(Date.parse(at)) || new Date(at).toISOString() !== at
      || records.filter((row) => row?.stage === INITIALIZED).length !== 1) {
    throw new Error('Initialized admission store unavailable');
  }
}

// Explicit first-use operation, separate from all admission/money/send paths.
// Never adopt an existing ref or retry/reconcile a failed push into permission.
async function bootstrapStore({ git, remote, branch, site, scopeSha256, now = () => new Date() }) {
  const identity = initializationIdentity(site, scopeSha256);
  const marker = { ...identity, at: now().toISOString() };
  if (git.fetchBranch(remote, branch)) throw new Error('Admission initialization refused');
  const commit = git.commitFiles(stateFiles(site, [marker]),
    { parent: null, message: 'Initialize admission state' });
  if (!/^[a-f0-9]{40}$/.test(commit || '')) throw new Error('Admission initialization refused');
  const metadata = { rootOid: commit, markerSha256: sha256(canonicalJson(marker)) };
  try {
    if (git.pushInitialBranch(remote, commit, branch) !== commit) throw new Error('Invalid acknowledgement');
  } catch (_) {
    const error = new Error('Admission initialization unknown');
    error.proposedRootOid = metadata.rootOid;
    error.proposedMarkerSha256 = metadata.markerSha256;
    throw error;
  }
  return metadata;
}

function createStore({ git, remote, branch, site, now = () => new Date(), message = 'Record publication state', requiredInitialization = null }) {
  const identity = requiredInitialization === null ? null : checkedInitialization(requiredInitialization, site);
  async function read() {
    const tip = git.fetchBranch(remote, branch);
    if (!tip) {
      if (identity) throw new Error('Initialized admission store unavailable');
      return { tip: null, records: [] };
    }
    const bytes = git.showFile(tip, STATE_FILE);
    if (!bytes) throw new Error(`${branch} has no ${STATE_FILE}`);
    const state = JSON.parse(bytes.toString('utf8'));
    if (state.schema_version !== 1 || state.site !== site || !Array.isArray(state.records)) {
      throw new Error(`${branch} does not hold ${site} publication state`);
    }
    if (identity) {
      requireMarker(state.records, identity);
      const guard = git.showFile(tip, 'vercel.json');
      if (!guard || guard.toString('utf8') !== INITIALIZED_GUARD) throw new Error('Initialized admission store unavailable');
    }
    return { tip, records: state.records };
  }

  // decide(records) returns the records to append (possibly none) and may
  // return a value for the caller as { append, value }.
  async function append(decide) {
    for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt += 1) {
      const { tip, records } = await read();
      const decision = await decide(records);
      const additions = Array.isArray(decision) ? decision : decision.append || [];
      const value = Array.isArray(decision) ? undefined : decision.value;
      if (additions.length === 0) return { records, value, appended: [] };
      const at = now().toISOString();
      const stamped = additions.map((record) => ({ ...record, at }));
      const next = [...records, ...stamped];
      const commit = git.commitFiles(
        stateFiles(site, next),
        { parent: tip, message },
      );
      try {
        git.pushBranch(remote, commit, branch, tip);
        return { records: next, value, appended: stamped };
      } catch (error) {
        if (!(error instanceof CompareAndSetLost)) throw error;
      }
    }
    throw new Error(`${branch} kept moving; gave up after ${MAX_ATTEMPTS} compare-and-set attempts`);
  }

  return { append, read };
}

module.exports = { STATE_FILE, bootstrapStore, createStore, initializationIdentity };
