const assert = require('node:assert/strict');
const test = require('node:test');

const { PROFILE, createVerificationBudget } = require('../kit/verification-budget');

function world(overrides = {}) {
  let records = [
    { stage: 'pilot_opening', periodStart: '2026-11-01T00:00:00.000Z', periodEnd: '2026-12-01T00:00:00.000Z', amountMicrousd: 0 },
    { stage: 'spend_reserved', generationToken: 'old-held', amountMicrousd: 7251456 },
    { stage: 'spend_reserved', generationToken: 'old-settled', amountMicrousd: 7251456 },
    { stage: 'spend_settled', generationToken: 'old-settled', actualMicrousd: 64110, releasedMicrousd: 7187346 },
  ];
  let queue = Promise.resolve();
  const store = {
    read: async () => ({ records: [...records] }),
    append(decide) {
      const result = queue.then(() => {
        const { append = [], value } = decide([...records]);
        records.push(...append);
        return { value };
      });
      queue = result.catch(() => {});
      return result;
    },
  };
  const owner = { admissionKey: 'run:100', runId: '100', revision: 'a'.repeat(40), runAttempt: '1' };
  const evidence = {
    billing: 'credits-no-applicable-byok', coverage: 'all-applicable-ci-keys',
    periodStart: '2026-11-01T00:00:00.000Z', periodEnd: '2026-12-01T00:00:00.000Z',
    actualMicrousd: 100000, checkedAt: '2026-11-17T16:00:00.000Z',
    scopeSha256: 'b'.repeat(64),
  };
  const budget = createVerificationBudget({ store, requireOwner: (_rows, key, run) => {
    assert.equal(key, owner.admissionKey); assert.equal(run, owner.runId);
  }, now: () => new Date('2026-11-17T16:10:00.000Z'), ...overrides });
  return { budget, owner, evidence, rows: () => records, replaceRows: rows => { records = rows; } };
}

test('the fixed whole-run reserve includes three full report contexts and 64 triage contexts', () => {
  assert.equal(PROFILE.model, 'moonshotai/kimi-k3.1-pro');
  assert.equal(PROFILE.reportAttempts, 3);
  assert.equal(PROFILE.triageRequests, 64);
  assert.equal(PROFILE.reserveMicrousd, 7956100);
  assert.ok(PROFILE.reserveMicrousd <= 8000000);
});

test('one atomic reservation consumes approval and retains the complete amount', async () => {
  const w = world();
  const r = await w.budget.reserve({ ...w.owner, evidence: w.evidence });
  assert.equal(r.reservedMicrousd, 7956100);
  assert.equal(r.validUntil, Date.parse('2026-11-17T17:00:00.000Z'));
  assert.equal(w.rows().filter(x => x.stage === 'verification_reserved').length, 1);
  assert.equal(w.rows().filter(x => x.stage === 'spend_reserved').length, 2);
  await assert.rejects(w.budget.reserve({ ...w.owner, evidence: w.evidence }), /consumed/);
});

test('concurrent attempts consume only one approval', async () => {
  const w = world();
  const outcomes = await Promise.allSettled([1, 2].map(() => w.budget.reserve({ ...w.owner, evidence: w.evidence })));
  assert.equal(outcomes.filter(x => x.status === 'fulfilled').length, 1);
});

for (const extra of [
  { evidence: null }, { runAttempt: '2' }, { runId: 'bad' }, { revision: 'short' },
  { evidence: { billing: 'byok' } },
  { evidence: { actualMicrousd: 4792445 } },
  { evidence: { actualMicrousd: 0 } },
  { evidence: { actualMicrousd: NaN } },
  { evidence: { checkedAt: '2026-11-16T16:00:00.000Z' } },
  { evidence: { checkedAt: '2026-11-18T16:00:00.000Z' } },
  { evidence: { coverage: 'current-key-only' } },
  { evidence: { scopeSha256: '' } },
]) test(`invalid or incomplete activation is refused: ${JSON.stringify(extra)}`, async () => {
  const w = world();
  const args = { ...w.owner, evidence: w.evidence, ...extra };
  if (extra.evidence) args.evidence = { ...w.evidence, ...extra.evidence };
  await assert.rejects(w.budget.reserve(args));
  assert.equal(w.rows().length, 4);
});

test('missing historical evidence cannot initialize a zero-liability period', async () => {
  const w = world(); w.replaceRows([]);
  await assert.rejects(w.budget.reserve({ ...w.owner, evidence: w.evidence }));
});

test('triage claims are durable, unique and bounded, with no refund or retry', async () => {
  const w = world(); await w.budget.reserve({ ...w.owner, evidence: w.evidence });
  for (let slot = 0; slot < 64; slot++) {
    await w.budget.claimTriage({ ...w.owner, slot, requestSha256: slot.toString(16).padStart(64, '0') });
  }
  await assert.rejects(w.budget.claimTriage({ ...w.owner, slot: 64, requestSha256: 'c'.repeat(64) }));
  await assert.rejects(w.budget.claimTriage({ ...w.owner, slot: 0, requestSha256: 'd'.repeat(64) }));
  assert.equal(w.rows().filter(x => x.stage === 'verification_triage_claimed').length, 64);
});

test('a restart, changed checkout or missing reservation cannot claim a send', async () => {
  const w = world();
  const args = { ...w.owner, slot: 0, requestSha256: 'e'.repeat(64) };
  await assert.rejects(w.budget.claimTriage(args));
  await w.budget.reserve({ ...w.owner, evidence: w.evidence });
  await assert.rejects(w.budget.claimTriage({ ...args, revision: 'f'.repeat(40) }));
  await assert.rejects(w.budget.claimTriage({ ...args, runAttempt: '2' }));
  await w.budget.assertReport(w.owner);
});

test('billing evidence must still be fresh inside the atomic reservation', async () => {
  let reads = 0;
  const w = world({ now: () => new Date(reads++ === 0
    ? '2026-11-17T16:10:00.000Z' : '2026-11-17T17:00:00.000Z') });
  await assert.rejects(w.budget.reserve({ ...w.owner, evidence: w.evidence }));
  assert.equal(w.rows().length, 4);
});

for (const [initial, checkedAt, expired] of [
  ['2026-11-17T16:10:00.000Z', '2026-11-17T16:00:00.000Z', '2026-11-17T17:00:00.000Z'],
  ['2026-11-30T23:59:00.000Z', '2026-11-30T23:55:00.000Z', '2026-12-01T00:00:00.000Z'],
]) test(`expired activation never authorizes a later send: ${expired}`, async () => {
  let clock = initial;
  const w = world({ now: () => new Date(clock) });
  await w.budget.reserve({ ...w.owner, evidence: { ...w.evidence, checkedAt } });
  clock = expired;
  await assert.rejects(w.budget.assertReport(w.owner));
  await assert.rejects(w.budget.claimTriage({ ...w.owner, slot: 0, requestSha256: 'f'.repeat(64) }));
  assert.equal(w.rows().filter(row => row.stage === 'verification_triage_claimed').length, 0);
});

test('an invalid current clock fails closed at reservation and later claims', async () => {
  let valid = false;
  const w = world({ now: () => new Date(valid ? '2026-11-17T16:10:00.000Z' : NaN) });
  await assert.rejects(w.budget.reserve({ ...w.owner, evidence: w.evidence }));
  valid = true;
  await w.budget.reserve({ ...w.owner, evidence: w.evidence });
  valid = false;
  await assert.rejects(w.budget.assertReport(w.owner));
  await assert.rejects(w.budget.claimTriage({ ...w.owner, slot: 0, requestSha256: 'f'.repeat(64) }));
});
