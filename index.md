# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities being actively exploited in the wild, with particularly concerning activity targeting Android devices and Windows systems. The most significant active exploitation involves CVE-2026-21385, a high-severity Qualcomm display component vulnerability affecting Android devices, and CVE-2026-21513, an MSHTML zero-day that was exploited by APT28 before Microsoft's February patch cycle. Additionally, a sophisticated phishing infrastructure called Starkiller is leveraging advanced techniques to bypass multi-factor authentication, while the ClawJacked vulnerability demonstrates new risks in AI agent security. Multiple threat actors are conducting coordinated campaigns against government entities and critical infrastructure, indicating a significant escalation in state-sponsored and criminal exploitation activities.

## Active Exploitation Details

### Qualcomm Android Display Component Vulnerability
- **Description**: High-severity security flaw impacting an open-source Qualcomm component used in Android devices' display functionality
- **Impact**: Allows attackers to exploit Android devices through the display component, potentially leading to privilege escalation and system compromise
- **Status**: Actively exploited in the wild; patches released by Google in latest Android security updates
- **CVE ID**: CVE-2026-21385

### MSHTML Zero-Day Vulnerability
- **Description**: Security flaw in Microsoft's MSHTML component that was exploited before the February 2026 Patch Tuesday
- **Impact**: Enables attackers to compromise Windows systems through web-based attacks
- **Status**: Actively exploited by APT28 threat actors; subsequently patched by Microsoft
- **CVE ID**: CVE-2026-21513

### ClawJacked OpenClaw AI Agent Vulnerability
- **Description**: High-severity vulnerability in the popular OpenClaw AI agent that allows malicious websites to hijack locally running AI agents via WebSocket connections
- **Impact**: Enables attackers to silently brute-force access to local AI agents, steal data, and execute unauthorized commands
- **Status**: Patched by OpenClaw developers following responsible disclosure

### Chrome Gemini Panel Privilege Escalation
- **Description**: Security flaw in Google Chrome's Gemini AI panel that could permit privilege escalation
- **Impact**: Allows malicious extensions to escalate privileges, access local files, and violate user privacy
- **Status**: Patched by Google; affected Chrome versions updated

## Affected Systems and Products

- **Android Devices**: All devices using Qualcomm display components, particularly those not yet updated with latest Android security patches
- **Windows Systems**: Systems running affected MSHTML components, targeted specifically by APT28 operations
- **OpenClaw AI Agent**: Local installations of OpenClaw before the security patch implementation
- **Google Chrome**: Chrome browsers with Gemini AI panel integration before the latest security updates
- **AWS Data Centers**: Three UAE facilities and one Bahrain facility affected by physical drone strike attacks
- **Cloud Imperium Games**: Star Citizen and Squadron 42 game platforms and user databases
- **University of Hawaii Cancer Center**: Epidemiology Division systems affecting 1.2 million individuals
- **npm Registry**: 26 malicious packages targeting cross-platform environments in supply chain attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Android and Windows systems
- **Adversary-in-the-Middle (AitM)**: Starkiller phishing suite uses reverse proxy techniques to intercept and bypass MFA protections
- **WebSocket Hijacking**: ClawJacked attack vector allowing malicious websites to connect to local AI agents
- **Supply Chain Attacks**: North Korean threat actors publishing malicious npm packages with hidden Pastebin C2 infrastructure
- **OAuth Redirect Abuse**: Sophisticated phishing campaigns leveraging legitimate OAuth mechanisms to bypass security defenses
- **Progressive Web App (PWA) Abuse**: Fake Google Security sites deploying PWA applications to steal credentials and MFA codes
- **Physical Infrastructure Attacks**: Drone strikes targeting cloud infrastructure in Middle East regions

## Threat Actor Activities

- **APT28**: Russian state-sponsored group actively exploiting CVE-2026-21513 MSHTML zero-day in targeted campaigns against high-value targets
- **SloppyLemming**: Conducting sophisticated attacks against government entities and critical infrastructure in Pakistan and Bangladesh using dual malware chains
- **North Korean Hackers**: Executing Contagious Interview campaign with 26 malicious npm packages containing cross-platform RAT capabilities
- **The Com Cybercriminal Collective**: Global law enforcement operation Project Compass resulted in 30 arrests and identification of 180 members
- **Iranian Threat Actors**: UK warns of heightened cyberattack risks from Iranian groups amid Middle East conflict escalation
- **CyberStrikeAI Tool Adopters**: Threat actors leveraging AI-powered attack tools in campaigns that previously breached hundreds of Fortinet FortiGate devices