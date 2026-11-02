// Stable identities and the artifact path rules. Every derivation hashes a
// fixed ASCII string whose parts are validated tokens, so no JSON
// canonicalization is involved.

import { sha256Hex } from "./util.js";

export const HEX64 = /^[0-9a-f]{64}$/;
export const TOKEN = /^[a-z0-9][a-z0-9._-]{0,63}$/;
export const SOURCE_REVISION = /^[A-Za-z0-9][A-Za-z0-9._:@+/-]{0,199}$/;
export const ID_TOKEN = /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/;
export const REASON = /^[a-z0-9_]{1,64}$/;

const SEGMENT = /^[A-Za-z0-9._-]+$/;
export const PATH_LIMIT = 200;

export function operationId(pipeline, policyId, fingerprint) {
  return sha256Hex(`report-control-plane/1\n${pipeline}\n${policyId}\n${fingerprint}`);
}

export function publicationId(target, artifactSha256) {
  return sha256Hex(`report-control-plane/publication/1\n${target}\n${artifactSha256}`);
}

// A relative ASCII path of safe segments, or null.
export function pathSegments(path) {
  if (typeof path !== "string" || path.length === 0 || path.length > PATH_LIMIT) return null;
  const segments = path.split("/");
  for (const segment of segments) {
    if (!SEGMENT.test(segment) || segment === "." || segment === "..") return null;
  }
  return segments;
}

// The execution side orders files by path segments, not by whole-string bytes;
// the two differ for a nested file beside a sibling ("a/b" before "a-c").
export function comparePaths(a, b) {
  const left = a.split("/");
  const right = b.split("/");
  for (let i = 0; i < Math.min(left.length, right.length); i += 1) {
    if (left[i] !== right[i]) return left[i] < right[i] ? -1 : 1;
  }
  return left.length - right.length;
}

// Digest of path, NUL, hex digest and newline over the canonical order.
export function artifactDigest(files) {
  return sha256Hex(files.map((f) => `${f.path}\0${f.sha256}\n`).join(""));
}
