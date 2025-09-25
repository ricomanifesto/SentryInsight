import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional


def extract_threat_actors_from_markdown(md: str) -> List[str]:
    """
    Extract likely threat actor names from the exploitation report markdown.
    Heuristics focus on the "Threat Actor Activities" section and common naming patterns.
    """
    actors: List[str] = []

    # Narrow scope to the Threat Actor Activities section if present
    section_re = re.compile(r"^##\s+Threat Actor Activities\s*$", re.IGNORECASE | re.MULTILINE)
    m = section_re.search(md)
    section_text = md
    if m:
        start = m.end()
        # find next H2
        next_h2 = re.search(r"^##\s+", md[start:], re.MULTILINE)
        section_text = md[start: start + next_h2.start()] if next_h2 else md[start:]

    # Patterns for common actor naming styles
    patterns = [
        re.compile(r"\b(?:APT|TA|UNC|FIN)[ -]?\d{1,4}\b", re.IGNORECASE),
        # Quoted codenames, e.g., “LapDogs”, "Sandworm"
        re.compile(r"[\"“”']([A-Z][A-Za-z0-9][A-Za-z0-9\-\s]{1,40})[\"“”']"),
    ]

    # Also capture explicit Actor/Group lines the template suggests
    for line in section_text.splitlines():
        line = line.strip()
        if not line:
            continue
        # - **Actor/Group**: NAME ...
        m_ag = re.search(r"\*\*Actor/Group\*\*:\s*([^\n\r]+)$", line, re.IGNORECASE)
        if m_ag:
            name = m_ag.group(1).strip()
            # cut after two spaces if more content follows
            name = name.split("  ")[0].strip()
            if name:
                actors.append(name)
                continue
        # - **Bolded Name** (common list style in Threat Actor Activities)
        m_bold = re.search(r"^-\s*\*\*([^*]+)\*\*", line)
        if m_bold:
            raw = m_bold.group(1).strip()
            # Remove trailing parenthetical, e.g., "LapDogs (China-linked)" -> "LapDogs"
            raw = re.sub(r"\s*\(.*\)$", "", raw).strip()
            # Sometimes multiple names are joined with '&'
            parts = [p.strip() for p in re.split(r"\s*&\s*", raw) if p.strip()]
            # Exclude label-like bold markers such as Campaign, Description, etc.
            label_exclusions = {"campaign", "campaigns", "description", "impact", "status", "cve id", "cve", "platform", "product/system name"}
            parts = [p for p in parts if p.lower() not in label_exclusions]
            actors.extend(parts)
            # proceed to next line
            continue
        for pat in patterns:
            for mm in pat.finditer(line):
                # group 1 for quoted names, else full match
                name = (mm.group(1) if mm.groups() else mm.group(0)).strip()
                # Normalize common prefixes to standard form (e.g., APT29)
                name = re.sub(r"\b(apt|ta|unc|fin)[\s-]?(\d{1,4})\b", lambda x: x.group(1).upper() + x.group(2), name, flags=re.IGNORECASE)
                actors.append(name)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for a in actors:
        if a not in seen:
            seen.add(a)
            unique.append(a)
    # Also scan the entire document for tags like APT/TA/UNC/FIN if the section misses some
    addl = []
    for mm in re.finditer(r"\b(?:APT|TA|UNC|FIN)[ -]?\d{1,4}\b", md, flags=re.IGNORECASE):
        addl.append(mm.group(0).upper().replace(' ', '').replace('-', ''))
    for a in addl:
        if a not in seen:
            seen.add(a)
            unique.append(a)
    return unique


def _vt_request(url: str, api_key: str) -> Optional[dict]:
    try:
        req = urllib.request.Request(url)
        req.add_header("x-apikey", api_key)
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status != 200:
                return None
            return json.loads(resp.read().decode("utf-8", errors="ignore"))
    except Exception:
        return None


def resolve_actor_to_vt_collection_id(actor: str, api_key: Optional[str]) -> Optional[str]:
    """
    Resolve an actor to a VirusTotal collection id using the /collections endpoint
    with filter collection_type:threat-actor. Requires Google TI privileges.
    """
    if not api_key:
        api_key = _get_vt_key_from_env_or_config()
        if not api_key:
            return None

    base = "https://www.virustotal.com/api/v3/collections?filter="
    filters = [
        f"collection_type:threat-actor name:\"{actor}\"",
        f"collection_type:threat-actor {actor}",  # open search term
    ]
    tried = set()
    for f in filters:
        url = base + urllib.parse.quote(f, safe="") + "&order=relevance-"
        data = _vt_request(url, api_key)
        if not data or "data" not in data:
            continue
        for item in data.get("data", []) or []:
            # Expect id like 'threat-actor--UUID'
            cid = item.get("id") or ""
            attrs = item.get("attributes", {}) or {}
            ctype = attrs.get("collection_type") or ""
            if isinstance(cid, str) and cid.startswith("threat-actor--"):
                return cid
            if isinstance(ctype, str) and ctype == "threat-actor" and isinstance(cid, str) and cid:
                return cid
        tried.add(f)
    # Try alias if available
    alias = _resolve_alias(actor)
    if alias and alias != actor:
        for f in [
            f"collection_type:threat-actor name:\"{alias}\"",
            f"collection_type:threat-actor {alias}",
        ]:
            if f in tried:
                continue
            url = base + urllib.parse.quote(f, safe="") + "&order=relevance-"
            data = _vt_request(url, api_key)
            if not data or "data" not in data:
                continue
            for item in data.get("data", []) or []:
                cid = item.get("id") or ""
                attrs = item.get("attributes", {}) or {}
                ctype = attrs.get("collection_type") or ""
                if isinstance(cid, str) and cid.startswith("threat-actor--"):
                    return cid
                if isinstance(ctype, str) and ctype == "threat-actor" and isinstance(cid, str) and cid:
                    return cid
    return None


def resolve_actor_to_vt_url(actor: str, api_key: Optional[str]) -> str:
    """
    Resolve an actor name to a stable VirusTotal GUI URL. Prefer direct collection link,
    otherwise link to a GUI search for the actor collections.
    """
    cid = resolve_actor_to_vt_collection_id(actor, api_key)
    if cid:
        return f"https://www.virustotal.com/gui/collection/{cid}"
    # Fallback: link to collections filtered for threat-actor by name in GUI search
    # If alias exists, prefer searching the alias name
    alias = _resolve_alias(actor)
    search_name = alias or actor
    q = urllib.parse.quote(f'collection_type:threat-actor name:"{search_name}"', safe="")
    return f"https://www.virustotal.com/gui/search/{q}"


def build_actors_mapping(md: str, api_key: Optional[str]) -> Dict[str, str]:
    names = extract_threat_actors_from_markdown(md)
    # Filter out generic or non-actor aggregates
    drop_terms = re.compile(r"\b(unattributed|cluster|clusters|campaigns?)\b", re.IGNORECASE)
    mapping: Dict[str, str] = {}
    for n in names:
        if drop_terms.search(n):
            continue
        try:
            mapping[n] = resolve_actor_to_vt_url(n, api_key)
        except Exception:
            # Ensure we still provide a usable search link on unexpected errors
            q = urllib.parse.quote(f'collection_type:threat-actor name:"{n}"', safe="")
            mapping[n] = f"https://www.virustotal.com/gui/search/{q}"
    return mapping


def write_actors_json(mapping: Dict[str, str], out_dir: Path) -> None:
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "actors.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)
    except Exception:
        # Non-fatal; UI will fall back to zero-actors state
        pass
def _load_aliases() -> Dict[str, str]:
    """Load optional actor aliases from config/actors_aliases.json and merge with built-ins."""
    builtins = {
        # Common mappings seen in industry reporting
        "UNC2165": "Scattered Spider",
        "OCTO TEMPEST": "Scattered Spider",
        "LAPSUS$": "Lapsus$",
        "COZY BEAR": "APT29",
        "NOBELIUM": "APT29",
        "CLOP": "TA505",  # often associated; keep if helpful
    }
    path = Path('config') / 'actors_aliases.json'
    try:
        if path.exists():
            data = json.loads(path.read_text(encoding='utf-8'))
            for k, v in (data or {}).items():
                if isinstance(k, str) and isinstance(v, str) and k.strip() and v.strip():
                    builtins[k.strip().upper()] = v.strip()
    except Exception:
        pass
    return builtins


ALIASES = _load_aliases()


def _resolve_alias(name: str) -> Optional[str]:
    if not name:
        return None
    return ALIASES.get(name.strip().upper())


def _get_vt_key_from_env_or_config() -> Optional[str]:
    # Check common env var names
    for var in ("VT_API_KEY", "VIRUSTOTAL_API_KEY", "VT_INTELLIGENCE_API_KEY", "GOOGLE_TI_API_KEY"):
        val = os.getenv(var)
        if val:
            return val
    # Fallback to config/config.json
    try:
        cfg = json.loads((Path('config')/ 'config.json').read_text(encoding='utf-8'))
        vt = (cfg.get('virustotal') or {}).get('api_key')
        if vt:
            return vt
    except Exception:
        pass
    return None
