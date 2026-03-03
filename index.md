# Exploitation Report

Critical security incidents continue to emerge across multiple platforms, with notable zero-day exploitation and sophisticated attack campaigns targeting various systems. The most significant developments include APT28's exploitation of CVE-2026-21513, a zero-day MSHTML vulnerability that was actively exploited before Microsoft's February 2026 Patch Tuesday. Additionally, the ClawJacked vulnerability in OpenClaw AI agents and a Chrome privilege escalation flaw in the Gemini panel represent emerging threats in AI-powered systems. Threat actors are also leveraging compromised browser extensions, malicious npm packages, and sophisticated phishing campaigns using Progressive Web Applications to steal credentials and cryptocurrency.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A security flaw in Microsoft's MSHTML component that was exploited in the wild before being patched
- **Impact**: Allows threat actors to execute malicious code and compromise target systems
- **Status**: Patched in Microsoft's February 2026 Patch Tuesday, but was actively exploited beforehand
- **CVE ID**: CVE-2026-21513

### ClawJacked OpenClaw AI Agent Vulnerability
- **Description**: A high-severity vulnerability in the OpenClaw AI agent that allows malicious websites to connect to locally running AI agents via WebSocket connections
- **Impact**: Enables attackers to hijack AI agents, steal sensitive data, and perform unauthorized actions on local systems
- **Status**: Patched by OpenClaw developers after disclosure

### Chrome Gemini Panel Privilege Escalation
- **Description**: A security flaw in Google Chrome's Gemini AI panel that permits malicious extensions to escalate privileges
- **Impact**: Attackers can gain access to local files, escalate system privileges, and violate user privacy
- **Status**: Patched by Google Chrome security team

### QuickLens Chrome Extension Compromise
- **Description**: The "QuickLens - Search Screen with Google Lens" Chrome extension was compromised to deliver malware
- **Impact**: Cryptocurrency theft and deployment of ClickFix attack techniques targeting thousands of users
- **Status**: Extension removed from Chrome Web Store

## Affected Systems and Products

- **Microsoft MSHTML**: Legacy web browser engine component in Windows systems
- **OpenClaw AI Agent**: Popular artificial intelligence agent platform used by developers
- **Google Chrome**: Web browser with Gemini AI integration panel
- **Chrome Web Store Extensions**: Browser extension ecosystem, specifically QuickLens extension
- **npm Package Registry**: JavaScript package repository targeted with 26 malicious packages
- **Google Cloud API**: Cloud service keys with Gemini access exposed publicly
- **Fortinet Systems**: Referenced in context of CyberStrikeAI tool usage by threat actors

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: APT28 leveraging unpatched MSHTML vulnerability for targeted attacks
- **WebSocket Hijacking**: Malicious websites connecting to local AI agents through ClawJacked vulnerability
- **Progressive Web Application (PWA) Phishing**: Fake Google Security sites deploying credential-stealing applications
- **Supply Chain Attacks**: Malicious npm packages in the Contagious Interview campaign
- **Browser Extension Compromise**: Hijacking legitimate extensions to steal cryptocurrency and deploy malware
- **API Key Abuse**: Exploitation of exposed Google Cloud API keys for unauthorized Gemini access
- **ClickFix Attacks**: Social engineering techniques combined with malware delivery
- **AI-Powered Attack Tools**: CyberStrikeAI platform adoption by cybercriminals

## Threat Actor Activities

- **APT28 (Russia-linked)**: Actively exploiting CVE-2026-21513 MSHTML zero-day vulnerability in targeted campaigns
- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks and conduct surveillance operations
- **North Korean Hackers**: Publishing 26 malicious npm packages hiding Pastebin C2 infrastructure for cross-platform RAT deployment
- **The Com Cybercrime Collective**: 30 members arrested and 179 suspects identified in Europol's Project Compass operation targeting children and teenagers
- **Iranian Cyber Groups**: UK warns of heightened cyberattack risks amid Middle East conflict tensions
- **CyberStrikeAI Users**: Threat actors adopting open-source AI security testing platform for malicious campaigns