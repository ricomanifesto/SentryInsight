// Exponential send backoff with ±20 % jitter.
export function backoff(settings, attempt) {
  const base = settings.SEND_BACKOFF_BASE_MS * 2 ** Math.max(0, attempt - 1);
  return Math.round(base * (0.8 + 0.4 * Math.random()));
}
