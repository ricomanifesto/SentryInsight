# Exploitation Report

Critical security vulnerabilities are currently under active exploitation across multiple platforms, with several high-impact threats targeting AI tools, browser extensions, and enterprise systems. The most significant concerns include CVE-2026-21513, an MSHTML zero-day vulnerability exploited by APT28 before Microsoft's February patch, and a high-severity ClawJacked vulnerability in the OpenClaw AI agent that allows malicious websites to hijack local AI instances. Additionally, the CyberStrikeAI platform has been weaponized by threat actors for AI-powered attacks, while malicious Chrome extensions and phishing campaigns are actively targeting cryptocurrency assets and user credentials. North Korean threat actors continue their sophisticated campaigns with new malware targeting air-gapped networks and supply chain attacks through compromised npm packages.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A critical security flaw in Microsoft's MSHTML engine that was exploited before Microsoft's February 2026 Patch Tuesday
- **Impact**: Allows attackers to gain unauthorized access and execute malicious code on targeted systems
- **Status**: Recently patched by Microsoft, but was actively exploited in the wild
- **CVE ID**: CVE-2026-21513

### ClawJacked OpenClaw Vulnerability
- **Description**: High-severity vulnerability in the OpenClaw AI agent that allows malicious websites to connect to locally running AI instances via WebSocket brute-force attacks
- **Impact**: Enables attackers to hijack local AI agents, steal sensitive data, and take over AI operations
- **Status**: Now patched but was actively exploited by malicious websites

### Chrome Gemini Panel Privilege Escalation
- **Description**: Security flaw in Google Chrome's Gemini AI panel that permits malicious extensions to escalate privileges
- **Impact**: Attackers can escalate privileges, access local files, violate user privacy during browsing, and access sensitive resources
- **Status**: Now patched by Google

### QuickLens Chrome Extension Compromise
- **Description**: The "QuickLens - Search Screen with Google Lens" Chrome extension was compromised to deliver malware
- **Impact**: Steals cryptocurrency from users and demonstrates ClickFix attack techniques
- **Status**: Extension removed from Chrome Web Store after compromise

## Affected Systems and Products

- **OpenClaw AI Agent**: Local AI instances vulnerable to WebSocket-based hijacking attacks
- **Google Chrome**: Gemini AI panel and extension system affected by privilege escalation vulnerabilities
- **Microsoft MSHTML Engine**: Windows systems running vulnerable MSHTML components
- **Chrome Extensions**: QuickLens and potentially other extensions compromised for cryptocurrency theft
- **Google Cloud API Keys**: Thousands exposed with unauthorized Gemini access capabilities
- **npm Registry**: 26 malicious packages published targeting cross-platform systems
- **Air-Gapped Networks**: Targeted by new North Korean malware using removable drives
- **Fortinet Systems**: Hundreds breached in campaigns utilizing CyberStrikeAI tools
- **Samsung Smart TVs**: Data collection practices affecting Texas residents

## Attack Vectors and Techniques

- **WebSocket Brute-Force**: Malicious websites attempting to connect to local AI agents through port scanning and connection attempts
- **AI-Powered Security Testing**: CyberStrikeAI platform weaponized for automated vulnerability discovery and exploitation
- **Extension Compromise**: Browser extensions hijacked to steal cryptocurrency and deploy malware
- **Supply Chain Attacks**: Malicious npm packages distributed in fake job interview campaigns
- **Air-Gap Bridging**: USB-based malware designed to transfer data between isolated and connected networks
- **Progressive Web App (PWA) Phishing**: Fake Google Security sites deploying PWA applications to steal credentials and MFA codes
- **ClickFix Social Engineering**: Deceptive techniques encouraging users to execute malicious commands
- **Deepfake Identity Attacks**: AI-generated content targeting identity verification systems

## Threat Actor Activities

- **APT28 (Russia-linked)**: Actively exploited CVE-2026-21513 MSHTML zero-day vulnerability before Microsoft's patch release
- **APT37 (North Korea)**: Deployed new malware targeting air-gapped networks with capabilities for covert surveillance and data exfiltration via removable drives
- **North Korean Threat Actors**: Published 26 malicious npm packages in continuation of Contagious Interview campaign, using Pastebin for command and control
- **The Com Cybercrime Collective**: 30 members arrested in Project Compass operation, with 179 total suspects identified targeting children and teenagers
- **Iranian Cyber Groups**: UK warns of heightened cyberattack risks amid Middle East conflicts
- **Kimwolf Botnet Operators**: Continued operation of world's largest disruptive botnet following vulnerability disclosure