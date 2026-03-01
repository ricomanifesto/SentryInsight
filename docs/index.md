# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms including network infrastructure, AI systems, and telecommunications equipment. The most severe threats include a three-year-long zero-day exploitation campaign against Cisco SD-WAN systems (CVE-2026-20127) that has been actively exploited by sophisticated threat actors, and ongoing web shell attacks compromising over 900 Sangoma FreePBX instances through command injection vulnerabilities. Additionally, CISA has issued warnings about RESURGE malware targeting Ivanti devices through CVE-2025-0282, while North Korean APT groups including APT37 and ScarCruft are deploying new tools to breach air-gapped networks and conduct covert surveillance operations.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been exploited for three years by unknown sophisticated threat actors
- **Impact**: Full system compromise with attackers leaving minimal forensic evidence
- **Status**: Active exploitation confirmed, sophisticated threat actor involved
- **CVE ID**: CVE-2026-20127

### Ivanti Connect RESURGE Malware
- **Description**: Zero-day attacks exploiting Ivanti Connect Secure devices using malicious implants that can remain dormant
- **Impact**: Persistent access to corporate VPN infrastructure with potential for lateral movement
- **Status**: Active exploitation with CISA warnings issued about dormant malware persistence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Remote code execution and persistent access to telecommunications infrastructure
- **Status**: Over 900 instances remain compromised with ongoing web shell attacks since December

### ClawJacked OpenClaw AI Vulnerability
- **Description**: High-severity flaw allowing malicious websites to hijack local OpenClaw AI agents via WebSocket connections
- **Impact**: Complete takeover of AI agent functionality and potential data exfiltration
- **Status**: Recently fixed by OpenClaw

### Trend Micro Apex One Critical Flaws
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software
- **Impact**: Remote code execution on vulnerable Windows systems
- **Status**: Recently patched by Trend Micro

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical flaw in Junos OS Evolved running on PTX Series routers
- **Impact**: Full router takeover allowing unauthenticated remote code execution with root privileges
- **Status**: Critical vulnerability disclosed, patch status unclear

## Affected Systems and Products

- **Cisco SD-WAN Systems**: Network infrastructure devices under active exploitation for three years
- **Ivanti Connect Secure**: VPN appliances targeted by RESURGE malware campaigns
- **Sangoma FreePBX Instances**: Over 900 telecommunications systems compromised with web shells
- **OpenClaw AI Agents**: Local AI systems vulnerable to WebSocket hijacking attacks
- **Trend Micro Apex One**: Windows-based security software with RCE vulnerabilities
- **Juniper PTX Series Routers**: Network infrastructure running Junos OS Evolved
- **Google Cloud API Keys**: Thousands of exposed keys providing unauthorized Gemini AI access
- **QuickLens Chrome Extension**: Compromised browser extension affecting thousands of users
- **Samsung Smart TVs**: Texas-based devices involved in unauthorized data collection

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Sophisticated actors leveraging unknown vulnerabilities for multi-year campaigns
- **Web Shell Deployment**: Command injection attacks installing persistent backdoors on FreePBX systems
- **WebSocket Hijacking**: Malicious websites exploiting local AI agent connections
- **Browser Extension Compromise**: Hijacking legitimate Chrome extensions to deploy malware and steal cryptocurrency
- **USB-Based Air-Gap Bridging**: North Korean groups using removable drives to transfer data between isolated networks
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command and control
- **ClickFix Social Engineering**: Fake error messages tricking users into running malicious commands
- **Go Module Poisoning**: Malicious Go crypto modules deploying Rekoobe backdoors and harvesting credentials

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks and conduct surveillance operations via removable drives
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware to compromise isolated systems
- **Sophisticated Unknown Actor**: Conducting three-year Cisco SD-WAN exploitation campaign with advanced evasion techniques
- **Kimwolf Botnet Operator "Dort"**: Managing the world's largest botnet through disclosed vulnerability exploitation
- **The Com Cybercrime Collective**: Targeting children and teenagers with 30 arrests made in Europol operation
- **Aeternum C2 Operators**: Using blockchain-based infrastructure to make botnet resilient to takedown efforts
- **Gaming Tool Threat Actors**: Distributing Java-based RATs through trojanized gaming utilities on browsers and chat platforms