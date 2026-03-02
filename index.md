# Exploitation Report

Current exploitation activity reveals several critical security incidents across multiple platforms and technologies. The most severe active exploitation involves a three-year-long campaign targeting Cisco SD-WAN systems through a maximum-severity zero-day vulnerability, alongside ongoing attacks against Sangoma FreePBX systems affecting over 900 instances worldwide. Additionally, significant security breaches have occurred through compromised Chrome extensions, exposed API keys enabling unauthorized access to AI systems, and sophisticated malware campaigns by North Korean threat actors targeting air-gapped networks. These incidents demonstrate a broad range of attack vectors from web-based exploits to supply chain compromises and advanced persistent threat operations.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability that has been actively exploited by an unknown but sophisticated threat actor for three years
- **Impact**: Allows unauthorized access to SD-WAN infrastructure with potential for network compromise and lateral movement
- **Status**: Under active exploitation for 3 years, recently disclosed
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: A command injection vulnerability in FreePBX systems that allows attackers to deploy web shells for persistent access
- **Impact**: Complete system compromise with ability to maintain persistent backdoor access through web shells
- **Status**: Over 900 instances remain infected despite patches being available since December
- **CVE ID**: Not specified in the articles

### Ivanti Connect Secure Zero-Day
- **Description**: A zero-day vulnerability in Ivanti Connect Secure systems exploited to deploy RESURGE malware implants
- **Impact**: Allows deployment of dormant malware that can persist undetected on compromised systems
- **Status**: Active exploitation with RESURGE malware remaining dormant on affected devices
- **CVE ID**: CVE-2025-0282

### OpenClaw AI Agent WebSocket Vulnerability (ClawJacked)
- **Description**: High-severity vulnerability allowing malicious websites to hijack locally running AI agents through WebSocket connections
- **Impact**: Enables malicious websites to silently brute-force access and take control of local AI agents
- **Status**: Patched by OpenClaw, but demonstrates new attack vectors against AI systems

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One that enable remote code execution on Windows systems
- **Impact**: Attackers can gain complete control over vulnerable Windows systems running Apex One
- **Status**: Recently patched, active exploitation potential remains high

## Affected Systems and Products

- **Cisco SD-WAN Systems**: All versions vulnerable to CVE-2026-20127, exploitation ongoing for 3 years
- **Sangoma FreePBX Instances**: Over 900 systems compromised with web shells still active
- **Ivanti Connect Secure**: Systems vulnerable to RESURGE malware implantation
- **Google Cloud API Keys**: Thousands of exposed keys providing unauthorized Gemini AI access
- **Chrome Web Store Extensions**: QuickLens extension compromised to steal cryptocurrency
- **Trend Micro Apex One**: Windows systems running vulnerable versions subject to RCE attacks
- **OpenClaw AI Agents**: Local installations vulnerable to WebSocket-based hijacking
- **Samsung Smart TVs**: Texas residents' viewing data collection without consent
- **Korean National Tax Service**: Cryptocurrency wallet seed phrase exposure leading to theft

## Attack Vectors and Techniques

- **WebSocket Hijacking**: ClawJacked attacks leverage WebSocket connections to hijack AI agents from malicious websites
- **Web Shell Deployment**: FreePBX attacks use command injection to install persistent web shells
- **Chrome Extension Compromise**: Supply chain attack through compromised browser extensions using ClickFix techniques
- **API Key Abuse**: Previously harmless Google API keys repurposed to access sensitive Gemini AI data
- **Blockchain-Based C2**: Aeternum botnet stores encrypted commands on Polygon blockchain for takedown resistance
- **USB-Based Air-Gap Crossing**: North Korean actors use removable drives to breach isolated networks
- **Trojanized Gaming Tools**: Java-based RATs distributed through compromised gaming utilities
- **Zoho WorkDrive C2**: Legitimate cloud services used for command and control communications

## Threat Actor Activities

- **APT37/ScarCruft (North Korea)**: Deploying new malware tools to breach air-gapped networks using USB-based vectors and Zoho WorkDrive for C2 communications
- **Unknown Sophisticated Actor**: Conducting three-year exploitation campaign against Cisco SD-WAN systems with minimal forensic evidence
- **Kimwolf Botnet Operators**: Operating the world's largest botnet through disclosed vulnerabilities, with "Dort" identified as a key botmaster
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, resulting in 30 arrests through Europol's Project Compass operation
- **Brazilian, Chinese, Vietnamese Scammers**: Operating celebrity-bait advertising scams across Meta platforms
- **Ukrainian Cybercriminal**: Operating OnlyFake AI-powered fake identification document service with over 10,000 fraudulent IDs sold
- **Various Threat Actors**: Exploiting FreePBX vulnerabilities to maintain persistent access through web shell infections across 900+ systems