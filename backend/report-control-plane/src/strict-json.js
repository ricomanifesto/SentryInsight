// A strict JSON reader: the grammar of RFC 8259, plus refusal of duplicate
// object keys, which JSON.parse would silently resolve to the last value.

export class JsonRefused extends Error {}

const STRING = /"(?:[^"\\\u0000-\u001f]|\\(?:["\\/bfnrt]|u[0-9a-fA-F]{4}))*"/y;
const NUMBER = /-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/y;
const SPACE = /[ \t\n\r]*/y;
const MAX_DEPTH = 32;
// An unpaired UTF-16 surrogate, which an escape such as \ud800 can produce:
// such a string has no UTF-8 encoding, so hashing it would silently rewrite it.
const LONE_SURROGATE = /[\ud800-\udbff](?![\udc00-\udfff])|(?<![\ud800-\udbff])[\udc00-\udfff]/;

export function parseStrictJson(text) {
  let at = 0;

  function skip() {
    SPACE.lastIndex = at;
    SPACE.exec(text);
    at = SPACE.lastIndex;
  }

  function token(pattern) {
    pattern.lastIndex = at;
    const match = pattern.exec(text);
    if (match === null) throw new JsonRefused("malformed");
    at = pattern.lastIndex;
    const value = JSON.parse(match[0]);
    if (typeof value === "string" && LONE_SURROGATE.test(value)) throw new JsonRefused("lone surrogate");
    return value;
  }

  function value(depth) {
    if (depth > MAX_DEPTH) throw new JsonRefused("too deep");
    skip();
    const c = text[at];
    if (c === "{") {
      at += 1;
      const object = Object.create(null);
      const seen = new Set();
      skip();
      if (text[at] === "}") {
        at += 1;
        return { ...object };
      }
      for (;;) {
        skip();
        const key = token(STRING);
        if (seen.has(key)) throw new JsonRefused("duplicate key");
        seen.add(key);
        skip();
        if (text[at] !== ":") throw new JsonRefused("malformed");
        at += 1;
        object[key] = value(depth + 1);
        skip();
        if (text[at] === ",") {
          at += 1;
          continue;
        }
        if (text[at] === "}") {
          at += 1;
          return { ...object };
        }
        throw new JsonRefused("malformed");
      }
    }
    if (c === "[") {
      at += 1;
      const list = [];
      skip();
      if (text[at] === "]") {
        at += 1;
        return list;
      }
      for (;;) {
        list.push(value(depth + 1));
        skip();
        if (text[at] === ",") {
          at += 1;
          continue;
        }
        if (text[at] === "]") {
          at += 1;
          return list;
        }
        throw new JsonRefused("malformed");
      }
    }
    if (c === '"') return token(STRING);
    for (const [literal, result] of [["true", true], ["false", false], ["null", null]]) {
      if (text.startsWith(literal, at)) {
        at += literal.length;
        return result;
      }
    }
    return token(NUMBER);
  }

  const result = value(0);
  skip();
  if (at !== text.length) throw new JsonRefused("trailing data");
  return result;
}

// Decode UTF-8 strictly, then parse; any failure is a refusal.
export function decodeStrictJson(bytes) {
  let text;
  try {
    // ignoreBOM keeps a leading byte order mark in the text so it is refused.
    text = new TextDecoder("utf-8", { fatal: true, ignoreBOM: true }).decode(bytes);
  } catch {
    throw new JsonRefused("not utf-8");
  }
  if (text.charCodeAt(0) === 0xfeff) throw new JsonRefused("byte order mark");
  return parseStrictJson(text);
}
