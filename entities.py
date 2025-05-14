import re
import string
from typing import List, Dict, Any, Optional, Set

def extract_entities(text: str) -> Dict[str, Any]:
    """
    Extract entities from text in a flexible, non-rule-based approach
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with extracted entities
    """
    # This function now delegates complex entity extraction to the AI analysis
    # We'll just do basic pattern matching for common items like CVEs
    result = {
        "cves": extract_cve_ids(text),
        "products": [],
        "organizations": [],
        "threat_actors": []
    }
    
    return result

def extract_cve_ids(text: str) -> List[str]:
    """Extract CVE IDs from text using a flexible pattern"""
    # Flexible pattern that can handle various CVE formats
    pattern = re.compile(r'CVE[-\s]?(\d{4})[-\s]?(\d{1,})', re.IGNORECASE)
    
    results = []
    for match in pattern.finditer(text):
        year = match.group(1)
        id_num = match.group(2)
        results.append(f"CVE-{year}-{id_num}")
    
    # Remove duplicates while preserving order
    seen = set()
    unique_results = []
    for item in results:
        if item not in seen:
            seen.add(item)
            unique_results.append(item)
    
    return unique_results

def extract_exploitation_details(text: str) -> Dict[str, Any]:
    """
    Extract exploitation details from text
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with exploitation details
    """
    # This function will now be minimal as we're using AI for detailed analysis
    # We'll just extract basic patterns that might be useful for filtering
    
    result = {
        "exploitation_status": "",
        "affected_systems": [],
        "attack_vectors": []
    }
    
    # Basic checks for exploitation patterns
    exploitation_patterns = [
        r'actively exploit(?:ed|ing)',
        r'in the wild',
        r'zero[\s-]day',
        r'0day',
        r'remote code execution',
        r'RCE',
        r'command injection',
        r'arbitrary code',
        r'privilege escalation',
        r'unauthenticated access',
        r'authentication bypass'
    ]
    
    for pattern in exploitation_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            result["exploitation_status"] = "Potentially Exploited"
            break
    
    return result

def extract_cvss_scores(text: str) -> List[Dict[str, Any]]:
    """Extract CVSS scores and versions from text"""
    # Enhanced pattern to catch more CVSS score references
    cvss_patterns = [
        # Standard pattern: "CVSS v3.1 score: 9.8"
        re.compile(r'CVSS\s+(?:v?(\d+\.\d+))?\s+(?:score:?|of|rating:?|base:?)\s+(\d+\.\d+)', re.IGNORECASE),
        
        # Alternative pattern: "scored 9.8 on the CVSS scale"
        re.compile(r'(?:scored|rating of|base score of)\s+(\d+\.\d+)(?:\s+(?:on|in)\s+the\s+CVSS)', re.IGNORECASE),
        
        # Simple pattern: just look for numbers that could be CVSS scores
        re.compile(r'(?:severity|criticality).*?(\d+\.\d+)\/10', re.IGNORECASE)
    ]
    
    scores = []
    
    # Try each pattern
    for pattern in cvss_patterns:
        for match in pattern.finditer(text):
            # If first pattern matched with version
            if len(match.groups()) > 1 and match.group(1) and match.group(1)[0].isdigit():
                version = match.group(1)
                score = float(match.group(2))
            # For other patterns
            else:
                # Find the decimal group
                for group in match.groups():
                    if group and '.' in group:
                        score = float(group)
                        version = "3.0"  # Default assumption
                        break
                else:
                    continue
            
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

def analyze_article_exploitation(article: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze an article to identify exploitation-related content
    
    Args:
        article: Article dictionary
        
    Returns:
        Dictionary with exploitation analysis
    """
    # Initialize result
    result = {
        "has_exploitation_content": False,
        "cves": [],
        "cvss_scores": [],
        "exploitation_details": {}
    }
    
    # Construct the text to analyze (combine title, summary, and content)
    text = article.get("title", "") + "\n" + article.get("summary", "")
    if "content" in article and article["content"]:
        text += "\n" + article["content"]
    
    # Extract CVEs
    cves = extract_cve_ids(text)
    result["cves"] = cves
    
    # Extract CVSS scores
    cvss_scores = extract_cvss_scores(text)
    result["cvss_scores"] = cvss_scores
    
    # Extract exploitation details
    exploitation_details = extract_exploitation_details(text)
    result["exploitation_details"] = exploitation_details
    
    # Key exploitation-related keywords
    exploitation_keywords = [
        "exploit", "vulnerability", "patch", "attack", "flaw", "zero-day", "0day", "CVE", 
        "threat", "malicious", "backdoor", "remote code execution", "RCE", "injection", 
        "arbitrary code", "authentication bypass", "auth bypass", "privilege escalation", 
        "vulnerabilities", "cybersecurity", "security update", "critical", "hacker", 
        "compromise", "breach", "fix", "updates", "CVSS", "security patch", "security fix",
        "vulnerability fixes", "security vulnerabilities", "arbitrary file", "unauthenticated",
        "fixes", "Patch Tuesday", "chained"
    ]
    
    # Check title and description for exploitation keywords
    exploitation_title = False
    
    title_lower = article.get("title", "").lower()
    for keyword in exploitation_keywords:
        if keyword.lower() in title_lower:
            exploitation_title = True
            break
    
    # If we have a title match, set has_exploitation_content to True
    if exploitation_title:
        result["has_exploitation_content"] = True
    
    # If we found CVEs, set has_exploitation_content to True
    if cves:
        result["has_exploitation_content"] = True
    
    # If we found CVSS scores, set has_exploitation_content to True
    if cvss_scores:
        result["has_exploitation_content"] = True
    
    # If we have exploitation status, set has_exploitation_content to True
    if exploitation_details.get("exploitation_status"):
        result["has_exploitation_content"] = True
    
    # If we have attack vectors, set has_exploitation_content to True
    if exploitation_details.get("attack_vectors"):
        result["has_exploitation_content"] = True
    
    # Check for zero-day mentions
    if "zero-day" in text.lower() or "0day" in text.lower() or "zero day" in text.lower():
        result["has_exploitation_content"] = True
    
    # Check for 'exploited' mentions
    if "exploit" in text.lower():
        result["has_exploitation_content"] = True
    
    return result
