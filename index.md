# Exploitation Report

Critical security incidents are actively impacting organizations across multiple sectors, with state-sponsored attackers and cybercriminal groups exploiting vulnerabilities in widely-used platforms and infrastructure. The most significant exploitation activity includes CVE-2026-5760 in SGLang enabling remote code execution, CVE-2024-3721 being actively exploited by Mirai botnets, and sophisticated supply chain attacks targeting cryptocurrency platforms and cloud services. Notable incidents include a $290 million cryptocurrency theft attributed to North Korean Lazarus hackers, malicious applications infiltrating Apple's App Store, and critical vulnerabilities in AI tools and IoT devices being weaponized for large-scale attacks.

## Active Exploitation Details

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Attackers can achieve remote code execution on susceptible systems
- **Status**: Actively exploitable with CVSS score of 9.8
- **CVE ID**: CVE-2026-5760

### TBK DVR Authentication Bypass
- **Description**: Security flaw in TBK DVR systems being exploited to build DDoS botnets using Mirai variant Nexcorium
- **Impact**: Complete device compromise and inclusion in DDoS botnet infrastructure
- **Status**: Actively exploited by threat actors
- **CVE ID**: CVE-2024-3721

### Anthropic Model Context Protocol Design Vulnerability
- **Description**: Critical "by design" weakness in the Model Context Protocol's architecture that enables remote code execution
- **Impact**: Remote code execution with cascading effects on AI supply chain
- **Status**: Actively exploitable design flaw threatening AI infrastructure

### Protobuf.js Remote Code Execution
- **Description**: Critical flaw in protobuf.js JavaScript library enabling arbitrary code execution
- **Impact**: JavaScript code execution in applications using the widely-adopted Protocol Buffers library
- **Status**: Proof-of-concept exploit code publicly available

## Affected Systems and Products

- **SGLang**: AI model serving framework vulnerable to malicious GGUF model file attacks
- **TBK DVR Systems**: Digital video recorders compromised for botnet recruitment
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted for Mirai botnet expansion
- **Apple App Store**: 26 malicious applications impersonating popular cryptocurrency wallets
- **KelpDAO**: DeFi platform suffering $290 million cryptocurrency theft
- **Vercel**: Cloud development platform experiencing data breach through third-party AI tool compromise
- **Serial-to-IP Devices**: OT infrastructure devices containing thousands of vulnerabilities
- **Microsoft Teams**: Platform increasingly abused for helpdesk impersonation attacks
- **WhatsApp**: Metadata leakage enabling user information inference
- **Seiko USA**: E-commerce website defaced with ransom demands

## Attack Vectors and Techniques

- **Malicious Model File Injection**: SGLang exploitation through crafted GGUF files
- **IoT Botnet Recruitment**: CVE-2024-3721 exploitation for Mirai variant deployment
- **App Store Infiltration**: Fake cryptocurrency wallet applications stealing seed phrases
- **OAuth Token Theft**: Compromised authentication tokens enabling lateral movement
- **SystemBC Proxy Botnet**: Ransomware gangs using proxy malware for bot-powered attacks
- **Helpdesk Impersonation**: Microsoft Teams abuse for social engineering attacks
- **Device Code Phishing**: New technique adopted by Tycoon 2FA phishing groups
- **Website Defacement**: Direct attacks on e-commerce platforms with ransom demands
- **Supply Chain Compromise**: Third-party AI tool access leading to broader infrastructure breaches

## Threat Actor Activities

- **Lazarus Group**: North Korean state-sponsored hackers responsible for $290 million KelpDAO cryptocurrency theft
- **Scattered Spider**: British cybercrime collective leader pleading guilty to wire fraud and identity theft charges
- **Gentlemen Ransomware Gang**: Deploying SystemBC proxy malware across 1,570+ compromised hosts for bot-powered attacks
- **ZionSiphon Operators**: Targeting Israeli water treatment and desalination OT systems with specialized malware
- **Tycoon 2FA Phishers**: Evolving tactics to include device code phishing techniques
- **Chinese Threat Actors**: Distributing 26 malicious cryptocurrency wallet applications through Apple App Store
- **Mirai Botnet Operators**: Exploiting TBK DVR and TP-Link router vulnerabilities for DDoS infrastructure expansion