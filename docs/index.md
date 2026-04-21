# Exploitation Report

Current exploitation activity reveals a diverse landscape of active threats targeting critical infrastructure, AI systems, and enterprise platforms. North Korean state-sponsored actors, specifically the Lazarus group, have executed a massive $290 million cryptocurrency heist against KelpDAO, demonstrating continued targeting of DeFi platforms. Critical vulnerabilities are being actively exploited across multiple domains, including a severe remote code execution flaw in SGLang with a CVSS score of 9.8, and ongoing exploitation of TBK DVR systems for botnet recruitment. Enterprise platforms face significant risks from malicious applications infiltrating official app stores, OAuth token theft, and sophisticated social engineering campaigns leveraging legitimate collaboration tools.

## Active Exploitation Details

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that allows attackers to achieve remote code execution through malicious GGUF model files
- **Impact**: Complete system compromise and remote code execution on susceptible systems
- **Status**: Actively exploitable with critical severity rating
- **CVE ID**: CVE-2026-5760

### TBK DVR Authentication Bypass
- **Description**: Security flaw in TBK DVR systems being exploited by Mirai botnet variants to hijack devices
- **Impact**: Device compromise and recruitment into DDoS botnets for coordinated attacks
- **Status**: Actively exploited in the wild by threat actors
- **CVE ID**: CVE-2024-3721

### Protobuf.js Remote Code Execution
- **Description**: Critical flaw in the widely-used JavaScript implementation of Google's Protocol Buffers library
- **Impact**: Remote code execution through JavaScript code injection
- **Status**: Proof-of-concept exploit code has been publicly released

### Anthropic Model Context Protocol Design Weakness
- **Description**: Critical "by design" architectural weakness in Anthropic's Model Context Protocol that enables remote code execution
- **Impact**: Potential cascading effects across AI supply chain and remote system compromise
- **Status**: Design-level vulnerability affecting MCP architecture

## Affected Systems and Products

- **KelpDAO DeFi Platform**: Targeted in $290 million cryptocurrency theft by North Korean hackers
- **Apple App Store (China)**: 26 malicious cryptocurrency wallet applications discovered impersonating legitimate services
- **TBK DVR Systems**: Digital video recorders compromised for botnet recruitment
- **SGLang AI Framework**: Machine learning inference systems vulnerable to malicious model files
- **Vercel Infrastructure**: Cloud development platform breached through compromised AI tool access
- **Protobuf.js Library**: Widely-deployed JavaScript implementation affecting numerous applications
- **Microsoft Teams**: Enterprise collaboration platform increasingly targeted for social engineering
- **Serial-to-IP OT Devices**: Industrial control system components containing thousands of vulnerabilities
- **Israeli Water Treatment Systems**: Critical infrastructure targeted by ZionSiphon malware
- **Grinex Cryptocurrency Exchange**: Sanctioned platform shut down following $13.74 million hack

## Attack Vectors and Techniques

- **Malicious Model Files**: Exploitation through crafted GGUF files targeting AI inference systems
- **OAuth Token Theft**: Compromise of authentication tokens for lateral movement and persistent access
- **App Store Infiltration**: Deployment of malicious applications through legitimate distribution channels
- **Social Engineering via Teams**: Abuse of Microsoft Teams for helpdesk impersonation and credential theft
- **Device Code Phishing**: Advanced phishing technique exploiting legitimate new-device login flows
- **Botnet Recruitment**: Exploitation of IoT devices for DDoS attack infrastructure
- **Supply Chain Compromise**: Targeting of third-party AI tools and development platforms
- **Website Defacement**: Direct compromise of public-facing websites for ransom demands

## Threat Actor Activities

- **Lazarus Group**: North Korean state-sponsored actors executed $290 million KelpDAO cryptocurrency theft
- **Scattered Spider**: British cybercrime collective leader pleaded guilty to wire fraud and identity theft charges
- **The Gentlemen Ransomware**: Deployment of SystemBC proxy malware across 1,570+ compromised corporate hosts
- **ZionSiphon Operators**: Targeted attacks against Israeli water treatment and desalination infrastructure
- **Tycoon 2FA Phishers**: Advanced persistent phishing campaigns targeting multi-factor authentication systems
- **Mirai Variant Groups**: Continued exploitation of IoT devices for botnet expansion using Nexcorium variant
- **Chinese Threat Actors**: Distribution of cryptocurrency-stealing applications through official app stores