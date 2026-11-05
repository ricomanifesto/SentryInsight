const assert = require('node:assert/strict');
const fs = require('node:fs'), path = require('node:path');
const test = require('node:test');
const { bootstrapGitEnvironment } = require('../../scripts/bootstrap_canary_ledger.cjs');
const { createGit } = require('../kit/git');
const { git, tempDir } = require('./helpers');

test('bootstrap Git context is fixed and never copies ambient secrets or controls', () => {
  const env = bootstrapGitEnvironment();
  assert.equal(env.GIT_CONFIG_GLOBAL, '/dev/null'); assert.equal(env.GIT_CONFIG_SYSTEM, '/dev/null');
  assert.equal(env.GIT_ALLOW_PROTOCOL, 'https'); assert.equal(env.GIT_TERMINAL_PROMPT, '0');
  for (const key of ['HOME', 'CODEX_HOME', 'OPENROUTER_API_KEY', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY',
    'HTTPS_PROXY', 'GIT_CONFIG_COUNT', 'GITHUB_TOKEN', 'GH_TOKEN', 'NODE_OPTIONS']) assert.equal(key in env, false);
});
test('the exact minimal context retains checkout-style repository-local conditional auth includes', (t) => {
  const base = tempDir(t, 'bootstrap-checkout-auth-'), repo = path.join(base, 'repo');
  fs.mkdirSync(repo); git(repo, 'init', '--quiet');
  const include = path.join(base, 'ephemeral-checkout-config');
  const marker = 'SYNTHETIC-CHECKOUT-HEADER';
  fs.writeFileSync(include, `[http "https://github.com/"]\n  extraheader = ${marker}\n`, { mode: 0o600 });
  git(repo, 'config', '--local', `includeIf.gitdir:${repo}/.git.path`, include);
  const child = createGit(repo, { env: bootstrapGitEnvironment(), timeoutMs: 3000 });
  assert.equal(child.run(['config', '--get', 'http.https://github.com/.extraheader']), marker);
  // This proves local config loading only. No network/authentication or real
  // GitHub write is attempted or inferred from this synthetic header.
});
