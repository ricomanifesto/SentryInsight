# Exploitation Report

Current cybersecurity threats reveal a diverse landscape of active exploitation targeting both enterprise systems and consumer applications. Critical vulnerabilities are being exploited across multiple vectors, including a severe flaw in SGLang with a CVSS score of 9.8 enabling remote code execution, active exploitation of TBK DVR systems through CVE-2024-3721 for botnet recruitment, and sophisticated malware campaigns targeting mobile payment systems and cryptocurrency applications. The threat landscape is further complicated by supply chain attacks affecting development platforms like Vercel, nation-state activities targeting critical infrastructure, and the emergence of new malware families specifically designed for operational technology environments.

## Active Exploitation Details

### SGLang Remote Code Execution Vulnerability
- **Description**: Critical vulnerability in SGLang that allows remote code execution through malicious GGUF model files
- **Impact**: Attackers can achieve complete system compromise and execute arbitrary code on susceptible systems
- **Status**: Actively being exploited with proof-of-concept available
- **CVE ID**: CVE-2026-5760

### TBK DVR Exploitation
- **Description**: Security flaw in TBK DVR systems being exploited by Mirai botnet variants
- **Impact**: Device hijacking for DDoS botnet recruitment and network compromise
- **Status**: Active exploitation confirmed for botnet expansion
- **CVE ID**: CVE-2024-3721

### Protobuf.js Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in the widely used JavaScript implementation of Google's Protocol Buffers
- **Impact**: JavaScript code execution in applications using the vulnerable library
- **Status**: Proof-of-concept exploit code has been published, increasing exploitation risk

### CISA KEV Catalog Additions
- **Description**: Eight new vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog, including three Cisco flaws
- **Impact**: Confirmed active exploitation in the wild affecting federal and enterprise systems
- **Status**: Active exploitation confirmed with federal remediation deadlines set for April-May 2026

## Affected Systems and Products

- **SGLang**: AI/ML systems using GGUF model files for language processing
- **TBK DVR Systems**: Digital video recorders vulnerable to botnet recruitment
- **TP-Link Wi-Fi Routers**: End-of-life devices targeted for Mirai botnet expansion
- **Protobuf.js Library**: JavaScript applications implementing Google's Protocol Buffers
- **HandyPay Mobile App**: Legitimate NFC payment application trojaned with NGate malware
- **Apple App Store**: 26 malicious cryptocurrency wallet applications targeting Chinese users
- **Microsoft Teams**: Enterprise collaboration platform abused for social engineering
- **Vercel Platform**: Web infrastructure provider experiencing data breach
- **KelpDAO**: DeFi project suffering $290 million cryptocurrency theft
- **Serial-to-IP Devices**: OT/industrial systems with thousands of vulnerabilities
- **Cisco Systems**: Multiple products affected by newly cataloged exploited vulnerabilities

## Attack Vectors and Techniques

- **Malicious Model File Injection**: Attackers embedding exploit code in GGUF model files to target SGLang systems
- **Mobile Application Trojaning**: Legitimate apps like HandyPay compromised to deliver NGate NFC payment malware
- **App Store Infiltration**: Fake cryptocurrency wallet applications deployed through official app stores
- **Social Engineering via Teams**: Helpdesk impersonation attacks using Microsoft Teams for initial access
- **OAuth Token Theft**: Stolen authentication tokens enabling lateral movement and persistent access
- **Device Code Phishing**: Tycoon 2FA phishing groups adopting new techniques to bypass multi-factor authentication
- **Supply Chain Compromise**: Third-party AI tools and development platforms breached for internal access
- **Botnet Recruitment**: Exploitation of IoT devices including DVRs and routers for DDoS capabilities
- **Cryptocurrency Targeting**: Multiple attack vectors focusing on digital asset theft and wallet compromise

## Threat Actor Activities

- **Lazarus Group**: North Korean state-sponsored hackers linked to $290 million KelpDAO cryptocurrency heist
- **Scattered Spider**: British cybercrime collective leader pleading guilty to wire fraud and identity theft charges
- **Gentlemen Ransomware**: Gang utilizing SystemBC proxy malware botnet with over 1,570 compromised corporate hosts
- **NGate Operators**: Cybercriminals distributing NFC payment data theft malware through trojaned mobile applications
- **Tycoon 2FA Phishers**: Groups evolving tactics to adopt device code phishing for enhanced credential theft
- **ZionSiphon Developers**: Threat actors creating specialized malware targeting Israeli water treatment and desalination systems
- **Chinese App Store Infiltrators**: Cybercriminals deploying 26 fake cryptocurrency wallet applications in Apple's China App Store
- **Nexcorium Botnet Operators**: Mirai variant distributors exploiting DVR and router vulnerabilities for DDoS infrastructure