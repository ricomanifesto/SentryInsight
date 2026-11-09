// Strict validation of admission requests and staged source bundles. Every
// refusal happens before any write and names a fixed reason token.

import { LIMITS, SCHEMAS } from "./config.js";
import { SOURCE_REVISION, TOKEN } from "./identity.js";
import { JsonRefused, decodeStrictJson } from "./strict-json.js";
import { sha256Hex, utf8 } from "./util.js";

// The record fields the execution side accepts; anything else is refused.
const STRING_FIELDS = new Set(["title", "link", "source", "content", "summary", "content_kind", "published_at"]);
// The producer's own publication time, RFC 3339 in UTC; anything else is refused.
const PUBLISHED_AT = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d{1,6})?Z$/;

export function validPublishedAt(value) {
  const m = PUBLISHED_AT.exec(value);
  if (m === null) return false;
  const [year, month, day, hour, minute, second] = m.slice(1).map(Number);
  const date = new Date(Date.UTC(year, month - 1, day, hour, minute, second));
  return (
    date.getUTCFullYear() === year && date.getUTCMonth() === month - 1 && date.getUTCDate() === day &&
    hour < 24 && minute < 60 && second < 60
  );
}
const LIST_FIELDS = new Set(["source_links", "cves"]);

export class RequestRefused extends Error {
  constructor(reason) {
    super(reason);
    this.reason = reason;
  }
}

// Byte length of a string as an ASCII-only JSON encoder writes it: every
// non-ASCII UTF-16 unit becomes a six-byte \uXXXX escape.
function asciiJsonLength(text) {
  let length = JSON.stringify(text).length;
  for (let i = 0; i < text.length; i += 1) if (text.charCodeAt(i) > 0x7f) length += 5;
  return length;
}

function canonicalRecordLength(record) {
  const keys = Object.keys(record).sort();
  let length = 2 + Math.max(0, keys.length - 1);
  for (const key of keys) {
    const value = record[key];
    length += asciiJsonLength(key) + 1;
    length += Array.isArray(value)
      ? 2 + Math.max(0, value.length - 1) + value.reduce((n, v) => n + asciiJsonLength(v), 0)
      : asciiJsonLength(value);
  }
  return length;
}

function validateArticle(record, limits) {
  if (record === null || typeof record !== "object" || Array.isArray(record)) {
    throw new RequestRefused("article_invalid");
  }
  for (const [key, value] of Object.entries(record)) {
    if (STRING_FIELDS.has(key)) {
      if (typeof value !== "string") throw new RequestRefused("article_invalid");
    } else if (LIST_FIELDS.has(key)) {
      if (!Array.isArray(value) || value.length > 64 || !value.every((v) => typeof v === "string" && v.length <= 2048)) {
        throw new RequestRefused("article_invalid");
      }
    } else {
      throw new RequestRefused("article_field_unknown");
    }
  }
  const { title, link, content, source } = record;
  if (record.published_at !== undefined && !validPublishedAt(record.published_at)) throw new RequestRefused("article_invalid");
  if (typeof title !== "string" || title.trim() === "" || title.length > limits.titleChars) {
    throw new RequestRefused("article_invalid");
  }
  if (typeof link !== "string" || link.length > limits.keyChars || !/^https?:\/\/[\x21-\x7e]+$/.test(link)) {
    throw new RequestRefused("article_invalid");
  }
  if (typeof content !== "string" || utf8(content).byteLength > limits.contentBytes) {
    throw new RequestRefused("article_invalid");
  }
  if (source !== undefined && source.length > limits.sourceChars) throw new RequestRefused("article_invalid");
  if (canonicalRecordLength(record) > limits.recordBytes) throw new RequestRefused("article_too_large");
  return record;
}

// The product labels a record 'feed' (the feed's own text) or 'article' (the
// fetched page). Any other label is kept as 'other'; an absent one stays null.
// The admitted bytes are unchanged either way.
const CONTENT_KINDS = new Set(["feed", "article"]);
export function contentKind(value) {
  if (value === undefined) return null;
  return CONTENT_KINDS.has(value) ? value : "other";
}

async function validateArticles(list, limits) {
  if (!Array.isArray(list) || list.length === 0 || list.length > limits.articles) {
    throw new RequestRefused("articles_invalid");
  }
  const keys = new Set();
  const articles = [];
  for (const record of list) {
    validateArticle(record, limits);
    if (keys.has(record.link)) throw new RequestRefused("article_duplicate_key");
    keys.add(record.link);
    articles.push({
      article_key: record.link,
      content_sha256: await sha256Hex(record.content),
      title: record.title,
      source: record.source ?? null,
      content_kind: contentKind(record.content_kind),
      content_bytes: utf8(record.content).byteLength,
      published_at: record.published_at ?? null,
    });
  }
  return articles;
}

function decode(bytes, limits) {
  if (bytes.byteLength === 0) throw new RequestRefused("request_malformed");
  if (bytes.byteLength > limits.bodyBytes) throw new RequestRefused("request_too_large");
  try {
    return decodeStrictJson(bytes);
  } catch (error) {
    if (error instanceof JsonRefused) throw new RequestRefused("request_malformed");
    throw error;
  }
}

function exactKeys(value, keys) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    throw new RequestRefused("request_malformed");
  }
  const present = Object.keys(value);
  if (present.some((key) => !keys.includes(key))) throw new RequestRefused("field_unknown");
  if (keys.some((key) => !(key in value))) throw new RequestRefused("field_missing");
}

// `limits` are the admission bounds; a projection passes its own, larger ones.
export async function parseAdmission(bytes, limits = LIMITS) {
  const value = decode(bytes, limits);
  exactKeys(value, ["schema", "pipeline", "policy_id", "source_revision", "articles"]);
  if (value.schema !== SCHEMAS.admission) throw new RequestRefused("schema_unsupported");
  if (typeof value.pipeline !== "string" || !TOKEN.test(value.pipeline)) throw new RequestRefused("pipeline_invalid");
  if (typeof value.policy_id !== "string" || !TOKEN.test(value.policy_id)) throw new RequestRefused("policy_invalid");
  if (typeof value.source_revision !== "string" || !SOURCE_REVISION.test(value.source_revision)) {
    throw new RequestRefused("source_revision_invalid");
  }
  if (value.source_revision.startsWith("schedule:")) throw new RequestRefused("source_revision_reserved");
  return {
    pipeline: value.pipeline,
    policyId: value.policy_id,
    sourceRevision: value.source_revision,
    articles: await validateArticles(value.articles, limits),
  };
}

export async function parseBundle(bytes) {
  const value = decode(bytes, LIMITS);
  exactKeys(value, ["schema", "articles"]);
  if (value.schema !== SCHEMAS.bundle) throw new RequestRefused("schema_unsupported");
  return { articles: await validateArticles(value.articles, LIMITS) };
}
