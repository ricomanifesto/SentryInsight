import asyncio
import sys
import types
from unittest.mock import patch

from src.services.audio import (
    extract_executive_summary,
    generate_executive_summary_audio,
)


def install_fake_elevenlabs(audio):
    client_module = types.ModuleType("elevenlabs.client")

    class FakeElevenLabs:
        def __init__(self, *, api_key):
            assert api_key == "test-key"
            self.text_to_speech = types.SimpleNamespace(convert=lambda **_kwargs: audio)

    client_module.ElevenLabs = FakeElevenLabs
    package_module = types.ModuleType("elevenlabs")
    package_module.client = client_module
    return {
        "elevenlabs": package_module,
        "elevenlabs.client": client_module,
    }


def test_extract_executive_summary_reads_named_section():
    report = """# Exploitation Report

## Executive Summary

First executive paragraph.

Second executive paragraph.

## Active Exploitation Details

### Example
- **Status**: Active.
"""

    assert extract_executive_summary(report) == (
        "First executive paragraph. Second executive paragraph."
    )


def test_extract_executive_summary_keeps_legacy_first_paragraph_fallback():
    report = """# Exploitation Report

Legacy executive paragraph.

## Active Exploitation Details

### Example
- **Status**: Active.
"""

    assert extract_executive_summary(report) == "Legacy executive paragraph."


def test_audio_generation_preserves_previous_file_when_stream_fails(tmp_path):
    def interrupted_audio():
        yield b"partial replacement"
        raise RuntimeError("stream interrupted")

    output_path = tmp_path / "executive_summary.mp3"
    output_path.write_bytes(b"previous valid audio")

    with (
        patch.dict("os.environ", {"ELEVENLABS_API_KEY": "test-key"}),
        patch.dict(sys.modules, install_fake_elevenlabs(interrupted_audio())),
    ):
        result = asyncio.run(
            generate_executive_summary_audio(
                "# Exploitation Report\n\n## Executive Summary\n\nExample.",
                str(output_path),
            )
        )

    assert result is False
    assert output_path.read_bytes() == b"previous valid audio"
    assert list(tmp_path.iterdir()) == [output_path]


def test_audio_generation_atomically_replaces_previous_file(tmp_path):
    output_path = tmp_path / "executive_summary.mp3"
    output_path.write_bytes(b"previous valid audio")
    output_path.chmod(0o640)

    with (
        patch.dict("os.environ", {"ELEVENLABS_API_KEY": "test-key"}),
        patch.dict(sys.modules, install_fake_elevenlabs([b"new ", b"audio"])),
    ):
        result = asyncio.run(
            generate_executive_summary_audio(
                "# Exploitation Report\n\n## Executive Summary\n\nExample.",
                str(output_path),
            )
        )

    assert result is True
    assert output_path.read_bytes() == b"new audio"
    assert output_path.stat().st_mode & 0o777 == 0o640
    assert list(tmp_path.iterdir()) == [output_path]


def test_audio_generation_preserves_previous_file_when_stream_is_empty(tmp_path):
    output_path = tmp_path / "executive_summary.mp3"
    output_path.write_bytes(b"previous valid audio")

    with (
        patch.dict("os.environ", {"ELEVENLABS_API_KEY": "test-key"}),
        patch.dict(sys.modules, install_fake_elevenlabs([])),
    ):
        result = asyncio.run(
            generate_executive_summary_audio(
                "# Exploitation Report\n\n## Executive Summary\n\nExample.",
                str(output_path),
            )
        )

    assert result is False
    assert output_path.read_bytes() == b"previous valid audio"
    assert list(tmp_path.iterdir()) == [output_path]
