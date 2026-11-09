// Binding names, fixed limits and the bounded settings read from variables.

export const BINDINGS = Object.freeze({
  db: "PRODUCT_DB",
  artifacts: "ARTIFACTS",
  queue: "ADMISSIONS",
});
// The default queue names; ADMISSIONS_QUEUE_NAME and DEAD_LETTER_QUEUE_NAME
// replace them. queueNames is the only place the effective names are decided.
export const QUEUES = Object.freeze({ admissions: "report-admissions", dead: "report-admissions-dead" });
const QUEUE_VARIABLES = Object.freeze({ admissions: "ADMISSIONS_QUEUE_NAME", dead: "DEAD_LETTER_QUEUE_NAME" });
// 1 to 63 lowercase letters, digits and hyphens, starting and ending with a
// letter or digit: a deliberately narrow subset of the platform's rule, so a
// padded, upper-case or punctuated name is refused rather than compared.
const QUEUE_NAME = /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/;

export const SCHEMAS = Object.freeze({
  admission: "report-control-plane/admission/1",
  bundle: "report-control-plane/source-bundle/1",
  receipt: "execution-receipt/1",
  manifest: "report-control-plane/artifact-manifest/1",
  export: "sentryinsight-export/1",
  exportPage: "sentryinsight-export-page/1",
  exportSource: "sentryinsight-export-source/1",
  projection: "report-control-plane/projection/1",
  observation: "report-control-plane/publication-observation/1",
});

export const LIMITS = Object.freeze({
  bodyBytes: 1024 * 1024,
  articles: 100,
  keyChars: 2048,
  titleChars: 512,
  sourceChars: 256,
  contentBytes: 64 * 1024,
  recordBytes: 64 * 1024,
  receiptBytes: 256 * 1024,
  artifactFiles: 64,
  artifactFileBytes: 4 * 1024 * 1024,
  artifactTotalBytes: 8 * 1024 * 1024,
  maxSendAttempts: 3,
  maxRetryRounds: 3,
  sweepBatch: 20,
});

// A projection records a run the producer already completed, so its snapshot
// carries the producer's full article text: larger records, the same count.
export const PROJECTION_LIMITS = Object.freeze({
  ...LIMITS,
  bodyBytes: 8 * 1024 * 1024,
  contentBytes: 256 * 1024,
  recordBytes: 320 * 1024,
  blobBytes: 8 * 1024 * 1024,
  projectionBytes: 64 * 1024,
});

const DEFAULTS = Object.freeze({
  CALL_TIMEOUT_MS: 10_000,
  CLAIM_MARGIN_MS: 5_000,
  SEND_BACKOFF_BASE_MS: 5_000,
  ENQUEUED_STALE_MS: 120_000,
  PUBLICATION_CLAIM_MS: 30_000,
  QUEUE_RETRY_DELAY_S: 5,
});

const BOUNDS = Object.freeze({
  CALL_TIMEOUT_MS: [100, 60_000],
  CLAIM_MARGIN_MS: [0, 60_000],
  SEND_BACKOFF_BASE_MS: [10, 600_000],
  ENQUEUED_STALE_MS: [100, 3_600_000],
  PUBLICATION_CLAIM_MS: [100, 600_000],
  QUEUE_RETRY_DELAY_S: [0, 3_600],
});

export class ConfigInvalid extends Error {}

// The effective admission and dead-letter queue names, each defaulting when
// its variable is absent. A malformed name, or two equal names, is refused.
export function queueNames(env) {
  const names = {};
  for (const [role, variable] of Object.entries(QUEUE_VARIABLES)) {
    const value = env[variable] === undefined ? QUEUES[role] : env[variable];
    if (typeof value !== "string" || !QUEUE_NAME.test(value)) throw new ConfigInvalid("queue_names");
    names[role] = value;
  }
  if (names.admissions === names.dead) throw new ConfigInvalid("queue_names");
  return Object.freeze(names);
}

export function settings(env) {
  // Every entry point reads settings before acting, so invalid queue names
  // refuse HTTP, Queue and Cron work alike before any write or send.
  const out = { queues: queueNames(env) };
  for (const [name, fallback] of Object.entries(DEFAULTS)) {
    const raw = env[name];
    const value = raw === undefined ? fallback : Number(raw);
    const [low, high] = BOUNDS[name];
    if (!Number.isInteger(value) || value < low || value > high) throw new ConfigInvalid(name);
    out[name] = value;
  }
  // The execution service and the publisher are each optional as a pair. With
  // neither variable set, that dependency is unconfigured: the routes and
  // sweeps that need it refuse or skip, and everything else serves. One
  // variable without the other, or a malformed value, is invalid.
  for (const [urlName, tokenName, flag] of [
    ["EXECUTION_URL", "EXECUTION_TOKEN", "executionConfigured"],
    ["PUBLISHER_URL", "PUBLISHER_TOKEN", "publisherConfigured"],
  ]) {
    const [rawUrl, rawToken] = [env[urlName], env[tokenName]];
    if (rawUrl === undefined && rawToken === undefined) {
      out[urlName] = null;
      out[tokenName] = null;
      out[flag] = false;
      continue;
    }
    let url;
    try {
      url = new URL(rawUrl);
    } catch {
      throw new ConfigInvalid(urlName);
    }
    if (!["http:", "https:"].includes(url.protocol) || url.search || url.hash) throw new ConfigInvalid(urlName);
    out[urlName] = url.href.replace(/\/$/, "");
    if (typeof rawToken !== "string" || rawToken.length < 16 || rawToken.length > 512 || /\s/.test(rawToken)) {
      throw new ConfigInvalid(tokenName);
    }
    out[tokenName] = rawToken;
    out[flag] = true;
  }
  // A claim must outlive the call it protects, so a caller that is still
  // waiting never sees its claim taken over.
  out.claimMs = out.CALL_TIMEOUT_MS + out.CLAIM_MARGIN_MS;
  return out;
}
