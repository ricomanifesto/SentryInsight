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
  for (const name of ["EXECUTION_URL", "PUBLISHER_URL"]) {
    const raw = env[name];
    let url;
    try {
      url = new URL(raw);
    } catch {
      throw new ConfigInvalid(name);
    }
    if (!["http:", "https:"].includes(url.protocol) || url.search || url.hash) throw new ConfigInvalid(name);
    out[name] = url.href.replace(/\/$/, "");
  }
  for (const name of ["EXECUTION_TOKEN", "PUBLISHER_TOKEN"]) {
    const raw = env[name];
    if (typeof raw !== "string" || raw.length < 16 || raw.length > 512 || /\s/.test(raw)) {
      throw new ConfigInvalid(name);
    }
    out[name] = raw;
  }
  // A claim must outlive the call it protects, so a caller that is still
  // waiting never sees its claim taken over.
  out.claimMs = out.CALL_TIMEOUT_MS + out.CLAIM_MARGIN_MS;
  return out;
}
