import re
from typing import List, Dict, Any, Optional

def extract_cve_ids(text: str) -> List[str]:
    """Extract CVE IDs from text"""
    cve_pattern = re.compile(r'CVE-\d{4}-\d{4,7}', re.IGNORECASE)
    return [match.upper() for match in cve_pattern.findall(text)]

def extract_cvss_scores(text: str) -> List[Dict[str, Any]]:
    """Extract CVSS scores and versions from text"""
    # Look for CVSS score patterns like "CVSS score of 9.8" or "CVSS v3.1 score: 9.8"
    cvss_pattern = re.compile(r'CVSS\s+(?:v?(\d+\.\d+))?\s+(?:score:?|of)\s+(\d+\.\d+)', re.IGNORECASE)
    scores = []
    
    for match in cvss_pattern.finditer(text):
        version = match.group(1) if match.group(1) else "3.0"  # Default to 3.0 if not specified
        score = float(match.group(2))
        
        # Determine severity based on CVSS score
        severity = "Unknown"
        if score >= 9.0:
            severity = "Critical"
        elif score >= 7.0:
            severity = "High"
        elif score >= 4.0:
            severity = "Medium"
        elif score > 0.0:
            severity = "Low"
        
        scores.append({
            "score": score,
            "version": version,
            "severity": severity
        })
    
    return scores

def extract_exploit_details(text: str) -> Dict[str, Any]:
    """Extract exploitation details from text"""
    # Look for exploitation status
    status_patterns = {
        "exploited": re.compile(r'(actively\s+exploit|being\s+exploit|in\s+the\s+wild|exploit\s+observed)', re.IGNORECASE),
        "available": re.compile(r'(exploit\s+available|proof\s+of\s+concept|poc\s+available)', re.IGNORECASE),
        "potential": re.compile(r'(potentially\s+exploitable|possible\s+exploit|might\s+be\s+exploit)', re.IGNORECASE)
    }
    
    # Extract affected systems/software
    affected_pattern = re.compile(r'affects?\s+([\w\s\-\.\,\&\/]+?)(?:version|v\.|\d|\.)', re.IGNORECASE)
    
    # Extract attack vectors
    vector_pattern = re.compile(r'(remote code execution|rce|command injection|sql injection|xss|cross-site scripting|buffer overflow|privilege escalation)', re.IGNORECASE)
    
    results = {
        "exploitation_status": None,
        "affected_systems": [],
        "attack_vectors": []
    }
    
    # Check for exploitation status
    for status, pattern in status_patterns.items():
        if pattern.search(text):
            results["exploitation_status"] = status
            break
    
    # Extract affected systems
    affected_matches = affected_pattern.findall(text)
    results["affected_systems"] = [match.strip() for match in affected_matches if match.strip()]
    
    # Extract attack vectors
    vector_matches = vector_pattern.findall(text)
    results["attack_vectors"] = [match.strip() for match in vector_matches if match.strip()]
    
    return results

def analyze_article_exploitation(article: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze a single article for exploitation-related content
    
    Args:
        article: Article dictionary with title, description, and content
        
    Returns:
        Dictionary with extracted information about CVEs, CVSS scores, and exploitation details
    """
    # Combine title, summary and content for analysis
    text = f"{article.get('title', '')} {article.get('summary', '')} {article.get('content', '')}"
    
    # Extract entities
    cves = extract_cve_ids(text)
    cvss_scores = extract_cvss_scores(text)
    exploit_details = extract_exploit_details(text)
    
    return {
        "cves": cves,
        "cvss_scores": cvss_scores,
        "exploitation_details": exploit_details,
        "has_exploitation_content": bool(cves) or bool(cvss_scores) or exploit_details["exploitation_status"] is not None
    }
