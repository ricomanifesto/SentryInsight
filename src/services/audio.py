import logging
import os
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# Rachel - calm, professional female voice
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"


def extract_executive_summary(report_markdown: str) -> str:
    """Extract the executive summary paragraph from the exploitation report markdown.

    The executive summary is the first paragraph after the '# Exploitation Report' heading.
    """
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


async def generate_executive_summary_audio(report_markdown: str, output_path: str) -> bool:
    """Generate an MP3 narration of the executive summary using Eleven Labs TTS.

    Returns True on success, False on failure. Failures are logged but do not raise.
    """
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        logger.warning("ELEVENLABS_API_KEY not set — skipping audio generation")
        return False

    summary_text = extract_executive_summary(report_markdown)
    if not summary_text:
        logger.warning("Could not extract executive summary from report — skipping audio generation")
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

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        logger.info(f"Audio saved to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error generating audio: {e}")
        return False
