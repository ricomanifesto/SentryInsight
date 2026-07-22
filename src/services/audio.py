import logging
import os
import re
import stat
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
        try:
            destination_mode = stat.S_IMODE(destination.stat().st_mode)
        except FileNotFoundError:
            destination_mode = None

        with tempfile.TemporaryDirectory(
            dir=destination.parent,
            prefix=f".{destination.name}.",
        ) as temporary_directory:
            temporary_path = Path(temporary_directory) / destination.name
            bytes_written = 0
            with temporary_path.open("xb") as f:
                for chunk in audio:
                    if chunk:
                        bytes_written += f.write(chunk)
                f.flush()
                os.fsync(f.fileno())

            if bytes_written == 0:
                raise ValueError("audio provider returned an empty stream")

            if destination_mode is not None:
                os.chmod(temporary_path, destination_mode)
            os.replace(temporary_path, destination)

        logger.info(f"Audio saved to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error generating audio: {e}")
        return False
