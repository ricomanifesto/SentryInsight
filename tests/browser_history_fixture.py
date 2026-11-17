"""Build isolated, real-renderer history cases for the browser suite only."""

# ruff: noqa: E402

import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_site_builder import HIGH_UNKNOWN, SRC_A, build_history, history_report


def main():
    pages = Path("test-results/pages").resolve()
    root = Path(tempfile.mkdtemp(prefix="history-fixture-", dir=pages))
    repeated = ("Earlier service flaw", ["CVE-2026-1111"], HIGH_UNKNOWN, [SRC_A])
    new = ("New service flaw", ["CVE-2026-2222"], HIGH_UNKNOWN, [SRC_A])
    unnumbered = ("Credential misuse", [], HIGH_UNKNOWN, [SRC_A])
    archive = {
        date: history_report(date, [repeated]) for date in ("2026-08-15", "2026-08-16")
    }
    cases = {
        "repeated": (repeated, archive),
        "no-cves": (unnumbered, archive),
        "no-archive": (unnumbered, {}),
        "new-cve": (new, archive),
    }
    paths = {}
    for name, (finding, reports) in cases.items():
        site = build_history(
            root / name, history_report("2026-08-17", [finding]), reports
        )
        paths[name] = "/" + site.relative_to(pages).as_posix() + "/"
    print(json.dumps({"root": str(root), "paths": paths}))


if __name__ == "__main__":
    main()
