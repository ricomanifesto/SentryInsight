const assert = require('node:assert/strict');
const childProcess = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');

const { canonicalJson, inventoryDigest, inventoryOfDir, inventoryText, parseInventory } = require('../kit/canonical');
const { loadSiteConfig } = require('../kit/config');
const { LAYOUT, buildDescriptor, releaseKeyOf } = require('../kit/release');
const { buildArtifactTree } = require('../kit/artifact');
const { proveServing } = require('../kit/proof');
const { PAYLOAD, fakeOrigin, sha256, siteConfig, tempDir, writeFiles } = require('./helpers');

const ADAPTER = path.join(__dirname, '..', 'adapter', 'build.js');
const RELEASE_REF = 'a'.repeat(40);
const PRODUCTION_ENV = {
  VERCEL_ENV: 'production',
  VERCEL_GIT_COMMIT_REF: 'vercel-production',
  VERCEL_GIT_COMMIT_SHA: RELEASE_REF,
  VERCEL_GIT_REPO_OWNER: 'ricomanifesto',
  VERCEL_GIT_REPO_SLUG: 'SentryDigest',
  VERCEL_PROJECT_PRODUCTION_URL: 'sentrydigest.ricomanifesto.com',
};

function payloadEntries(t, files = PAYLOAD) {
  const dir = tempDir(t, 'payload-');
  writeFiles(dir, files);
  return { dir, entries: inventoryOfDir(dir) };
}

function descriptorFor(t, overrides = {}) {
  const { dir, entries } = payloadEntries(t);
  const config = loadSiteConfig(siteConfig());
  const built = buildDescriptor({
    config,
    kind: 'release',
    sourceRevision: 'b'.repeat(40),
    sourceCommittedAt: '2026-11-02T00:00:00Z',
    publicationMode: { mode: 'prepare', proof: 'on' },
    payloadEntries: entries,
    contentIdentity: { newest_issue_date: '2026-01-02' },
    ...overrides,
  });
  return { config, payloadDir: dir, entries, ...built };
}

function runAdapter(treeDir, env = PRODUCTION_ENV) {
  return childProcess.spawnSync(process.execPath, [path.join(treeDir, ...LAYOUT.adapter.split('/'))], {
    cwd: treeDir,
    env: { PATH: process.env.PATH, ...env },
    encoding: 'utf8',
  });
}

function materializeTree(t, files) {
  const dir = tempDir(t, 'artifact-tree-');
  for (const [relativePath, bytes] of files) {
    const target = path.join(dir, ...relativePath.split('/'));
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, bytes);
  }
  return dir;
}

test('canonical inventory lines are sorted bytewise with two spaces and regular files only', (t) => {
  const { dir, entries } = payloadEntries(t);
  const text = inventoryText(entries);
  assert.equal(text.split('\n').filter(Boolean).length, Object.keys(PAYLOAD).length);
  assert.match(text, /^[0-9a-f]{64} {2}LICENSE\n/);
  assert.deepEqual(parseInventory(text), entries.map(({ path: p, sha256: s }) => ({ path: p, sha256: s })));
  assert.equal(inventoryDigest(entries), sha256(text));
  fs.symlinkSync('index.html', path.join(dir, 'linked.html'));
  assert.throws(() => inventoryOfDir(dir), /linked\.html is a symlink/);
  assert.throws(() => parseInventory(`${'0'.repeat(64)}  b\n${'0'.repeat(64)}  a\n`), /sorted/);
  assert.throws(() => parseInventory(`${'0'.repeat(64)} a\n`), /malformed/);
  assert.equal(canonicalJson({ b: 1, a: { d: [2, 1], c: null } }), '{\n  "a": {\n    "c": null,\n    "d": [\n      2,\n      1\n    ]\n  },\n  "b": 1\n}\n');
});

test('site configuration rejects malformed, preview and local origins and illegal publication states', () => {
  assert.equal(loadSiteConfig(siteConfig()).site, 'SentryDigest');
  const withOrigin = (production) => siteConfig({
    origins: { ...siteConfig().origins, SentryDigest: { ...siteConfig().origins.SentryDigest, production } },
  });
  for (const origin of [
    'http://sentrydigest.ricomanifesto.com/',
    'https://sentrydigest.ricomanifesto.com/SentryDigest/',
    'https://sentrydigest.ricomanifesto.com',
    'https://localhost/',
    'https://127.0.0.1/',
    'https://sentrydigest-abc123.vercel.app/',
    'https://ricomanifesto.github.io/',
    'https://user:pass@sentrydigest.ricomanifesto.com/',
    'https://sentrydigest.ricomanifesto.com:8443/',
    'https://sentrydigest.ricomanifesto.com/?preview=1',
  ]) {
    assert.throws(() => loadSiteConfig(withOrigin(origin)), /production origin/, origin);
  }
  for (const publication of [
    { mode: 'active', proof: 'off' },
    { mode: 'disabled', proof: 'on' },
    { mode: 'live', proof: 'on' },
    { mode: 'prepare', proof: 'maybe' },
  ]) {
    assert.throws(() => loadSiteConfig(siteConfig({ publication })), /publication state/, JSON.stringify(publication));
  }
  assert.throws(
    () => loadSiteConfig(siteConfig({ origins: { ...siteConfig().origins, SentryDigest: { ...siteConfig().origins.SentryDigest, legacy: 'https://example.github.io/SentryDigest/' } } })),
    /legacy origin/,
  );
  assert.throws(() => loadSiteConfig(siteConfig({ artifact_branch: 'main' })), /artifact branch/);
});

test('descriptor is deterministic, carries no wall-clock or provider values, and keys the release', (t) => {
  const first = descriptorFor(t);
  const second = descriptorFor(t);
  assert.equal(first.bytes.toString(), second.bytes.toString());
  assert.equal(first.releaseKey, second.releaseKey);
  const descriptor = JSON.parse(first.bytes);
  assert.deepEqual(Object.keys(descriptor).sort(), [
    'content_identity', 'descriptor_path', 'expected_origin', 'expected_repository', 'kind',
    'payload_byte_total', 'payload_digest', 'payload_file_count', 'publication_mode', 'release_key',
    'schema_version', 'site', 'source_committed_at', 'source_revision',
  ]);
  assert.equal(descriptor.payload_digest, inventoryDigest(first.entries));
  assert.equal(descriptor.expected_origin, 'https://sentrydigest.ricomanifesto.com/');
  assert.equal(descriptor.descriptor_path, LAYOUT.descriptor);
  assert.equal(
    first.releaseKey,
    releaseKeyOf({ site: 'SentryDigest', kind: 'release', sourceRevision: 'b'.repeat(40), payloadDigest: descriptor.payload_digest, rollbackOf: '' }),
  );
  const rollback = descriptorFor(t, { kind: 'rollback', rollbackOf: first.releaseKey, reason: 'alias-regressed' });
  assert.notEqual(rollback.releaseKey, first.releaseKey);
  assert.equal(JSON.parse(rollback.bytes).rollback_of, first.releaseKey);
  assert.throws(() => descriptorFor(t, { kind: 'rollback' }), /rollback_of/);
});

test('artifact tree holds payload, descriptor, adapter and provider configuration only', (t) => {
  const built = descriptorFor(t);
  const tree = buildArtifactTree({ payloadDir: built.payloadDir, descriptorBytes: built.bytes });
  const paths = [...tree.files.keys()].sort();
  assert.ok(paths.includes(LAYOUT.descriptor));
  assert.ok(paths.includes(LAYOUT.adapter));
  assert.ok(paths.includes(LAYOUT.providerConfig));
  assert.deepEqual(paths.filter((p) => p.startsWith(LAYOUT.payloadPrefix)).map((p) => p.slice(LAYOUT.payloadPrefix.length)).sort(), Object.keys(PAYLOAD).sort());
  assert.equal(paths.length, Object.keys(PAYLOAD).length + 3);
  assert.equal(tree.treeDigest, inventoryDigest([...tree.files].map(([p, b]) => ({ path: p, sha256: sha256(b) }))));
  assert.deepEqual(JSON.parse(tree.files.get(LAYOUT.providerConfig)), { buildCommand: `node ${LAYOUT.adapter}`, framework: null });
});

test('the adapter emits payload, descriptor, receipt and listing with production routing', (t) => {
  const built = descriptorFor(t);
  const tree = buildArtifactTree({ payloadDir: built.payloadDir, descriptorBytes: built.bytes });
  const treeDir = materializeTree(t, tree.files);
  const run = runAdapter(treeDir);
  assert.equal(run.status, 0, run.stderr);

  const output = path.join(treeDir, '.vercel', 'output');
  const emitted = inventoryOfDir(path.join(output, 'static')).map((entry) => entry.path).sort();
  assert.deepEqual(emitted, [...Object.keys(PAYLOAD), LAYOUT.descriptor, LAYOUT.receipt, LAYOUT.listing].sort());
  assert.ok(!emitted.includes(LAYOUT.adapter) && !emitted.includes(LAYOUT.providerConfig));

  const listing = parseInventory(fs.readFileSync(path.join(output, 'static', ...LAYOUT.listing.split('/')), 'utf8'));
  assert.deepEqual(listing.map((entry) => entry.path), emitted.filter((p) => p !== LAYOUT.listing));
  const receipt = JSON.parse(fs.readFileSync(path.join(output, 'static', ...LAYOUT.receipt.split('/')), 'utf8'));
  assert.deepEqual(receipt, {
    environment: 'production',
    git_commit_sha: RELEASE_REF,
    git_ref: 'vercel-production',
    production_host: 'sentrydigest.ricomanifesto.com',
    release_key: built.releaseKey,
    repository: 'ricomanifesto/SentryDigest',
    schema_version: 1,
  });
  const config = JSON.parse(fs.readFileSync(path.join(output, 'config.json'), 'utf8'));
  assert.equal(config.version, 3);
  assert.deepEqual(config.routes[0].headers, { 'Cache-Control': 'public, max-age=0, must-revalidate', 'X-Content-Type-Options': 'nosniff' });
  assert.ok(config.routes.some((route) => route.src === '^/archive$' && route.status === 308));
  assert.equal(config.overrides['feed.xml'].contentType, 'application/xml; charset=utf-8');
  assert.equal(config.overrides.LICENSE.contentType, 'text/plain; charset=utf-8');
  assert.equal(JSON.stringify(config).includes('noindex'), false);
});

test('the adapter fails closed on environment, ref, repository, host, proof and tree tampering', (t) => {
  const built = descriptorFor(t);
  const tree = buildArtifactTree({ payloadDir: built.payloadDir, descriptorBytes: built.bytes });
  const cases = [
    ['preview environment', { ...PRODUCTION_ENV, VERCEL_ENV: 'preview' }, /environment/],
    ['missing environment', { ...PRODUCTION_ENV, VERCEL_ENV: undefined }, /VERCEL_ENV/],
    ['other ref', { ...PRODUCTION_ENV, VERCEL_GIT_COMMIT_REF: 'main' }, /ref/],
    ['other repository', { ...PRODUCTION_ENV, VERCEL_GIT_REPO_SLUG: 'GRCInsight' }, /repository/],
    ['malformed commit', { ...PRODUCTION_ENV, VERCEL_GIT_COMMIT_SHA: 'abc' }, /commit/],
    ['other production host', { ...PRODUCTION_ENV, VERCEL_PROJECT_PRODUCTION_URL: 'sentrydigest-x.vercel.app' }, /production host/],
  ];
  for (const [name, env, expected] of cases) {
    const treeDir = materializeTree(t, tree.files);
    const run = runAdapter(treeDir, Object.fromEntries(Object.entries(env).filter(([, v]) => v !== undefined)));
    assert.notEqual(run.status, 0, name);
    assert.match(run.stderr, expected, name);
    assert.equal(fs.existsSync(path.join(treeDir, '.vercel', 'output')), false, name);
  }

  const deferred = materializeTree(t, tree.files);
  const env = { ...PRODUCTION_ENV };
  delete env.VERCEL_PROJECT_PRODUCTION_URL;
  assert.equal(runAdapter(deferred, env).status, 0);
  const receipt = JSON.parse(fs.readFileSync(path.join(deferred, '.vercel', 'output', 'static', ...LAYOUT.receipt.split('/')), 'utf8'));
  assert.equal(receipt.production_host, 'deferred');

  const tamper = [
    ['tampered payload', (dir) => fs.appendFileSync(path.join(dir, 'site', 'index.html'), 'x'), /payload/],
    ['extra payload file', (dir) => fs.writeFileSync(path.join(dir, 'site', 'extra.html'), 'x'), /payload/],
    ['missing payload file', (dir) => fs.rmSync(path.join(dir, 'site', 'LICENSE')), /payload/],
    ['extra tree file', (dir) => fs.writeFileSync(path.join(dir, 'notes.txt'), 'x'), /unexpected/],
    ['symlink', (dir) => fs.symlinkSync('index.html', path.join(dir, 'site', 'link.html')), /symlink/],
  ];
  for (const [name, change, expected] of tamper) {
    const treeDir = materializeTree(t, tree.files);
    change(treeDir);
    const run = runAdapter(treeDir);
    assert.notEqual(run.status, 0, name);
    assert.match(run.stderr, expected, name);
  }

  const preBoundary = descriptorFor(t, { publicationMode: { mode: 'prepare', proof: 'off' } });
  const preTree = materializeTree(t, buildArtifactTree({ payloadDir: preBoundary.payloadDir, descriptorBytes: preBoundary.bytes }).files);
  const refused = runAdapter(preTree);
  assert.notEqual(refused.status, 0);
  assert.match(refused.stderr, /proof is off/);
});

test('serving proof accepts the exact release and rejects every binding mismatch', async (t) => {
  const built = descriptorFor(t);
  const tree = buildArtifactTree({ payloadDir: built.payloadDir, descriptorBytes: built.bytes });
  const release = {
    releaseKey: built.releaseKey,
    releaseRef: RELEASE_REF,
    descriptorBytes: built.bytes,
    payloadEntries: built.entries,
  };
  const prove = (fetchUrl, overrides = {}) => proveServing({
    config: built.config,
    release: { ...release, ...overrides },
    fetchUrl,
    attempts: 1,
    sleep: async () => {},
  });

  const treeDir = materializeTree(t, tree.files);
  assert.equal(runAdapter(treeDir).status, 0);
  const origin = fakeOrigin(path.join(treeDir, '.vercel', 'output'));
  const proved = await prove(origin.fetchUrl);
  assert.equal(proved.ok, true, JSON.stringify(proved.failures));
  assert.equal(proved.listing_digest, sha256(fs.readFileSync(path.join(treeDir, '.vercel', 'output', 'static', ...LAYOUT.listing.split('/')))));
  assert.equal(proved.served_file_count, Object.keys(PAYLOAD).length + 3);
  assert.match(proved.served_digest, /^[0-9a-f]{64}$/);
  assert.ok(proved.samples.every((sample) => sample.ok));
  assert.deepEqual(proved.absent.map((entry) => entry.status), [404, 404]);

  assert.equal((await prove(origin.fetchUrl, { releaseRef: 'c'.repeat(40) })).ok, false);
  assert.equal((await prove(origin.fetchUrl, { releaseKey: 'd'.repeat(64) })).ok, false);

  const variants = [
    ['wrong repository', { ...PRODUCTION_ENV, VERCEL_GIT_REPO_SLUG: 'SentryDigest' }, (dir) => {
      const receiptPath = path.join(dir, '.vercel', 'output', 'static', ...LAYOUT.receipt.split('/'));
      const receipt = JSON.parse(fs.readFileSync(receiptPath));
      receipt.repository = 'someone/SentryDigest';
      fs.writeFileSync(receiptPath, `${JSON.stringify(receipt)}\n`);
    }, /receipt/],
    ['extra listed file', PRODUCTION_ENV, (dir) => {
      const staticDir = path.join(dir, '.vercel', 'output', 'static');
      fs.writeFileSync(path.join(staticDir, 'extra.txt'), 'x');
      const listingPath = path.join(staticDir, ...LAYOUT.listing.split('/'));
      const entries = [...parseInventory(fs.readFileSync(listingPath, 'utf8')), { path: 'extra.txt', sha256: sha256('x') }];
      fs.writeFileSync(listingPath, inventoryText(entries));
    }, /unexpected served file extra\.txt/],
    ['missing receipt line', PRODUCTION_ENV, (dir) => {
      const listingPath = path.join(dir, '.vercel', 'output', 'static', ...LAYOUT.listing.split('/'));
      const entries = parseInventory(fs.readFileSync(listingPath, 'utf8')).filter((entry) => entry.path !== LAYOUT.receipt);
      fs.writeFileSync(listingPath, inventoryText(entries));
    }, /no build receipt/],
    ['tampered sample', PRODUCTION_ENV, (dir) => fs.appendFileSync(path.join(dir, '.vercel', 'output', 'static', 'feed.xml'), 'x'), /feed\.xml/],
    ['adapter served', PRODUCTION_ENV, (dir) => {
      const target = path.join(dir, '.vercel', 'output', 'static', ...LAYOUT.adapter.split('/'));
      fs.mkdirSync(path.dirname(target), { recursive: true });
      fs.writeFileSync(target, 'x');
    }, /must not be served/],
  ];
  for (const [name, env, change, expected] of variants) {
    const dir = materializeTree(t, tree.files);
    assert.equal(runAdapter(dir, env).status, 0, name);
    change(dir);
    const result = await prove(fakeOrigin(path.join(dir, '.vercel', 'output')).fetchUrl);
    assert.equal(result.ok, false, name);
    assert.match(result.failures.join('\n'), expected, name);
  }

  const unavailable = await prove(async () => { throw new Error('ECONNREFUSED'); });
  assert.equal(unavailable.ok, false);
  assert.match(unavailable.failures.join('\n'), /ECONNREFUSED/);
});
