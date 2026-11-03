const assert = require('node:assert/strict');
const test = require('node:test');

const { inventoryDigest, inventoryOfDir } = require('../kit/canonical');
const { LAYOUT } = require('../kit/release');
const { git } = require('./helpers');
const { createWorld } = require('./world');

const OFF = { mode: 'prepare', proof: 'off' };
const ON = { mode: 'prepare', proof: 'on' };
const DISABLED = { mode: 'disabled', proof: 'off' };

function stages(records, releaseKey) {
  return records.filter((record) => record.release_key === releaseKey).map((record) => record.stage);
}

test('disabled publication validates and builds but writes no branch', async (t) => {
  const world = createWorld(t, { publication: DISABLED });
  const source = world.commitSource(world.payload, DISABLED);
  const result = await world.publisher().publish({ sourceRevision: source });

  assert.equal(result.outcome, 'disabled');
  assert.match(result.release_key, /^[0-9a-f]{64}$/);
  assert.equal(world.remoteTip('vercel-production'), null);
  assert.equal(world.remoteTip('publication-state'), null);

  world.failBuild = 'validation failed: feed.xml is not well-formed XML';
  await assert.rejects(world.publisher().publish({ sourceRevision: source }), /not well-formed XML/);
});

test('a pre-boundary release advances the branch with the exact tree and is not proved', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  const result = await world.publisher().publish({ sourceRevision: source });

  assert.equal(result.outcome, 'released');
  const tip = world.remoteTip('vercel-production');
  assert.equal(result.release_ref, tip);
  const descriptor = world.readDescriptor(tip);
  assert.equal(descriptor.source_revision, source);
  assert.deepEqual(descriptor.publication_mode, OFF);
  assert.equal(descriptor.release_key, result.release_key);

  const files = git(world.remote, 'ls-tree', '-r', '--name-only', tip).split('\n').sort();
  assert.deepEqual(files, [
    LAYOUT.adapter, LAYOUT.descriptor,
    ...Object.keys(world.payload).map((p) => `${LAYOUT.payloadPrefix}${p}`),
    LAYOUT.providerConfig,
  ].sort());
  const message = git(world.remote, 'log', '-1', '--format=%B', tip);
  assert.match(message, new RegExp(`Release-Key: ${result.release_key}`));
  assert.match(message, new RegExp(`Source-Revision: ${source}`));
  assert.match(message, /Payload-Digest: [0-9a-f]{64}/);
  assert.match(message, /Tree-Digest: [0-9a-f]{64}/);
  assert.deepEqual(stages(await world.records(), result.release_key), ['released']);
  assert.equal(world.served, null);
});

test('rebuilding the same source is a no-op that resumes, with an identical descriptor', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  const first = await world.publisher().publish({ sourceRevision: source });
  const descriptorBytes = git(world.remote, 'show', `${first.release_ref}:${LAYOUT.descriptor}`);
  const second = await world.publisher().publish({ sourceRevision: source });

  assert.equal(second.outcome, 'no-op');
  assert.equal(second.release_key, first.release_key);
  assert.equal(world.branchCommits('vercel-production').length, 1);
  assert.equal(git(world.remote, 'show', `${first.release_ref}:${LAYOUT.descriptor}`), descriptorBytes);
});

test('a crash after the push and before the state record adopts the tip without a second commit', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  world.hooks.afterArtifactPush = () => { throw new Error('crashed after push'); };
  await assert.rejects(world.publisher().publish({ sourceRevision: source }), /crashed after push/);
  const tip = world.remoteTip('vercel-production');
  assert.ok(tip);
  assert.deepEqual(await world.records(), []);

  delete world.hooks.afterArtifactPush;
  const resumed = await world.publisher().publish({ sourceRevision: source });
  assert.equal(resumed.outcome, 'no-op');
  assert.equal(world.remoteTip('vercel-production'), tip);
  const released = (await world.records()).filter((record) => record.stage === 'released');
  assert.equal(released.length, 1);
  assert.equal(released[0].release_ref, tip);
  assert.equal(released[0].recovered, true);
});

test('a crash before the push rebuilds the same release key', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  world.hooks.beforeArtifactPush = () => { throw new Error('crashed before push'); };
  await assert.rejects(world.publisher().publish({ sourceRevision: source }), /crashed before push/);
  assert.equal(world.remoteTip('vercel-production'), null);
  const records = await world.records();
  assert.ok(records.every((record) => record.stage !== 'released'));
  delete world.hooks.beforeArtifactPush;
  const first = await world.publisher().publish({ sourceRevision: source });
  assert.equal(first.outcome, 'released');
  const rebuilt = await world.publisher().publish({ sourceRevision: source });
  assert.equal(rebuilt.release_key, first.release_key);
  assert.equal(rebuilt.outcome, 'no-op');
});

test('the proof boundary freezes the tip until the boundary release is proved', async (t) => {
  const world = createWorld(t);
  const preBoundary = world.commitSource(world.payload, OFF);
  await world.publisher().publish({ sourceRevision: preBoundary });

  const boundarySource = world.commitSource({ 'index.html': '<!doctype html><title>B0</title>\n' }, ON, 'proof on');
  const boundary = await world.publisher().publish({ sourceRevision: boundarySource });
  assert.equal(boundary.outcome, 'verification-failed');
  const b0 = world.remoteTip('vercel-production');
  assert.equal(world.readDescriptor(b0).publication_mode.proof, 'on');

  const later = world.commitSource({ 'index.html': '<!doctype html><title>C</title>\n' }, ON, 'later');
  const held = await world.publisher().publish({ sourceRevision: later });
  assert.equal(held.outcome, 'held');
  assert.equal(world.remoteTip('vercel-production'), b0);

  // The operator connects; only the boundary tip is ever built.
  world.deploy(b0);
  const newest = world.commitSource({ 'index.html': '<!doctype html><title>D</title>\n' }, ON, 'newest');
  const advanced = await world.publisher().publish({ sourceRevision: newest });
  assert.equal(stages(await world.records(), boundary.release_key).at(-1), 'serving');
  assert.equal(advanced.outcome, 'verification-failed');
  assert.notEqual(world.remoteTip('vercel-production'), b0);
  assert.equal(world.readDescriptor(world.remoteTip('vercel-production')).source_revision, newest);

  world.deploy();
  const proved = await world.publisher().resume();
  assert.equal(proved.tip.outcome, 'serving');
  assert.equal(proved.tip.proof.ok, true);
  assert.match(proved.tip.proof.served_digest, /^[0-9a-f]{64}$/);
});

test('an operator failure attestation is terminal and a missing attestation stays held', async (t) => {
  const world = createWorld(t);
  const first = world.commitSource(world.payload, ON);
  const a = await world.publisher().publish({ sourceRevision: first });
  assert.equal(a.outcome, 'verification-failed');
  const second = world.commitSource({ 'index.html': 'B\n' }, ON, 'B');
  assert.equal((await world.publisher().publish({ sourceRevision: second })).outcome, 'held');

  await assert.rejects(world.publisher().resolve({ releaseKey: 'f'.repeat(64), attestation: 'x' }), /not the artifact tip/);
  await assert.rejects(world.publisher().resolve({ releaseKey: a.release_key, attestation: '' }), /attestation/);
  await world.publisher().resolve({ releaseKey: a.release_key, attestation: 'provider build failed for this commit' });
  const advanced = await world.publisher().publish({ sourceRevision: second });
  assert.equal(advanced.outcome, 'verification-failed');
  assert.equal(world.readDescriptor(world.remoteTip('vercel-production')).source_revision, second);
});

test('an older source is superseded and proof-off cannot reopen after the boundary', async (t) => {
  const world = createWorld(t);
  const older = world.commitSource(world.payload, ON);
  const newer = world.commitSource({ 'index.html': 'newer\n' }, ON, 'newer');
  await world.publisher().publish({ sourceRevision: newer });
  world.deploy();
  await world.publisher().resume();

  const stale = await world.publisher().publish({ sourceRevision: older });
  assert.equal(stale.outcome, 'superseded');
  assert.equal(world.branchCommits('vercel-production').length, 1);

  const reopened = world.commitSource({ 'index.html': 'proof off again\n' }, OFF, 'proof off');
  const refused = await world.publisher().publish({ sourceRevision: reopened });
  assert.equal(refused.outcome, 'rejected');
  assert.match(refused.reason, /proof boundary/);
  assert.equal(world.branchCommits('vercel-production').length, 1);
});

test('a failed validation or build preserves the last proved release', async (t) => {
  const world = createWorld(t);
  const good = world.commitSource(world.payload, ON);
  await world.publisher().publish({ sourceRevision: good });
  world.deploy();
  await world.publisher().resume();
  const tip = world.remoteTip('vercel-production');

  const bad = world.commitSource({ 'feed.xml': '<rss>' }, ON, 'bad');
  world.failBuild = 'feed.xml is not well-formed XML';
  const result = await world.publisher().publish({ sourceRevision: bad });
  assert.equal(result.outcome, 'rejected');
  assert.match(result.reason, /not well-formed XML/);
  assert.equal(world.remoteTip('vercel-production'), tip);
  const records = await world.records();
  assert.ok(records.some((record) => record.stage === 'rejected' && record.source_revision === bad));
});

test('rollback republishes a proved payload with truthful source and refuses pre-boundary targets', async (t) => {
  const world = createWorld(t);
  const pre = world.commitSource(world.payload, OFF);
  const preRelease = await world.publisher().publish({ sourceRevision: pre });
  const first = world.commitSource({ 'index.html': 'first\n' }, ON, 'first');
  const firstRelease = await world.publisher().publish({ sourceRevision: first });
  world.deploy();
  await world.publisher().resume();
  const second = world.commitSource({ 'index.html': 'second\n' }, ON, 'second');
  await world.publisher().publish({ sourceRevision: second });
  world.deploy();
  await world.publisher().resume();

  await assert.rejects(world.publisher().rollback({ targetReleaseKey: preRelease.release_key, reason: 'test' }), /pre-boundary/);
  const rolled = await world.publisher().rollback({ targetReleaseKey: firstRelease.release_key, reason: 'operator request' });
  const descriptor = world.readDescriptor(world.remoteTip('vercel-production'));
  assert.equal(descriptor.kind, 'rollback');
  assert.equal(descriptor.rollback_of, firstRelease.release_key);
  assert.equal(descriptor.source_revision, first);
  assert.equal(descriptor.payload_digest, world.readDescriptor(firstRelease.release_ref).payload_digest);
  assert.equal(rolled.outcome, 'verification-failed');
  world.deploy();
  assert.equal((await world.publisher().resume()).tip.outcome, 'serving');
});

async function provedRelease(world, files, message) {
  const source = world.commitSource(files, ON, message);
  const result = await world.publisher().publish({ sourceRevision: source });
  world.deploy();
  await world.publisher().resume();
  return { source, ...result };
}

test('a repeated rollback request is idempotent and writes no second commit', async (t) => {
  const world = createWorld(t);
  const a = await provedRelease(world, world.payload, 'A');
  await provedRelease(world, { 'index.html': 'B\n' }, 'B');
  const rolled = await world.publisher().rollback({ targetReleaseKey: a.release_key, reason: 'operator request' });
  world.deploy();
  assert.equal((await world.publisher().resume()).tip.outcome, 'serving');
  const tip = world.remoteTip('vercel-production');

  const repeated = await world.publisher().rollback({ targetReleaseKey: a.release_key, reason: 'operator request' });
  assert.equal(repeated.outcome, 'no-op');
  assert.equal(repeated.release_key, rolled.release_key);
  assert.equal(world.remoteTip('vercel-production'), tip);
});

test('proof belongs to the exact artifact commit, so a later rollback with the same key is proved again', async (t) => {
  const world = createWorld(t);
  const a = await provedRelease(world, world.payload, 'A');
  await provedRelease(world, { 'index.html': 'B\n' }, 'B');
  const firstRollback = await world.publisher().rollback({ targetReleaseKey: a.release_key, reason: 'operator' });
  world.deploy();
  await world.publisher().resume();
  await provedRelease(world, { 'index.html': 'C\n' }, 'C');

  // Rolling back to A again after C writes a new commit with the same
  // release key; the earlier rollback commit's proof does not carry over.
  const secondRollback = await world.publisher().rollback({ targetReleaseKey: a.release_key, reason: 'operator' });
  assert.equal(secondRollback.release_key, firstRollback.release_key);
  assert.notEqual(secondRollback.release_ref, firstRollback.release_ref);
  assert.equal(secondRollback.outcome, 'verification-failed');
  const unproved = world.remoteTip('vercel-production');
  assert.equal((await world.publisher().resume()).tip.outcome, 'verification-failed');

  const d = world.commitSource({ 'index.html': 'D\n' }, ON, 'D');
  const held = await world.publisher().publish({ sourceRevision: d });
  assert.equal(held.outcome, 'held');
  assert.equal(world.remoteTip('vercel-production'), unproved);

  world.deploy();
  assert.equal((await world.publisher().resume()).tip.outcome, 'serving');
  assert.equal((await world.publisher().publish({ sourceRevision: d })).outcome, 'verification-failed');
  assert.notEqual(world.remoteTip('vercel-production'), unproved);
});

test('rollback refuses a target that was never proved serving', async (t) => {
  const world = createWorld(t);
  const a = world.commitSource(world.payload, ON, 'A');
  const releaseA = await world.publisher().publish({ sourceRevision: a });
  await world.publisher().resolve({ releaseKey: releaseA.release_key, attestation: 'provider build failed' });
  await provedRelease(world, { 'index.html': 'B\n' }, 'B');
  const tip = world.remoteTip('vercel-production');

  await assert.rejects(
    world.publisher().rollback({ targetReleaseKey: releaseA.release_key, reason: 'operator' }),
    /never proved serving/,
  );
  assert.equal(world.remoteTip('vercel-production'), tip);
});

test('an alias that regresses to an attested failure is repaired by a rollback release', async (t) => {
  const world = createWorld(t);
  const a = world.commitSource(world.payload, ON);
  const releaseA = await world.publisher().publish({ sourceRevision: a });
  const commitA = world.remoteTip('vercel-production');
  await world.publisher().resolve({ releaseKey: releaseA.release_key, attestation: 'provider reported failure' });
  const b = world.commitSource({ 'index.html': 'B\n' }, ON, 'B');
  const releaseB = await world.publisher().publish({ sourceRevision: b });
  world.deploy();
  await world.publisher().resume();
  assert.equal(stages(await world.records(), releaseB.release_key).at(-1), 'serving');

  world.deploy(commitA);
  const repaired = await world.publisher().resume();
  assert.equal(repaired.tip.outcome, 'alias-regressed');
  const descriptor = world.readDescriptor(world.remoteTip('vercel-production'));
  assert.equal(descriptor.kind, 'rollback');
  assert.equal(descriptor.rollback_of, releaseB.release_key);
  assert.equal(descriptor.payload_digest, world.readDescriptor(releaseB.release_ref).payload_digest);
});

test('a lost compare-and-set on the artifact branch re-reads instead of overwriting', async (t) => {
  const world = createWorld(t);
  const base = world.commitSource(world.payload, OFF);
  await world.publisher().publish({ sourceRevision: base });
  const mine = world.commitSource({ 'index.html': 'mine\n' }, OFF, 'mine');
  const theirs = world.commitSource({ 'index.html': 'theirs\n' }, OFF, 'theirs');
  let raced = false;
  world.hooks.beforeArtifactPush = async () => {
    if (raced) return;
    raced = true;
    delete world.hooks.beforeArtifactPush;
    await world.publisher({ hooks: {} }).publish({ sourceRevision: theirs });
  };
  const result = await world.publisher().publish({ sourceRevision: mine });
  assert.equal(result.outcome, 'superseded');
  assert.equal(world.readDescriptor(world.remoteTip('vercel-production')).source_revision, theirs);
  assert.equal(world.branchCommits('vercel-production').length, 2);
});

test('payload digest in the descriptor equals the canonical inventory of the built payload', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  const built = await world.buildPayload({ sourceRevision: source });
  const result = await world.publisher().publish({ sourceRevision: source });
  const descriptor = world.readDescriptor(result.release_ref);
  assert.equal(descriptor.payload_digest, inventoryDigest(inventoryOfDir(built.payloadDir)));
  assert.equal(descriptor.payload_file_count, Object.keys(world.payload).length);
});
