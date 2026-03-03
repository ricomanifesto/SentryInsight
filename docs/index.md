# Exploitation Report

Current threat activity demonstrates a concerning trend of active zero-day exploitation across multiple platforms and attack vectors. The most critical development involves the active exploitation of CVE-2026-21385, a high-severity vulnerability in Qualcomm's Android display component, which Google has confirmed is being exploited in the wild. Additionally, CVE-2026-21513, a Microsoft HTML zero-day vulnerability, has been tied to APT28 operations and was exploited before Microsoft's February 2026 Patch Tuesday. The threat landscape is further complicated by the emergence of AI-powered attack tools, sophisticated phishing campaigns using Progressive Web Apps, and multiple vulnerabilities in popular AI platforms like OpenClaw that enable remote code execution and data theft.

## Active Exploitation Details

### Qualcomm Android Display Component Zero-Day
- **Description**: High-severity security flaw impacting an open-source Qualcomm component used in Android devices' display functionality
- **Impact**: Allows attackers to exploit Android devices through the display component, potentially gaining elevated access
- **Status**: Actively exploited in the wild, patches released by Google as part of 129 Android security vulnerabilities
- **CVE ID**: CVE-2026-21385

### Microsoft HTML Zero-Day Vulnerability
- **Description**: Security flaw in Microsoft's MSHTML component that was exploited before official patching
- **Impact**: Enables attackers to compromise systems through HTML-based attacks
- **Status**: Exploited by APT28 before February 2026 Patch Tuesday, now patched
- **CVE ID**: CVE-2026-21513

### OpenClaw AI Agent Hijacking Vulnerability (ClawJacked)
- **Description**: High-severity vulnerability in the popular AI agent OpenClaw that allows malicious websites to connect to locally running AI agents via WebSocket
- **Impact**: Enables remote attackers to hijack local AI agents, steal sensitive data, and execute commands on victim systems
- **Status**: Recently patched, but was actively exploited through malicious website connections

### Chrome Gemini Panel Privilege Escalation
- **Description**: Security flaw in Google Chrome's Gemini AI panel that could permit privilege escalation
- **Impact**: Attackers could escalate privileges, gain access to local files, violate user privacy during browsing, and access sensitive resources
- **Status**: Now patched by Google

## Affected Systems and Products

- **Android Devices**: All Android devices using Qualcomm display components vulnerable to zero-day exploitation
- **Microsoft Windows Systems**: Systems running MSHTML components targeted by APT28 operations
- **Google Chrome Browser**: Users with Gemini AI panel functionality at risk for privilege escalation attacks
- **OpenClaw AI Platform**: Local AI agent installations vulnerable to remote hijacking via malicious websites
- **Chrome Extensions**: QuickLens extension compromised to deliver cryptocurrency theft malware
- **npm Package Registry**: 26 malicious packages published by North Korean actors for cross-platform RAT deployment
- **Progressive Web Apps**: Fake Google security sites delivering credential and MFA code theft applications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Qualcomm and Microsoft components
- **WebSocket Hijacking**: ClawJacked attacks using malicious websites to connect to local AI agents through WebSocket protocols
- **Supply Chain Compromise**: Malicious npm packages and compromised Chrome extensions delivering malware payloads
- **Progressive Web App Phishing**: Sophisticated phishing campaigns using PWA technology to steal credentials and MFA codes
- **AI-Powered Attack Tools**: Adoption of CyberStrikeAI platform for enhanced automated attack capabilities
- **ClickFix Social Engineering**: Chrome extension compromise combined with social engineering to deliver cryptocurrency theft malware
- **Cross-Platform RAT Deployment**: North Korean actors using npm packages with Pastebin C2 infrastructure for multi-platform remote access

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Actively exploiting CVE-2026-21513 Microsoft HTML zero-day before official patching, demonstrating advanced persistent threat capabilities
- **SloppyLemming**: Conducting targeted campaigns against Pakistan and Bangladesh government entities using dual malware chains and sophisticated attack infrastructure
- **North Korean Threat Actors**: Publishing 26 malicious npm packages as part of the ongoing "Contagious Interview" campaign, using Pastebin for C2 communications and cross-platform RAT deployment
- **CyberStrikeAI Users**: Multiple threat actors adopting AI-powered security testing platforms for enhanced attack automation and effectiveness
- **The Com Cybercriminal Collective**: 30 alleged members arrested in Project Compass, with nearly 180 members identified in global law enforcement operation
- **Cryptocurrency Theft Groups**: Exploiting exposed wallet seeds and compromising browser extensions to steal millions in cryptocurrency funds