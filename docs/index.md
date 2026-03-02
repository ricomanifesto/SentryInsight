# Exploitation Report

Critical vulnerabilities are actively being exploited across multiple platforms, with several high-severity flaws demanding immediate attention. The ClawJacked vulnerability in OpenClaw AI agents allows malicious websites to hijack local instances through WebSocket connections, while Cisco SD-WAN systems have been compromised by an unknown sophisticated threat actor exploiting CVE-2026-20127 for three years. Additionally, over 900 Sangoma FreePBX instances remain infected with web shells following command injection attacks, and CISA has warned about dormant RESURGE malware on Ivanti devices exploiting CVE-2025-0282. These incidents highlight the persistent threat landscape targeting both enterprise infrastructure and emerging AI technologies.

## Active Exploitation Details

### ClawJacked Vulnerability in OpenClaw AI Agents
- **Description**: A high-severity security flaw that allows malicious websites to connect to locally running OpenClaw AI agents and take control of them through WebSocket connections
- **Impact**: Attackers can silently brute-force access to local OpenClaw instances and steal sensitive data from compromised systems
- **Status**: OpenClaw has released a fix for this vulnerability

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been actively exploited by sophisticated threat actors
- **Impact**: Complete system compromise allowing unauthorized access to network infrastructure
- **Status**: Under active exploitation for three years by unknown advanced persistent threat actors
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Remote code execution and persistent access to compromised FreePBX instances
- **Status**: Over 900 instances remain infected with web shells despite patches being available

### Ivanti Connect Secure Zero-Day
- **Description**: Zero-day vulnerability in Ivanti Connect Secure systems being exploited to deploy RESURGE malware
- **Impact**: Installation of dormant malware implants that can provide persistent backdoor access
- **Status**: CISA has issued warnings about RESURGE malware remaining dormant on patched systems
- **CVE ID**: CVE-2025-0282

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software allowing remote code execution
- **Impact**: Complete system compromise on Windows systems running vulnerable Apex One versions
- **Status**: Patches have been released by Trend Micro

## Affected Systems and Products

- **OpenClaw AI Agents**: Local instances vulnerable to WebSocket hijacking attacks
- **Cisco SD-WAN Systems**: Network infrastructure compromised through maximum-severity vulnerability
- **Sangoma FreePBX Instances**: Over 900 systems remain infected with web shells
- **Ivanti Connect Secure**: Enterprise VPN solutions targeted with RESURGE malware
- **Trend Micro Apex One**: Windows-based endpoint security systems vulnerable to RCE
- **Google API Keys**: Previously harmless keys now expose Gemini AI data and private information
- **Chrome Extensions**: QuickLens extension compromised to steal cryptocurrency and push malware

## Attack Vectors and Techniques

- **WebSocket Hijacking**: Malicious websites exploiting ClawJacked vulnerability to connect to local AI agents
- **Command Injection**: Attackers using injection techniques to deploy web shells on FreePBX systems  
- **Zero-Day Exploitation**: Advanced persistent threats leveraging unknown vulnerabilities for extended periods
- **Browser Extension Compromise**: Legitimate Chrome extensions hijacked to distribute malware and steal crypto
- **USB-Based Attacks**: North Korean APT groups using removable drives to breach air-gapped networks
- **Blockchain C2 Infrastructure**: Aeternum botnet storing encrypted commands on Polygon blockchain for resilience
- **Supply Chain Attacks**: Trojanized gaming tools distributed via browsers and chat platforms

## Threat Actor Activities

- **APT37/ScarCruft**: North Korean threat actors deploying new malware to breach air-gapped networks using USB drives and Zoho WorkDrive for C2 communications
- **Unknown Sophisticated Actor**: Exploiting Cisco SD-WAN zero-day for three years while leaving minimal forensic evidence
- **Kimwolf Botnet Operators**: Managing the world's largest and most disruptive botnet through disclosed vulnerabilities
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, resulting in 30 arrests through Europol's Project Compass operation
- **Cryptocurrency Scammers**: Pig butchering operations resulting in $61 million in seized Tether and $4.8 million theft from exposed Korean tax agency wallet
- **OnlyFake Operators**: Ukrainian cybercriminals using AI to generate over 10,000 fake identification documents