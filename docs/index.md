# Exploitation Report

Critical exploitation activity continues across multiple sectors, with state-sponsored actors leading significant cryptocurrency heists and malicious applications infiltrating trusted platforms. The most severe incidents include a $290 million DeFi heist attributed to North Korean Lazarus group, widespread malicious wallet applications in China's App Store targeting cryptocurrency assets, and active exploitation of vulnerabilities in SGLang and TBK DVR systems. Additionally, serial-to-IP devices are exposing thousands of vulnerabilities in operational technology environments, while ransomware groups are evolving their tactics with advanced proxy botnets for corporate network infiltration.

## Active Exploitation Details

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Attackers can achieve complete system compromise and remote code execution on susceptible systems
- **Status**: Actively exploitable with critical severity rating
- **CVE ID**: CVE-2026-5760 (CVSS 9.8)

### TBK DVR Authentication Bypass
- **Description**: Security flaw in TBK DVR systems allowing unauthorized access and device hijacking
- **Impact**: Enables threat actors to compromise devices for DDoS botnet recruitment and lateral movement
- **Status**: Actively exploited by Mirai botnet variants
- **CVE ID**: CVE-2024-3721

### Anthropic Model Context Protocol Design Weakness
- **Description**: Critical "by design" weakness in the Model Context Protocol's architecture that could enable remote code execution
- **Impact**: Potential for cascading effects across AI supply chain with remote code execution capabilities
- **Status**: Actively researched vulnerability threatening AI infrastructure

### Protobuf.js Remote Code Execution
- **Description**: Critical remote code execution flaw in protobuf.js JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables JavaScript code execution in applications using the vulnerable library
- **Status**: Proof-of-concept exploit code has been published, increasing exploitation risk

## Affected Systems and Products

- **KelpDAO DeFi Platform**: $290 million cryptocurrency theft impacting decentralized finance infrastructure
- **Apple App Store China**: 26 malicious wallet applications impersonating legitimate cryptocurrency wallets
- **SGLang Systems**: AI/ML platforms using SGLang framework vulnerable to GGUF model file attacks
- **TBK DVR Devices**: Digital video recording systems exposed to botnet recruitment
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted for Mirai botnet expansion
- **Vercel Infrastructure**: Web development platform compromised through AI tool access vectors
- **Serial-to-IP Devices**: Industrial OT devices translating machine protocols to Internet communications
- **Microsoft Teams**: Enterprise collaboration platform increasingly targeted for social engineering
- **Seiko USA Website**: E-commerce platform compromised with Shopify database theft claims
- **Protobuf.js Applications**: JavaScript applications using Google Protocol Buffers implementation

## Attack Vectors and Techniques

- **Malicious Model Files**: Exploitation through crafted GGUF files targeting SGLang systems
- **App Store Infiltration**: Deployment of fake cryptocurrency wallet applications to steal seed phrases
- **OAuth Token Theft**: Compromised authentication tokens used for lateral movement and data access
- **Social Engineering**: Microsoft Teams abuse for helpdesk impersonation and credential harvesting
- **Botnet Recruitment**: IoT device compromise for DDoS infrastructure expansion
- **Device Code Phishing**: Legitimate service flows abused to trick victims into granting account access
- **Website Defacement**: Direct compromise with ransom demands and data theft claims
- **Supply Chain Compromise**: Third-party AI tools used as initial access vectors

## Threat Actor Activities

- **Lazarus Group**: North Korean state-sponsored group behind $290 million KelpDAO cryptocurrency heist
- **Scattered Spider**: British-led cybercrime collective targeting cryptocurrency platforms with wire fraud and identity theft
- **The Gentlemen Ransomware**: Gang utilizing SystemBC proxy malware botnet with over 1,570 compromised corporate hosts
- **Nexcorium Operators**: Threat actors deploying Mirai variant targeting TBK DVR and TP-Link router infrastructure
- **Tycoon 2FA Group**: Phishing collective adopting device code techniques to bypass multi-factor authentication
- **ZionSiphon Operators**: Specialized malware targeting Israeli water treatment and desalination operational technology systems
- **Chinese Malware Distributors**: Operators placing 26 fraudulent cryptocurrency wallet applications in Apple's China App Store