const assert = require('node:assert/strict');
const childProcess = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');

const { inventoryDigest, inventoryOfDir } = require('../kit/canonical');
const { CLOSED_PATHS, parseApproval, verifyApprovedPayload } = require('../kit/defensive');
const { createWorld } = require('./world');

const OFF = { mode: 'prepare', proof: 'off' };
const ON = { mode: 'prepare', proof: 'on' };
const FACTS = 'f'.repeat(64);
const CLI = path.join(__dirname, '..', 'cli.js');

// Inert control: the world's own payload is its closed path inventory.
const closedFor = new Map();

async function approvalFor(world, source) {
  const { payloadDir } = await world.buildPayload({ sourceRevision: source });
  const entries = inventoryOfDir(payloadDir);
  closedFor.set(source, entries.map((entry) => entry.path));
  return parseApproval({ head: source, factsSha256: FACTS, packageSha256: inventoryDigest(entries) });
}

const defensive = (world, approval, overrides = {}) => world.publisher({
  defensive: true, approval, approvedPaths: closedFor.get(approval?.head) || [], ...overrides,
});
const closed = (source) => closedFor.get(source);

test('an approved package publishes the exact approved payload digest', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  const approval = await approvalFor(world, source);
  const result = await defensive(world, approval).publish({ sourceRevision: source });
  assert.equal(result.outcome, 'released');
  const descriptor = world.readDescriptor(world.remoteTip('vercel-production'));
  assert.equal(descriptor.payload_digest, approval.packageSha256);
  assert.equal(descriptor.source_revision, approval.head);
});

for (const [name, change] of [
  ['package digest', (approval) => ({ ...approval, packageSha256: '0'.repeat(64) })],
  ['head', (approval) => ({ ...approval, head: 'a'.repeat(40) })],
]) test(`a ${name} mismatch refuses before any state record or ref write`, async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  const approval = parseApproval(change(await approvalFor(world, source)));
  await assert.rejects(defensive(world, approval).publish({ sourceRevision: source }), /mismatch/);
  assert.equal(world.remoteTip('vercel-production'), null);
  assert.equal(world.remoteTip('publication-state'), null);
});

test('defensive mode without an approval refuses', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  await assert.rejects(defensive(world, null).publish({ sourceRevision: source }), /needs an approval/);
  assert.equal(world.remoteTip('vercel-production'), null);
});

test('payload bytes tampered after the build fail verification', async (t) => {
  const world = createWorld(t);
  const source = world.commitSource(world.payload, OFF);
  const approval = await approvalFor(world, source);
  const { payloadDir } = await world.buildPayload({ sourceRevision: source });
  const check = () => verifyApprovedPayload(approval, { sourceRevision: source, payloadDir, closedPaths: closed(source) });
  assert.equal(check(), approval.packageSha256);
  fs.appendFileSync(path.join(payloadDir, 'index.html'), '<!-- tampered -->');
  assert.throws(check, /digest mismatch/);
  fs.writeFileSync(path.join(payloadDir, 'extra.html'), 'x');
  assert.throws(check, /inventory is not closed/);
});

for (const name of ['bad\nname.html', 'ctl\u0001.html', 'back\\slash.html']) {
  test(`an unsafe path name refuses before any byte is digested: ${JSON.stringify(name)}`, async (t) => {
    const world = createWorld(t);
    const source = world.commitSource(world.payload, OFF);
    const approval = await approvalFor(world, source);
    const { payloadDir } = await world.buildPayload({ sourceRevision: source });
    fs.writeFileSync(path.join(payloadDir, name), 'x');
    assert.throws(() => verifyApprovedPayload(approval, { sourceRevision: source, payloadDir, closedPaths: [...closed(source), name] }), /path is unsafe/);
  });
}

test('the production closed inventory is the packager closed inventory', () => {
  assert.ok(CLOSED_PATHS.includes('index.md') && CLOSED_PATHS.includes('reports/index.json'));
  assert.ok(!CLOSED_PATHS.some((relative) => /^reports\/\d{4}-\d{2}-\d{2}\./.test(relative)));
});

test('a direct publisher refuses when the checkout HEAD is not the approved head', async (t) => {
  const world = createWorld(t);
  const approvedSource = world.commitSource(world.payload, OFF);
  const approval = await approvalFor(world, approvedSource);
  world.commitSource({ 'index.html': '<!doctype html><title>Later</title>\n' }, OFF, 'later');
  await assert.rejects(defensive(world, approval).publish({ sourceRevision: approvedSource }), /checkout mismatch/);
  assert.equal(world.remoteTip('vercel-production'), null);
  assert.equal(world.remoteTip('publication-state'), null);
});

test('legacy resume and rollback are held before extraction or ref writes', async (t) => {
  const world = createWorld(t);
  const legacy = world.commitSource(world.payload, OFF);
  await world.publisher().publish({ sourceRevision: legacy });
  const prior = world.remoteTip('vercel-production');
  const recordsBefore = await world.records();
  const approval = await approvalFor(world, legacy);
  const publisher = defensive(world, approval);
  await assert.rejects(publisher.resume(), /held by the defensive publication gate/);
  await assert.rejects(publisher.rollback({ targetReleaseKey: 'a'.repeat(64), reason: 'x' }), /held by the defensive publication gate/);
  assert.equal(world.remoteTip('vercel-production'), prior);
  assert.deepEqual(await world.records(), recordsBefore);
});

test('an unproved legacy tip holds the promotion and preserves the prior pointer', async (t) => {
  const world = createWorld(t);
  const legacy = world.commitSource(world.payload, ON);
  const first = await world.publisher().publish({ sourceRevision: legacy });
  assert.equal(first.outcome, 'verification-failed');
  const prior = world.remoteTip('vercel-production');
  const next = world.commitSource({ 'index.html': '<!doctype html><title>N</title>\n' }, ON, 'next');
  const approval = await approvalFor(world, next);
  const held = await defensive(world, approval).publish({ sourceRevision: next });
  assert.equal(held.outcome, 'held');
  assert.equal(world.remoteTip('vercel-production'), prior);
  // No implicit resume: the legacy tip was not re-proved by the promotion.
  const proofs = (await world.records()).filter((r) => r.release_ref === prior && r.stage === 'verification-failed');
  assert.equal(proofs.length, 1);
});

for (const argv of [
  ['resume'],
  ['rollback', '--target', 'a'.repeat(64), '--reason', 'x'],
  ['publish', '--source', 'a'.repeat(40)],
  ['publish', '--source', 'a'.repeat(40), '--approved-head', 'b'.repeat(40),
    '--approved-facts-sha256', FACTS, '--approved-package-sha256', FACTS],
]) test(`the CLI refuses before configuration, Git or network: ${argv.slice(0, 3).join(' ')}`, () => {
  const run = childProcess.spawnSync(process.execPath, [CLI, ...argv], {
    encoding: 'utf8', env: { PATH: process.env.PATH }, timeout: 20000,
  });
  assert.equal(run.status, 1);
  assert.match(run.stderr, /held by the defensive publication gate|approval is missing or malformed|approval head mismatch/);
});
