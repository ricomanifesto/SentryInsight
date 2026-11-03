// Release identity and the public release descriptor.
//
// release_key = SHA-256 of the canonical JSON array
//   [site, kind, source_revision, payload_digest, rollback_of or ""]
// The descriptor is deterministic and carries no wall-clock, provider, project
// or local values, and nothing that depends on its own bytes.
const { canonicalJson, inventoryDigest, sha256 } = require('./canonical');
const { emittedOrigin } = require('./config');

// Paths inside the artifact commit and the served output.
const LAYOUT = Object.freeze({
  payloadPrefix: 'site/',
  descriptor: '_release/descriptor.json',
  receipt: '_release/build-receipt.json',
  listing: '_release/served-inventory.txt',
  adapter: '_publication/build.js',
  providerConfig: 'vercel.json',
});

const SHA1 = /^[0-9a-f]{40}$/;
const SHA256 = /^[0-9a-f]{64}$/;

function releaseKeyOf({ site, kind, sourceRevision, payloadDigest, rollbackOf = '' }) {
  return sha256(JSON.stringify([site, kind, sourceRevision, payloadDigest, rollbackOf || '']));
}

function buildDescriptor({
  config,
  kind,
  sourceRevision,
  sourceCommittedAt,
  publicationMode,
  payloadEntries,
  contentIdentity,
  rollbackOf = '',
  reason = '',
}) {
  if (!['release', 'rollback'].includes(kind)) throw new Error(`release kind ${kind} is not release or rollback`);
  if (kind === 'rollback' && !SHA256.test(rollbackOf)) throw new Error('a rollback needs rollback_of naming the target release key');
  if (kind === 'release' && (rollbackOf || reason)) throw new Error('only a rollback carries rollback_of and reason');
  if (!SHA1.test(sourceRevision)) throw new Error('source revision must be a full commit id');
  if (payloadEntries.length === 0) throw new Error('payload is empty');
  if (payloadEntries.some((entry) => entry.path.startsWith('_release/') || entry.path.startsWith('_publication/'))) {
    throw new Error('payload must not use the reserved release paths');
  }
  const payloadDigest = inventoryDigest(payloadEntries);
  const releaseKey = releaseKeyOf({ site: config.site, kind, sourceRevision, payloadDigest, rollbackOf });
  const descriptor = {
    schema_version: 1,
    site: config.site,
    release_key: releaseKey,
    kind,
    rollback_of: kind === 'rollback' ? rollbackOf : undefined,
    reason: kind === 'rollback' ? reason : undefined,
    source_revision: sourceRevision,
    source_committed_at: sourceCommittedAt,
    publication_mode: { mode: publicationMode.mode, proof: publicationMode.proof },
    payload_digest: payloadDigest,
    payload_file_count: payloadEntries.length,
    payload_byte_total: payloadEntries.reduce((total, entry) => total + entry.bytes, 0),
    content_identity: contentIdentity,
    expected_origin: config.origins[config.site].production,
    expected_repository: config.repository,
    descriptor_path: LAYOUT.descriptor,
  };
  return { descriptor, bytes: Buffer.from(canonicalJson(descriptor)), releaseKey, payloadDigest };
}

function parseDescriptor(bytes) {
  const descriptor = JSON.parse(Buffer.isBuffer(bytes) ? bytes.toString('utf8') : bytes);
  if (descriptor.schema_version !== 1 || !SHA256.test(descriptor.release_key) || !SHA1.test(descriptor.source_revision)) {
    throw new Error('release descriptor is malformed');
  }
  return descriptor;
}

module.exports = { LAYOUT, SHA1, SHA256, buildDescriptor, emittedOrigin, parseDescriptor, releaseKeyOf };
