# Exploitation Report

Critical exploitation activity spans multiple attack vectors, with threat actors leveraging zero-day vulnerabilities, compromised browser extensions, and novel attack techniques targeting everything from network appliances to AI systems. Most concerning are the ongoing attacks against Cisco SD-WAN infrastructure through CVE-2026-20127, which has been actively exploited for three years, and the recently disclosed CVE-2025-0282 affecting Ivanti Connect devices. Advanced persistent threat groups, particularly North Korean actors APT37 and ScarCruft, are deploying sophisticated malware to breach air-gapped networks, while cybercriminals continue to exploit web applications and compromised infrastructure for financial gain.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: Maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been under active exploitation by sophisticated threat actors
- **Impact**: Complete system compromise allowing attackers persistent access to network infrastructure
- **Status**: Active exploitation for three years with minimal evidence left by attackers
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Security Bypass
- **Description**: Zero-day vulnerability exploited through RESURGE malware implant that can remain dormant on affected systems
- **Impact**: Persistent access to enterprise network infrastructure with ability to maintain stealth presence
- **Status**: Actively exploited with CISA warning about dormant malware persistence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in FreePBX systems leading to web shell deployment
- **Impact**: Remote code execution and persistent backdoor access to telecommunications infrastructure
- **Status**: Over 900 instances remain compromised with ongoing web shell attacks since December

### ClawJacked OpenClaw AI Hijacking
- **Description**: High-severity vulnerability allowing malicious websites to connect to locally running AI agents via WebSocket
- **Impact**: Complete takeover of local AI agents enabling data theft and unauthorized operations
- **Status**: Fixed by OpenClaw but represents emerging AI security threat vector

## Affected Systems and Products

- **Cisco SD-WAN**: Network infrastructure appliances with maximum-severity vulnerability
- **Ivanti Connect**: Enterprise connectivity solutions vulnerable to RESURGE malware
- **Sangoma FreePBX**: Over 900 telecommunications systems compromised with web shells
- **OpenClaw AI**: Local AI agent systems vulnerable to remote hijacking
- **Google Chrome Extensions**: QuickLens extension compromised affecting thousands of users
- **Trend Micro Apex One**: Windows endpoint security systems with critical RCE vulnerabilities
- **Google Cloud API**: API keys providing unauthorized access to Gemini AI services
- **Samsung Smart TVs**: Data collection systems affecting Texas consumers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched vulnerabilities in critical infrastructure
- **Web Shell Deployment**: Command injection leading to persistent backdoor access
- **Browser Extension Compromise**: Malicious updates to legitimate Chrome extensions for crypto theft
- **ClickFix Social Engineering**: Fake error messages tricking users into executing malicious code
- **WebSocket Hijacking**: Malicious websites connecting to local AI services
- **USB-Based Malware**: Physical media used to bridge air-gapped networks
- **Blockchain C2 Infrastructure**: Encrypted commands stored on Polygon blockchain for botnet resilience
- **Cloud API Abuse**: Exploitation of exposed Google API keys for unauthorized AI access

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using removable drives and conducting covert surveillance operations
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for command-and-control communications and USB malware to compromise isolated systems
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with advanced evasion techniques
- **Aeternum C2 Operators**: Operating blockchain-based botnet infrastructure using Polygon for command storage and takedown resilience
- **QuickLens Attackers**: Compromising browser extensions to steal cryptocurrency from thousands of users
- **The Com Collective**: Online cybercrime group targeting children and teenagers, resulting in 30 arrests through Europol operation