// One fixed, default-off production verification. The complete reservation
// remains held: optional usage receipts never release uncertain liabilities.
const { sha256, canonicalJson } = require('./canonical');

const PROFILE = Object.freeze({
  id: 'kimi-moonshot-verification-20261117',
  model: 'moonshotai/kimi-k3.1-pro',
  provider: 'moonshotai/mxfp4',
  reportAttempts: 3,
  reportContext: 1048576,
  reportOutput: 32000,
  reportPromptPrice: '2',
  reportCompletionPrice: '10',
  triageModel: 'typesafe/jev-1.13',
  triageProvider: 'typesafe',
  triageRequests: 64,
  triageContext: 262144,
  triagePromptPrice: '0.042',
  triageCompletionPrice: '0',
  reserveMicrousd: Math.ceil(3 * (1048576 * 2 + 32000 * 10) + 64 * 262144 * 42 / 1000),
  limitMicrousd: 8000000,
  periodMicrousd: 20000000,
  periodStart: '2026-11-01T00:00:00.000Z',
  periodEnd: '2026-12-01T00:00:00.000Z',
});
const PROFILE_SHA256 = sha256(canonicalJson(PROFILE));
const HEX64 = /^[a-f0-9]{64}$/;
const money = value => Number.isSafeInteger(value) && value >= 0;
const same = (left, right) => Object.keys(right).every(key => left[key] === right[key]);

function identity(options) {
  if (typeof options.admissionKey !== 'string' || !/^(?:run:[0-9]+|digest:[a-f0-9]{40})$/.test(options.admissionKey)
      || typeof options.runId !== 'string' || !/^[0-9]{1,20}$/.test(options.runId)
      || typeof options.revision !== 'string' || !/^[a-f0-9]{40}$/.test(options.revision)
      || options.runAttempt !== '1') throw new Error('invalid verification identity');
  return { admission_key: options.admissionKey, run_id: options.runId, revision: options.revision,
    profile_id: PROFILE.id, profile_sha256: PROFILE_SHA256 };
}

function billingEvidence(value, now) {
  // This is an explicit, fresh operator attestation from the existing
  // management view, not a claim inferred from ordinary key metadata or
  // response usage.cost. No credentials or account details are persisted.
  if (!Number.isFinite(now) || !value || value.billing !== 'credits-no-applicable-byok'
      || value.coverage !== 'all-applicable-ci-keys'
      || value.periodStart !== PROFILE.periodStart || value.periodEnd !== PROFILE.periodEnd
      || !money(value.actualMicrousd) || typeof value.scopeSha256 !== 'string'
      || !HEX64.test(value.scopeSha256) || !Number.isFinite(Date.parse(value.checkedAt))
      || now - Date.parse(value.checkedAt) < 0 || now - Date.parse(value.checkedAt) >= 3600000
      || now < Date.parse(PROFILE.periodStart) || now >= Date.parse(PROFILE.periodEnd)) {
    throw new Error('verification billing evidence unavailable');
  }
  return value;
}

function historicalLiability(records) {
  const opening = records.filter(row => row.stage === 'pilot_opening');
  if (opening.length !== 1 || opening[0].periodStart !== PROFILE.periodStart
      || opening[0].periodEnd !== PROFILE.periodEnd || opening[0].amountMicrousd !== 0) {
    throw new Error('historical period evidence unavailable');
  }
  const held = new Map();
  let settled = 0;
  for (const row of records) {
    if (row.stage === 'spend_reserved') {
      if (typeof row.generationToken !== 'string' || held.has(row.generationToken)
          || !money(row.amountMicrousd)) throw new Error('invalid historical reservation');
      held.set(row.generationToken, row.amountMicrousd);
    } else if (row.stage === 'spend_settled') {
      if (!held.has(row.generationToken) || !money(row.actualMicrousd)
          || !money(row.releasedMicrousd)
          || row.actualMicrousd + row.releasedMicrousd !== held.get(row.generationToken)) {
        throw new Error('invalid historical settlement');
      }
      settled += row.actualMicrousd;
      held.delete(row.generationToken);
    }
  }
  const uncertain = [...held.values()].reduce((sum, amount) => sum + amount, 0);
  if (!money(uncertain) || !money(settled) || uncertain < 7251456) {
    throw new Error('historical uncertainty hold missing');
  }
  return { uncertain, settled };
}

function createVerificationBudget({ store, requireOwner, now = () => new Date() }) {
  function owned(records, bound) {
    requireOwner(records, bound.admission_key, bound.run_id);
    const reservations = records.filter(row => row.stage === 'verification_reserved');
    const current = now().getTime();
    if (reservations.length !== 1 || !same(reservations[0], bound)
        || reservations[0].amountMicrousd !== PROFILE.reserveMicrousd
        || !Number.isFinite(reservations[0].valid_until)
        || !Number.isFinite(current) || current < Date.parse(PROFILE.periodStart)
        || current >= Math.min(reservations[0].valid_until, Date.parse(PROFILE.periodEnd))) {
      throw new Error('verification reservation unavailable');
    }
  }

  async function reserve(options) {
    const bound = identity(options);
    const evidence = billingEvidence(options.evidence, now().getTime());
    const result = await store.append(records => {
      billingEvidence(evidence, now().getTime());
      requireOwner(records, bound.admission_key, bound.run_id);
      if (records.some(row => row.stage === 'verification_reserved')) {
        throw new Error('verification approval already consumed');
      }
      const { uncertain, settled } = historicalLiability(records);
      if (evidence.actualMicrousd < settled
          || uncertain + evidence.actualMicrousd + PROFILE.reserveMicrousd > PROFILE.periodMicrousd) {
        throw new Error('verification period capacity unavailable');
      }
      const validUntil = Math.min(Date.parse(evidence.checkedAt) + 3600000, Date.parse(PROFILE.periodEnd));
      return { append: [{ stage: 'verification_reserved', ...bound,
        amountMicrousd: PROFILE.reserveMicrousd, evidence_sha256: sha256(canonicalJson(evidence)),
        valid_until: validUntil }],
      value: { reservedMicrousd: PROFILE.reserveMicrousd, profileSha256: PROFILE_SHA256, validUntil } };
    });
    return result.value;
  }

  async function claimTriage(options) {
    const bound = identity(options);
    if (!Number.isInteger(options.slot) || options.slot < 0 || options.slot >= PROFILE.triageRequests
        || typeof options.requestSha256 !== 'string' || !HEX64.test(options.requestSha256)) {
      throw new Error('invalid verification triage claim');
    }
    await store.append(records => {
      owned(records, bound);
      const claims = records.filter(row => row.stage === 'verification_triage_claimed');
      if (claims.length >= PROFILE.triageRequests || claims.some(row => row.slot === options.slot
          || row.request_sha256 === options.requestSha256)) throw new Error('verification triage already claimed');
      return { append: [{ stage: 'verification_triage_claimed', ...bound,
        slot: options.slot, request_sha256: options.requestSha256 }] };
    });
    return { claimed: true };
  }

  async function assertReport(options) {
    const bound = identity(options);
    owned((await store.read()).records, bound);
    return { verified: true };
  }

  return { reserve, claimTriage, assertReport };
}

module.exports = { PROFILE, PROFILE_SHA256, createVerificationBudget };
