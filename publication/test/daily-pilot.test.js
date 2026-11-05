const assert = require('node:assert/strict');
const test = require('node:test');
const { DailyPilot } = require('../kit/daily-pilot');
const { ProductionSpendBudget } = require('../kit/production-spend');
const { createStore } = require('../kit/store');
const { CompareAndSetLost } = require('../kit/git');
const REV = 'a'.repeat(40), SOURCE = 'b'.repeat(64), BASIS = 'c'.repeat(64);
function config(extra = {}) { return { month: '2030-01', activationStart: '2030-01-01T00:00:00.000Z', opening: { amountMicrousd: 0, basisSha256: BASIS }, ...extra }; }
function binding(id = 1, extra = {}) { return { admissionKey: `run:${id}`, runId: String(id), runAttempt: '1', revision: REV, sourceSha256: SOURCE, ...extra }; }
function world() {
  let tip = null, n = 0, time = new Date('2030-01-03T00:00:00.000Z'); const commits = new Map();
  const git = { fetchBranch: () => tip, showFile: (id) => commits.get(id), commitFiles(files) { const id = String(++n); commits.set(id, files.get('state.json')); return id; }, pushBranch(_r, id, _b, expected) { if (tip !== expected) throw new CompareAndSetLost(); tip = id; } };
  const store = createStore({ git, remote: 'synthetic', branch: 'synthetic', site: 'SentryInsight', now: () => time });
  return { store, setTime(value) { time = new Date(value); }, make(c = config(), revision = REV) {
    const dailyGate = new DailyPilot(c);
    return new ProductionSpendBudget({ store, requireOwner: () => 0, policy: dailyGate.policy(revision), dailyGate, now: () => time });
  } };
}
test('missing activation is disabled; unknown opening liability never becomes zero', async () => {
  const w = world();
  await assert.rejects(w.make(null).reserveGeneration(binding()), /Spend/);
  await assert.rejects(w.make(config({ opening: null })).reserveGeneration(binding()), /Spend/);
  assert.equal((await w.store.read()).records.length, 0);
});
test('concurrent runs share one durable UTC day and whole-generation reservation', async () => {
  const w = world(); const results = await Promise.allSettled([w.make().reserveGeneration(binding(1)), w.make().reserveGeneration(binding(2))]);
  assert.equal(results.filter((r) => r.status === 'fulfilled').length, 1);
  const records = (await w.store.read()).records;
  assert.equal(records.filter((r) => r.stage === 'pilot_daily').length, 1);
  assert.equal(records.filter((r) => r.stage === 'spend_reserved').length, 1);
  assert.equal(records.find((r) => r.stage === 'spend_reserved').amountMicrousd, 7251456);
});
test('new revision/rerun/readmission cannot reopen a claimed day', async () => {
  const w = world(); await w.make().reserveGeneration(binding()); const revision = 'd'.repeat(40);
  await assert.rejects(w.make(config(), revision).reserveGeneration(binding(2, { revision })), /Spend/);
  assert.equal((await w.store.read()).records.filter((r) => r.stage === 'pilot_daily').length, 1);
});
test('next day does not reset money; unresolved previous month blocks rollover', async () => {
  const w = world(); await w.make().reserveGeneration(binding(1));
  w.setTime('2030-01-04T00:00:00.000Z'); await w.make().reserveGeneration(binding(2));
  w.setTime('2030-01-05T00:00:00.000Z'); await assert.rejects(w.make().reserveGeneration(binding(3)), /Spend/);
  w.setTime('2030-02-01T00:00:00.000Z');
  await assert.rejects(w.make(config({ month: '2030-02' })).reserveGeneration(binding(4)), /Spend/);
});
test('opening liability is immutable and charged in the same period budget', async () => {
  const w = world(); const c = config({ opening: { amountMicrousd: 13000000, basisSha256: BASIS } });
  await assert.rejects(w.make(c).reserveGeneration(binding()), /Spend/);
  assert.equal((await w.store.read()).records.length, 0);
});
test('complete known settlement refunds money but never the daily slot', async () => {
  const w = world(); const b = w.make(); const g = await b.reserveGeneration(binding());
  const send = await b.beginSend(g, { operation: 'report', requestSha256: 'f'.repeat(64) });
  await b.finishSend(g, send, { outcome: 'accepted', receipt: { model: 'moonshotai/kimi-k3.1-pro', provider: null, serviceTier: null, promptTokens: 100, completionTokens: 20, reasoningTokens: 3, totalTokens: 120, costMicrousd: 400, costCoverage: 'complete' } });
  await b.settleGeneration(g, { outcome: 'completed' });
  await assert.rejects(w.make().reserveGeneration(binding(2)), /Spend/);
  w.setTime('2030-01-04T00:00:00.000Z'); await w.make().reserveGeneration(binding(2));
});

test('unknown in-scope pre-ledger opening remains disabled in a later month', async () => {
  const w = world(); w.setTime('2030-02-03T00:00:00.000Z');
  await assert.rejects(w.make(config({ month: '2030-02', opening: null })).reserveGeneration(binding()), /Spend/);
  assert.equal((await w.store.read()).records.length, 0);
});
test('a changed known opening assertion cannot refund or rewrite an existing month', async () => {
  const w = world(); await w.make().reserveGeneration(binding()); w.setTime('2030-01-04T00:00:00.000Z');
  await assert.rejects(w.make(config({ opening: { amountMicrousd: 1, basisSha256: 'd'.repeat(64) } })).reserveGeneration(binding(2)), /Spend/);
  const records = (await w.store.read()).records;
  assert.equal(records.filter((r) => r.stage === 'pilot_opening').length, 1);
  assert.equal(records.filter((r) => r.stage === 'pilot_daily').length, 1);
});
