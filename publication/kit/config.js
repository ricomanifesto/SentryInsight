// Public site configuration: each site's legacy Pages root, confirmed
// production origin and which of the two its pages currently emit, plus this
// repository's committed publication state. Validation is strict so a
// malformed, preview or local destination can never become production.
const fs = require('node:fs');
const path = require('node:path');

const SITES = ['SentryDigest', 'SentryInsight', 'GRCInsight'];
const OWNER = 'ricomanifesto';
const PUBLICATION_STATES = new Set(['disabled/off', 'prepare/off', 'prepare/on', 'active/on']);
const ARTIFACT_BRANCH = 'vercel-production';

function fail(message) {
  throw new Error(`publication site configuration: ${message}`);
}

function parseOrigin(value, label) {
  let url;
  try {
    url = new URL(value);
  } catch {
    fail(`${label} ${JSON.stringify(value)} is not a URL`);
  }
  if (url.href !== value) fail(`${label} ${value} must be written in canonical form`);
  if (url.protocol !== 'https:' || url.username || url.password || url.port || url.search || url.hash) {
    fail(`${label} ${value} must be plain https without credentials, port, query or fragment`);
  }
  return url;
}

function checkProductionOrigin(site, value) {
  const label = `${site} production origin`;
  const url = parseOrigin(value, label);
  if (url.pathname !== '/') fail(`${label} ${value} must serve from the host root`);
  const host = url.hostname;
  if (host === 'localhost' || /^[\d.]+$/.test(host) || host.includes(':') || !host.includes('.')) {
    fail(`${label} ${value} is a local address`);
  }
  if (/(^|\.)(vercel\.app|github\.io|vercel\.sh|now\.sh)$/.test(host) || host.endsWith('.localhost')) {
    fail(`${label} ${value} is a preview or legacy hosting domain`);
  }
}

function checkLegacyOrigin(site, value) {
  const expected = `https://${OWNER}.github.io/${site}/`;
  if (value !== expected) fail(`${site} legacy origin must be ${expected}`);
}

function loadSiteConfig(input) {
  const config = typeof input === 'string' ? JSON.parse(input) : structuredClone(input);
  if (config.schema_version !== 1) fail('schema_version must be 1');
  if (!SITES.includes(config.site)) fail(`site must be one of ${SITES.join(', ')}`);
  if (config.repository !== `${OWNER}/${config.site}`) fail(`repository must be ${OWNER}/${config.site}`);
  for (const site of SITES) {
    const origins = config.origins?.[site];
    if (!origins) fail(`origins.${site} is required`);
    checkLegacyOrigin(site, origins.legacy);
    checkProductionOrigin(site, origins.production);
    if (!['legacy', 'production'].includes(origins.emitted)) fail(`origins.${site}.emitted must be legacy or production`);
  }
  const state = `${config.publication?.mode}/${config.publication?.proof}`;
  if (!PUBLICATION_STATES.has(state)) {
    fail(`publication state ${state} is not one of ${[...PUBLICATION_STATES].join(', ')}`);
  }
  if (config.artifact_branch !== ARTIFACT_BRANCH) fail(`artifact branch must be ${ARTIFACT_BRANCH}`);
  if (!/^[a-z][a-z0-9-]*$/.test(config.state_branch || '') || config.state_branch === ARTIFACT_BRANCH || config.state_branch === 'main') {
    fail('state branch must be a dedicated branch name');
  }
  if (!Array.isArray(config.payload_builder) || config.payload_builder.length === 0) fail('payload_builder is required');
  for (const key of ['machine_endpoint', 'sitemap', 'asset', 'dated_archive']) {
    if (typeof config.proof_samples?.[key] !== 'string') fail(`proof_samples.${key} is required`);
  }
  new RegExp(config.proof_samples.dated_archive);
  for (const consumer of config.consumers || []) {
    if (!SITES.includes(consumer.name) || consumer.repository !== `${OWNER}/${consumer.name}` || consumer.event_type !== 'sentrydigest-updated') {
      fail(`consumer ${JSON.stringify(consumer)} is not an accepted downstream site`);
    }
  }
  return Object.freeze(config);
}

function readSiteConfig(repoRoot) {
  return loadSiteConfig(fs.readFileSync(path.join(repoRoot, 'publication', 'site.json'), 'utf8'));
}

// The origins a reader or validator accepts for a site during the transition.
function acceptedOrigins(config, site) {
  const origins = config.origins[site];
  return [origins.legacy, origins.production];
}

function emittedOrigin(config, site) {
  const origins = config.origins[site];
  return origins[origins.emitted];
}

module.exports = {
  ARTIFACT_BRANCH,
  OWNER,
  SITES,
  acceptedOrigins,
  emittedOrigin,
  loadSiteConfig,
  readSiteConfig,
};
