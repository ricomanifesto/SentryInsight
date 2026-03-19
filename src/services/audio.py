import logging
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import formatdate
from pathlib import Path
from time import mktime

logger = logging.getLogger(__name__)

# Rachel - calm, professional female voice
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"

PODCAST_BASE_URL = "https://ricomanifesto.github.io/SentryInsight"
MAX_FEED_EPISODES = 20


def extract_executive_summary(report_markdown: str) -> str:
    """Extract the executive summary paragraph from the exploitation report markdown."""
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


def extract_threat_actor_section(report_markdown: str) -> str:
    """Extract the Threat Actor Activities section from the report markdown."""
    lines = report_markdown.split("\n")
    found_heading = False
    section_lines = []

    for line in lines:
        if re.match(r"^##\s+Threat Actor Activities", line):
            found_heading = True
            continue
        if found_heading:
            if re.match(r"^##\s+", line):
                break
            section_lines.append(line)

    return "\n".join(section_lines).strip()


async def generate_podcast_script(threat_actor_text: str, config: dict, full_report: str = "") -> str:
    """Use Claude to generate an insightful podcast script from threat actor intelligence.

    Takes the threat actor section for focus, plus the full report for context
    on vulnerabilities, attack vectors, and affected systems.
    """
    from langchain_anthropic import ChatAnthropic
    from langchain_core.messages import HumanMessage, SystemMessage

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error("ANTHROPIC_API_KEY not set — cannot generate podcast script")
        return ""

    model_name = config.get("analysis", {}).get("model", "claude-sonnet-4-20250514")
    model = ChatAnthropic(api_key=api_key, model=model_name, max_tokens=4000)

    today = datetime.now().strftime("%B %d, %Y")

    messages = [
        SystemMessage(content="You are a seasoned cybersecurity analyst and podcast host. You go beyond surface-level reporting to deliver strategic insight, connecting dots between threat actors, vulnerabilities, and real-world impact. Your audience is security professionals who already read the headlines — they listen to you for the analysis they can't get elsewhere."),
        HumanMessage(content=f"""Create an insightful podcast episode script focused on threat actor activity. This should be a 3-4 minute briefing that goes DEEPER than the bullet points — your audience can already read those.

FOCUS SECTION — Threat Actor Activities:

{threat_actor_text}

FULL REPORT CONTEXT (use this to enrich your analysis):

{full_report}

Script requirements:
- Open with: "Welcome to the SentryInsight Threat Actor Briefing for {today}."
- Do NOT just restate the bullet points. Instead, provide ANALYSIS:
  * Why does each threat actor matter strategically? What's the bigger picture?
  * Are there connections between actors or campaigns? Common attack vectors or targets?
  * What patterns or trends should defenders pay attention to?
  * What concrete actions should security teams take this week?
- Connect threat actors to the specific vulnerabilities and attack vectors from the full report when relevant
- Group related actors or themes together rather than covering each one in isolation
- End with 2-3 key takeaways and a sign-off: "That's your threat actor briefing for today. Stay vigilant, and we'll see you next time."
- Do NOT use markdown formatting, bullet points, asterisks, or special characters — this will be read aloud by a text-to-speech engine
- Write in plain spoken English with natural pauses and transitions
- Be direct and opinionated — take a position on what matters most""")
    ]

    try:
        response = await model.ainvoke(messages)
        script = response.content
        logger.info(f"Generated podcast script ({len(script)} chars)")
        return script
    except Exception as e:
        logger.error(f"Error generating podcast script: {e}")
        return ""


def generate_podcast_audio(script: str, output_path: str) -> bool:
    """Generate podcast MP3 from a script using Eleven Labs TTS."""
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        logger.warning("ELEVENLABS_API_KEY not set — skipping podcast audio generation")
        return False

    logger.info(f"Generating podcast audio ({len(script)} chars)")

    try:
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(api_key=api_key)
        audio = client.text_to_speech.convert(
            text=script,
            voice_id=VOICE_ID,
            model_id=MODEL_ID,
            output_format=OUTPUT_FORMAT,
        )

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        logger.info(f"Podcast audio saved to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error generating podcast audio: {e}")
        return False


def generate_podcast_feed(episode_mp3_path: str, episode_date: str, summary: str) -> bool:
    """Generate or update the podcast.xml RSS feed."""
    feed_path = "podcast.xml"
    mp3_filename = Path(episode_mp3_path).name
    episode_url = f"{PODCAST_BASE_URL}/podcast/{mp3_filename}"
    mp3_size = os.path.getsize(episode_mp3_path)
    # Estimate duration from file size and 128kbps bitrate
    duration_seconds = int((mp3_size * 8) / (128 * 1000))
    duration_str = f"{duration_seconds // 60}:{duration_seconds % 60:02d}"
    mp3_size = str(mp3_size)
    pub_date = formatdate(mktime(datetime.strptime(episode_date, "%Y-%m-%d").timetuple()), usegmt=True)

    # Parse existing feed to preserve prior episodes
    existing_items = []
    if os.path.exists(feed_path):
        try:
            tree = ET.parse(feed_path)
            channel = tree.find("channel")
            if channel is not None:
                for item in channel.findall("item"):
                    existing_items.append(item)
        except Exception:
            logger.warning("Could not parse existing podcast.xml — creating fresh feed")

    # Build the feed
    ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
    ET.register_namespace("itunes", ITUNES_NS)

    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "SentryInsight Threat Actor Briefing"
    ET.SubElement(channel, "link").text = PODCAST_BASE_URL
    ET.SubElement(channel, "description").text = "Daily cybersecurity threat actor intelligence briefings powered by SentryInsight. Stay informed about the latest threat groups, campaigns, and adversary activities."
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(channel, f"{{{ITUNES_NS}}}author").text = "SentryInsight"
    ET.SubElement(channel, f"{{{ITUNES_NS}}}summary").text = "Automated threat actor intelligence briefings from SentryInsight."
    image = ET.SubElement(channel, f"{{{ITUNES_NS}}}image")
    image.set("href", f"{PODCAST_BASE_URL}/assets/podcast-cover.png")
    category = ET.SubElement(channel, f"{{{ITUNES_NS}}}category")
    category.set("text", "Technology")
    ET.SubElement(channel, f"{{{ITUNES_NS}}}explicit").text = "no"
    ET.SubElement(channel, f"{{{ITUNES_NS}}}type").text = "episodic"
    owner = ET.SubElement(channel, f"{{{ITUNES_NS}}}owner")
    ET.SubElement(owner, f"{{{ITUNES_NS}}}name").text = "SentryInsight"
    ET.SubElement(owner, f"{{{ITUNES_NS}}}email").text = "thericox2@gmail.com"

    # New episode
    new_item = ET.SubElement(channel, "item")
    ET.SubElement(new_item, "title").text = f"Threat Actor Briefing — {episode_date}"
    ET.SubElement(new_item, "description").text = summary
    ET.SubElement(new_item, "pubDate").text = pub_date
    ET.SubElement(new_item, "guid").text = episode_url
    ET.SubElement(new_item, f"{{{ITUNES_NS}}}duration").text = duration_str
    ET.SubElement(new_item, f"{{{ITUNES_NS}}}episodeType").text = "full"
    enclosure = ET.SubElement(new_item, "enclosure")
    enclosure.set("url", episode_url)
    enclosure.set("length", mp3_size)
    enclosure.set("type", "audio/mpeg")

    # Re-add prior episodes (skip duplicates for same date), limit to MAX_FEED_EPISODES
    count = 1
    for item in existing_items:
        guid = item.find("guid")
        if guid is not None and guid.text == episode_url:
            continue
        if count >= MAX_FEED_EPISODES:
            break
        channel.append(item)
        count += 1

    try:
        ET.indent(rss, space="  ")
        tree = ET.ElementTree(rss)
        tree.write(feed_path, encoding="unicode", xml_declaration=True)
        logger.info(f"Podcast feed updated at {feed_path} ({count} episodes)")
        return True
    except Exception as e:
        logger.error(f"Error writing podcast feed: {e}")
        return False


async def generate_executive_summary_audio(report_markdown: str, output_path: str) -> bool:
    """Generate an MP3 narration of the executive summary using Eleven Labs TTS."""
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
