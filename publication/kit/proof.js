// Serving proof against the confirmed production origin, anonymously.
//
// The served listing must equal the release payload plus the descriptor plus
// exactly one build receipt. The descriptor must be byte-identical to the
// release descriptor; the receipt must hash to its listing line and name the
// production environment, the origin host, the artifact branch, the expected
// repository, the release commit and the release key. Representative samples
// must hash to their listing lines, and the adapter and provider
// configuration must return 404.
//
// listing_digest is the SHA-256 of the fetched listing bytes. The complete
// served inventory (every listed file plus the listing itself) and its digest
// are computed here, outside the served files, so nothing is self-referential.
const { inventoryDigest, parseInventory, sha256 } = require('./canonical');
const { LAYOUT } = require('./release');

const RECORDED_HEADERS = ['content-type', 'cache-control', 'x-robots-tag', 'etag', 'age', 'location'];

function headerOf(response, name) {
  const headers = response.headers;
  if (!headers) return undefined;
  return typeof headers.get === 'function' ? headers.get(name) ?? undefined : headers[name];
}

function urlFor(origin, relativePath) {
  if (relativePath === 'index.html') return origin;
  if (relativePath.endsWith('/index.html')) return `${origin}${relativePath.slice(0, -'index.html'.length)}`;
  return `${origin}${relativePath}`;
}

function samplePaths(config, payloadEntries) {
  const samples = config.proof_samples;
  const archive = new RegExp(samples.dated_archive);
  const dated = payloadEntries.map((entry) => entry.path).filter((p) => archive.test(p)).sort();
  return [
    'index.html',
    samples.machine_endpoint,
    dated.at(-1),
    samples.sitemap,
    samples.asset,
  ].filter(Boolean);
}

async function attemptProof({ config, release, fetchUrl }) {
  const origin = config.origins[config.site].production;
  const failures = [];
  const record = { samples: [], absent: [] };
  const get = async (url) => {
    const response = await fetchUrl(url);
    const body = Buffer.isBuffer(response.body) ? response.body : Buffer.from(response.body ?? '');
    return {
      status: response.status,
      body,
      headers: Object.fromEntries(RECORDED_HEADERS.map((name) => [name, headerOf(response, name)]).filter(([, v]) => v !== undefined)),
    };
  };

  const listingResponse = await get(`${origin}${LAYOUT.listing}`);
  if (listingResponse.status !== 200) {
    failures.push(`listing returned ${listingResponse.status}`);
    return { failures, record };
  }
  let listing;
  try {
    listing = parseInventory(listingResponse.body);
  } catch (error) {
    failures.push(`listing is malformed: ${error.message}`);
    return { failures, record };
  }
  record.listing_digest = sha256(listingResponse.body);
  const listed = new Map(listing.map((entry) => [entry.path, entry.sha256]));

  const expected = new Map(release.payloadEntries.map((entry) => [entry.path, entry.sha256]));
  expected.set(LAYOUT.descriptor, sha256(release.descriptorBytes));
  for (const [relativePath, digest] of expected) {
    if (!listed.has(relativePath)) failures.push(`listing is missing ${relativePath}`);
    else if (listed.get(relativePath) !== digest) failures.push(`listing hash for ${relativePath} differs from the release`);
  }
  for (const relativePath of listed.keys()) {
    if (!expected.has(relativePath) && relativePath !== LAYOUT.receipt) failures.push(`listing has unexpected served file ${relativePath}`);
  }
  if (!listed.has(LAYOUT.receipt)) failures.push('listing has no build receipt');

  const descriptorResponse = await get(`${origin}${LAYOUT.descriptor}`);
  try {
    record.served_release_key = JSON.parse(descriptorResponse.body.toString('utf8')).release_key;
  } catch {
    record.served_release_key = null;
  }
  if (descriptorResponse.status !== 200 || !descriptorResponse.body.equals(Buffer.from(release.descriptorBytes))) {
    failures.push(`served descriptor differs from the release descriptor (served release ${record.served_release_key ?? 'unknown'})`);
  }

  const receiptResponse = await get(`${origin}${LAYOUT.receipt}`);
  if (receiptResponse.status !== 200 || sha256(receiptResponse.body) !== listed.get(LAYOUT.receipt)) {
    failures.push('build receipt does not match its listing line');
  } else {
    let receipt = {};
    try {
      receipt = JSON.parse(receiptResponse.body.toString('utf8'));
    } catch {
      failures.push('build receipt is not valid JSON');
    }
    const checks = {
      release_key: release.releaseKey,
      git_commit_sha: release.releaseRef,
      git_ref: config.artifact_branch,
      repository: config.repository,
      environment: 'production',
      production_host: new URL(origin).host,
    };
    for (const [field, value] of Object.entries(checks)) {
      if (receipt[field] !== value) failures.push(`build receipt ${field} is ${JSON.stringify(receipt[field])}, expected ${value}`);
    }
    record.receipt = receipt;
  }

  for (const relativePath of samplePaths(config, release.payloadEntries)) {
    const url = urlFor(origin, relativePath);
    const response = await get(url);
    const ok = response.status === 200 && listed.get(relativePath) === sha256(response.body);
    if (!ok) failures.push(`sample ${relativePath} (${url}) returned ${response.status} with bytes that do not match the listing`);
    record.samples.push({ path: relativePath, url, status: response.status, ok, headers: response.headers });
  }
  record.samples.push(
    { path: LAYOUT.listing, status: 200, ok: true, headers: listingResponse.headers },
    { path: LAYOUT.descriptor, status: descriptorResponse.status, ok: descriptorResponse.status === 200, headers: descriptorResponse.headers },
  );

  for (const relativePath of [LAYOUT.adapter, LAYOUT.providerConfig]) {
    const response = await get(`${origin}${relativePath}`);
    record.absent.push({ path: relativePath, status: response.status });
    if (response.status !== 404) failures.push(`${relativePath} must not be served (status ${response.status})`);
  }

  if (failures.length === 0) {
    const served = [...listing, { path: LAYOUT.listing, sha256: record.listing_digest }];
    record.served_digest = inventoryDigest(served);
    record.served_file_count = served.length;
  }
  return { failures, record };
}

// Bounded wait with exponential backoff; the last attempt's findings are
// returned. Expiry is a resumable verification failure, never success.
async function proveServing({ config, release, fetchUrl, attempts = 6, baseDelayMs = 10000, sleep, now = () => new Date() }) {
  let last = { failures: ['no proof attempt ran'], record: { samples: [], absent: [] } };
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      last = await attemptProof({ config, release, fetchUrl });
    } catch (error) {
      last = { failures: [`origin request failed: ${error.message}`], record: { samples: [], absent: [] } };
    }
    if (last.failures.length === 0) break;
    if (attempt < attempts) await sleep(baseDelayMs * 2 ** (attempt - 1));
  }
  return {
    ok: last.failures.length === 0,
    failures: last.failures,
    origin: config.origins[config.site].production,
    tls: new URL(config.origins[config.site].production).protocol === 'https:',
    checked_at: now().toISOString(),
    ...last.record,
  };
}

module.exports = { proveServing, samplePaths, urlFor };
