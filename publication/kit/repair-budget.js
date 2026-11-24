// Separate bounded budget for informed repair requests, kept in the same CAS
// admission store as the original request budget. Its stages
// (`repair_reserved` / `repair_finished`) are distinct from the original
// episode's (`request_reserved` / `request_finished`), so a repair slot can
// never collide with, extend or reopen the original episode. A repair slot is
// available only after the original episode's latest completion recorded a
// received response, never during paid verification, at most MAX_REPAIRS_CAP
// times per admitted run, and one slot at a time. Each slot is bound to its
// own request digest.
const { randomBytes } = require('node:crypto');

const MAX_REPAIRS_CAP = 6;
const FINISH_STATES = new Set([
  'not_sent', 'retryable_rejection', 'response_received', 'permanent_rejection',
  'uncertain', 'deferred_rejection',
]);

function boundedRepairIdentity(options) {
  const fields = [
    ['admission_key', options.admissionKey, /^(?:run:[0-9]+|digest:[a-f0-9]{40})$/],
    ['run_id', options.runId, /^[0-9]{1,20}$/],
    ['revision', options.revision, /^[a-f0-9]{40}$/],
    ['request_sha256', options.requestSha256, /^[a-f0-9]{64}$/],
  ];
  const bound = {};
  for (const [name, value, format] of fields) {
    if (typeof value !== 'string' || !format.test(value)) throw new Error('invalid repair budget identity');
    bound[name] = value;
  }
  if (!Number.isInteger(options.maxRepairs) || options.maxRepairs < 1 || options.maxRepairs > MAX_REPAIRS_CAP) {
    throw new Error('invalid repair budget limit');
  }
  return { ...bound, max_repairs: options.maxRepairs };
}

function validCompletion(disposition, delay) {
  return FINISH_STATES.has(disposition) && Number.isFinite(delay) && delay >= 0 && delay <= 30;
}

function createRepairBudget({ store, requireOwner }) {
  function replay(records, bound) {
    const start = requireOwner(records, bound.admission_key, bound.run_id);
    if (!Number.isInteger(start) || start < 0) throw new Error('repair episode missing');
    let slot = 0;
    let reservation = null;
    let completion = null;
    let episodeMax = null;
    let originalResponded = false;
    let verification = false;
    for (const record of records.slice(start + 1)) {
      if (record.admission_key !== bound.admission_key) continue;
      if (record.stage === 'verification_reserved') verification = true;
      if (record.stage === 'request_finished') originalResponded = record.disposition === 'response_received';
      if (!['repair_reserved', 'repair_finished'].includes(record.stage)) continue;
      if (record.run_id !== bound.run_id || record.revision !== bound.revision) {
        throw new Error('repair budget identity changed');
      }
      if (episodeMax === null) episodeMax = record.max_repairs;
      if (record.max_repairs !== episodeMax || record.max_repairs !== bound.max_repairs) {
        throw new Error('repair budget limit changed');
      }
      if (record.stage === 'repair_reserved') {
        if ((reservation && !completion) || record.slot !== slot + 1 || record.slot > bound.max_repairs
            || typeof record.request_sha256 !== 'string' || !/^[a-f0-9]{64}$/.test(record.request_sha256)
            || typeof record.token !== 'string' || !/^[a-f0-9]{32}$/.test(record.token)) {
          throw new Error('unresolved repair budget');
        }
        slot = record.slot;
        reservation = record;
        completion = null;
        continue;
      }
      if (!reservation || completion || record.slot !== slot || record.token !== reservation.token
          || record.request_sha256 !== reservation.request_sha256
          || !validCompletion(record.disposition, record.retry_after)
          || !Number.isFinite(Date.parse(record.at))) {
        throw new Error('invalid repair completion');
      }
      completion = record;
    }
    return { slot, reservation, completion, originalResponded, verification };
  }

  async function reserveRepair(options) {
    const bound = boundedRepairIdentity(options);
    const token = randomBytes(16).toString('hex');
    const result = await store.append((records) => {
      const state = replay(records, bound);
      if (state.verification) throw new Error('repair forbidden during paid verification');
      if (!state.originalResponded) throw new Error('repair requires a received original response');
      if (state.reservation && !state.completion) throw new Error('repair budget held by unfinished slot');
      if (state.slot >= bound.max_repairs) throw new Error('repair budget exhausted');
      const slot = state.slot + 1;
      return {
        append: [{ stage: 'repair_reserved', ...bound, slot, token }],
        value: { slot, max_repairs: bound.max_repairs, request_sha256: bound.request_sha256, token },
      };
    });
    return result.value;
  }

  async function finishRepair(options) {
    const bound = boundedRepairIdentity(options);
    if (!validCompletion(options.disposition, options.retryAfterSeconds)) {
      throw new Error('invalid repair disposition');
    }
    await store.append((records) => {
      const state = replay(records, bound);
      if (!state.reservation || state.completion || options.slot !== state.slot
          || options.token !== state.reservation.token
          || bound.request_sha256 !== state.reservation.request_sha256) {
        throw new Error('repair reservation not owned');
      }
      return [{
        stage: 'repair_finished',
        ...bound,
        slot: state.slot,
        token: state.reservation.token,
        disposition: options.disposition,
        retry_after: options.retryAfterSeconds,
      }];
    });
    return { recorded: true };
  }

  return { reserveRepair, finishRepair };
}

module.exports = { MAX_REPAIRS_CAP, createRepairBudget };
