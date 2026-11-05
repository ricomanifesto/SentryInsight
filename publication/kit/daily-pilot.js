// Internal UTC gate. No activation date or opening liability is inferred.
const { canonicalJson } = require('./canonical');
const { ProductionSpendPolicy } = require('./production-spend');
const MONTHLY_MICROUSD = 20000000, GENERATION_MICROUSD = 7251456;
function requireValue(value) { if (!value) throw new Error('Spend daily admission unavailable'); }
function exact(value, names) { requireValue(value && Object.keys(value).sort().join(',') === [...names].sort().join(',')); }
function integer(n) { return Number.isSafeInteger(n) && n >= 0; }
class DailyPilot {
  #config;
  constructor(config = null) {
    if (config === null) { this.#config = null; return; }
    exact(config, ['month', 'activationStart', 'opening']);
    requireValue(typeof config.month === 'string' && /^20[0-9]{2}-(?:0[1-9]|1[0-2])$/.test(config.month));
    requireValue(typeof config.activationStart === 'string' && Number.isFinite(Date.parse(config.activationStart))
      && new Date(config.activationStart).toISOString() === config.activationStart);
    if (config.opening !== null) {
      exact(config.opening, ['amountMicrousd', 'basisSha256']);
      requireValue(integer(config.opening.amountMicrousd) && /^[a-f0-9]{64}$/.test(config.opening.basisSha256));
    }
    this.#config = JSON.parse(JSON.stringify(config));
  }
  policy(revision) {
    if (!this.#config || !this.#config.opening) return new ProductionSpendPolicy();
    const start = `${this.#config.month}-01T00:00:00.000Z`;
    const date = new Date(start); date.setUTCMonth(date.getUTCMonth() + 1);
    return new ProductionSpendPolicy({ version: 1, enabled: true, id: 'sentry-calendar-pilot-v1', revision,
      periodStart: start, periodEnd: date.toISOString(), expiresAt: date.toISOString(),
      generationMicrousd: GENERATION_MICROUSD, periodMicrousd: MONTHLY_MICROUSD,
      model: 'moonshotai/kimi-k3.1-pro', provider: 'moonshotai/mxfp4',
      operations: [{ id: 'report', maxOutputTokens: 32000, maxAttempts: 3 }] });
  }
  prepare({ records, bound, policy, generationToken, now }) {
    requireValue(this.#config && this.#config.opening && now.getTime() >= Date.parse(this.#config.activationStart));
    requireValue(now.toISOString().slice(0, 7) === this.#config.month);
    requireValue(canonicalJson(policy) === canonicalJson(this.policy(bound.revision).value));
    const opening = { stage: 'pilot_opening', periodStart: policy.periodStart, periodEnd: policy.periodEnd,
      amountMicrousd: this.#config.opening.amountMicrousd, basisSha256: this.#config.opening.basisSha256 };
    const day = now.toISOString().slice(0, 10); let priorOpening = null;
    for (const row of records.filter((r) => typeof r.stage === 'string' && r.stage.startsWith('pilot_'))) {
      if (row.stage === 'pilot_opening') {
        exact(row, [...Object.keys(opening), 'at']);
        requireValue(integer(row.amountMicrousd) && /^[a-f0-9]{64}$/.test(row.basisSha256));
        if (row.periodStart === policy.periodStart) {
          requireValue(!priorOpening); const { at, ...value } = row;
          requireValue(canonicalJson(value) === canonicalJson(opening)); priorOpening = row;
        }
      } else {
        requireValue(row.stage === 'pilot_daily');
        exact(row, ['stage', 'day', 'admissionKey', 'runId', 'revision', 'sourceSha256', 'generationToken', 'at']);
        requireValue(typeof row.day === 'string' && /^20[0-9]{2}-[0-9]{2}-[0-9]{2}$/.test(row.day));
        requireValue(row.day !== day);
      }
    }
    return { openingMicrousd: opening.amountMicrousd, append: [
      ...(priorOpening ? [] : [opening]),
      { stage: 'pilot_daily', day, ...bound, generationToken },
    ].map((row) => { const value = { ...row }; delete value.runAttempt; return value; }) };
  }
}
module.exports = { DailyPilot, MONTHLY_MICROUSD, GENERATION_MICROUSD };
