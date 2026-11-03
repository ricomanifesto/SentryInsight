// Append-only operational records on a dedicated branch that the provider
// never builds. Each append re-reads the branch, lets the caller decide what
// to add from the current records, and pushes a child commit with
// compare-and-set; a lost race re-reads and decides again. Records are
// non-secret and separate from report evidence and the served payload.
const { canonicalJson } = require('./canonical');
const { CompareAndSetLost } = require('./git');

const STATE_FILE = 'state.json';
const MAX_ATTEMPTS = 8;

function createStore({ git, remote, branch, site, now = () => new Date(), message = 'Record publication state' }) {
  async function read() {
    const tip = git.fetchBranch(remote, branch);
    if (!tip) return { tip: null, records: [] };
    const bytes = git.showFile(tip, STATE_FILE);
    if (!bytes) throw new Error(`${branch} has no ${STATE_FILE}`);
    const state = JSON.parse(bytes.toString('utf8'));
    if (state.schema_version !== 1 || state.site !== site || !Array.isArray(state.records)) {
      throw new Error(`${branch} does not hold ${site} publication state`);
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
        new Map([[STATE_FILE, Buffer.from(canonicalJson({ schema_version: 1, site, records: next }))]]),
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

module.exports = { STATE_FILE, createStore };
