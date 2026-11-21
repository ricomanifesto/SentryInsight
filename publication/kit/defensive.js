// The approved defensive package gate shared by every Node publish path.
//
// Approval is the triple (exact source head, canonical committed facts
// SHA-256, complete sorted inventory SHA-256). The package is built by the
// one shared Python packager from pinned inputs only, and its inventory is
// recomputed here with the kit's own inventoryDigest before anything reads
// the artifact branch, writes a state record or pushes a ref.
const childProcess = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const { inventoryDigest, inventoryOfDir } = require('./canonical');
const { contentIdentityFor } = require('./content');

const HEX40 = /^[0-9a-f]{40}$/;
const HEX64 = /^[0-9a-f]{64}$/;
const PACKAGER = path.join('scripts', 'package_defensive.py');
// Control characters (newline included) and backslashes never name a path.
const UNSAFE_NAME = /[\u0000-\u001f\u007f\\]/;
// Exactly the paths the shared packager generates (src/core/defensive_package.py
// closed_inventory); nothing else may appear in an approved package.
const CLOSED_PATHS = Object.freeze([
  '.nojekyll',
  'assets/apple-touch-icon.png', 'assets/favicon.ico', 'assets/icon-192.png', 'assets/icon-512.png',
  'assets/icon-small.svg', 'assets/icon.svg', 'assets/logo-lockup-dark.png', 'assets/logo-lockup-light.png',
  'assets/logo.png', 'assets/logo.svg', 'assets/report.js', 'assets/site.css', 'assets/social-preview.png',
  'assets/vendor/DOMPURIFY-LICENSE.txt', 'assets/vendor/dompurify.min.js',
  'contracts/reporting-identity-v1.json',
  'current-findings.json', 'index.html', 'index.md',
  'reports/index.html', 'reports/index.json', 'sitemap.xml',
]);

// Names first, before any byte is read: safe, regular and exactly closed.
function approvedPaths(root, closedPaths = CLOSED_PATHS) {
  const found = [];
  const visit = (directory, prefix) => {
    for (const name of fs.readdirSync(directory)) {
      const relative = prefix ? `${prefix}/${name}` : name;
      if (UNSAFE_NAME.test(relative) || ['', '.', '..'].includes(name)) throw new Error('defensive package path is unsafe');
      const stats = fs.lstatSync(path.join(directory, name));
      if (stats.isSymbolicLink()) throw new Error('defensive package entry is not regular');
      if (stats.isDirectory()) visit(path.join(directory, name), relative);
      else if (stats.isFile()) found.push(relative);
      else throw new Error('defensive package entry is not regular');
    }
  };
  visit(root, '');
  const expected = new Set(closedPaths);
  if (found.length !== expected.size || found.some((relative) => !expected.has(relative))) {
    throw new Error('defensive package inventory is not closed');
  }
  return found;
}

function parseApproval({ head, factsSha256, packageSha256 } = {}) {
  if (!HEX40.test(head || '') || !HEX64.test(factsSha256 || '') || !HEX64.test(packageSha256 || '')) {
    throw new Error('defensive approval is missing or malformed');
  }
  return Object.freeze({ head, factsSha256, packageSha256 });
}

function verifyApprovedPayload(approval, { sourceRevision, payloadDir, closedPaths = CLOSED_PATHS }) {
  if (sourceRevision !== approval.head) throw new Error('defensive approval head mismatch');
  approvedPaths(payloadDir, closedPaths);
  const digest = inventoryDigest(inventoryOfDir(payloadDir));
  if (digest !== approval.packageSha256) throw new Error('defensive package digest mismatch');
  return digest;
}

function createDefensiveBuild({ repoRoot, approval, site = 'SentryInsight', python = 'python3' }) {
  const scratchDirs = [];
  const build = async ({ sourceRevision }) => {
    if (sourceRevision !== approval.head) throw new Error('defensive approval head mismatch');
    const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'defensive-package-'));
    scratchDirs.push(scratch);
    const payloadDir = path.join(scratch, 'package');
    const result = childProcess.spawnSync(python, [
      '-B', PACKAGER, 'build',
      '--source', repoRoot,
      '--revision', sourceRevision,
      '--output', payloadDir,
      '--approve-head', approval.head,
      '--approve-facts', approval.factsSha256,
      '--approve-package', approval.packageSha256,
    ], { cwd: repoRoot, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
    if (result.status !== 0) {
      let code = 'packager_failed';
      try { code = JSON.parse(result.stdout).refused || code; } catch { /* fixed code only */ }
      throw new Error(`defensive package refused: ${code}`);
    }
    verifyApprovedPayload(approval, { sourceRevision, payloadDir });
    return { payloadDir, contentIdentity: contentIdentityFor({ site, payloadDir, repoRoot }) };
  };
  build.cleanup = () => scratchDirs.forEach((dir) => fs.rmSync(dir, { recursive: true, force: true }));
  return build;
}

module.exports = { CLOSED_PATHS, approvedPaths, createDefensiveBuild, parseApproval, verifyApprovedPayload };
