const assert = require('node:assert/strict');
const test = require('node:test');
const { canonicalJson, sha256 } = require('../kit/canonical');
const { CompareAndSetLost } = require('../kit/git');
const { createStore, initializationIdentity, bootstrapStore } = require('../kit/store');
const fs = require('node:fs'), path = require('node:path');
const { createGit } = require('../kit/git');
const { createAdmission } = require('../kit/admission');
const { DailyPilot } = require('../kit/daily-pilot');
const { loadSiteConfig } = require('../kit/config');
const { GIT_ENV, git: command, siteConfig, tempDir } = require('./helpers');
const { initialize } = require('../../scripts/bootstrap_canary_ledger.cjs');
const source = require('../../config/full-feed-canary.json');
const childProcess = require('node:child_process');

const scopeSha256 = 'f'.repeat(64), site = 'SentryInsight';
const now = () => new Date('2030-01-02T03:04:05.000Z');
function fixture() {
  const bodies = new Map(); let next = 0;
  const state = { tip: null, commits: [], pushes: [], initialPushes: [], reads: 0 };
  const git = {
    fetchBranch() { state.reads += 1; return state.tip; },
    showFile(tip, name) { return bodies.get(tip)?.get(name); },
    commitFiles(files, options) {
      const tip = String(++next).padStart(40, '0');
      bodies.set(tip, new Map(files));
      state.commits.push({ tip, ...options }); return tip;
    },
    pushBranch(remote, tip, branch, expected) {
      state.pushes.push({ remote, tip, branch, expected });
      if (state.tip !== expected) throw new CompareAndSetLost();
      state.tip = tip;
      return tip;
    },
    pushInitialBranch(remote, tip, branch) {
      state.initialPushes.push({ remote, tip, branch });
      if (state.tip !== null) throw new Error('private-sentinel');
      state.tip = tip;
      return tip;
    },
  };
  const options = { git, remote: 'fixture', branch: 'publication-admission', site, now };
  const load = (records) => {
    state.tip = git.commitFiles(new Map([
      ['state.json', Buffer.from(canonicalJson({ schema_version: 1, site, records }))],
      ['vercel.json', Buffer.from(canonicalJson({ git: { deploymentEnabled: false } }))],
    ]), { parent: null });
  };
  return { git, state, options, load };
}
const strict = (w, overrides = {}) => createStore({ ...w.options, requiredInitialization: initializationIdentity(site, scopeSha256), ...overrides });
const seed = (w) => bootstrapStore({ ...w.options, scopeSha256 });

test('legacy free state still permits its existing first-use behavior', async () => {
  const w = fixture(); assert.deepEqual(await createStore(w.options).read(), { tip: null, records: [] });
  await createStore(w.options).append(() => [{ stage: 'admitted' }]);
  assert.equal(w.state.pushes.length, 1);
});
test('paid missing state refuses before decision, commit, or write', async () => {
  const w = fixture(); let decisions = 0;
  await assert.rejects(strict(w).read());
  await assert.rejects(strict(w).append(() => { decisions += 1; return [{ stage: 'admitted' }]; }));
  assert.equal(decisions, 0); assert.deepEqual(w.state.commits, []); assert.deepEqual(w.state.pushes, []);
});
test('initialization identity is stable, scope-bound and grants no financial permission', () => {
  const identity = initializationIdentity(site, scopeSha256);
  assert.deepEqual(identity, initializationIdentity(site, scopeSha256));
  assert.notDeepEqual(identity, initializationIdentity(site, 'e'.repeat(64)));
  assert.equal(identity.stage, 'admission_store_initialized');
  assert.equal(identity.schema_version, 1); assert.equal(identity.site, site);
  for (const value of ['', null, 'F'.repeat(64), 'private-sentinel']) assert.throws(() => initializationIdentity(site, value));
  for (const key of ['admission_key', 'run_id', 'revision', 'day', 'generationToken', 'amountMicrousd']) assert.equal(key in identity, false);
});
test('explicit bootstrap creates one canonical marker root with one expected-absent push', async () => {
  const w = fixture(), result = await seed(w);
  assert.equal(w.state.commits.length, 1); assert.equal(w.state.commits[0].parent, null);
  assert.equal(w.state.initialPushes.length, 1); assert.equal(w.state.pushes.length, 0);
  const records = (await strict(w).read()).records;
  assert.deepEqual(records, [{ ...initializationIdentity(site, scopeSha256), at: now().toISOString() }]);
  assert.equal(result.rootOid, w.state.tip); assert.equal(result.markerSha256, sha256(canonicalJson(records[0])));
});
test('bootstrap refuses every existing state including the identical marker without adoption', async () => {
  const w = fixture(); await seed(w); const writes = w.state.initialPushes.length;
  await assert.rejects(seed(w)); assert.equal(w.state.initialPushes.length, writes);
  const other = fixture(); other.load([]); await assert.rejects(seed(other)); assert.equal(other.state.initialPushes.length, 0);
});
test('unknown bootstrap ACK is not retried or reconciled into authority', async () => {
  const w = fixture(), push = w.git.pushInitialBranch;
  w.git.pushInitialBranch = (...args) => { push(...args); throw new Error('private-sentinel'); };
  await assert.rejects(seed(w), (error) => error.message === 'Admission initialization unknown');
  assert.equal(w.state.reads, 1); assert.equal(w.state.initialPushes.length, 1);
  await assert.rejects(seed(w)); assert.equal(w.state.initialPushes.length, 1);
});
test('paid reads refuse missing, foreign, malformed, displaced and repeated markers', async () => {
  const base = { ...initializationIdentity(site, scopeSha256), at: now().toISOString() };
  const cases = [[], [{ stage: 'admitted' }], [{ ...base, site: 'Other' }], [{ ...base, schema_version: 2 }],
    [{ ...base, initialization_id: '0'.repeat(64) }], [{ ...base, scope_sha256: 'e'.repeat(64) }],
    [{ ...base, at: 'yesterday' }], [{ ...base, extra: 'private-sentinel' }],
    [{ stage: 'admitted' }, base], [base, base]];
  for (const records of cases) { const w = fixture(); w.load(records); await assert.rejects(strict(w).read()); }
});
test('paid CAS retry refuses deletion rather than creating a new wallet root', async () => {
  const w = fixture(); await seed(w); let decisions = 0;
  w.git.pushBranch = () => { w.state.pushes.push('lost'); w.state.tip = null; throw new CompareAndSetLost(); };
  await assert.rejects(strict(w).append(() => { decisions += 1; return [{ stage: 'admitted' }]; }));
  assert.equal(decisions, 1); assert.equal(w.state.pushes.length, 1); assert.equal(w.state.initialPushes.length, 1);
});
test('a legacy free recreation after deletion does not satisfy paid initialization', async () => {
  const w = fixture(); await seed(w); w.state.tip = null;
  await createStore(w.options).append(() => [{ stage: 'admitted' }]);
  await assert.rejects(strict(w).read());
  assert.equal(w.state.pushes.length, 1); assert.equal(w.state.initialPushes.length, 1);
});
test('normal later records retain the same marker but a new scope refuses', async () => {
  const w = fixture(); await seed(w); await strict(w).append(() => [{ stage: 'admitted', revision: 'a'.repeat(40) }]);
  await strict(w).append(() => [{ stage: 'admitted', revision: 'b'.repeat(40) }]);
  assert.equal((await strict(w).read()).records.length, 3);
  await assert.rejects(strict(w, { requiredInitialization: initializationIdentity(site, 'e'.repeat(64)) }).read());
});
test('every marked append retains the hosting guard, including the legacy writer', async () => {
  const w = fixture(); await seed(w);
  const expected = canonicalJson({ git: { deploymentEnabled: false } });
  assert.equal(w.git.showFile(w.state.tip, 'vercel.json').toString(), expected);
  await strict(w).append(() => [{ stage: 'admitted' }]);
  await createStore(w.options).append(() => [{ stage: 'skipped' }]);
  assert.equal(w.git.showFile(w.state.tip, 'vercel.json').toString(), expected);
  assert.equal((await strict(w).read()).records.length, 3);
  const show = w.git.showFile; w.git.showFile = (tip, name) => name === 'vercel.json' ? null : show(tip, name);
  await assert.rejects(strict(w).read());
});

function localWorld(t) {
  const base = tempDir(t, 'initialized-ledger-'), remote = path.join(base, 'remote.git'), repo = path.join(base, 'repo');
  command(base, 'init', '--quiet', '--bare', remote); fs.mkdirSync(repo);
  command(repo, 'init', '--quiet', '--initial-branch=main'); command(repo, 'remote', 'add', 'origin', remote);
  fs.writeFileSync(path.join(repo, 'README.md'), 'fixture\n');
  command(repo, 'add', '.'); command(repo, 'commit', '--quiet', '-m', 'fixture');
  const native = createGit(repo, { env: GIT_ENV, timeoutMs: 10000 });
  return { repo, remote, git: native, options: { git: native, remote, branch: 'publication-admission', site, now } };
}
test('native Git bootstrap and paid admission share marker, money and original physical token', async (t) => {
  const w = localWorld(t), revision = command(w.repo, 'rev-parse', 'HEAD');
  await seed(w);
  const daily = new DailyPilot({ month: '2030-01', activationStart: '2030-01-01T00:00:00.000Z',
    opening: { amountMicrousd: 0, basisSha256: scopeSha256 } });
  const admission = createAdmission({ repoRoot: w.repo, remote: w.remote, config: loadSiteConfig(siteConfig({ site, repository: `ricomanifesto/${site}` })),
    consumer: site, fetchUrl: () => { throw new Error('no source fetch'); }, gitEnv: GIT_ENV, now,
    requiredInitialization: initializationIdentity(site, scopeSha256),
    productionDailyPilot: daily, productionSpendPolicy: daily.policy(revision) });
  assert.equal((await admission.admit({ eventName: 'workflow_dispatch', runId: '800', runAttempt: '1' })).decision, 'admitted');
  await admission.invoked({ admissionKey: 'run:800', runId: '800' });
  const grant = await admission.productionSpend.reserveOneShotGeneration({ admissionKey: 'run:800', runId: '800', runAttempt: '1',
    revision, sourceSha256: 'a'.repeat(64) });
  const token = await admission.productionSpend.beginSend(grant, { operation: 'report', requestSha256: 'b'.repeat(64) });
  assert.match(token.token, /^[a-f0-9]{32}$/);
  assert.equal(token.generationToken, grant.generationToken);
  await assert.rejects(admission.productionSpend.beginSend(grant, { operation: 'report', requestSha256: 'b'.repeat(64) }));
  const records = (await admission.readState()).records;
  assert.equal(records[0].stage, 'admission_store_initialized');
  assert.equal(records.filter((row) => row.stage === 'pilot_daily').length, 1);
  assert.equal(records.filter((row) => row.stage === 'spend_reserved').length, 1);
  assert.equal(records.find((row) => row.stage === 'spend_reserved').physicalLimit, 1);
  assert.equal(records.find((row) => row.stage === 'spend_sending').token, token.token);
  assert.equal(records.find((row) => row.stage === 'request_reserved').token, token.token);
  assert.equal(records.find((row) => row.stage === 'request_reserved').limit, 1);
  assert.deepEqual(JSON.parse(w.git.showFile(command(w.repo, 'rev-parse', 'refs/publication/remote/publication-admission'), 'vercel.json')),
    { git: { deploymentEnabled: false } });
});
test('bootstrap ACK uncertainty retains only proposed identity, never initialized status', async () => {
  const w = fixture(); w.git.pushInitialBranch = () => { throw new Error('private-sentinel'); };
  await assert.rejects(seed(w), (error) => {
    assert.match(error.proposedRootOid, /^[a-f0-9]{40}$/);
    assert.match(error.proposedMarkerSha256, /^[a-f0-9]{64}$/);
    assert.equal(error.message, 'Admission initialization unknown'); return true;
  });
});
test('native bootstrap does not replace an existing ref or retry an expected-absent race', async (t) => {
  const w = localWorld(t); await seed(w);
  const original = command(w.remote, 'rev-parse', 'refs/heads/publication-admission');
  await assert.rejects(seed(w)); assert.equal(command(w.remote, 'rev-parse', 'refs/heads/publication-admission'), original);
  assert.throws(() => w.git.pushInitialBranch(w.remote, command(w.repo, 'rev-parse', 'HEAD'), 'publication-admission'),
    (error) => error.message === 'Admission initialization unknown');
  assert.equal(command(w.remote, 'rev-parse', 'refs/heads/publication-admission'), original);
});
test('closed bootstrap command binds reviewed source, fixed target and approved opening scope', async () => {
  const raw = { ...source, execution_date: '2026-11-05', metadata_audience_approved: true,
    pilot: { month: '2026-11', activationStart: '2026-11-05T00:00:00.000Z', opening: { amountMicrousd: 0, basisSha256: scopeSha256 } } };
  const bytes = Buffer.from(JSON.stringify(raw)), head = 'a'.repeat(40), w = fixture(), calls = [];
  w.git.run = (args) => {
    calls.push(args);
    if (args[0] === 'rev-parse') return head;
    if (args[0] === 'status') return '';
    if (args[0] === 'remote') return 'https://github.com/ricomanifesto/SentryInsight.git';
    if (args[0] === 'ls-remote') return `${raw.production_main}\trefs/heads/main`;
    throw new Error('private-sentinel');
  };
  const inputs = { git: w.git, manifestBytes: bytes, expectedCommit: head, expectedManifest: sha256(bytes), confirm: true,
    now: () => new Date('2026-11-05T03:04:05.000Z') };
  for (const extra of [{ confirm: false }, { expectedCommit: 'b'.repeat(40) }, { expectedManifest: 'c'.repeat(64) },
    { now: () => new Date('2026-11-06T00:00:00.000Z') },
    { manifestBytes: Buffer.from(JSON.stringify({...source, pilot: null})), expectedManifest: sha256(JSON.stringify({...source, pilot: null})) }]) {
    await assert.rejects(initialize({ ...inputs, ...extra })); assert.equal(w.state.initialPushes.length, 0);
  }
  const result = await initialize(inputs); assert.equal(result.status, 'initialized');
  assert.equal(w.state.initialPushes[0].remote, 'origin'); assert.equal(w.state.initialPushes[0].branch, 'publication-admission');
  assert.equal(result.initialization_id, initializationIdentity(site, scopeSha256).initialization_id);
  assert.equal(JSON.stringify(result).includes('private-sentinel'), false);
});
test('wrong-head bootstrap CLI refuses with fixed secret-free output', () => {
  const bytes = fs.readFileSync(path.resolve(__dirname, '../../config/full-feed-canary.json'));
  const result = childProcess.spawnSync(process.execPath, [path.resolve(__dirname, '../../scripts/bootstrap_canary_ledger.cjs'),
    '--expected-commit', 'a'.repeat(40), '--expected-manifest', sha256(bytes), '--initialize-public-ledger'],
  { env: { PATH: '/usr/bin:/bin:/opt/homebrew/bin', OPENROUTER_API_KEY: 'private-sentinel',
    AWS_ACCESS_KEY_ID: 'private-sentinel', AWS_SECRET_ACCESS_KEY: 'private-sentinel', HTTPS_PROXY: 'private-sentinel' },
  timeout: 3000, maxBuffer: 8192, encoding: 'utf8' });
  assert.equal(result.status, 1); assert.equal(result.stderr, '');
  assert.deepEqual(JSON.parse(result.stdout), { status: 'initialization_refused' });
  assert.equal(result.stdout.includes('private-sentinel'), false);
});
