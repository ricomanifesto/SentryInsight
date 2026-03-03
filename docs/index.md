# Exploitation Report

Critical vulnerability activity dominates the current threat landscape, with multiple high-severity exploits targeting AI platforms, browser components, and enterprise systems. The most concerning development is the active exploitation of CVE-2026-21513, a zero-day MSHTML vulnerability leveraged by Russian state-sponsored group APT28 before Microsoft's February 2026 Patch Tuesday. Additionally, the ClawJacked vulnerability in OpenClaw AI agents presents significant risks to organizations utilizing AI automation tools, while compromised Chrome extensions and malicious npm packages demonstrate the expanding attack surface across development environments.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A security flaw in Microsoft's MSHTML engine that was exploited by APT28 before being patched in February 2026
- **Impact**: Allows attackers to execute arbitrary code and compromise target systems through web-based attacks
- **Status**: Patched by Microsoft in February 2026 Patch Tuesday, but was actively exploited as a zero-day before the patch
- **CVE ID**: CVE-2026-21513

### ClawJacked OpenClaw Vulnerability
- **Description**: A high-severity vulnerability in the OpenClaw AI agent platform that allows malicious websites to hijack locally running AI agents via WebSocket connections
- **Impact**: Enables attackers to silently brute-force access to local AI agents, steal sensitive data, and take control of AI automation workflows
- **Status**: Patched by OpenClaw developers, but represents ongoing risks to AI agent deployments

### Chrome Gemini Panel Privilege Escalation
- **Description**: A vulnerability in Google Chrome's Gemini AI panel that could be exploited by malicious extensions to escalate privileges
- **Impact**: Attackers could gain access to local files, violate user privacy during browsing sessions, and access sensitive system resources
- **Status**: Patched by Google Chrome security team

### Fortinet Infrastructure Compromises
- **Description**: Ongoing exploitation of Fortinet systems by threat actors using AI-powered attack tools including CyberStrikeAI
- **Impact**: Hundreds of Fortinet devices breached, potentially exposing enterprise networks and sensitive data
- **Status**: Active campaign with widespread impact across multiple organizations

## Affected Systems and Products

- **OpenClaw AI Platform**: AI agent automation systems vulnerable to WebSocket hijacking attacks
- **Google Chrome Browser**: Gemini AI panel components affected by privilege escalation vulnerabilities
- **Microsoft MSHTML Engine**: Web rendering components in Windows systems targeted by state-sponsored attacks
- **Fortinet Network Appliances**: Enterprise security devices compromised through AI-powered attack campaigns
- **npm Package Registry**: 26 malicious packages published by North Korean threat actors targeting developers
- **Chrome Extension Platform**: QuickLens extension compromised to steal cryptocurrency and deploy malware
- **Google Cloud API Infrastructure**: Thousands of exposed API keys providing unauthorized access to Gemini endpoints

## Attack Vectors and Techniques

- **WebSocket Hijacking**: Malicious websites exploiting ClawJacked vulnerability to connect to local AI agents
- **AI-Powered Automation**: CyberStrikeAI platform being weaponized for large-scale infrastructure attacks
- **Browser Extension Compromise**: Legitimate Chrome extensions hijacked to deploy cryptocurrency theft malware
- **Supply Chain Poisoning**: North Korean actors publishing malicious npm packages with Pastebin command-and-control infrastructure
- **Progressive Web App (PWA) Phishing**: Fake Google security sites deploying PWA applications to steal credentials and MFA codes
- **Cross-Platform RAT Deployment**: Multi-stage malware campaigns targeting developers through fake interview processes
- **API Key Exploitation**: Abuse of exposed Google Cloud API keys to access private Gemini AI endpoints

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Actively exploiting CVE-2026-21513 MSHTML zero-day vulnerability before patch release
- **North Korean Threat Groups**: Publishing 26 malicious npm packages in continued Contagious Interview campaign targeting software developers
- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks and conduct surveillance through removable drive propagation
- **The Com Cybercriminal Collective**: 30 alleged members arrested in Project Compass law enforcement operation, with nearly 180 total members identified
- **Iranian Cyber Operations**: UK warns of heightened Iranian cyberattack risks amid Middle East conflicts
- **Cryptocurrency Theft Groups**: Exploiting exposed wallet seeds and compromised browser extensions for multi-million dollar theft operations