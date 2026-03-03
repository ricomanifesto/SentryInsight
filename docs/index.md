# Exploitation Report

The current threat landscape shows significant exploitation activity across multiple attack vectors, with particular concern around AI-powered attacks and zero-day vulnerabilities. Most notably, threat actors are leveraging AI tools like CyberStrikeAI for enhanced attack capabilities, while exploiting critical vulnerabilities in popular platforms including Google Chrome's Gemini panel and the OpenClaw AI agent framework. State-sponsored groups, particularly APT28 and North Korean actors, continue active exploitation campaigns targeting both traditional systems and emerging AI technologies. The emergence of sophisticated phishing campaigns using Progressive Web Applications (PWAs) and the compromise of browser extensions demonstrate evolving attack methodologies that bypass traditional security measures.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A security flaw in Microsoft's MSHTML component that was exploited as a zero-day before being patched in February 2026
- **Impact**: Allows attackers to execute arbitrary code and compromise target systems
- **Status**: Patched by Microsoft in February 2026 Patch Tuesday, but was actively exploited before disclosure
- **CVE ID**: CVE-2026-21513

### Chrome Gemini Panel Privilege Escalation
- **Description**: A vulnerability in Google Chrome's Gemini AI panel that allows malicious extensions to escalate privileges
- **Impact**: Enables attackers to gain access to local files on the system and escalate privileges beyond normal extension boundaries
- **Status**: Now patched by Google

### OpenClaw ClawJacked Vulnerability
- **Description**: A high-severity flaw dubbed "ClawJacked" in the OpenClaw AI agent that allows malicious websites to hijack local AI agents via WebSocket connections
- **Impact**: Permits unauthorized access to locally running AI agents, enabling data theft and system compromise through brute-force attacks
- **Status**: Fixed by OpenClaw developers

### Google Cloud API Key Exposure
- **Description**: Thousands of publicly exposed Google Cloud API keys that provide unauthorized access to Gemini endpoints
- **Impact**: Allows attackers to access private data and authenticate to sensitive Gemini API endpoints
- **Status**: Ongoing exposure identified through research

## Affected Systems and Products

- **Google Chrome**: Gemini AI panel vulnerability affecting privilege escalation mechanisms
- **Microsoft MSHTML**: Component exploited by state-sponsored actors before patching
- **OpenClaw AI Agent**: WebSocket vulnerability allowing remote hijacking of local instances
- **Google Cloud Platform**: API keys providing unauthorized Gemini access across thousands of projects
- **Chrome Extensions**: QuickLens extension compromised to deliver cryptocurrency theft malware
- **NPM Package Registry**: 26 malicious packages published by North Korean actors for cross-platform RAT deployment
- **Fortinet Systems**: Targeted in campaigns using CyberStrikeAI for reconnaissance and exploitation
- **Progressive Web Applications**: Fake Google security sites deploying credential harvesting PWAs

## Attack Vectors and Techniques

- **AI-Powered Attacks**: CyberStrikeAI tool adoption by threat actors for enhanced reconnaissance and exploitation capabilities
- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities before public disclosure and fixes
- **WebSocket Hijacking**: Malicious websites connecting to local AI agents through unprotected WebSocket interfaces
- **Extension Compromise**: Legitimate browser extensions modified to deliver malware and steal cryptocurrency
- **Supply Chain Attacks**: Malicious NPM packages hiding command and control infrastructure using Pastebin
- **PWA-Based Phishing**: Progressive Web Applications mimicking legitimate Google services to harvest credentials and MFA codes
- **ClickFix Attacks**: Social engineering techniques combined with malicious browser extensions
- **API Key Abuse**: Exploitation of exposed cloud API keys for unauthorized service access

## Threat Actor Activities

- **APT28 (Russia-linked)**: Actively exploiting CVE-2026-21513 MSHTML zero-day vulnerability in targeted campaigns against high-value targets
- **North Korean Actors**: Publishing 26 malicious NPM packages as part of the ongoing "Contagious Interview" campaign, using Pastebin for C2 communications
- **APT37 (North Korean)**: Deploying new malware tools specifically designed to breach air-gapped networks and conduct surveillance operations
- **The Com Cybercrime Collective**: 30 members arrested in Project Compass operation, with 179 total suspects identified targeting children and teenagers
- **Kimwolf Botnet Operators**: Continued operation of one of the world's largest botnets following vulnerability disclosure
- **Cryptocurrency Thieves**: Exploiting browser extension compromises and exposed wallet seeds to steal millions in digital assets