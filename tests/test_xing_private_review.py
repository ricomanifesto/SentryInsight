"""Offline access-boundary tests using published upstream test identities only."""

import asyncio
import os
from pathlib import Path
import socket

import pytest
import httpx

from evals.xing_synthetic import private_review as review
from evals.xing_synthetic.policy import PilotError, MAX_RESPONSE_BYTES
from evals.xing_synthetic.fixtures import CASE_NAMES

# Public, deliberately unsuitable for real data. No identity is generated here.
# https://github.com/FiloSottile/age/blob/v1.3.2/cmd/age/testdata/x25519.txt
PUBLIC = "age1xmwwc06ly3ee5rytxm9mflaz2u56jjj36s0mypdrwsvlul66mv4q47ryef"
IDENTITY = "AGE-SECRET-KEY-1EGTZVFFV20835NWYV6270LXYVK2VKNX2MMDKWYKLMGR48UAWX40Q2P2LM0"
# Independent public example identity from v1.3.2/age_test.go.
WRONG_IDENTITY = (
    "AGE-SECRET-KEY-184JMZMVQH3E6U0PSL869004Y3U2NYV7R30EU99CSEDNPH02YUVFSZW44VU"
)
PIN = review.sha256(PUBLIC.encode())
SHA = "a" * 40
REQUEST = "b" * 64
RUN = "123456789"
NOW = 1800000000
ANSWER = "Synthetic answer, not reviewed.\n\x1b[31mUntrusted terminal sequence."


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("No network in private review tests")

    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture
def binary():
    value = os.getenv("XING_TEST_AGE_BINARY")
    if not value:
        pytest.skip(
            "Native age integration requires XING_TEST_AGE_BINARY; see evaluation guide"
        )
    return review.verify_age(Path(value))


@pytest.fixture
def keys(tmp_path):
    paths = []
    for name, value in (
        ("published-test", IDENTITY),
        ("published-wrong", WRONG_IDENTITY),
    ):
        path = tmp_path / name
        path.write_text(value + "\n")
        path.chmod(0o600)
        paths.append(path)
    return paths


def encrypted(binary, tmp_path):
    engine = review.EncryptedReview(binary, PUBLIC, PIN, RUN)
    asyncio.run(engine.preflight())
    metadata = asyncio.run(
        engine.seal(tmp_path, CASE_NAMES[0], ANSWER, SHA, REQUEST, now=NOW)
    )
    return engine, metadata, tmp_path / "encrypted-review" / metadata["file"]


def open_answer(binary, path, identity, metadata, **overrides):
    options = dict(
        expected_digest=metadata["ciphertext_sha256"],
        recipient_sha256=PIN,
        candidate_sha=SHA,
        run_id=RUN,
        case=CASE_NAMES[0],
        request_sha=REQUEST,
        now=NOW,
    )
    options.update(overrides)
    return asyncio.run(review.open_review(binary, path, identity, **options))


@pytest.mark.parametrize(
    "recipient,pin",
    [
        (PUBLIC, ""),
        (PUBLIC, "f" * 64),
        (PUBLIC + "\n", PIN),
        (PUBLIC + "," + PUBLIC, PIN),
        (IDENTITY, PIN),
        ("ssh-ed25519 AAAA", PIN),
        ("age1plugin1example", PIN),
        ("-R /tmp/recipients", PIN),
        (None, None),
    ],
)
def test_unapproved_or_alternate_recipient_types_rejected(recipient, pin):
    with pytest.raises(PilotError, match="review_recipient_unapproved"):
        review.validate_recipient(recipient, pin)


def test_no_key_in_setup_environment(monkeypatch, tmp_path):
    monkeypatch.setenv("OPENROUTER_API_KEY", "synthetic-unused-value")
    with pytest.raises(PilotError, match="secret_in_setup_step"):
        review.install_age(tmp_path / "age")


def test_binary_identity_rejects_substitute(tmp_path):
    path = tmp_path / "age"
    path.write_bytes(b"not the pinned binary")
    with pytest.raises(PilotError, match="review_binary_identity"):
        review.verify_age(path)


def test_only_pinned_recipient_can_read_without_plaintext_artifacts(
    binary, tmp_path, keys, capsys, monkeypatch
):
    monkeypatch.setenv(
        "OPENROUTER_API_KEY", "synthetic-credential-must-not-reach-child"
    )
    original = asyncio.create_subprocess_exec

    async def observed(*args, **kwargs):
        assert kwargs["env"] == {"PATH": "/usr/bin:/bin", "LANG": "C"}
        assert all("synthetic-credential" not in str(x) for x in args)
        return await original(*args, **kwargs)

    monkeypatch.setattr(asyncio, "create_subprocess_exec", observed)
    _, metadata, path = encrypted(binary, tmp_path)
    assert ANSWER.encode() not in path.read_bytes()
    assert path.stat().st_mode & 0o777 == 0o600
    assert metadata["expires_at"] - metadata["created_at"] == 86400
    assert path.stat().st_size <= review.MAX_CIPHER_BYTES
    assert open_answer(binary, path, keys[0], metadata)["answer"] == ANSWER
    with pytest.raises(PilotError, match="review_crypto_failed"):
        open_answer(binary, path, keys[1], metadata)
    assert not list(tmp_path.rglob("*.txt"))
    assert capsys.readouterr().out == ""


@pytest.mark.parametrize(
    "override",
    [
        {"candidate_sha": "c" * 40},
        {"run_id": "987654321"},
        {"case": CASE_NAMES[1]},
        {"request_sha": "d" * 64},
        {"recipient_sha256": "e" * 64},
        {"now": NOW - 1},
        {"now": NOW + 86400},
    ],
)
def test_context_and_one_day_window_verified_before_answer(
    binary, tmp_path, keys, override
):
    _, metadata, path = encrypted(binary, tmp_path)
    with pytest.raises(PilotError, match="review_bundle_rejected"):
        open_answer(binary, path, keys[0], metadata, **override)


def test_trusted_digest_and_full_authentication_required(binary, tmp_path, keys):
    _, metadata, path = encrypted(binary, tmp_path)
    with pytest.raises(PilotError, match="review_ciphertext_identity"):
        open_answer(
            binary, path, Path("missing-identity"), metadata, expected_digest="e" * 64
        )
    data = bytearray(path.read_bytes())
    data[-1] ^= 1
    path.write_bytes(data)
    # Even if a caller incorrectly trusts the modified digest, age authentication fails.
    with pytest.raises(PilotError, match="review_crypto_failed"):
        open_answer(
            binary, path, keys[0], metadata, expected_digest=review.sha256(data)
        )


def test_bad_native_checksum_rejected_before_request(binary):
    wrong = PUBLIC[:-1] + ("q" if PUBLIC[-1] != "q" else "p")
    engine = review.EncryptedReview(binary, wrong, review.sha256(wrong.encode()), RUN)
    with pytest.raises(PilotError, match="review_crypto_failed"):
        asyncio.run(engine.preflight())


def test_bounded_output_and_answer_count(binary, tmp_path):
    engine = review.EncryptedReview(binary, PUBLIC, PIN, RUN)
    with pytest.raises(PilotError, match="review_bounds"):
        asyncio.run(
            engine.seal(
                tmp_path, CASE_NAMES[0], "x" * (MAX_RESPONSE_BYTES + 1), SHA, REQUEST
            )
        )
    with pytest.raises(PilotError, match="review_crypto_failed"):
        asyncio.run(
            review._age(binary, ["--encrypt", "--recipient", PUBLIC], b"public", 4)
        )
    for case in CASE_NAMES:
        asyncio.run(engine.seal(tmp_path, case, "Synthetic", SHA, REQUEST, now=NOW))
    with pytest.raises(PilotError, match="review_bounds"):
        asyncio.run(
            engine.seal(tmp_path, CASE_NAMES[0], "Synthetic", SHA, REQUEST, now=NOW)
        )
    assert len(list(tmp_path.rglob("*.age"))) == 6


def test_loose_identity_permissions_rejected(binary, tmp_path, keys):
    _, metadata, path = encrypted(binary, tmp_path)
    keys[0].chmod(0o644)
    with pytest.raises(PilotError, match="review_identity_permissions"):
        open_answer(binary, path, keys[0], metadata)


def test_partial_ciphertext_write_is_removed(binary, tmp_path, monkeypatch):
    engine = review.EncryptedReview(binary, PUBLIC, PIN, RUN)
    original = Path.chmod

    def failed(path, mode, *args, **kwargs):
        if path.suffix == ".age":
            raise OSError("synthetic write error")
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "chmod", failed)
    with pytest.raises(PilotError, match="review_write_failed"):
        asyncio.run(engine.seal(tmp_path, CASE_NAMES[0], ANSWER, SHA, REQUEST, now=NOW))
    assert not list(tmp_path.rglob("*.age"))


def test_existing_ciphertext_is_not_replaced_or_deleted(binary, tmp_path):
    _, metadata, path = encrypted(binary, tmp_path)
    before = path.read_bytes()
    engine = review.EncryptedReview(binary, PUBLIC, PIN, RUN)
    with pytest.raises(PilotError, match="review_write_failed"):
        asyncio.run(engine.seal(tmp_path, CASE_NAMES[0], ANSWER, SHA, REQUEST, now=NOW))
    assert path.read_bytes() == before


def test_six_mock_model_answers_remain_encrypted_until_local_review(
    binary, tmp_path, keys
):
    import test_xing_synthetic as pilot

    cases = asyncio.run(pilot.fixtures.prepare_cases(pilot.FixedBudget()))
    answers = [pilot.fixtures.reference_report(case) for case in cases]
    provider = pilot.Provider(answers)
    engine = review.EncryptedReview(binary, PUBLIC, PIN, RUN)

    async def no_wait(delay):
        pass

    result = asyncio.run(
        pilot.runner.run_cases(
            cases,
            secret=pilot.SECRET,
            output=tmp_path / "pilot",
            candidate_sha=SHA,
            review_outputs=True,
            review_recipient=engine,
            transport=httpx.MockTransport(provider.handle),
            sleep=no_wait,
            clock=lambda: 100,
        )
    )
    assert result["complete"] and len(provider.calls) == 6
    assert result["human_review"] == "not_performed" and not result["production_ready"]
    for case, answer, trial in zip(cases, answers, result["trials"], strict=True):
        metadata = trial["encrypted_review"]
        path = tmp_path / "pilot/encrypted-review" / metadata["file"]
        decoded = asyncio.run(
            review.open_review(
                binary,
                path,
                keys[0],
                expected_digest=metadata["ciphertext_sha256"],
                recipient_sha256=PIN,
                candidate_sha=SHA,
                run_id=RUN,
                case=case.name,
                request_sha=case.request_sha256,
            )
        )
        assert decoded["answer"] == answer
        assert answer.encode() not in path.read_bytes()
    files = list((tmp_path / "pilot").rglob("*"))
    assert not any(p.is_file() and p.suffix not in {".age", ".json"} for p in files)
