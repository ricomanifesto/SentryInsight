const assert = require('node:assert/strict');
const test = require('node:test');

const {
  READINESS_PROFILE, READINESS_PROFILE_SHA256, createReadinessBudget, createVerificationBudget,
} = require('../kit/verification-budget');

const MANIFEST = 'a'.repeat(64);
const REQUEST = 'e'.repeat(64);

function world(overrides = {}, extraRows = []) {
  let records = [
    { stage: 'pilot_opening', periodStart: '2026-11-01T00:00:00.000Z', periodEnd: '2026-12-01T00:00:00.000Z', amountMicrousd: 0 },
    { stage: 'spend_reserved', generationToken: 'old-held', amountMicrousd: 7251456 },
    ...extraRows,
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
  const owner = { admissionKey: 'run:100', runId: '100', revision: 'c'.repeat(40), runAttempt: '1' };
  const evidence = {
    billing: 'credits-no-applicable-byok', coverage: 'all-applicable-ci-keys',
    periodStart: '2026-11-01T00:00:00.000Z', periodEnd: '2026-12-01T00:00:00.000Z',
    actualMicrousd: 100000, checkedAt: '2026-11-21T08:55:00.000Z', scopeSha256: 'b'.repeat(64),
  };
  const options = { store, requireOwner: (_rows, key, run) => {
    assert.equal(key, owner.admissionKey); assert.equal(run, owner.runId);
  }, now: () => new Date('2026-11-21T09:00:00.000Z'), ...overrides };
  return { budget: createReadinessBudget(options), verification: createVerificationBudget(options),
    owner, evidence, rows: () => records };
}

const reserve = w => w.budget.reserve({ ...w.owner, evidence: w.evidence, factManifestSha256: MANIFEST });
const claim = (w, extra = {}) => w.budget.claimReport({ ...w.owner, requestSha256: REQUEST, factManifestSha256: MANIFEST, ...extra });

test('one full context plus full output, zero triage, under the hard cap', () => {
  assert.equal(READINESS_PROFILE.model, 'moonshotai/kimi-k3.1-pro');
  assert.equal(READINESS_PROFILE.provider, 'moonshotai/mxfp4');
  assert.equal(READINESS_PROFILE.reportAttempts, 1);
  assert.equal(READINESS_PROFILE.triageRequests, 0);
  assert.equal(READINESS_PROFILE.reserveMicrousd, 1048576 * 2 + 32000 * 10);
  assert.equal(READINESS_PROFILE.reserveMicrousd, 2417152);
  assert.ok(READINESS_PROFILE.reserveMicrousd <= READINESS_PROFILE.limitMicrousd);
  assert.ok(READINESS_PROFILE.limitMicrousd <= 2420000);
  // The Python route pins this same digest independently.
  assert.equal(READINESS_PROFILE_SHA256, 'b892d97a1df2c76e5547a078a8c81bb9d622bf4d2aba688facbcd802bab5c951');
  assert.ok(Object.isFrozen(READINESS_PROFILE));
});

test('one reservation binds the manifest digest and consumes the approval', async () => {
  const w = world();
  const result = await reserve(w);
  assert.deepEqual(result, { reservedMicrousd: 2417152, profileSha256: READINESS_PROFILE_SHA256,
    factManifestSha256: MANIFEST, validUntil: Date.parse('2026-11-21T09:55:00.000Z') });
  const [row] = w.rows().filter(r => r.stage === 'readiness_reserved');
  assert.equal(row.fact_manifest_sha256, MANIFEST);
  assert.equal(row.amountMicrousd, 2417152);
  await assert.rejects(reserve(w), /consumed/);
});

test('concurrent reservations consume only one approval', async () => {
  const w = world();
  const outcomes = await Promise.allSettled([1, 2].map(() => reserve(w)));
  assert.equal(outcomes.filter(x => x.status === 'fulfilled').length, 1);
});

for (const [name, rows] of [
  ['earlier paid verification', [{ stage: 'verification_reserved', admission_key: 'run:90' }]],
  ['earlier readiness claim', [{ stage: 'readiness_report_claimed', admission_key: 'run:90' }]],
  ['unresolved send under this admission', [{ stage: 'request_reserved', admission_key: 'run:100' }]],
]) test(`no readmission after ${name}`, async () => {
  const w = world({}, rows);
  await assert.rejects(reserve(w), /consumed or prior send unresolved/);
  assert.equal(w.rows().filter(r => r.stage === 'readiness_reserved').length, 0);
});

for (const extra of [
  { factManifestSha256: undefined }, { factManifestSha256: 'A'.repeat(64) },
  { runAttempt: '2' }, { evidence: { billing: 'byok' } },
  { evidence: { checkedAt: '2026-11-21T07:00:00.000Z' } },
]) test(`invalid activation is refused: ${JSON.stringify(extra)}`, async () => {
  const w = world();
  const args = { ...w.owner, evidence: w.evidence, factManifestSha256: MANIFEST, ...extra };
  if (extra.evidence) args.evidence = { ...w.evidence, ...extra.evidence };
  await assert.rejects(w.budget.reserve(args));
  assert.equal(w.rows().length, 2);
});

test('missing unresolved-liability history refuses the reservation', async () => {
  const w = world();
  w.rows().splice(1, 1);
  await assert.rejects(reserve(w), /uncertainty hold missing/);
});

test('exactly one durable report claim, bound to the reserved manifest', async () => {
  const w = world();
  await assert.rejects(claim(w), /reservation unavailable/);
  await reserve(w);
  await assert.rejects(claim(w, { factManifestSha256: 'f'.repeat(64) }), /manifest changed/);
  assert.deepEqual(await claim(w), { claimed: true });
  await assert.rejects(claim(w), /already claimed/);
  await assert.rejects(claim(w, { requestSha256: 'd'.repeat(64) }), /already claimed/);
  assert.equal(w.rows().filter(r => r.stage === 'readiness_report_claimed').length, 1);
  assert.equal(w.rows().filter(r => r.stage.startsWith('verification_triage')).length, 0);
});

test('an expired reservation never authorizes the claim', async () => {
  let clock = '2026-11-21T09:00:00.000Z';
  const w = world({ now: () => new Date(clock) });
  await reserve(w);
  clock = '2026-11-21T09:55:00.000Z';
  await assert.rejects(claim(w), /reservation unavailable/);
});

test('a readiness reservation blocks a later whole-run verification reservation', async () => {
  const w = world();
  await reserve(w);
  await assert.rejects(w.verification.reserve({ ...w.owner, evidence: w.evidence }), /consumed/);
});
