// Minimal Git plumbing over the git CLI. Branch updates are compare-and-set:
// a push names the exact remote value it expects to replace (or that the
// branch must not exist yet), so a concurrent writer makes the push fail
// instead of being overwritten.
const childProcess = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

class CompareAndSetLost extends Error {}

function createGit(repoRoot, { env = process.env, timeoutMs } = {}) {
  const run = (args, { input, encoding = 'utf8', extraEnv = {}, allowFailure = false } = {}) => {
    const result = childProcess.spawnSync('git', args, {
      cwd: repoRoot,
      env: { ...env, ...extraEnv },
      input,
      encoding: encoding === 'buffer' ? undefined : encoding,
      maxBuffer: 512 * 1024 * 1024,
      timeout: timeoutMs,
    });
    if (result.status !== 0) {
      if (allowFailure) return null;
      const stderr = Buffer.isBuffer(result.stderr) ? result.stderr.toString('utf8') : result.stderr;
      const error = new Error(`git ${args.join(' ')} failed: ${String(stderr || result.error || '').trim()}`);
      error.stderr = stderr;
      throw error;
    }
    return encoding === 'buffer' ? result.stdout : result.stdout.trim();
  };

  const git = {
    run,
    // The remote's current value of a branch, fetched into a private ref.
    fetchBranch(remote, branch) {
      const listed = run(['ls-remote', remote, `refs/heads/${branch}`]);
      if (!listed) return null;
      const tip = listed.split(/\s+/)[0];
      run(['fetch', '--quiet', '--no-tags', remote, `+refs/heads/${branch}:refs/publication/remote/${branch}`]);
      return tip;
    },
    showFile(commit, filePath, { encoding = 'buffer' } = {}) {
      return run(['show', `${commit}:${filePath}`], { encoding, allowFailure: true });
    },
    listTree(commit) {
      const output = run(['ls-tree', '-r', '-z', '--full-tree', commit]);
      return output.split('\0').filter(Boolean).map((line) => {
        const tab = line.indexOf('\t');
        const [mode, type, oid] = line.slice(0, tab).split(' ');
        return { mode, type, oid, path: line.slice(tab + 1) };
      });
    },
    isAncestor(ancestor, descendant) {
      return run(['merge-base', '--is-ancestor', ancestor, descendant], { allowFailure: true }) !== null;
    },
    commitDate(revision) {
      return run(['show', '-s', '--format=%cI', revision]);
    },
    // Writes the given files as a new commit on top of parent (or as a root
    // commit) without touching any working tree or the repository index.
    commitFiles(files, { parent, message, extraEnv = {} }) {
      const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'publication-tree-'));
      try {
        const index = path.join(scratch, 'index');
        const tree = path.join(scratch, 'tree');
        for (const [relativePath, bytes] of files) {
          const target = path.join(tree, ...relativePath.split('/'));
          fs.mkdirSync(path.dirname(target), { recursive: true });
          fs.writeFileSync(target, bytes);
        }
        fs.mkdirSync(tree, { recursive: true });
        const scoped = { GIT_INDEX_FILE: index, GIT_WORK_TREE: tree, ...extraEnv };
        run(['--work-tree', tree, 'add', '--all', '--force', '.'], { extraEnv: scoped });
        const treeId = run(['write-tree'], { extraEnv: scoped });
        const args = ['commit-tree', treeId, '-m', message];
        if (parent) args.push('-p', parent);
        return run(args, { extraEnv });
      } finally {
        fs.rmSync(scratch, { recursive: true, force: true });
      }
    },
    // Compare-and-set branch update on the remote.
    // Initialization has a distinct one-attempt contract: expected absent,
    // no automatic readback/adoption after a failed acknowledgement.
    pushInitialBranch(remote, commit, branch) {
      const result = run(['push', '--quiet', '--porcelain', `--force-with-lease=refs/heads/${branch}:`, remote,
        `${commit}:refs/heads/${branch}`], { allowFailure: true });
      if (result === null) throw new Error('Admission initialization unknown');
      return commit;
    },
    pushBranch(remote, commit, branch, expected) {
      const lease = `--force-with-lease=refs/heads/${branch}:${expected || ''}`;
      const result = run(['push', '--quiet', '--porcelain', lease, remote, `${commit}:refs/heads/${branch}`], { allowFailure: true });
      if (result === null) {
        const current = run(['ls-remote', remote, `refs/heads/${branch}`]).split(/\s+/)[0] || null;
        if (current === commit) return;
        if (current !== (expected || null)) {
          throw new CompareAndSetLost(`${branch} moved on the remote (expected ${expected || 'absent'}, found ${current || 'absent'})`);
        }
        throw new Error(`push of ${branch} to ${remote} failed`);
      }
    },
    readBlobs(oids) {
      if (oids.length === 0) return [];
      const output = run(['cat-file', '--batch'], { input: `${oids.join('\n')}\n`, encoding: 'buffer' });
      const blobs = [];
      let offset = 0;
      for (const oid of oids) {
        const newline = output.indexOf(10, offset);
        const [headerOid, type, size] = output.subarray(offset, newline).toString('utf8').split(' ');
        if (headerOid !== oid || type !== 'blob') throw new Error(`git object ${oid} is not a readable blob`);
        blobs.push(output.subarray(newline + 1, newline + 1 + Number(size)));
        offset = newline + 1 + Number(size) + 1;
      }
      return blobs;
    },
  };
  return git;
}

module.exports = { CompareAndSetLost, createGit };
