# Exploitation Report

Critical exploitation activity is currently being observed across multiple platforms, with several zero-day vulnerabilities actively exploited in the wild. The most significant threats include a Qualcomm Android component zero-day (CVE-2026-21385) confirmed by Google, an MSHTML zero-day (CVE-2026-21513) exploited by APT28 before Microsoft's February patch, and a high-severity OpenClaw AI agent vulnerability dubbed "ClawJacked." Additionally, sophisticated phishing campaigns are leveraging OAuth redirect mechanisms and MFA bypass techniques through tools like the Starkiller phishing suite, while North Korean threat actors continue targeting developers through malicious npm packages.

## Active Exploitation Details

### Qualcomm Android Component Zero-Day
- **Description**: High-severity security flaw in an open-source Qualcomm display component used in Android devices
- **Impact**: Attackers can exploit the vulnerability to compromise Android devices through the display component
- **Status**: Actively exploited in the wild; patches released by Google in Android security updates addressing 129 vulnerabilities
- **CVE ID**: CVE-2026-21385

### MSHTML Zero-Day Vulnerability
- **Description**: Security flaw in Microsoft's MSHTML component that was exploited before the February 2026 Patch Tuesday
- **Impact**: Allows threat actors to compromise systems through browser-based attacks
- **Status**: Exploited by APT28 before official patching; now patched by Microsoft
- **CVE ID**: CVE-2026-21513

### OpenClaw AI Agent Vulnerability (ClawJacked)
- **Description**: High-severity vulnerability in the popular AI agent OpenClaw allowing malicious websites to hijack locally running AI agents via WebSocket connections
- **Impact**: Malicious websites can silently brute-force access to locally running OpenClaw instances, take control of AI agents, and steal sensitive data
- **Status**: Vulnerability has been patched by OpenClaw developers

### Google Chrome Gemini Panel Privilege Escalation
- **Description**: Security flaw in Google Chrome's Gemini AI panel that could permit malicious extensions to escalate privileges
- **Impact**: Attackers could escalate privileges, gain access to local files, violate user privacy while browsing, and access sensitive resources
- **Status**: Now patched by Google

## Affected Systems and Products

- **Android Devices**: Devices using Qualcomm display components are vulnerable to the zero-day exploit
- **Windows Systems**: Systems with MSHTML components targeted by APT28 exploitation
- **OpenClaw AI Platform**: Locally running OpenClaw instances vulnerable to WebSocket hijacking attacks
- **Google Chrome Browser**: Chrome installations with Gemini AI panel affected by privilege escalation vulnerability
- **AWS Data Centers**: Three facilities in UAE and one in Bahrain damaged by drone strikes causing service outages
- **Cloud Imperium Games**: Star Citizen and Squadron 42 game systems breached affecting user personal information
- **University of Hawaii Cancer Center**: Systems compromised by ransomware affecting nearly 1.2 million individuals
- **npm Registry**: 26 malicious packages published targeting developers in Contagious Interview campaign

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Android Qualcomm components and Windows MSHTML
- **OAuth Redirect Abuse**: Phishing campaigns using OAuth URL redirection to bypass conventional email and browser defenses
- **MFA Bypass via AitM**: Starkiller phishing suite uses adversary-in-the-middle reverse proxy techniques to circumvent multi-factor authentication
- **WebSocket Hijacking**: ClawJacked attack allows malicious websites to connect to local AI agents through brute-force WebSocket connections
- **Chrome Extension Compromise**: QuickLens extension compromised to deliver malware and steal cryptocurrency from users
- **PWA-Based Phishing**: Fake Google Security sites deliver Progressive Web Apps to steal credentials and MFA codes
- **Supply Chain Attacks**: North Korean actors publishing malicious npm packages with hidden Pastebin command and control infrastructure
- **Dual Malware Chains**: SloppyLemming using sophisticated multi-stage malware deployment against government targets

## Threat Actor Activities

- **APT28 (Russia-linked)**: Exploited MSHTML zero-day vulnerability before Microsoft's February 2026 patch release, targeting government and critical infrastructure
- **SloppyLemming**: Conducting targeted attacks against government entities and critical infrastructure in Pakistan and Bangladesh using dual malware deployment chains
- **North Korean Threat Actors**: Publishing 26 malicious npm packages as part of ongoing Contagious Interview campaign, hiding Pastebin C2 infrastructure for cross-platform RAT deployment
- **The Com Cybercriminal Collective**: 30 alleged members arrested in Project Compass global law enforcement operation, with nearly 180 members identified overall
- **Iranian State Actors**: UK NCSC warns of heightened cyberattack risks from Iranian groups amid ongoing Middle East conflict
- **Cryptocurrency Thieves**: Actors compromising Chrome extensions like QuickLens to steal cryptocurrency from thousands of users
- **Phishing Operators**: Multiple campaigns using sophisticated OAuth abuse and MFA bypass techniques targeting government entities and high-value individuals