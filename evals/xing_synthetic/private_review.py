"""Single-recipient age envelopes; no plaintext files or production promotion."""

import argparse
import asyncio
from contextlib import contextmanager, suppress
import hashlib
import hmac
import io
import json
import os
from pathlib import Path
import platform
import re
import stat
import tarfile
import time
import urllib.request

from .policy import MAX_RESPONSE_BYTES, PilotError

VERSION = "v1.3.2"
RETENTION_SECONDS = 86400
MAX_CLEAR_BYTES = MAX_RESPONSE_BYTES + 4096
MAX_CIPHER_BYTES = MAX_CLEAR_BYTES + 4096
AGE_RELEASES = {
    ("Darwin", "arm64"): (
        "darwin-arm64",
        "e2020b073c44f692685a24d6abc378817eb81ffaaf49fd0531ef8565f767f2f5",
        "4012dfc2725883beafb710894af4f599b7a94f8c8e0f51f02cc96ab8df33915e",
    ),
    ("Linux", "x86_64"): (
        "linux-amd64",
        "cbe24006683f8eb669266162894b9a522a1af52f2665fbc63a4bb032ed26ac10",
        "eb7dd1b518f0a307c99cd97782623c5321da049154b04acd2d98d21aa7bc9b2c",
    ),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _hex(value: str, length: int) -> bool:
    return (
        isinstance(value, str)
        and re.fullmatch(r"[0-9a-f]{%d}" % length, value) is not None
    )


def validate_recipient(recipient: str, expected_sha256: str) -> str:
    # Only one canonical native X25519 recipient. No normalization, lists,
    # SSH, plugins, file references, passphrases or private identities.
    if (
        not isinstance(recipient, str)
        or not re.fullmatch(r"age1[023456789acdefghjklmnpqrstuvwxyz]{58}", recipient)
        or not _hex(expected_sha256, 64)
        or not hmac.compare_digest(sha256(recipient.encode()), expected_sha256)
    ):
        raise PilotError("review_recipient_unapproved")
    return expected_sha256


def _release() -> tuple[str, str, str]:
    try:
        return AGE_RELEASES[(platform.system(), platform.machine())]
    except KeyError:
        raise PilotError("review_platform_unsupported") from None


def verify_age(binary: Path) -> Path:
    binary = binary.resolve(strict=True)
    if not binary.is_file() or binary.stat().st_size > 16 * 1024 * 1024:
        raise PilotError("review_binary_identity")
    if sha256(binary.read_bytes()) != _release()[2]:
        raise PilotError("review_binary_identity")
    return binary


def install_age(binary: Path) -> None:
    if os.getenv("OPENROUTER_API_KEY"):
        raise PilotError("secret_in_setup_step")
    if binary.exists():
        verify_age(binary)
        return
    target, archive_sha, binary_sha = _release()
    url = f"https://github.com/FiloSottile/age/releases/download/{VERSION}/age-{VERSION}-{target}.tar.gz"
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read(24 * 1024 * 1024)
    if sha256(data) != archive_sha:
        raise PilotError("review_archive_identity")
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
        member = archive.getmember("age/age")
        if not member.isfile() or member.size > 16 * 1024 * 1024:
            raise PilotError("review_binary_identity")
        stream = archive.extractfile(member)
        if stream is None:
            raise PilotError("review_binary_identity")
        data = stream.read(16 * 1024 * 1024)
    if sha256(data) != binary_sha:
        raise PilotError("review_binary_identity")
    binary.parent.mkdir(parents=True, exist_ok=True)
    with binary.open("xb") as stream:
        stream.write(data)
    binary.chmod(0o700)


async def _age(
    binary: Path,
    arguments: list[str],
    data: bytes,
    limit: int,
    *,
    pass_fds: tuple[int, ...] = (),
) -> bytes:
    binary = verify_age(binary)
    process = None
    writer = None
    try:
        async with asyncio.timeout(15):
            process = await asyncio.create_subprocess_exec(
                str(binary),
                *arguments,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.DEVNULL,
                # Never forward the API key, account config, agents or proxy env.
                env={"PATH": "/usr/bin:/bin", "LANG": "C"},
                pass_fds=pass_fds,
            )
            assert process.stdin is not None and process.stdout is not None

            async def feed():
                assert process is not None and process.stdin is not None
                process.stdin.write(data)
                await process.stdin.drain()
                process.stdin.close()

            writer = asyncio.create_task(feed())
            result = bytearray()
            while chunk := await process.stdout.read(
                min(65536, limit + 1 - len(result))
            ):
                result.extend(chunk)
                if len(result) > limit:
                    raise PilotError("review_crypto_failed")
            await writer
            if await process.wait() != 0:
                raise PilotError("review_crypto_failed")
            return bytes(result)
    except Exception:
        raise PilotError("review_crypto_failed") from None
    finally:
        if process is not None and process.returncode is None:
            with suppress(ProcessLookupError):
                process.kill()
            await process.wait()
        if writer is not None:
            writer.cancel()
            with suppress(
                asyncio.CancelledError, BrokenPipeError, ConnectionResetError
            ):
                await writer


def _context(candidate_sha: str, run_id: str, case: str, request_sha: str) -> dict:
    from .fixtures import CASE_NAMES

    if (
        not _hex(candidate_sha, 40)
        or not _hex(request_sha, 64)
        or not isinstance(run_id, str)
        or not re.fullmatch(r"[0-9]{1,20}", run_id)
        or case not in CASE_NAMES
    ):
        raise PilotError("review_context")
    return {
        "candidate_sha": candidate_sha,
        "run_id": run_id,
        "run_attempt": 1,
        "case": case,
        "request_sha256": request_sha,
    }


class EncryptedReview:
    def __init__(self, binary: Path, recipient: str, expected_sha256: str, run_id: str):
        self.recipient_sha256 = validate_recipient(recipient, expected_sha256)
        self.binary = verify_age(binary)
        self.recipient = recipient
        if not re.fullmatch(r"[0-9]{1,20}", run_id):
            raise PilotError("review_context")
        self.run_id = run_id
        self.seen: set[str] = set()

    async def preflight(self) -> None:
        # Native age validates the checksum/point before any model request.
        await _age(
            self.binary,
            ["--encrypt", "--recipient", self.recipient],
            b"",
            MAX_CIPHER_BYTES,
        )

    async def seal(
        self,
        output: Path,
        case: str,
        raw: str,
        candidate_sha: str,
        request_sha: str,
        *,
        now: int | None = None,
    ) -> dict:
        context = _context(candidate_sha, self.run_id, case, request_sha)
        if (
            case in self.seen
            or len(self.seen) >= 6
            or not raw
            or len(raw.encode()) > MAX_RESPONSE_BYTES
        ):
            raise PilotError("review_bounds")
        created = int(time.time()) if now is None else now
        if type(created) is not int or created < 0:
            raise PilotError("review_context")
        bundle = {
            "schema": 1,
            **context,
            "recipient_sha256": self.recipient_sha256,
            "created_at": created,
            "expires_at": created + RETENTION_SECONDS,
            "answer": raw,
        }
        clear = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")).encode()
        if len(clear) > MAX_CLEAR_BYTES:
            raise PilotError("review_bounds")
        cipher = await _age(
            self.binary,
            ["--encrypt", "--recipient", self.recipient],
            clear,
            MAX_CIPHER_BYTES,
        )
        if not cipher.startswith(b"age-encryption.org/v1\n"):
            raise PilotError("review_crypto_failed")
        target = output / "encrypted-review"
        target.mkdir(mode=0o700, exist_ok=True)
        path = target / f"{case}.age"
        created_file = False
        try:
            with path.open("xb") as stream:
                created_file = True
                stream.write(cipher)
            path.chmod(0o600)
        except Exception:
            if created_file:
                path.unlink(missing_ok=True)
            raise PilotError("review_write_failed") from None
        self.seen.add(case)
        return {
            "file": path.name,
            "ciphertext_sha256": sha256(cipher),
            "recipient_sha256": self.recipient_sha256,
            "bytes": len(cipher),
            "created_at": created,
            "expires_at": created + RETENTION_SECONDS,
        }


async def open_review(
    binary: Path,
    path: Path,
    identity: Path,
    *,
    expected_digest: str,
    recipient_sha256: str,
    candidate_sha: str,
    run_id: str,
    case: str,
    request_sha: str,
    now: int | None = None,
) -> dict:
    # These expected values must come from the trusted workflow run/receipt,
    # never solely from a file supplied alongside an untrusted ciphertext.
    context = _context(candidate_sha, run_id, case, request_sha)
    if not _hex(expected_digest, 64) or not _hex(recipient_sha256, 64):
        raise PilotError("review_context")
    with _regular_input(path) as stream:
        cipher = stream.read(MAX_CIPHER_BYTES + 1)
    if len(cipher) > MAX_CIPHER_BYTES or not hmac.compare_digest(
        sha256(cipher), expected_digest
    ):
        raise PilotError("review_ciphertext_identity")
    # Restrict user-local input to one native identity; no plugins or SSH keys.
    with _regular_input(identity, owner_only=True) as stream:
        key = stream.read(4097)
        lines = [
            line for line in key.splitlines() if line and not line.startswith(b"#")
        ]
        if (
            len(key) > 4096
            or len(lines) != 1
            or not re.fullmatch(
                rb"AGE-SECRET-KEY-1[023456789ACDEFGHJKLMNPQRSTUVWXYZ]{58}", lines[0]
            )
        ):
            raise PilotError("review_identity_format")
        stream.seek(0)
        # Keep the verified file open; do not resolve the pathname again in age.
        clear = await _age(
            binary,
            ["--decrypt", "--identity", f"/dev/fd/{stream.fileno()}"],
            cipher,
            MAX_CLEAR_BYTES,
            pass_fds=(stream.fileno(),),
        )
    try:
        bundle = json.loads(clear)
        if set(bundle) != {
            "schema",
            *context,
            "recipient_sha256",
            "created_at",
            "expires_at",
            "answer",
        }:
            raise ValueError
        if (
            type(bundle["schema"]) is not int
            or bundle["schema"] != 1
            or type(bundle["run_attempt"]) is not int
            or any(bundle[k] != v for k, v in context.items())
        ):
            raise ValueError
        if bundle["recipient_sha256"] != recipient_sha256:
            raise ValueError
        created, expires = bundle["created_at"], bundle["expires_at"]
        current = int(time.time()) if now is None else now
        if (
            type(created) is not int
            or type(expires) is not int
            or created < 0
            or expires - created != RETENTION_SECONDS
            or not created <= current < expires
        ):
            raise ValueError
        if (
            not isinstance(bundle["answer"], str)
            or not bundle["answer"]
            or len(bundle["answer"].encode()) > MAX_RESPONSE_BYTES
        ):
            raise ValueError
    except (ValueError, TypeError, KeyError, UnicodeError):
        raise PilotError("review_bundle_rejected") from None
    return bundle


@contextmanager
def _regular_input(path: Path, *, owner_only: bool = False):
    """Reject special files and symlinks before any potentially blocking read."""
    fd = None
    try:
        try:
            fd = os.open(
                path, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC
            )
            info = os.fstat(fd)
        except OSError:
            raise PilotError("review_file_access") from None
        if not stat.S_ISREG(info.st_mode):
            raise PilotError("review_file_type")
        if owner_only and (info.st_uid != os.getuid() or info.st_mode & 0o077):
            raise PilotError("review_identity_permissions")
        with os.fdopen(fd, "rb") as stream:
            fd = None  # The stream owns this descriptor, including on failure.
            yield stream
    finally:
        if fd is not None:
            os.close(fd)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("setup", "preflight", "open"))
    parser.add_argument("--age-binary", type=Path, required=True)
    parser.add_argument("--recipient")
    parser.add_argument("--recipient-sha256")
    parser.add_argument("--run-id")
    parser.add_argument("--file", type=Path)
    parser.add_argument("--identity-file", type=Path)
    parser.add_argument("--ciphertext-sha256")
    parser.add_argument("--candidate-sha")
    parser.add_argument("--case")
    parser.add_argument("--request-sha256")
    args = parser.parse_args()
    try:
        if args.mode == "setup":
            install_age(args.age_binary)
            print('{"age_setup":"verified"}')
        elif args.mode == "preflight":
            if os.getenv("OPENROUTER_API_KEY"):
                raise PilotError("secret_in_setup_step")
            review = EncryptedReview(
                args.age_binary, args.recipient, args.recipient_sha256, args.run_id
            )
            asyncio.run(review.preflight())
            print('{"review_recipient":"verified"}')
        else:
            if os.getenv("GITHUB_ACTIONS") or os.getenv("OPENROUTER_API_KEY"):
                raise PilotError("review_local_only")
            result = asyncio.run(
                open_review(
                    args.age_binary,
                    args.file,
                    args.identity_file,
                    expected_digest=args.ciphertext_sha256,
                    recipient_sha256=args.recipient_sha256,
                    candidate_sha=args.candidate_sha,
                    run_id=args.run_id,
                    case=args.case,
                    request_sha=args.request_sha256,
                )
            )
            # JSON escapes control/terminal sequences. Output is local only.
            print(json.dumps(result, ensure_ascii=True, allow_nan=False))
        return 0
    except Exception:
        print('{"outcome":"private_review_failed"}')
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
