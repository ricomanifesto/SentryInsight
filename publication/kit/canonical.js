// Canonical inventory and JSON encodings shared by the publisher, the hosting
// adapter and the serving proof. An inventory line is
// "<sha256-hex>  <relative-posix-path>\n"; lines are sorted bytewise; only
// regular files are listed and modes are ignored. A digest is the SHA-256 of
// the listing bytes.
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const LINE = /^([0-9a-f]{64}) {2}([^\n]+)$/;

function sha256(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex');
}

function comparePaths(left, right) {
  return Buffer.compare(Buffer.from(left), Buffer.from(right));
}

function assertRelativePath(relativePath) {
  const segments = relativePath.split('/');
  if (!relativePath || relativePath.startsWith('/') || relativePath.includes('\\') || relativePath.includes('\0')
      || segments.some((segment) => segment === '' || segment === '.' || segment === '..')) {
    throw new Error(`${JSON.stringify(relativePath)} is not a safe relative path`);
  }
}

// Every regular file under root, refusing symlinks and other file types.
function inventoryOfDir(root) {
  const entries = [];
  const visit = (directory, prefix) => {
    for (const name of fs.readdirSync(directory)) {
      const absolute = path.join(directory, name);
      const relative = prefix ? `${prefix}/${name}` : name;
      const stats = fs.lstatSync(absolute);
      if (stats.isSymbolicLink()) throw new Error(`${relative} is a symlink; symlinks are refused`);
      if (stats.isDirectory()) visit(absolute, relative);
      else if (stats.isFile()) {
        const bytes = fs.readFileSync(absolute);
        entries.push({ path: relative, sha256: sha256(bytes), bytes: bytes.length });
      } else throw new Error(`${relative} is not a regular file`);
    }
  };
  visit(root, '');
  return entries.sort((left, right) => comparePaths(left.path, right.path));
}

function inventoryText(entries) {
  const sorted = [...entries].sort((left, right) => comparePaths(left.path, right.path));
  for (let index = 0; index < sorted.length; index += 1) {
    assertRelativePath(sorted[index].path);
    if (index > 0 && sorted[index - 1].path === sorted[index].path) throw new Error(`${sorted[index].path} is listed twice`);
  }
  return sorted.map((entry) => `${entry.sha256}  ${entry.path}\n`).join('');
}

function inventoryDigest(entries) {
  return sha256(inventoryText(entries));
}

function parseInventory(text) {
  const source = Buffer.isBuffer(text) ? text.toString('utf8') : text;
  if (source && !source.endsWith('\n')) throw new Error('inventory is malformed: missing final newline');
  const entries = source.split('\n').slice(0, -1).map((line, index) => {
    const match = line.match(LINE);
    if (!match) throw new Error(`inventory is malformed at line ${index + 1}`);
    assertRelativePath(match[2]);
    return { path: match[2], sha256: match[1] };
  });
  for (let index = 1; index < entries.length; index += 1) {
    if (comparePaths(entries[index - 1].path, entries[index].path) >= 0) throw new Error('inventory is not sorted bytewise or repeats a path');
  }
  return entries;
}

function sortKeys(value) {
  if (Array.isArray(value)) return value.map(sortKeys);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().filter((key) => value[key] !== undefined).map((key) => [key, sortKeys(value[key])]));
  }
  return value;
}

// Deterministic JSON: sorted keys, two-space indentation, final newline.
function canonicalJson(value) {
  return `${JSON.stringify(sortKeys(value), null, 2)}\n`;
}

module.exports = {
  assertRelativePath,
  canonicalJson,
  comparePaths,
  inventoryDigest,
  inventoryOfDir,
  inventoryText,
  parseInventory,
  sha256,
};
