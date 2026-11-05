const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const { ProductionSpendPolicy, ProductionSpendBudget, usdToMicrousd, MODEL, PROVIDER, SITE } = require('../kit/production-spend');
const { createStore } = require('../kit/store');
const { CompareAndSetLost } = require('../kit/git');
const { createAdmission } = require('../kit/admission');
const { loadSiteConfig } = require('../kit/config');
const { GIT_ENV, git, siteConfig, tempDir } = require('./helpers');
const SENTRY = SITE === 'SentryInsight';
const START = '2030-01-01T00:00:00.000Z';
const END = '2030-02-01T00:00:00.000Z';
const REV = 'a'.repeat(40), SOURCE = 'b'.repeat(64), REQUEST = 'c'.repeat(64);
function options(extra = {}) {
  return { version: 1, enabled: true, id: 'fictional-policy', revision: REV,
    periodStart: START, periodEnd: END, expiresAt: END,
    generationMicrousd: 10000000, periodMicrousd: 20000000,
    model: MODEL, provider: PROVIDER,
    operations: SENTRY ? [{ id: 'report', maxOutputTokens: 8000, maxAttempts: 3 }]
      : [{ id: 'analysis', maxOutputTokens: 8000, maxAttempts: 1 }, { id: 'plan', maxOutputTokens: 8000, maxAttempts: 1 }], ...extra };
}
function binding(n = 1, extra = {}) { return { admissionKey: `run:${n}`, runId: String(n), runAttempt: '1', revision: REV, sourceSha256: SOURCE, ...extra }; }
function receipt(extra = {}) { return { model: MODEL, provider: null, serviceTier: null,
  promptTokens: 100, completionTokens: 20, reasoningTokens: 3, totalTokens: 120, costMicrousd: 400, costCoverage: 'complete', ...extra }; }
function fixture(config = options()) {
  let tip = null, seq = 0, clock = new Date('2030-01-03T00:00:00.000Z');
  const commits = new Map();
  const g = { fetchBranch: () => tip, showFile: (id) => commits.get(id),
    commitFiles(files) { const id = String(++seq); commits.set(id, files.get('state.json')); return id; },
    pushBranch(_remote, id, _branch, expected) { if (expected !== tip) throw new CompareAndSetLost(); tip = id; } };
  const store = createStore({ git: g, remote: 'synthetic', branch: 'synthetic', site: SITE, now: () => clock });
  const owners = new Map([[1, '1'], [2, '2'], [3, '3']]);
  function requireOwner(_records, key, run) { assert.equal(owners.get(Number(key.slice(4))), run); return 0; }
  const make = (p = config, s = store) => new ProductionSpendBudget({ store: s, requireOwner,
    policy: p === undefined ? undefined : new ProductionSpendPolicy(p), now: () => clock });
  return { store, make, owners, setClock: (value) => { clock = new Date(value); } };
}
async function send(budget, gen, operation, outcome = 'accepted', info = receipt()) {
  const handle = await budget.beginSend(gen, { operation, requestSha256: REQUEST });
  await budget.finishSend(gen, handle, { outcome, receipt: info }); return handle;
}
async function complete(budget, gen) {
  for (const op of options().operations) await send(budget, gen, op.id);
  return budget.settleGeneration(gen, { outcome: 'completed' });
}
function held(records) {
  return records.filter((r) => r.stage === 'spend_reserved').reduce((s, r) => s + r.amountMicrousd, 0)
    - records.filter((r) => r.stage === 'spend_settled').reduce((s, r) => s + r.releasedMicrousd, 0);
}

test('absent/disabled policy is inert and appends nothing', async () => {
  const f = fixture();
  for (const p of [undefined, { version: 1, enabled: false }]) {
    const b = new ProductionSpendBudget({ store: f.store, requireOwner() { throw Error('not called'); }, policy: p });
    await assert.rejects(b.reserveGeneration(binding()), /Spend/);
  }
  assert.equal((await f.store.read()).records.length, 0);
});
for (const [name, value] of [['negative', -1], ['bool', true], ['float', 1.5], ['nan', NaN], ['infinity', Infinity], ['unsafe', Number.MAX_SAFE_INTEGER + 1]]) {
  test(`strict money rejects ${name}`, () => assert.throws(() => new ProductionSpendPolicy(options({ periodMicrousd: value })), /Spend/));
}
for (const [input, output] of [['0', 0], ['0.0000001', 1], ['0.01115', 11150], ['2.0000000', 2000000]]) {
  test(`decimal cost conservatively rounds ${input}`, () => assert.equal(usdToMicrousd(input), output));
}
for (const input of [null, true, -1, 1.5, 'NaN', '-1', '1e3', '9007199254740992']) {
  test(`malformed decimal refuses ${String(input)}`, () => assert.throws(() => usdToMicrousd(input), /Spend/));
}
test('policy and operation snapshots are immutable', () => {
  const raw = options(); const p = new ProductionSpendPolicy(raw); raw.operations[0].maxOutputTokens = 1;
  assert.equal(p.value.operations[0].maxOutputTokens, 8000); assert(Object.isFrozen(p.value)); assert(Object.isFrozen(p.value.operations[0]));
});
test('context fallback is reserved financially, not a tokenizer estimate', async () => {
  const f = fixture(); const b = f.make(); await b.reserveGeneration(binding());
  const r = (await f.store.read()).records.find((v) => v.stage === 'spend_reserved');
  assert.equal(r.amountMicrousd, (1048576 * 2 + 8000 * 10) * (SENTRY ? 3 : 2));
});
test('atomic racing generations cannot exceed the exact period boundary', async () => {
  const amount = (1048576 * 2 + 8000 * 10) * (SENTRY ? 3 : 2);
  const f = fixture(options({ generationMicrousd: amount, periodMicrousd: amount }));
  const results = await Promise.allSettled([f.make().reserveGeneration(binding(1)), f.make().reserveGeneration(binding(2))]);
  assert.equal(results.filter((v) => v.status === 'fulfilled').length, 1);
  assert.equal(held((await f.store.read()).records), amount);
});
for (const changed of [{ runAttempt: '2' }, { revision: 'd'.repeat(40) }, { sourceSha256: 'private raw source' }, { runId: '2' }]) {
  test(`generation identity refuses ${Object.keys(changed)[0]}`, async () => {
    const f = fixture(); await assert.rejects(f.make().reserveGeneration(binding(1, changed)), /Spend/);
    assert.equal((await f.store.read()).records.length, 0);
  });
}
test('restart/replay/readmission/policy changes cannot reset a generation or money', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  for (const b2 of [f.make(), f.make(options({ id: 'changed-policy' }))]) {
    await assert.rejects(b2.reserveGeneration(binding()), /Spend/);
    await assert.rejects(b2.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST }), /Spend/);
  }
  f.owners.set(1, '2'); await assert.rejects(b.reserveGeneration(binding(1, { runId: '2' })), /Spend/);
});
test('missing or contradictory usage stops continuation and retains full hold', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding()); const initial = held((await f.store.read()).records);
  const h = await b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST });
  await b.finishSend(g, h, { outcome: 'accepted', receipt: receipt({ costMicrousd: null }) });
  await assert.rejects(b.beginSend(g, { operation: options().operations.at(-1).id, requestSha256: REQUEST }), /Spend/);
  await assert.rejects(b.settleGeneration(g, { outcome: 'completed' }), /Spend/);
  assert.equal(held((await f.store.read()).records), initial);
});
test('terminal settlement releases excess once and preserves unavailable attestation', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding()); await complete(b, g);
  const records = (await f.store.read()).records;
  assert.equal(held(records), SENTRY ? 400 : 800);
  assert.equal(records.find((r) => r.stage === 'spend_finished').receipt.serviceTier, null);
  await assert.rejects(b.settleGeneration(g, { outcome: 'completed' }), /Spend/);
  await assert.rejects(b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST }), /Spend/);
});
test('known rejected first stage cannot authorize plan; terminal refusal may settle unused slots', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  await send(b, g, options().operations[0].id, 'rejected');
  await assert.rejects(b.beginSend(g, { operation: options().operations.at(-1).id, requestSha256: REQUEST }), /Spend/);
  await b.settleGeneration(g, { outcome: 'refused' }); assert.equal(held((await f.store.read()).records), 400);
});
test('expiry blocks new sends but permits trusted recording and settlement', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  const h = await b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST });
  f.setClock('2030-02-03T00:00:00.000Z');
  await b.finishSend(g, h, { outcome: 'rejected', receipt: receipt() });
  await b.settleGeneration(g, { outcome: 'refused' });
  await assert.rejects(b.reserveGeneration(binding(2)), /Spend/);
});
test('unknown earlier period survives rollover and cannot become zero', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  await send(b, g, options().operations[0].id, 'uncertain', null);
  f.setClock('2030-02-03T00:00:00.000Z');
  const later = f.make(options({ periodStart: END, periodEnd: '2030-03-01T00:00:00.000Z', expiresAt: '2030-03-01T00:00:00.000Z' }));
  await assert.rejects(later.reserveGeneration(binding(2)), /Spend/);
});
test('lost append acknowledgement latches this owner and does not replay', async () => {
  const f = fixture(); let calls = 0;
  const b = f.make(options(), { append: async (fn) => { calls++; await f.store.append(fn); throw Error('PRIVATE ANSWER KEY'); } });
  await assert.rejects(b.reserveGeneration(binding()), /Spend/);
  await assert.rejects(b.reserveGeneration(binding(2)), /Spend/);
  assert.equal(calls, 1); assert.equal((await f.store.read()).records.length, 1);
  assert(!JSON.stringify((await f.store.read()).records).includes('PRIVATE ANSWER KEY'));
});
for (const bad of [{ model: 'wrong' }, { serviceTier: 'priority' }, { provider: 'wrong' }, { totalTokens: 119 }, { completionTokens: 1 }, { promptTokens: 1048577 }, { costMicrousd: 99999 }, { costMicrousd: false }]) {
  test(`inconsistent response ${Object.keys(bad)[0]} remains held`, async () => {
    const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding()); const h = await b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST });
    await assert.rejects(b.finishSend(g, h, { outcome: 'accepted', receipt: receipt(bad) }), /Spend/);
    await assert.rejects(b.settleGeneration(g, { outcome: 'completed' }), /Spend/);
  });
}
test('actual local Git CAS and admission ownership remain the authority', async (t) => {
  const root = tempDir(t, 'spend-local-'); const remote = path.join(root, 'remote.git'); const repo = path.join(root, 'repo');
  git(root, 'init', '--quiet', '--bare', remote); fs.mkdirSync(repo); git(repo, 'init', '--quiet', '--initial-branch=main');
  git(repo, 'remote', 'add', 'origin', remote); fs.writeFileSync(path.join(repo, 'README.md'), 'fixture'); git(repo, 'add', '.'); git(repo, 'commit', '--quiet', '-m', 'fixture');
  const a = createAdmission({ repoRoot: repo, remote, config: loadSiteConfig(siteConfig({ site: SITE, repository: `ricomanifesto/${SITE}` })), consumer: SITE,
    fetchUrl: async () => { throw Error('network forbidden'); }, gitEnv: GIT_ENV, productionSpendPolicy: new ProductionSpendPolicy(options()), now: () => new Date('2030-01-03T00:00:00.000Z') });
  await a.admit({ eventName: 'workflow_dispatch', payload: null, runId: '1', runAttempt: '1', readmit: false });
  await assert.rejects(a.productionSpend.reserveGeneration(binding()), /Spend/);
  await a.invoked({ admissionKey: 'run:1', runId: '1' });
  const g = await a.productionSpend.reserveGeneration(binding()); await complete(a.productionSpend, g);
  const records = (await a.readState()).records; assert.equal(held(records), SENTRY ? 400 : 800);
  if (SENTRY) {
    const reserved = records.find((r) => r.stage === 'request_reserved'); const spent = records.find((r) => r.stage === 'spend_sending');
    assert.equal(reserved.token, spent.token); assert.equal(reserved.attempt, spent.attempt);
  }
});

for (const bad of [{ periodStart: '2030-01-01' }, { expiresAt: START }, { model: 'openrouter/auto' }, { provider: 'other' }, { operations: [] }, { generationMicrousd: 0 }]) {
  test(`malformed trusted policy ${Object.keys(bad)[0]} refuses`, () => assert.throws(() => new ProductionSpendPolicy(options(bad)), /Spend/));
}
test('source/request/handle rebinds and raw fields refuse without ledger leakage', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  for (const bad of [{ ...g, sourceSha256: 'd'.repeat(64) }, { ...g, revision: 'd'.repeat(40) }, { ...g, runId: '2' }, { ...g, answer: 'PRIVATE ANSWER' }]) {
    await assert.rejects(b.beginSend(bad, { operation: options().operations[0].id, requestSha256: REQUEST }), /Spend/);
  }
  await assert.rejects(b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST, policy: 'PRIVATE KEY' }), /Spend/);
  assert(!JSON.stringify((await f.store.read()).records).includes('PRIVATE'));
});
test('terminal settlement validates outcome and preserves all earlier physical outcomes', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  const h = await send(b, g, options().operations[0].id, 'rejected');
  await assert.rejects(b.finishSend(g, h, { outcome: 'accepted', receipt: receipt() }), /Spend/);
  await assert.rejects(b.settleGeneration(g, { outcome: 'completed' }), /Spend/);
  await b.settleGeneration(g, { outcome: 'refused' });
  assert.equal((await f.store.read()).records.filter((v) => v.stage === 'spend_finished')[0].outcome, 'rejected');
});
test('fully known old period can roll over while overlapping/new policy cannot erase funds', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding()); await complete(b, g);
  await assert.rejects(f.make(options({ id: 'new-bucket' })).reserveGeneration(binding(2)), /Spend/);
  f.setClock('2030-02-03T00:00:00.000Z');
  const later = f.make(options({ id: 'next-explicit-period', periodStart: END, periodEnd: '2030-03-01T00:00:00.000Z', expiresAt: '2030-03-01T00:00:00.000Z' }));
  await later.reserveGeneration(binding(2));
});
for (const failure of ['send', 'finish', 'settle']) {
  test(`unknown ${failure} acknowledgement holds and is never automatically replayed`, async () => {
    const f = fixture(); let fail = false, writes = 0;
    const store = { append: async (fn) => { writes++; const value = await f.store.append(fn); if (fail) throw Error('PRIVATE ERROR KEY'); return value; } };
    const b = f.make(options(), store); const g = await b.reserveGeneration(binding());
    let action;
    if (failure === 'send') action = () => b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST });
    else if (failure === 'finish') {
      const h = await b.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST }); action = () => b.finishSend(g, h, { outcome: 'accepted', receipt: receipt() });
    } else {
      for (const op of options().operations) await send(b, g, op.id); action = () => b.settleGeneration(g, { outcome: 'completed' });
    }
    fail = true; await assert.rejects(action(), /Spend/); const count = writes;
    await assert.rejects(action(), /Spend/); assert.equal(writes, count);
    await assert.rejects(f.make().reserveGeneration(binding()), /Spend/);
    assert(!JSON.stringify((await f.store.read()).records).includes('PRIVATE'));
  });
}
test('operation attempts and ordering never mint another controller', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  if (!SENTRY) {
    await assert.rejects(b.beginSend(g, { operation: 'plan', requestSha256: REQUEST }), /Spend/);
    await send(b, g, 'analysis', 'retryable');
    await assert.rejects(b.beginSend(g, { operation: 'analysis', requestSha256: REQUEST }), /Spend/);
    await assert.rejects(b.beginSend(g, { operation: 'plan', requestSha256: REQUEST }), /Spend/);
    await b.settleGeneration(g, { outcome: 'refused' });
  } else {
    for (let i = 0; i < 3; i++) await send(b, g, 'report', 'retryable');
    await assert.rejects(b.beginSend(g, { operation: 'report', requestSha256: REQUEST }), /Spend/);
    const records = (await f.store.read()).records;
    assert.equal(records.filter((v) => v.stage === 'request_reserved').length, 3);
    assert.deepEqual(records.filter((v) => v.stage === 'request_reserved').map((v) => v.token), records.filter((v) => v.stage === 'spend_sending').map((v) => v.token));
    await b.settleGeneration(g, { outcome: 'refused' });
  }
});

for (const malformed of ['missing', 'mismatched']) {
  test(`malformed ${malformed} append acknowledgement is unknown and cannot authorize`, async () => {
    const f = fixture(); let writes = 0;
    const store = { append: async (fn) => { writes++; await f.store.append(fn); return malformed === 'missing' ? {} : { value: { raw: 'PRIVATE SECRET' } }; } };
    const b = f.make(options(), store);
    await assert.rejects(b.reserveGeneration(binding()), (error) => error.code === 'persistence_unknown' && !error.message.includes('PRIVATE'));
    await assert.rejects(b.reserveGeneration(binding(2)), /Spend/);
    assert.equal(writes, 1);
  });
}

test('reported platform cost with unknown total liability is partial, never refundable', async () => {
  const f = fixture(); const b = f.make(); const g = await b.reserveGeneration(binding());
  const amount = held((await f.store.read()).records);
  await send(b, g, options().operations[0].id, 'accepted', receipt({ costCoverage: 'unknown' }));
  await assert.rejects(b.settleGeneration(g, { outcome: 'completed' }), /Spend/);
  await assert.rejects(b.beginSend(g, { operation: options().operations.at(-1).id, requestSha256: REQUEST }), /Spend/);
  const rows = (await f.store.read()).records;
  assert.equal(rows.find((v) => v.stage === 'spend_finished').receipt.costMicrousd, 400);
  assert.equal(rows.find((v) => v.stage === 'spend_finished').outcome, 'uncertain');
  assert.equal(held(rows), amount);
});

test('same-period financial terms permit a new revision without resetting exact cap usage', async () => {
  const amount = (1048576 * 2 + 8000 * 10) * (SENTRY ? 3 : 2), known = SENTRY ? 400 : 800;
  const terms = options({ generationMicrousd: amount, periodMicrousd: amount + known });
  const f = fixture(terms); const first = f.make(); const g = await first.reserveGeneration(binding()); await complete(first, g);
  const revision = 'd'.repeat(40), next = f.make({ ...terms, revision });
  await next.reserveGeneration(binding(2, { revision }));
  assert.equal(held((await f.store.read()).records), amount + known);
  await assert.rejects(next.reserveGeneration(binding(3, { revision })), /Spend/);
});
test('new revision counts unresolved old same-period allocation in full', async () => {
  const amount = (1048576 * 2 + 8000 * 10) * (SENTRY ? 3 : 2);
  const terms = options({ generationMicrousd: amount, periodMicrousd: amount * 2 });
  const f = fixture(terms); await f.make().reserveGeneration(binding());
  const revision = 'd'.repeat(40), next = f.make({ ...terms, revision });
  await next.reserveGeneration(binding(2, { revision }));
  assert.equal(held((await f.store.read()).records), amount * 2);
  await assert.rejects(next.reserveGeneration(binding(3, { revision })), /Spend/);
});
test('cross-revision comparison never permits rebinding an existing generation', async () => {
  const f = fixture(); const first = f.make(); const g = await first.reserveGeneration(binding());
  const revision = 'd'.repeat(40), next = f.make(options({ revision }));
  await assert.rejects(next.reserveGeneration(binding(1, { revision })), /Spend/);
  await assert.rejects(next.beginSend(g, { operation: options().operations[0].id, requestSha256: REQUEST }), /Spend/);
  assert.equal((await f.store.read()).records.length, 1);
});
test('no-decision undefined acknowledgement is unknown and latches once', async () => {
  const f = fixture(); let calls = 0;
  const b = f.make(options(), { append: async () => { calls++; return { value: undefined }; } });
  await assert.rejects(b.reserveGeneration(binding()), (error) => error.code === 'persistence_unknown');
  await assert.rejects(b.reserveGeneration(binding(2)), /Spend/);
  assert.equal(calls, 1); assert.equal((await f.store.read()).records.length, 0);
});

test('a produced decision followed by replay refusal is persistence unknown', async () => {
  const f = fixture(); let calls = 0;
  const store = { append: async (decide) => {
    calls++; await f.store.append(decide); return f.store.append(decide);
  } };
  const b = f.make(options(), store);
  await assert.rejects(b.reserveGeneration(binding()), (error) => error.code === 'persistence_unknown');
  await assert.rejects(b.reserveGeneration(binding(2)), /Spend/);
  assert.equal(calls, 1); assert.equal((await f.store.read()).records.length, 1);
});
