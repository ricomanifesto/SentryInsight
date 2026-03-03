# Exploitation Report

Current cybersecurity landscape reveals critical active exploitation across multiple platforms, with notable zero-day vulnerabilities in Android and Windows systems being actively exploited by sophisticated threat actors. The most concerning activity includes CVE-2026-21385, a Qualcomm display component vulnerability affecting Android devices, and CVE-2026-21513, an MSHTML zero-day linked to Russian state-sponsored APT28 operations. Additionally, threat actors are leveraging AI-powered tools like CyberStrikeAI for automated attacks against Fortinet FortiGate appliances across 55 countries, while advanced phishing campaigns employ OAuth redirect mechanisms and reverse proxy techniques to bypass multi-factor authentication protections.

## Active Exploitation Details

### Qualcomm Android Display Component Vulnerability
- **Description**: High-severity security flaw in an open-source Qualcomm component used in Android devices' display functionality
- **Impact**: Attackers can exploit this vulnerability to gain elevated privileges on affected Android devices
- **Status**: Actively exploited in the wild; patches released by Google in Android security updates addressing 129 total vulnerabilities
- **CVE ID**: CVE-2026-21385

### Microsoft MSHTML Zero-Day
- **Description**: Security vulnerability in Microsoft's MSHTML component that was exploited before the February 2026 Patch Tuesday
- **Impact**: Enables threat actors to execute malicious code and compromise Windows systems
- **Status**: Actively exploited by APT28; patched by Microsoft in recent security updates
- **CVE ID**: CVE-2026-21513

### Chrome Extension Privilege Escalation
- **Description**: Security flaw in Google Chrome that allowed malicious extensions to escalate privileges through the Gemini panel
- **Impact**: Attackers could gain access to local files and escalate system privileges
- **Status**: Now patched by Google, but was exploitable through malicious Chrome extensions

### AI-Powered FortiGate Attacks
- **Description**: Automated attacks targeting Fortinet FortiGate appliances using the CyberStrikeAI open-source security testing platform
- **Impact**: Compromise of network security appliances across multiple countries
- **Status**: Active campaign affecting organizations in 55 countries

## Affected Systems and Products

- **Android Devices**: Devices using Qualcomm display components vulnerable to privilege escalation attacks
- **Microsoft Windows**: Systems running MSHTML component targeted by APT28 operations
- **Google Chrome**: Browsers with malicious extensions capable of privilege escalation via Gemini panel
- **Fortinet FortiGate**: Network security appliances targeted by AI-automated attacks across 55 countries
- **cPanel Systems**: Website management panels being sold in underground markets for phishing infrastructure
- **AWS Data Centers**: Infrastructure in UAE and Bahrain damaged by drone strikes causing service outages

## Attack Vectors and Techniques

- **OAuth Redirect Abuse**: Phishing campaigns leveraging OAuth URL redirection to bypass email and browser security defenses
- **AitM Reverse Proxy**: Starkiller phishing suite using Adversary-in-the-Middle techniques to bypass multi-factor authentication
- **AI-Automated Exploitation**: CyberStrikeAI platform enabling automated vulnerability discovery and exploitation
- **PWA-Based Phishing**: Progressive Web Apps deployed via fake Google Security sites to steal credentials and MFA codes
- **Dual Malware Chains**: SloppyLemming threat group using sophisticated multi-stage infection processes
- **cPanel Credential Abuse**: Compromised site management panels sold as plug-and-play phishing infrastructure

## Threat Actor Activities

- **APT28 (Fancy Bear)**: Russian state-sponsored group exploiting MSHTML zero-day vulnerability in targeted operations
- **SloppyLemming**: Threat cluster targeting government entities and critical infrastructure in Pakistan and Bangladesh using dual malware delivery chains
- **Pro-Iranian Actors**: Multiple groups launching cyberattack campaigns in retaliation for US-Israeli military actions, targeting economic and infrastructure disruption
- **Cybercriminal Collective "The Com"**: Nearly 180 members identified with 30 arrested in global Project Compass law enforcement operation
- **Underground Markets**: Active trading of compromised cPanel credentials and site management panels for phishing operations