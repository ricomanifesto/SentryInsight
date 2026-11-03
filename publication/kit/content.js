// Site content identity recorded in the release descriptor, read from the
// accepted payload bytes. SentryDigest's digest_content_digest is computed by
// the repository's own canonical article records.
const fs = require('node:fs');
const path = require('node:path');

const { sha256 } = require('./canonical');

function readPayload(payloadDir, relativePath) {
  const filePath = path.join(payloadDir, ...relativePath.split('/'));
  if (!fs.existsSync(filePath)) throw new Error(`${relativePath} is missing from the accepted payload`);
  return fs.readFileSync(filePath);
}

function digestContent(repoRoot) {
  return require(path.join(repoRoot, 'scripts', 'digest-content-identity.js'));
}

function contentIdentityFor({ site, payloadDir, repoRoot }) {
  if (site === 'SentryDigest') {
    const news = readPayload(payloadDir, 'news-data.json');
    const feed = readPayload(payloadDir, 'feed.xml');
    const archive = path.join(payloadDir, 'archive');
    const dates = fs.existsSync(archive)
      ? fs.readdirSync(archive).filter((name) => /^\d{4}-\d{2}-\d{2}$/.test(name)).sort()
      : [];
    return {
      digest_content_digest: digestContent(repoRoot).digestContentDigest(JSON.parse(news.toString('utf8'))),
      feed_sha256: sha256(feed),
      news_data_sha256: sha256(news),
      newest_issue_date: dates.at(-1) || null,
    };
  }
  if (site === 'SentryInsight') {
    const findings = JSON.parse(readPayload(payloadDir, 'current-findings.json').toString('utf8'));
    return { report_date: findings.report_date, generated_at: findings.generated_at };
  }
  if (site === 'GRCInsight') {
    const bytes = readPayload(payloadDir, 'publication-state.json');
    return { report_generated_at: JSON.parse(bytes.toString('utf8')).report_generated_at, publication_state_digest: sha256(bytes) };
  }
  throw new Error(`no content identity for ${site}`);
}

// SentryDigest content identity at an earlier commit, from its committed
// news-data.json, for the activation seed.
function digestContentAt(git, repoRoot, revision) {
  const news = git.showFile(revision, 'news-data.json');
  if (!news) throw new Error(`news-data.json is missing at ${revision}`);
  return { digest_content_digest: digestContent(repoRoot).digestContentDigest(JSON.parse(news.toString('utf8'))) };
}

module.exports = { contentIdentityFor, digestContentAt };
