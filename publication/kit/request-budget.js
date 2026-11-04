// Every send belongs to an actual admitted episode in the existing CAS store.
// A reservation without acknowledged completion prevents subsequent sends.
const { randomBytes } = require('node:crypto');

const FINISH_STATES = new Set([
  'not_sent', 'retryable_rejection', 'response_received', 'permanent_rejection',
  'uncertain', 'deferred_rejection',
]);
const RETRY_STATES = new Set(['not_sent', 'retryable_rejection']);

function boundedIdentity(options) {
  const fields = [
    ['admission_key', options.admissionKey, /^(?:run:[0-9]+|digest:[a-f0-9]{40})$/],
    ['run_id', options.runId, /^[0-9]{1,20}$/],
    ['revision', options.revision, /^[a-f0-9]{40}$/],
    ['request_sha256', options.requestSha256, /^[a-f0-9]{64}$/],
  ];
  const bound = {};
  for (const [name, value, format] of fields) {
    if (typeof value !== 'string' || !format.test(value)) throw new Error('invalid request budget identity');
    bound[name] = value;
  }
  if (!Number.isInteger(options.limit) || options.limit < 1 || options.limit > 3) throw new Error('invalid request budget identity');
  return { ...bound, limit: options.limit };
}

function validCompletion(disposition, delay) {
  return FINISH_STATES.has(disposition) && Number.isFinite(delay) && delay >= 0 && delay <= 30;
}

function createRequestBudget({ store, requireOwner, now = () => new Date() }) {
  function replay(records, bound) {
    // The admission owner supplies the actual admitted-record boundary. An
    // invoked marker or a restarted caller is never a new request episode.
    const start = requireOwner(records, bound.admission_key, bound.run_id);
    if (!Number.isInteger(start) || start < 0) throw new Error('request episode missing');
    let attempt = 0;
    let reservation = null;
    let completion = null;
    for (const record of records.slice(start + 1)) {
      if (record.admission_key !== bound.admission_key
          || !['request_reserved', 'request_finished'].includes(record.stage)) continue;
      for (const name of Object.keys(bound)) {
        if (record[name] !== bound[name]) throw new Error('request budget identity changed');
      }
      if (record.stage === 'request_reserved') {
        const previousAllowsRetry = !reservation || (completion && RETRY_STATES.has(completion.disposition));
        if (!previousAllowsRetry || record.attempt !== attempt + 1 || record.attempt > bound.limit
            || typeof record.token !== 'string' || !/^[a-f0-9]{32}$/.test(record.token)) {
          throw new Error('unresolved request budget');
        }
        attempt = record.attempt;
        reservation = record;
        completion = null;
        continue;
      }
      if (!reservation || completion || record.attempt !== attempt || record.token !== reservation.token
          || !validCompletion(record.disposition, record.retry_after)
          || !Number.isFinite(Date.parse(record.at))) throw new Error('invalid request completion');
      completion = record;
    }
    return { attempt, reservation, completion };
  }

  async function reserveRequest(options) {
    const bound = boundedIdentity(options);
    const token = randomBytes(16).toString('hex');
    const result = await store.append((records) => {
      const state = replay(records, bound);
      if (state.attempt >= bound.limit || (state.reservation
          && (!state.completion || !RETRY_STATES.has(state.completion.disposition)))) {
        throw new Error('request budget held or exhausted');
      }
      if (state.completion) {
        const availableAt = Date.parse(state.completion.at) + state.completion.retry_after * 1000;
        if (now().getTime() < availableAt) throw new Error('request retry delay not elapsed');
      }
      const attempt = state.attempt + 1;
      return {
        append: [{ stage: 'request_reserved', ...bound, attempt, token }],
        value: { attempt, limit: bound.limit, request_sha256: bound.request_sha256, token },
      };
    });
    return result.value;
  }

  async function finishRequest(options) {
    const bound = boundedIdentity(options);
    if (!validCompletion(options.disposition, options.retryAfterSeconds)) throw new Error('invalid request disposition');
    await store.append((records) => {
      const state = replay(records, bound);
      if (!state.reservation || state.completion || options.attempt !== state.attempt
          || options.token !== state.reservation.token) throw new Error('request reservation not owned');
      return [{
        stage: 'request_finished', ...bound, attempt: state.attempt,
        token: state.reservation.token, disposition: options.disposition,
        retry_after: options.retryAfterSeconds,
      }];
    });
    return { recorded: true };
  }

  return { reserveRequest, finishRequest };
}

module.exports = { createRequestBudget };
