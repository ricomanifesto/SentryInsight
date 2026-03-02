# Exploitation Report

The current threat landscape reveals several critical exploitation activities, with the most concerning being the active exploitation of a Cisco SD-WAN zero-day vulnerability that has been leveraged by sophisticated threat actors for three years. Additionally, ongoing attacks against Sangoma FreePBX instances have compromised over 900 systems through command injection vulnerabilities, while threat actors continue to exploit weaknesses in AI systems and infrastructure components to establish persistent access and steal sensitive data.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity zero-day vulnerability in Cisco SD-WAN infrastructure that has been under active exploitation
- **Impact**: Allows sophisticated threat actors to gain unauthorized access to SD-WAN infrastructure with minimal detection
- **Status**: Has been exploited for 3 years by unknown but sophisticated attackers who left very little evidence behind
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: A command injection vulnerability in Sangoma FreePBX systems that enables web shell deployment
- **Impact**: Allows attackers to install persistent web shells for ongoing system access and control
- **Status**: Actively exploited since December with over 900 instances still compromised
- **CVE ID**: CVE-2025-0282

### ClawJacked OpenClaw AI Agent Vulnerability
- **Description**: A high-severity vulnerability in OpenClaw AI agent that allows malicious websites to hijack locally running AI agents via WebSocket connections
- **Impact**: Enables unauthorized access to local AI agents, allowing attackers to take over control and potentially steal sensitive data
- **Status**: Vulnerability has been patched by OpenClaw

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Critical vulnerability affecting SD-WAN deployments with maximum severity rating
- **Sangoma FreePBX Systems**: Over 900 instances compromised with persistent web shell infections
- **OpenClaw AI Agent**: Popular AI agent vulnerable to remote hijacking attacks via malicious websites
- **Ivanti Connect Secure**: Affected by RESURGE malware implants that can remain dormant on devices
- **Google Cloud API Keys**: Thousands of exposed API keys with unauthorized access to Gemini AI endpoints
- **Trend Micro Apex One**: Critical remote code execution vulnerabilities in Windows systems
- **Chrome Extensions**: QuickLens extension compromised to deliver malware and steal cryptocurrency

## Attack Vectors and Techniques

- **WebSocket Hijacking**: Malicious websites exploiting OpenClaw through WebSocket connections to gain control of local AI agents
- **Web Shell Deployment**: Command injection attacks against FreePBX systems to install persistent backdoors
- **Blockchain-Based C2**: Aeternum botnet using Polygon blockchain to store encrypted commands and evade takedown efforts
- **USB-Based Air-Gap Bypass**: North Korean groups using removable drives to breach isolated networks
- **Browser Extension Compromise**: Legitimate Chrome extensions being hijacked to deliver ClickFix attacks and crypto theft
- **AI-Powered Social Engineering**: Use of artificial intelligence to generate fake identification documents and conduct sophisticated scams

## Threat Actor Activities

- **APT37/ScarCruft (North Korean)**: Deploying new malware tools to breach air-gapped networks using USB-based attack vectors and leveraging Zoho WorkDrive for command-and-control communications
- **Unknown Sophisticated Actor**: Exploiting Cisco SD-WAN zero-day for three years while maintaining operational security and leaving minimal forensic evidence
- **Kimwolf Botmaster "Dort"**: Operating the world's largest and most disruptive botnet through exploited vulnerabilities
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, leading to 30 arrests in Europol-coordinated operations
- **Multiple Criminal Groups**: Conducting pig butchering cryptocurrency scams resulting in $61 million in seized Tether tokens
- **Gaming Community Threat Actors**: Distributing Java-based remote access trojans through trojanized gaming utilities via browsers and chat platforms