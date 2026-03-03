# Exploitation Report

Critical zero-day exploitation activity continues to pose significant threats to organizations worldwide. APT28, a Russia-linked state-sponsored threat actor, has been actively exploiting CVE-2026-21513, an MSHTML zero-day vulnerability that was being leveraged before Microsoft's February 2026 Patch Tuesday. Additionally, the ClawJacked vulnerability in the popular AI agent OpenClaw has been patched but demonstrated how malicious websites could hijack locally running AI agents through WebSocket exploitation. North Korean threat actors have escalated their supply chain attacks by publishing 26 malicious npm packages with Pastebin command-and-control infrastructure, while Chrome extension compromises continue targeting cryptocurrency assets. These incidents highlight the growing sophistication of attacks targeting AI tools, browser extensions, and zero-day vulnerabilities.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A security flaw in Microsoft's MSHTML component that was exploited in the wild before being patched
- **Impact**: Allows threat actors to gain unauthorized access and execute malicious code through browser-based attacks
- **Status**: Patched by Microsoft in February 2026 Patch Tuesday, but was actively exploited before the fix
- **CVE ID**: CVE-2026-21513

### ClawJacked OpenClaw Vulnerability
- **Description**: High-severity vulnerability in the OpenClaw AI agent that allowed malicious websites to silently brute-force access to locally running instances
- **Impact**: Malicious websites could hijack local AI agents, steal sensitive data, and take control of OpenClaw functionality through WebSocket connections
- **Status**: Patched by OpenClaw developers

### Chrome Extension Privilege Escalation
- **Description**: Security flaw in Google Chrome's Gemini panel that permitted malicious extensions to escalate privileges
- **Impact**: Attackers could gain access to local files, violate user privacy during browsing, and access sensitive system resources
- **Status**: Patched by Google

### Compromised Chrome Extensions
- **Description**: Multiple Chrome extensions including QuickLens have been compromised to distribute malware and steal cryptocurrency
- **Impact**: Theft of cryptocurrency assets, credential harvesting, and malware distribution to thousands of users
- **Status**: Affected extensions removed from Chrome Web Store

## Affected Systems and Products

- **Microsoft MSHTML**: Legacy browser component vulnerable to zero-day exploitation
- **OpenClaw AI Agent**: Popular AI automation tool affected by WebSocket hijacking vulnerability
- **Google Chrome**: Browser affected by Gemini panel privilege escalation flaw
- **Chrome Extensions**: Various extensions compromised including QuickLens - Search Screen with Google Lens
- **npm Registry**: 26 malicious packages published targeting Node.js developers
- **Google Cloud API Keys**: Thousands exposed with unauthorized Gemini access capabilities
- **Fortinet Systems**: Previously breached in campaigns linked to CyberStrikeAI tool usage

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: APT28 leveraging unpatched MSHTML vulnerability before official disclosure
- **WebSocket Hijacking**: Malicious websites connecting to local AI agents through insecure WebSocket implementations
- **Supply Chain Attacks**: North Korean actors publishing malicious npm packages with hidden command-and-control infrastructure
- **Extension Compromise**: Hijacking legitimate Chrome extensions to distribute malware and steal cryptocurrency
- **Social Engineering**: Fake Google security sites using Progressive Web App (PWA) technology to steal credentials and MFA codes
- **AI Tool Weaponization**: CyberStrikeAI security testing platform being adopted by threat actors for offensive operations
- **Pastebin C2 Infrastructure**: Using Pastebin as command-and-control infrastructure for cross-platform remote access trojans

## Threat Actor Activities

- **APT28 (Fancy Bear)**: Russian state-sponsored group actively exploiting MSHTML zero-day vulnerability in targeted campaigns
- **APT37**: North Korean hackers deploying new malware tools to breach air-gapped networks and conduct covert surveillance through removable drives
- **North Korean Threat Actors**: Conducting Contagious Interview campaigns with 26 malicious npm packages hiding Pastebin command-and-control for cross-platform RATs
- **The Com Cybercriminal Collective**: Global law enforcement operation Project Compass resulted in 30 arrests and identification of nearly 180 members
- **Cryptocurrency Thieves**: Exploiting exposed wallet seeds and compromised browser extensions to steal millions in digital assets
- **Iranian Cyber Groups**: UK NCSC warning of heightened Iranian cyberattack risks amid Middle East conflict escalation