#!/usr/bin/env node
// Hosting adapter, committed into each release on the artifact branch and run
// by the provider's build step. It fetches, renders and generates nothing: it
// verifies the accepted payload against the release descriptor, checks the
// provider's build environment, and copies the accepted bytes into the Build
// Output API v3 layout with a build receipt and a listing of every other
// served file. Any failed check exits non-zero before output is written.
//
// Served files: the payload at the site root, _release/descriptor.json,
// _release/build-receipt.json and _release/served-inventory.txt. The adapter
// and the provider configuration are never served.
'use strict';

const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const PAYLOAD_PREFIX = 'site/';
const DESCRIPTOR = '_release/descriptor.json';
const RECEIPT = '_release/build-receipt.json';
const LISTING = '_release/served-inventory.txt';
const ADAPTER = '_publication/build.js';
const PROVIDER_CONFIG = 'vercel.json';
const ARTIFACT_REF = 'vercel-production';
const PRODUCTION_HEADERS = {
  'Cache-Control': 'public, max-age=0, must-revalidate',
  'X-Content-Type-Options': 'nosniff',
};
const CONTENT_TYPES = {
  '.json': 'application/json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.webmanifest': 'application/manifest+json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
};

function fail(message) {
  process.stderr.write(`adapter refused to build: ${message}\n`);
  process.exit(1);
}

function sha256(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex');
}

function compare(left, right) {
  return Buffer.compare(Buffer.from(left), Buffer.from(right));
}

function listFiles(root) {
  const files = [];
  const visit = (directory, prefix) => {
    for (const name of fs.readdirSync(directory)) {
      const absolute = path.join(directory, name);
      const relative = prefix ? `${prefix}/${name}` : name;
      const stats = fs.lstatSync(absolute);
      if (stats.isSymbolicLink()) fail(`${relative} is a symlink`);
      if (stats.isDirectory()) visit(absolute, relative);
      else if (stats.isFile()) files.push(relative);
      else fail(`${relative} is not a regular file`);
    }
  };
  visit(root, '');
  return files.sort(compare);
}

function inventory(entries) {
  return [...entries].sort((a, b) => compare(a.path, b.path)).map((e) => `${e.sha256}  ${e.path}\n`).join('');
}

function canonicalJson(value) {
  const sort = (item) => (Array.isArray(item) ? item.map(sort)
    : item && typeof item === 'object' ? Object.fromEntries(Object.keys(item).sort().map((key) => [key, sort(item[key])])) : item);
  return `${JSON.stringify(sort(value), null, 2)}\n`;
}

function requireEnv(name) {
  const value = process.env[name];
  if (!value) fail(`${name} is not set; system environment variables must be exposed to the build`);
  return value;
}

function routesFor(paths) {
  const routes = [{ src: '^/.*$', headers: PRODUCTION_HEADERS, continue: true }];
  for (const relative of paths) {
    if (relative === 'index.html') {
      routes.push({ src: '^/$', dest: '/index.html' });
    } else if (relative.endsWith('/index.html')) {
      const directory = `/${relative.slice(0, -'/index.html'.length)}`;
      const escaped = directory.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      routes.push({ src: `^${escaped}$`, status: 308, headers: { Location: `${directory}/` } });
      routes.push({ src: `^${escaped}/$`, dest: `/${relative}` });
    }
  }
  routes.push({ handle: 'filesystem' });
  return routes;
}

function overridesFor(paths) {
  const overrides = {};
  for (const relative of paths) {
    const type = relative === 'LICENSE' || relative === '.nojekyll'
      ? 'text/plain; charset=utf-8'
      : CONTENT_TYPES[path.extname(relative)];
    if (type) overrides[relative] = { contentType: type };
  }
  return overrides;
}

function main() {
  const root = process.cwd();
  const output = path.join(root, '.vercel', 'output');
  if (fs.existsSync(output)) fail('.vercel/output already exists');

  // The artifact tree may hold only the payload, the descriptor, this adapter
  // and the provider configuration.
  const treeFiles = listFiles(root).filter((relative) => !relative.startsWith('.git/') && !relative.startsWith('.vercel/'));
  for (const relative of treeFiles) {
    if (![DESCRIPTOR, ADAPTER, PROVIDER_CONFIG].includes(relative) && !relative.startsWith(PAYLOAD_PREFIX)) {
      fail(`unexpected file ${relative} in the artifact tree`);
    }
  }
  if (!treeFiles.includes(DESCRIPTOR)) fail(`${DESCRIPTOR} is missing`);
  const descriptorBytes = fs.readFileSync(path.join(root, DESCRIPTOR));
  let descriptor;
  try {
    descriptor = JSON.parse(descriptorBytes.toString('utf8'));
  } catch {
    fail('the release descriptor is not valid JSON');
  }
  if (descriptor.schema_version !== 1 || !/^[0-9a-f]{64}$/.test(descriptor.release_key || '')) fail('the release descriptor is malformed');
  if (descriptor.publication_mode?.proof !== 'on') {
    fail('publication proof is off for this release; pre-boundary releases are never deployed');
  }

  // Payload bytes must equal the accepted payload inventory.
  const payloadPaths = treeFiles.filter((relative) => relative.startsWith(PAYLOAD_PREFIX)).map((relative) => relative.slice(PAYLOAD_PREFIX.length));
  const payloadEntries = payloadPaths.map((relative) => {
    const bytes = fs.readFileSync(path.join(root, PAYLOAD_PREFIX, ...relative.split('/')));
    return { path: relative, sha256: sha256(bytes), bytes: bytes.length };
  });
  if (payloadPaths.some((relative) => relative.startsWith('_release/') || relative.startsWith('_publication/'))) {
    fail('the payload uses a reserved release path');
  }
  if (sha256(inventory(payloadEntries)) !== descriptor.payload_digest
      || payloadEntries.length !== descriptor.payload_file_count
      || payloadEntries.reduce((total, entry) => total + entry.bytes, 0) !== descriptor.payload_byte_total) {
    fail('the payload does not match the release descriptor');
  }

  // Provider build environment: production build of the artifact branch for
  // the expected repository.
  const environment = requireEnv('VERCEL_ENV');
  if (environment !== 'production') fail(`environment ${environment} is not production`);
  const ref = requireEnv('VERCEL_GIT_COMMIT_REF');
  if (ref !== ARTIFACT_REF) fail(`ref ${ref} is not ${ARTIFACT_REF}`);
  const commit = requireEnv('VERCEL_GIT_COMMIT_SHA');
  if (!/^[0-9a-f]{40}$/.test(commit)) fail(`commit ${commit} is not a full commit id`);
  const repository = `${requireEnv('VERCEL_GIT_REPO_OWNER')}/${requireEnv('VERCEL_GIT_REPO_SLUG')}`;
  if (repository !== descriptor.expected_repository) fail(`repository ${repository} is not ${descriptor.expected_repository}`);
  const expectedHost = new URL(descriptor.expected_origin).host;
  const productionHost = process.env.VERCEL_PROJECT_PRODUCTION_URL || '';
  if (productionHost && productionHost !== expectedHost) fail(`production host ${productionHost} is not ${expectedHost}`);

  // The receipt is written first; its content does not depend on any
  // inventory. The listing then covers every other served file.
  const receipt = Buffer.from(canonicalJson({
    schema_version: 1,
    repository,
    git_ref: ref,
    git_commit_sha: commit,
    environment,
    production_host: productionHost || 'deferred',
    release_key: descriptor.release_key,
  }));
  const staticDir = path.join(output, 'static');
  const write = (relative, bytes) => {
    const target = path.join(staticDir, ...relative.split('/'));
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, bytes);
  };
  for (const relative of payloadPaths) write(relative, fs.readFileSync(path.join(root, PAYLOAD_PREFIX, ...relative.split('/'))));
  write(DESCRIPTOR, descriptorBytes);
  write(RECEIPT, receipt);
  const listed = [
    ...payloadEntries,
    { path: DESCRIPTOR, sha256: sha256(descriptorBytes) },
    { path: RECEIPT, sha256: sha256(receipt) },
  ];
  write(LISTING, inventory(listed));

  const served = [...payloadPaths, DESCRIPTOR, RECEIPT, LISTING].sort(compare);
  fs.writeFileSync(path.join(output, 'config.json'), canonicalJson({
    version: 3,
    routes: routesFor(served),
    overrides: overridesFor(served),
  }));
  process.stdout.write(`${JSON.stringify({
    release_key: descriptor.release_key,
    served_files: served.length,
    production_host: productionHost || 'deferred',
  })}\n`);
}

main();
