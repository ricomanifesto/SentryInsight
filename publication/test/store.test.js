const assert = require('node:assert/strict');
const test = require('node:test');

const { canonicalJson } = require('../kit/canonical');
const { createStore } = require('../kit/store');

const GUARD = canonicalJson({ git: { deploymentEnabled: false } });

// An in-memory branch: commitFiles writes a fresh tree, exactly like the real
// Git adapter, so anything not passed in is dropped from the next commit.
function memoryGit(initialFiles) {
  const commits = new Map([['root', new Map(initialFiles)]]);
  let tip = 'root';
  let counter = 0;
  return {
    commits,
    tipFiles: () => commits.get(tip),
    fetchBranch: () => tip,
    showFile: (revision, file) => commits.get(revision).get(file) || null,
    commitFiles(files) {
      counter += 1;
      const id = `c${counter}`;
      commits.set(id, new Map(files));
      return id;
    },
    pushBranch(_remote, commit) {
      tip = commit;
    },
  };
}

function state(records) {
  return Buffer.from(canonicalJson({ schema_version: 1, site: 'SentryInsight', records }));
}

test('an initialized ledger keeps its hosting guard on every append', async () => {
  const records = [{ stage: 'admission_store_initialized', at: '2026-11-05T00:00:00.000Z' }];
  const git = memoryGit([['state.json', state(records)], ['vercel.json', Buffer.from(GUARD)]]);
  const store = createStore({ git, remote: 'origin', branch: 'publication-admission', site: 'SentryInsight' });

  await store.append(() => [{ stage: 'admitted', admission_key: 'run:1', run_id: '1' }]);

  assert.equal(git.tipFiles().get('vercel.json').toString('utf8'), GUARD);
  assert.equal(JSON.parse(git.tipFiles().get('state.json')).records.length, 2);
});

test('an uninitialized ledger stays a single state file', async () => {
  const git = memoryGit([['state.json', state([])]]);
  const store = createStore({ git, remote: 'origin', branch: 'publication-admission', site: 'SentryInsight' });

  await store.append(() => [{ stage: 'admitted', admission_key: 'run:1', run_id: '1' }]);

  assert.deepEqual([...git.tipFiles().keys()], ['state.json']);
});

test('an existing hosting guard is kept even without the initialization record', async () => {
  const git = memoryGit([['state.json', state([])], ['vercel.json', Buffer.from(GUARD)]]);
  const store = createStore({ git, remote: 'origin', branch: 'publication-admission', site: 'SentryInsight' });

  await store.append(() => [{ stage: 'admitted', admission_key: 'run:1', run_id: '1' }]);

  assert.equal(git.tipFiles().get('vercel.json').toString('utf8'), GUARD);
});
