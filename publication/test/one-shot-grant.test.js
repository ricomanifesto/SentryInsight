const assert = require('node:assert/strict');
const test = require('node:test');
const { DailyPilot } = require('../kit/daily-pilot');
const { ProductionSpendBudget } = require('../kit/production-spend');
const { createStore } = require('../kit/store');
const { CompareAndSetLost } = require('../kit/git');
const REV = 'a'.repeat(40), SOURCE = 'b'.repeat(64), REQUEST = 'c'.repeat(64);
function world() {
  let tip = null, n = 0; const blobs = new Map();
  const git = { fetchBranch: () => tip, showFile: (id) => blobs.get(id), commitFiles(files) { const id = String(++n); blobs.set(id, files.get('state.json')); return id; }, pushBranch(_r, id, _b, old) { if (old !== tip) throw new CompareAndSetLost(); tip = id; } };
  const now = () => new Date('2030-01-03T00:00:00.000Z');
  const store = createStore({ git, remote: 'synthetic', branch: 'synthetic', site: 'SentryInsight', now });
  const pilot = new DailyPilot({ month: '2030-01', activationStart: '2030-01-01T00:00:00.000Z', opening: { amountMicrousd: 0, basisSha256: 'd'.repeat(64) } });
  const make = () => new ProductionSpendBudget({ store, requireOwner: () => 0, policy: pilot.policy(REV), dailyGate: pilot, now });
  return { store, make, binding: { admissionKey: 'run:1', runId: '1', runAttempt: '1', revision: REV, sourceSha256: SOURCE } };
}
function receipt() { return { model: 'moonshotai/kimi-k3.1-pro', provider: null, serviceTier: null, promptTokens: 100, completionTokens: 20, reasoningTokens: 2, totalTokens: 120, costMicrousd: 400, costCoverage: 'complete' }; }
for (const outcome of ['accepted', 'rejected', 'retryable', 'uncertain']) {
  test(`one-shot ${outcome} cannot mint a second physical token`, async () => {
    const w = world(), b = w.make(); const g = await b.reserveOneShotGeneration(w.binding);
    const h = await b.beginSend(g, { operation: 'report', requestSha256: REQUEST });
    await b.finishSend(g, h, { outcome, receipt: outcome === 'uncertain' ? null : receipt() });
    await assert.rejects(b.beginSend(g, { operation: 'report', requestSha256: REQUEST }), /Spend/);
    await assert.rejects(w.make().reserveOneShotGeneration(w.binding), /Spend/);
    const rows = (await w.store.read()).records;
    assert.equal(rows.filter((r) => r.stage === 'request_reserved').length, 1);
    assert.equal(rows.find((r) => r.stage === 'request_reserved').limit, 1);
    assert.equal(rows.find((r) => r.stage === 'spend_reserved').amountMicrousd, 7251456);
    assert.equal(rows.find((r) => r.stage === 'spend_reserved').physicalLimit, 1);
    assert.equal(rows.find((r) => r.stage === 'request_reserved').token, h.token);
  });
}
test('ordinary daily reserve retains all three physical attempts and full hold', async () => {
  const w = world(), b = w.make(); const g = await b.reserveGeneration(w.binding);
  await b.beginSend(g, { operation: 'report', requestSha256: REQUEST });
  const rows = (await w.store.read()).records;
  assert.equal(rows.find((r) => r.stage === 'request_reserved').limit, 3);
  assert.equal(rows.find((r) => r.stage === 'spend_reserved').amountMicrousd, 7251456);
});
test('actual Moonshot AI label is preserved without inventing complete billing proof', async () => {
  const w = world(), b = w.make(); const g = await b.reserveOneShotGeneration(w.binding);
  const h = await b.beginSend(g, { operation: 'report', requestSha256: REQUEST });
  const actual = { ...receipt(), provider: 'Moonshot AI', promptTokens: 2780, completionTokens: 559, reasoningTokens: 168, totalTokens: 3339, costMicrousd: 11150, costCoverage: 'unknown' };
  await b.finishSend(g, h, { outcome: 'accepted', receipt: actual });
  const rows = (await w.store.read()).records;
  assert.equal(rows.find((r) => r.stage === 'spend_finished').receipt.provider, 'Moonshot AI');
  assert.equal(rows.find((r) => r.stage === 'spend_finished').outcome, 'uncertain');
  await assert.rejects(b.settleGeneration(g, { outcome: 'completed' }), /Spend/);
});
