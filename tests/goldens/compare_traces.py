"""Compare two derivation traces written by ``trace_plugin``.

Boundary functions (review planning, prompts, version resolution, evidence
validation, reviewed reports, artifacts) must produce the same ordered outcome
sequence in every test. Memoized derivations are called fewer times, so for
those each test must produce the same set of distinct outcomes: removing a
repeated identical computation cannot remove or add a distinct result.
Tests that only exist afterwards are reported, not failed.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

MEMOIZED = {
    "src.core.finding_evidence.build_finding_detail_context",
    "src.core.finding_evidence._partition_detail_spans",
    "src.core.finding_evidence.assess_exploitation",
    "src.core.version_references._scopes",
    "src.core.version_references._finding_scope",
}


def load(path: Path) -> dict[tuple[str, str], list[str]]:
    entries: dict[tuple[str, str], list[tuple[int, str]]] = defaultdict(list)
    for line in path.read_text().splitlines():
        node, name, seq, outcome = json.loads(line)
        entries[(node, name)].append((seq, outcome))
    return {
        key: [outcome for _, outcome in sorted(calls)] for key, calls in entries.items()
    }


def main(before: str, after: str) -> int:
    old, new = load(Path(before)), load(Path(after))
    old_nodes = {node for node, _ in old}
    failures = []
    for key, outcomes in sorted(old.items()):
        current = new.get(key, [])
        if key[1] in MEMOIZED:
            if set(outcomes) != set(current):
                failures.append(("distinct", *key))
        elif outcomes != current:
            failures.append(("sequence", *key))
    extra = sorted(key for key in new if key not in old and key[0] in old_nodes)
    failures += [("unexpected", *key) for key in extra if key[1] not in MEMOIZED]
    added = sorted({node for node, _ in new} - old_nodes)
    print(f"keys before={len(old)} after={len(new)} failures={len(failures)}")
    print(
        f"calls before={sum(map(len, old.values()))} after={sum(map(len, new.values()))}"
    )
    print(f"tests added={len(added)}")
    for failure in failures[:40]:
        print("DIFF", *failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
