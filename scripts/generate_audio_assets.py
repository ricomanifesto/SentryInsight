"""One-time script to generate static podcast audio assets via Eleven Labs."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs.client import ElevenLabs

ASSETS_DIR = Path("assets/audio")
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

ASSETS = {
    "intro.mp3": {
        "text": "Dark electronic cybersecurity podcast intro jingle, synthesizer, tension building, tech atmosphere, professional, cinematic",
        "duration": 8.0,
    },
    "outro.mp3": {
        "text": "Cybersecurity podcast outro, synthesizer fade out, resolving tension, professional closing, ambient electronic",
        "duration": 6.0,
    },
    "transition.mp3": {
        "text": "Short digital transition whoosh, subtle tech beep, clean, futuristic interface sound",
        "duration": 2.0,
    },
    "alert.mp3": {
        "text": "Urgent cybersecurity alert tone, warning klaxon, digital alarm, tense, short sharp",
        "duration": 3.0,
    },
}


def generate_asset(filename: str, text: str, duration: float):
    path = ASSETS_DIR / filename
    print(f"Generating {filename} ({duration}s)...")

    audio = client.text_to_sound_effects.convert(
        text=text,
        duration_seconds=duration,
        output_format="mp3_44100_128",
    )

    with open(path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    size = os.path.getsize(path)
    print(f"  Saved {path} ({size / 1024:.0f} KB)")


if __name__ == "__main__":
    for filename, params in ASSETS.items():
        generate_asset(filename, params["text"], params["duration"])
    print("\nAll assets generated.")
