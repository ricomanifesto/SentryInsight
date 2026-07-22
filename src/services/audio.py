import logging
import os
import re
import tempfile
from pathlib import Path

logger = logging.getLogger(__name__)

# Rachel - calm, professional female voice
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"


def extract_executive_summary(report_markdown: str) -> str:
    """Extract executive summary text from the exploitation report markdown."""
    section_summary = extract_named_executive_summary(report_markdown)
    if section_summary:
        return section_summary

    return extract_legacy_executive_summary(report_markdown)


def extract_named_executive_summary(report_markdown: str) -> str:
    """Extract paragraphs under the explicit Executive Summary section."""
    lines = report_markdown.split("\n")
    found_heading = False
    summary_lines = []

    for line in lines:
        stripped = line.strip()
        if re.match(r"^##\s+Executive Summary\s*$", stripped, re.IGNORECASE):
            found_heading = True
            continue
        if found_heading:
            if stripped.startswith("##"):
                break
            if stripped and stripped != "---":
                summary_lines.append(stripped)

    return " ".join(summary_lines)


def extract_legacy_executive_summary(report_markdown: str) -> str:
    """Extract the legacy first paragraph after the report heading."""
    lines = report_markdown.split("\n")
    found_heading = False
    summary_lines = []

    for line in lines:
        if re.match(r"^#\s+Exploitation Report", line):
            found_heading = True
            continue
        if found_heading:
            stripped = line.strip()
            if not stripped:
                if summary_lines:
                    break
                continue
            if stripped.startswith("#"):
                break
            summary_lines.append(stripped)

    return " ".join(summary_lines)


async def generate_executive_summary_audio(
    report_markdown: str, output_path: str
) -> bool:
    """Generate an MP3 narration of the executive summary using Eleven Labs TTS."""
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        logger.warning("ELEVENLABS_API_KEY not set — skipping audio generation")
        return False

    summary_text = extract_executive_summary(report_markdown)
    if not summary_text:
        logger.warning(
            "Could not extract executive summary from report — skipping audio generation"
        )
        return False

    logger.info(f"Generating audio for executive summary ({len(summary_text)} chars)")

    temporary_path: Path | None = None
    try:
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(api_key=api_key)
        audio = client.text_to_speech.convert(
            text=summary_text,
            voice_id=VOICE_ID,
            model_id=MODEL_ID,
            output_format=OUTPUT_FORMAT,
        )

        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        bytes_written = 0
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as f:
            temporary_path = Path(f.name)
            for chunk in audio:
                if chunk:
                    bytes_written += f.write(chunk)
            f.flush()
            os.fsync(f.fileno())

        if bytes_written == 0:
            raise ValueError("audio provider returned an empty stream")

        os.replace(temporary_path, destination)
        temporary_path = None

        logger.info(f"Audio saved to {output_path}")
        return True
    except Exception as e:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        logger.error(f"Error generating audio: {e}")
        return False
