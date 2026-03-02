# Exploitation Report

The current threat landscape reveals several critical exploitation activities across multiple platforms and attack vectors. Most notably, APT28 has been actively exploiting a zero-day MSHTML vulnerability before Microsoft's February 2026 patch cycle, while over 900 Sangoma FreePBX instances remain compromised with web shells from ongoing attacks. Chrome users face risks from malicious extensions exploiting privilege escalation vulnerabilities through the Gemini AI panel, and North Korean threat actors continue their sophisticated supply chain attacks through compromised npm packages. Additional concerns include AI agent hijacking through WebSocket vulnerabilities and widespread crypto theft through various attack methods.

## Active Exploitation Details

### MSHTML Zero-Day Vulnerability
- **Description**: A security flaw in Microsoft's MSHTML component that was exploited as a zero-day before the February 2026 Patch Tuesday
- **Impact**: Allows threat actors to gain unauthorized access and execute malicious code on targeted systems
- **Status**: Patched by Microsoft in February 2026, but was actively exploited before the patch release
- **CVE ID**: CVE-2026-21513

### Chrome Gemini Panel Privilege Escalation
- **Description**: A vulnerability in Google Chrome's Gemini AI panel that allows malicious extensions to escalate privileges
- **Impact**: Attackers can gain access to local files on the system, violate user privacy while browsing, and access sensitive resources
- **Status**: Now patched by Google Chrome
- **CVE ID**: Not specified in the articles

### Sangoma FreePBX Command Injection
- **Description**: A command injection vulnerability in Sangoma FreePBX systems that allows attackers to deploy web shells
- **Impact**: Complete system compromise allowing persistent access and control over PBX systems
- **Status**: Over 900 instances remain infected despite patches being available

### Ivanti Connect Zero-Day
- **Description**: A zero-day vulnerability in Ivanti Connect Secure devices exploited to deploy RESURGE malware
- **Impact**: Allows deployment of dormant malware implants that can remain undetected on compromised devices
- **Status**: Currently being exploited with RESURGE malware deployments
- **CVE ID**: CVE-2025-0282

### OpenClaw WebSocket Vulnerability (ClawJacked)
- **Description**: A high-severity vulnerability in the OpenClaw AI agent that allows malicious websites to hijack local AI agents via WebSocket connections
- **Impact**: Remote takeover of AI agents, data theft, and unauthorized access to local systems
- **Status**: Fixed by OpenClaw developers

## Affected Systems and Products

- **Google Chrome**: Gemini AI panel vulnerability affecting users with malicious extensions installed
- **Microsoft MSHTML**: Component vulnerability exploited by APT28 before February 2026 patches
- **Sangoma FreePBX**: Over 900 instances compromised with web shells from command injection attacks
- **Ivanti Connect Secure**: Devices affected by zero-day exploitation and RESURGE malware implants
- **OpenClaw AI Agent**: Local AI agents vulnerable to WebSocket-based hijacking attacks
- **npm Registry**: 26 malicious packages published containing cross-platform RAT malware
- **Chrome Extensions**: QuickLens extension compromised to steal cryptocurrency and deploy malware
- **Google Cloud API**: Thousands of exposed API keys providing unauthorized access to Gemini endpoints
- **Go Modules**: Malicious cryptocurrency modules deploying Rekoobe backdoors on Linux systems

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeted exploitation of unpatched vulnerabilities in MSHTML and Ivanti systems
- **Supply Chain Attacks**: Malicious npm packages and compromised Chrome extensions used to deliver malware
- **WebSocket Hijacking**: ClawJacked attacks exploiting AI agent communication protocols
- **Web Shell Deployment**: Command injection attacks leading to persistent backdoor access
- **Social Engineering**: ClickFix attacks and fraudulent browser extension installations
- **API Key Abuse**: Exploitation of exposed Google Cloud API keys for unauthorized service access
- **Malware Implants**: Deployment of dormant malware like RESURGE that can remain undetected
- **Cross-Platform RAT**: Node.js-based remote access tools targeting multiple operating systems

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Actively exploiting CVE-2026-21513 MSHTML zero-day before Microsoft patches
- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks and conduct covert surveillance
- **North Korean Hackers**: Publishing 26 malicious npm packages in Contagious Interview campaign with Pastebin C2 infrastructure
- **Cybercriminal Groups**: Compromising Chrome extensions like QuickLens to steal cryptocurrency from thousands of users
- **Unknown Attackers**: Targeting Sangoma FreePBX systems with command injection attacks and web shell deployment
- **The Com Collective**: Online cybercrime group targeting children and teenagers, resulting in 30 arrests in Europol operation
- **Kimwolf Botnet Operators**: Assembling and operating the world's largest disruptive botnet through vulnerability exploitation