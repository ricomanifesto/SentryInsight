const SITE = 'SentryInsight', MODEL = 'moonshotai/kimi-k3.1-pro', PROVIDER = 'moonshotai/mxfp4';
const PROVIDER_LABEL = 'Moonshot AI', IDS = ['report'], OUTPUT_MAX = 32000, ATTEMPTS = 3;
const ATTEMPT_FACTORY = require('./request-budget').createRequestBudget;
// Internal, unwired spending primitive. Constructor policy is trusted job data,
// never HTTP/model/workflow input. The store is public operational metadata.
const { randomBytes } = require('node:crypto');
const { canonicalJson } = require('./canonical');
const CONTEXT = 1048576; // Provider context contract assumption, not billing proof.
const P = new Set(['spend_reserved', 'spend_sending', 'spend_finished', 'spend_settled']);
const BINDING = ['admissionKey', 'runId', 'runAttempt', 'revision', 'sourceSha256'];
class SpendError extends Error {
  constructor(code = 'refused') { super('Spend unavailable or held'); this.code = code; }
}
function need(value) { if (!value) throw new SpendError(); }
function keys(value, expected) {
  need(value !== null && typeof value === 'object' && !Array.isArray(value)
    && Object.keys(value).sort().join(',') === [...expected].sort().join(','));
}
function integer(n, min = 0) { need(Number.isSafeInteger(n) && n >= min); return n; }
function sum(a, b) { return integer(a + b); }
function product(a, b) { return integer(a * b); }
function matches(s, regex) { return typeof s === 'string' && regex.test(s); }
function utc(s) { need(typeof s === 'string' && Number.isFinite(Date.parse(s)) && new Date(s).toISOString() === s); return Date.parse(s); }
function copy(value) { return JSON.parse(JSON.stringify(value)); }
function freeze(value) { if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); } return value; }
function usdToMicrousd(value) {
  need(typeof value === 'string' && /^(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$/.test(value) && value.length <= 40);
  const [whole, fraction = ''] = value.split('.');
  const units = BigInt(whole) * 1000000n + BigInt((fraction + '000000').slice(0, 6))
    + (/[1-9]/.test(fraction.slice(6)) ? 1n : 0n);
  need(units <= BigInt(Number.MAX_SAFE_INTEGER)); return Number(units);
}
class ProductionSpendPolicy {
  constructor(raw) {
    if (raw === undefined) raw = { version: 1, enabled: false };
    need(raw && raw.version === 1 && typeof raw.enabled === 'boolean');
    if (!raw.enabled) { keys(raw, ['version', 'enabled']); this.value = freeze(copy(raw)); Object.freeze(this); return; }
    keys(raw, ['version', 'enabled', 'id', 'revision', 'periodStart', 'periodEnd', 'expiresAt',
      'generationMicrousd', 'periodMicrousd', 'model', 'provider', 'operations']);
    need(matches(raw.id, /^[a-z0-9-]{1,64}$/) && matches(raw.revision, /^[a-f0-9]{40}$/));
    const start = utc(raw.periodStart), end = utc(raw.periodEnd), expiry = utc(raw.expiresAt);
    need(start < expiry && expiry <= end);
    integer(raw.generationMicrousd, 1); integer(raw.periodMicrousd, 1);
    need(raw.generationMicrousd <= raw.periodMicrousd && raw.model === MODEL && raw.provider === PROVIDER);
    need(Array.isArray(raw.operations) && raw.operations.length === IDS.length);
    raw.operations.forEach((op, i) => {
      keys(op, ['id', 'maxOutputTokens', 'maxAttempts']);
      integer(op.maxOutputTokens, 1); integer(op.maxAttempts, 1);
      need(op.id === IDS[i] && op.maxOutputTokens <= OUTPUT_MAX && op.maxAttempts <= ATTEMPTS);
    });
    this.value = freeze(copy(raw)); Object.freeze(this);
  }
}
function binding(value) {
  keys(value, BINDING);
  need(matches(value.admissionKey, /^(?:run:[0-9]+|digest:[a-f0-9]{40})$/)
    && matches(value.runId, /^[0-9]{1,20}$/) && value.runAttempt === '1'
    && matches(value.revision, /^[a-f0-9]{40}$/) && matches(value.sourceSha256, /^[a-f0-9]{64}$/));
  return copy(value);
}
function financialTerms(policy) {
  return canonicalJson(Object.fromEntries(Object.entries(policy).filter(([name]) => name !== 'revision')));
}
function reserveAmount(policy) {
  return policy.operations.reduce((total, op) => sum(total, product(sum(product(CONTEXT, 2), product(op.maxOutputTokens, 10)), op.maxAttempts)), 0);
}
function checkedReceipt(value, op) {
  if (value === null) return { receipt: null, complete: false };
  keys(value, ['model', 'provider', 'serviceTier', 'promptTokens', 'completionTokens', 'reasoningTokens', 'totalTokens', 'costMicrousd', 'costCoverage']);
  need(['complete', 'unknown'].includes(value.costCoverage));
  need(value.model === null || value.model === MODEL);
  need(value.provider === null || value.provider === PROVIDER_LABEL);
  need(value.serviceTier === null || value.serviceTier === 'default');
  for (const name of ['promptTokens', 'completionTokens', 'reasoningTokens', 'totalTokens', 'costMicrousd']) {
    if (value[name] !== null) integer(value[name]);
  }
  if (value.promptTokens !== null) need(value.promptTokens <= CONTEXT);
  if (value.completionTokens !== null) need(value.completionTokens <= op.maxOutputTokens);
  if (value.completionTokens !== null && value.reasoningTokens !== null) need(value.reasoningTokens <= value.completionTokens);
  if (value.promptTokens !== null && value.completionTokens !== null) {
    if (value.totalTokens !== null) need(value.totalTokens === sum(value.promptTokens, value.completionTokens));
    if (value.costMicrousd !== null) need(value.costMicrousd <= sum(product(value.promptTokens, 2), product(value.completionTokens, 10)));
  }
  if (value.costMicrousd !== null) need(value.costMicrousd <= sum(product(CONTEXT, 2), product(op.maxOutputTokens, 10)));
  const complete = value.costCoverage === 'complete' && ['model', 'promptTokens', 'completionTokens', 'reasoningTokens', 'totalTokens', 'costMicrousd'].every((name) => value[name] !== null);
  return { receipt: copy(value), complete };
}
function physicalCeiling(g, op) { return Math.min(op.maxAttempts, g.physicalLimit ?? op.maxAttempts); }
function terminal(g) {
  for (const op of g.policy.operations) {
    const sends = g.sends.filter((s) => s.operation === op.id);
    const last = sends.at(-1);
    if (!last || !last.finished || !last.finished.complete || last.finished.outcome === 'uncertain') return null;
    if (last.finished.outcome === 'rejected' || (last.finished.outcome === 'retryable' && sends.length === physicalCeiling(g, op))) return 'refused';
    if (last.finished.outcome !== 'accepted') return null;
  }
  return 'completed';
}
function replay(records) {
  const generations = new Map();
  for (const row of records) {
    if (typeof row.stage !== 'string' || !row.stage.startsWith('spend_')) continue;
    need(P.has(row.stage)); utc(row.at);
    if (row.stage === 'spend_reserved') {
      const oneShot = Object.hasOwn(row, 'physicalLimit');
      keys(row, ['stage', 'at', 'binding', 'policy', 'generationToken', 'amountMicrousd', ...(oneShot ? ['physicalLimit'] : [])]);
      need(!oneShot || row.physicalLimit === 1);
      const bound = binding(row.binding), policy = new ProductionSpendPolicy(row.policy).value;
      need(policy.enabled && bound.revision === policy.revision && matches(row.generationToken, /^[a-f0-9]{32}$/));
      need(![...generations.values()].some((g) => g.binding.admissionKey === bound.admissionKey));
      need(!generations.has(row.generationToken) && row.amountMicrousd === reserveAmount(policy));
      generations.set(row.generationToken, { binding: bound, policy, amount: row.amountMicrousd, sends: [], settled: null, physicalLimit: oneShot ? 1 : null });
      continue;
    }
    const g = generations.get(row.generationToken); need(g && !g.settled);
    if (row.stage === 'spend_sending') {
      keys(row, ['stage', 'at', 'generationToken', 'operation', 'attempt', 'token', 'requestSha256']);
      need(matches(row.token, /^[a-f0-9]{32}$/) && matches(row.requestSha256, /^[a-f0-9]{64}$/));
      need(![...generations.values()].some((v) => v.sends.some((s) => s.token === row.token)));
      const index = g.policy.operations.findIndex((op) => op.id === row.operation); need(index >= 0);
      for (const previous of g.policy.operations.slice(0, index)) need(g.sends.filter((s) => s.operation === previous.id).at(-1)?.finished?.outcome === 'accepted');
      const op = g.policy.operations[index], sends = g.sends.filter((s) => s.operation === op.id), last = sends.at(-1);
      need(!terminal(g) && row.attempt === sends.length + 1 && row.attempt <= physicalCeiling(g, op));
      if (last) need(last.finished?.complete && last.finished.outcome === 'retryable' && last.requestSha256 === row.requestSha256);
      g.sends.push({ ...row, finished: null });
    } else if (row.stage === 'spend_finished') {
      keys(row, ['stage', 'at', 'generationToken', 'token', 'outcome', 'receipt']);
      const s = g.sends.find((v) => v.token === row.token); need(s && !s.finished);
      const op = g.policy.operations.find((v) => v.id === s.operation);
      const checked = checkedReceipt(row.receipt, op);
      need(['accepted', 'rejected', 'retryable', 'uncertain'].includes(row.outcome));
      need(checked.complete || row.outcome === 'uncertain');
      s.finished = { ...checked, outcome: row.outcome };
    } else {
      keys(row, ['stage', 'at', 'generationToken', 'outcome', 'actualMicrousd', 'releasedMicrousd']);
      need(terminal(g) === row.outcome);
      const actual = g.sends.reduce((total, s) => sum(total, s.finished.receipt.costMicrousd), 0);
      need(row.actualMicrousd === actual && row.releasedMicrousd === g.amount - actual);
      g.settled = row;
    }
  }
  return generations;
}
class ProductionSpendBudget {
  #store; #owner; #policy; #now; #owned = new Set(); #blocked = false; #attempts; #daily;
  constructor({ store, requireOwner, policy, dailyGate, now = () => new Date() }) {
    this.#store = store; this.#owner = requireOwner; this.#now = now; this.#daily = dailyGate;
    this.#policy = (policy instanceof ProductionSpendPolicy ? policy : new ProductionSpendPolicy(policy)).value;
    this.#attempts = ATTEMPT_FACTORY ? ATTEMPT_FACTORY({ store, requireOwner, now }) : null;
  }
  #active() {
    need(this.#policy.enabled);
    const time = this.#now().getTime(); need(Number.isFinite(time) && time >= utc(this.#policy.periodStart) && time < utc(this.#policy.expiresAt));
  }
  #generation(records, handle) {
    keys(handle, [...BINDING, 'generationToken']);
    need(this.#owned.has(handle.generationToken));
    const g = replay(records).get(handle.generationToken);
    need(g && !g.settled && canonicalJson(g.binding) === canonicalJson(Object.fromEntries(BINDING.map((k) => [k, handle[k]])))
      && canonicalJson(g.policy) === canonicalJson(this.#policy));
    this.#owner(records, handle.admissionKey, handle.runId); return g;
  }
  async #append(decide) {
    need(!this.#blocked);
    let expected, produced = false;
    try {
      const result = await this.#store.append((records) => {
        try {
          const decision = decide(records); expected = decision.value; produced = true; return decision;
        } catch (error) { if (error instanceof SpendError) throw error; throw new SpendError(); }
      });
      if (!produced || !expected || typeof expected !== 'object' || Array.isArray(expected)
          || !result || !Object.hasOwn(result, 'value') || !result.value
          || typeof result.value !== 'object' || Array.isArray(result.value)
          || Object.keys(result.value).sort().join(',') !== Object.keys(expected).sort().join(',')
          || canonicalJson(result.value) !== canonicalJson(expected)) throw new Error('Invalid append acknowledgement');
      return result.value;
    } catch (error) {
      if (error instanceof SpendError && !produced) throw error;
      this.#blocked = true; throw new SpendError('persistence_unknown');
    }
  }
  reserveGeneration(input) { return this.#reserve(input, null); }
  reserveOneShotGeneration(input) { return this.#reserve(input, 1); }
  async #reserve(input, physicalLimit) {
    this.#active(); const bound = binding(input); need(bound.revision === this.#policy.revision);
    const generationToken = randomBytes(16).toString('hex'), amount = reserveAmount(this.#policy);
    const result = await this.#append((records) => {
      this.#active(); this.#owner(records, bound.admissionKey, bound.runId);
      need(this.#daily || !records.some((r) => typeof r.stage === 'string' && r.stage.startsWith('pilot_')));
      const daily = this.#daily ? this.#daily.prepare({ records, bound, policy: this.#policy, generationToken, now: this.#now() }) : { append: [], openingMicrousd: 0 };
      const previous = [...replay(records).values()];
      need(!previous.some((g) => g.binding.admissionKey === bound.admissionKey));
      if (this.#attempts) need(!records.some((r) => r.stage === 'request_reserved' && r.admission_key === bound.admissionKey));
      let used = integer(daily.openingMicrousd);
      for (const g of previous) {
        const same = g.policy.periodStart === this.#policy.periodStart && g.policy.periodEnd === this.#policy.periodEnd;
        if (!same) {
          need(g.settled && utc(g.policy.periodEnd) <= utc(this.#policy.periodStart));
        } else {
          need(financialTerms(g.policy) === financialTerms(this.#policy));
          used = sum(used, g.settled ? g.settled.actualMicrousd : g.amount);
        }
      }
      need(amount <= this.#policy.generationMicrousd && sum(used, amount) <= this.#policy.periodMicrousd);
      return { append: [...daily.append, { stage: 'spend_reserved', binding: bound, policy: this.#policy, generationToken, amountMicrousd: amount, ...(physicalLimit === 1 ? { physicalLimit: 1 } : {}) }], value: freeze({ ...bound, generationToken }) };
    });
    this.#owned.add(generationToken); return result;
  }
  async beginSend(handle, input) {
    this.#active(); keys(input, ['operation', 'requestSha256']); need(matches(input.requestSha256, /^[a-f0-9]{64}$/));
    const token = randomBytes(16).toString('hex');
    return this.#append((records) => {
      this.#active(); const g = this.#generation(records, handle), op = g.policy.operations.find((v) => v.id === input.operation); need(op);
      const sends = g.sends.filter((s) => s.operation === op.id), attempt = sends.length + 1;
      const row = { stage: 'spend_sending', generationToken: handle.generationToken, operation: op.id, attempt, token, requestSha256: input.requestSha256 };
      const attemptRecords = this.#attempts ? this.#attempts.reserveDecision(records, { admissionKey: handle.admissionKey, runId: handle.runId, revision: handle.revision, requestSha256: input.requestSha256, limit: physicalCeiling(g, op) }, token).append : [];
      replay([...records, { ...row, at: this.#now().toISOString() }]);
      return { append: [...attemptRecords, row], value: freeze({ generationToken: handle.generationToken, token }) };
    });
  }
  async finishSend(handle, physical, input) {
    keys(input, ['outcome', 'receipt']); keys(physical, ['generationToken', 'token']); need(physical.generationToken === handle.generationToken);
    need(['accepted', 'rejected', 'retryable', 'uncertain'].includes(input.outcome));
    return this.#append((records) => {
      const g = this.#generation(records, handle), s = g.sends.find((v) => v.token === physical.token); need(s && !s.finished);
      const op = g.policy.operations.find((v) => v.id === s.operation), checked = checkedReceipt(input.receipt, op);
      const outcome = checked.complete ? input.outcome : 'uncertain';
      const row = { stage: 'spend_finished', generationToken: handle.generationToken, token: s.token, outcome, receipt: checked.receipt };
      const dispositions = { accepted: 'response_received', rejected: 'permanent_rejection', retryable: 'retryable_rejection', uncertain: 'uncertain' };
      const attemptRecords = this.#attempts ? this.#attempts.finishDecision(records, { admissionKey: handle.admissionKey, runId: handle.runId, revision: handle.revision, requestSha256: s.requestSha256, limit: physicalCeiling(g, op), attempt: s.attempt, token: s.token, disposition: dispositions[outcome], retryAfterSeconds: 0 }).append : [];
      replay([...records, { ...row, at: this.#now().toISOString() }]);
      return { append: [...attemptRecords, row], value: { recorded: true, outcome } };
    });
  }
  async settleGeneration(handle, input) {
    keys(input, ['outcome']); need(['completed', 'refused'].includes(input.outcome));
    return this.#append((records) => {
      const g = this.#generation(records, handle); need(terminal(g) === input.outcome);
      const actual = g.sends.reduce((total, s) => sum(total, s.finished.receipt.costMicrousd), 0);
      const row = { stage: 'spend_settled', generationToken: handle.generationToken, outcome: input.outcome, actualMicrousd: actual, releasedMicrousd: g.amount - actual };
      return { append: [row], value: { recorded: true, actualMicrousd: actual, releasedMicrousd: row.releasedMicrousd } };
    });
  }
}
module.exports = { ProductionSpendPolicy, ProductionSpendBudget, usdToMicrousd, SITE, MODEL, PROVIDER };
