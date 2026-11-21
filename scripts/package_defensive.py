"""Build or verify the defensive package; prints one bounded JSON line.

  build  --revision <commit> --output <new dir> [--source <repo>]
         [--generated-at <YYYY-MM-DDTHH:MM:SSZ>]
         [--approve-head H --approve-facts F --approve-package P]
  verify --package <dir> --approve-package P

Without an approval, build is the local $0 path: it renders the package and
prints the proposed approval triple. With one, any difference refuses before
the output directory exists. Nothing here uploads, publishes or uses a key.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.defensive_package import (  # noqa: E402
    Approval,
    DefensivePackageError,
    build_package,
    verify_package,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build")
    build.add_argument(
        "--source", type=Path, default=Path(__file__).resolve().parents[1]
    )
    build.add_argument("--revision", required=True)
    build.add_argument("--output", type=Path, required=True)
    build.add_argument("--generated-at")
    for name in ("head", "facts", "package"):
        build.add_argument(f"--approve-{name}")
    verify = commands.add_parser("verify")
    verify.add_argument("--package", type=Path, required=True)
    verify.add_argument("--approve-package", required=True)
    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "verify":
            digest = verify_package(arguments.package, arguments.approve_package)
            result = {"verified": True, "package_sha256": digest}
        else:
            parts = (
                arguments.approve_head,
                arguments.approve_facts,
                arguments.approve_package,
            )
            if any(parts) and not all(parts):
                raise DefensivePackageError("approval_incomplete")
            approval = Approval(*parts) if all(parts) else None
            built = build_package(
                source=arguments.source,
                revision=arguments.revision,
                output=arguments.output,
                generated_at=arguments.generated_at,
                approval=approval,
            )
            result = {**built.proposal(), "approved": approval is not None}
    except DefensivePackageError as refusal:
        sys.stdout.write(json.dumps({"refused": str(refusal)}) + "\n")
        return 1
    sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
