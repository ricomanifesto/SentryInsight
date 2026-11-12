"""Reuse only a completed main-push Validate run for this exact checkout.

Read-only, bounded GitHub lookup. Any uncertainty requests full local validation.
"""

import json
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPOSITORY = "ricomanifesto/SentryInsight"
REPOSITORY_ID = 983149115
MAX_BYTES = 256 * 1024
TIMEOUT = 10


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward Authorization to a redirect destination.
        return None


def repository_matches(value):
    return (
        isinstance(value, dict)
        and type(value.get("id")) is int
        and value["id"] == REPOSITORY_ID
        and value.get("full_name") == REPOSITORY
    )


def has_validated_run(payload, sha):
    if not isinstance(payload, dict):
        return False
    runs = payload.get("workflow_runs")
    if not isinstance(runs, list) or len(runs) != 1:
        return False
    run = runs[0]
    return (
        isinstance(run, dict)
        and run.get("head_sha") == sha
        and run.get("head_branch") == "main"
        and run.get("event") == "push"
        and run.get("status") == "completed"
        and run.get("conclusion") == "success"
        and run.get("path") == ".github/workflows/validate.yml"
        and repository_matches(run.get("repository"))
        and repository_matches(run.get("head_repository"))
    )


def find_validated_commit(environ=None):
    env = os.environ if environ is None else environ
    sha = env.get("GITHUB_SHA", "")
    token = env.get("GH_TOKEN", "")
    if (
        env.get("GITHUB_REPOSITORY") != REPOSITORY
        or not re.fullmatch(r"[0-9a-f]{40}", sha)
        or not token.strip()
    ):
        return False
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        ).stdout.strip()
        if head != sha:
            return False
        query = urllib.parse.urlencode(
            dict(
                head_sha=sha, event="push", branch="main", status="success", per_page=1
            )
        )
        request = urllib.request.Request(
            f"https://api.github.com/repos/{REPOSITORY}/actions/workflows/validate.yml/runs?{query}",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        opener = urllib.request.build_opener(NoRedirect())
        with opener.open(request, timeout=TIMEOUT) as response:
            if response.status != 200:
                return False
            body = response.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            return False
        return has_validated_run(json.loads(body), sha)
    except Exception:
        # Error strings, URLs, bodies and subprocess output may contain secrets.
        print("::warning::Validate lookup unavailable; running full local validation.")
        return False


def main():
    passed = find_validated_commit()
    with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as output:
        output.write(f"passed={str(passed).lower()}\n")
    print(f"Exact checkout has a successful main Validate run: {str(passed).lower()}")


if __name__ == "__main__":
    main()
