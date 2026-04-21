# Exploitation Report

Critical exploitation activity is currently targeting diverse infrastructure and applications across multiple vectors. The most severe threat involves state-sponsored actors conducting large-scale cryptocurrency heists, with North Korean Lazarus Group suspected in a $290 million DeFi platform attack. Simultaneously, AI and machine learning systems face unprecedented risks with critical vulnerabilities in SGLang enabling remote code execution through malicious model files, while Anthropic's Model Context Protocol contains fundamental design weaknesses that threaten AI supply chain security. IoT and OT systems remain heavily compromised, with Mirai botnet variants actively exploiting DVR vulnerabilities and targeted malware like ZionSiphon specifically designed to attack Israeli critical infrastructure. Enterprise environments are under attack through legitimate collaboration platforms like Microsoft Teams, while serial-to-IP devices contain thousands of vulnerabilities creating extensive attack surfaces for industrial systems.

## Active Exploitation Details

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical security vulnerability in SGLang that enables remote code execution through malicious GGUF model files
- **Impact**: Attackers can achieve remote code execution on susceptible systems by exploiting the model file processing mechanism
- **Status**: Recently disclosed with proof-of-concept available
- **CVE ID**: CVE-2026-5760

### TBK DVR Authentication Bypass
- **Description**: Security flaw in TBK DVR systems allowing unauthorized access and device compromise
- **Impact**: Threat actors can hijack DVR devices to build DDoS botnets using Mirai variants
- **Status**: Actively exploited in the wild by Nexcorium botnet operators
- **CVE ID**: CVE-2024-3721

### Anthropic MCP Design Vulnerability
- **Description**: Critical "by design" weakness in the Model Context Protocol's architecture
- **Impact**: Could enable remote code execution and create cascading effects across AI supply chains
- **Status**: Fundamental architectural issue requiring design changes

### Protobuf.js Remote Code Execution
- **Description**: Critical remote code execution flaw in protobuf.js, a widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: Enables JavaScript code execution in applications using the vulnerable library
- **Status**: Proof-of-concept exploit code has been published

## Affected Systems and Products

- **SGLang Framework**: AI/ML systems using SGLang for model processing and inference
- **TBK DVR Systems**: Digital video recording devices vulnerable to authentication bypass
- **TP-Link Wi-Fi Routers**: End-of-life router models being incorporated into botnets
- **Anthropic MCP**: AI systems implementing the Model Context Protocol
- **KelpDAO DeFi Platform**: Decentralized finance platform suffering $290 million theft
- **Apple App Store**: 26 malicious cryptocurrency wallet applications targeting Chinese users
- **Vercel Infrastructure**: Web development platform experiencing data breach
- **Microsoft Teams**: Enterprise collaboration platform being abused for social engineering
- **Israeli Water Systems**: Water treatment and desalination systems targeted by ZionSiphon malware
- **Protobuf.js Library**: JavaScript applications using Google Protocol Buffers implementation
- **Serial-to-IP Devices**: Industrial OT devices converting serial communications to IP protocols
- **SystemBC Infrastructure**: Proxy malware botnet with over 1,570 compromised corporate hosts

## Attack Vectors and Techniques

- **Malicious Model Files**: Exploitation through crafted GGUF model files in AI systems
- **DDoS Botnet Recruitment**: Compromising IoT devices to build distributed attack infrastructure
- **Social Engineering via Teams**: Impersonating helpdesk personnel through Microsoft Teams external collaboration
- **App Store Infiltration**: Deploying fake cryptocurrency wallet applications to steal recovery phrases
- **OAuth Token Theft**: Compromising authentication tokens for lateral movement and persistent access
- **Website Defacement**: Attacking e-commerce platforms and threatening data exposure for ransom
- **AI Supply Chain Attacks**: Exploiting fundamental protocol weaknesses in AI infrastructure
- **Device Code Phishing**: Tricking victims into authorizing account access through legitimate device login flows
- **OT Infrastructure Targeting**: Specialized malware designed for critical infrastructure systems
- **Legitimate Tool Abuse**: Using trusted applications and services for malicious purposes

## Threat Actor Activities

- **Lazarus Group**: State-sponsored North Korean hackers suspected in $290 million KelpDAO cryptocurrency theft, continuing pattern of targeting DeFi platforms
- **Scattered Spider**: British cybercrime collective leader pleads guilty to wire fraud and aggravated identity theft charges related to cryptocurrency theft operations
- **Gentlemen Ransomware Gang**: Deploying SystemBC proxy malware to establish persistent bot networks across corporate environments for ransomware operations
- **Nexcorium Operators**: Actively exploiting TBK DVR vulnerabilities to expand Mirai botnet infrastructure for DDoS attacks
- **ZionSiphon Developers**: Creating specialized malware specifically targeting Israeli water treatment and desalination systems
- **Chinese Threat Actors**: Infiltrating Apple App Store with 26 fake cryptocurrency wallet applications targeting users in China
- **Tycoon 2FA Phishers**: Evolving tactics to adopt device code phishing techniques for bypassing multi-factor authentication
- **Vercel Attackers**: Compromising cloud infrastructure through AI tool access vectors and selling stolen data
- **Teams Impersonators**: Increasing abuse of Microsoft Teams for helpdesk impersonation and social engineering attacks