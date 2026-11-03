// The artifact commit tree: the accepted payload under site/, the release
// descriptor, the hosting adapter and the provider configuration. Only the
// payload, the descriptor, and the receipt and listing the adapter writes are
// ever served.
const fs = require('node:fs');
const path = require('node:path');

const { canonicalJson, inventoryDigest, inventoryOfDir, sha256 } = require('./canonical');
const { LAYOUT } = require('./release');

const ADAPTER_SOURCE = path.join(__dirname, '..', 'adapter', 'build.js');
const PROVIDER_CONFIG = Object.freeze({ buildCommand: `node ${LAYOUT.adapter}`, framework: null });

function buildArtifactTree({ payloadDir, descriptorBytes }) {
  const files = new Map();
  for (const entry of inventoryOfDir(payloadDir)) {
    files.set(`${LAYOUT.payloadPrefix}${entry.path}`, fs.readFileSync(path.join(payloadDir, ...entry.path.split('/'))));
  }
  files.set(LAYOUT.descriptor, Buffer.from(descriptorBytes));
  files.set(LAYOUT.adapter, fs.readFileSync(ADAPTER_SOURCE));
  files.set(LAYOUT.providerConfig, Buffer.from(canonicalJson(PROVIDER_CONFIG)));
  return { files, treeDigest: treeDigestOf(files) };
}

function treeDigestOf(files) {
  return inventoryDigest([...files].map(([relativePath, bytes]) => ({ path: relativePath, sha256: sha256(bytes) })));
}

// The payload of an earlier artifact commit, written to a directory, for a
// rollback that republishes exact prior bytes without any rebuild.
function extractPayload(git, commit, targetDir) {
  const entries = git.listTree(commit).filter((entry) => entry.path.startsWith(LAYOUT.payloadPrefix));
  const blobs = git.readBlobs(entries.map((entry) => entry.oid));
  entries.forEach((entry, index) => {
    if (entry.mode !== '100644' && entry.mode !== '100755') throw new Error(`${entry.path} is not a regular file in ${commit}`);
    const target = path.join(targetDir, ...entry.path.slice(LAYOUT.payloadPrefix.length).split('/'));
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, blobs[index]);
  });
  return targetDir;
}

module.exports = { PROVIDER_CONFIG, buildArtifactTree, extractPayload, treeDigestOf };
