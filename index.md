# Exploitation Report

The cybersecurity landscape is experiencing significant active exploitation across multiple critical vulnerabilities. Two zero-day vulnerabilities are currently under active attack: CVE-2025-10035 affecting Fortra's GoAnywhere Managed File Transfer solution, and an unpatched Local File Inclusion (LFI) to Remote Code Execution (RCE) vulnerability in Gladinet CentreStack and TrioFox products. Additionally, CL0P-linked hackers are exploiting a zero-day flaw in Oracle's E-Business Suite software that has impacted dozens of organizations since August 2025. The threat landscape also includes widespread botnet activity with RondoDox targeting 56 n-day vulnerabilities across more than 30 device types, and multiple sophisticated malware campaigns leveraging social engineering and legitimate tools for credential theft and system compromise.

## Active Exploitation Details

### GoAnywhere Managed File Transfer Critical Vulnerability
- **Description**: A critical security flaw in Fortra's GoAnywhere Managed File Transfer (MFT) solution
- **Impact**: Allows attackers to gain unauthorized access to file transfer systems and potentially compromise sensitive data
- **Status**: Under active exploitation; Fortra has provided full timeline of exploitation and patching efforts
- **CVE ID**: CVE-2025-10035

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: An unpatched Local File Inclusion (LFI) vulnerability that can be escalated to Remote Code Execution (RCE)
- **Impact**: Attackers can execute arbitrary code on affected systems, leading to full system compromise
- **Status**: Currently under active in-the-wild exploitation; no patch available

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: A zero-day security flaw in Oracle's E-Business Suite (EBS) software
- **Impact**: Enables unauthorized access to enterprise business applications and data
- **Status**: Actively exploited by CL0P-linked hackers since August 9, 2025, affecting dozens of organizations

## Affected Systems and Products

- **Fortra GoAnywhere MFT**: Managed File Transfer solutions used by enterprises for secure file transfers
- **Gladinet CentreStack**: Cloud file server and sync solutions for enterprises
- **TrioFox**: File server modernization and cloud migration platform
- **Oracle E-Business Suite**: Enterprise resource planning and business applications
- **Node.js Applications**: Single Executable Application (SEA) feature being abused by Stealit malware
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting
- **Android Devices**: Targeted by ClayRat spyware impersonating popular applications
- **HR SaaS Platforms**: University payroll systems targeted by Storm-2657 threat actor
- **Multiple Device Types**: Over 30 distinct devices targeted by RondoDox botnet exploiting 56 vulnerabilities
- **SonicWall Cloud Backup Service**: All customers' firewall configuration files potentially compromised

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in enterprise software
- **Social Engineering**: Storm-2657 using targeted phishing to hijack HR employee accounts for payroll diversion
- **Malware Distribution**: Stealit campaign using Node.js SEA feature to distribute payloads via game and VPN installers
- **Supply Chain Attacks**: Malicious npm packages designed to harvest credentials from developer environments
- **Mobile Malware**: ClayRat spyware distributed through fake applications mimicking WhatsApp, TikTok, and YouTube
- **Botnet Operations**: RondoDox conducting large-scale attacks against known vulnerabilities across diverse device ecosystems
- **Credential Harvesting**: Multiple campaigns focused on stealing authentication tokens and login credentials
- **Legitimate Tool Abuse**: Threat actors using Velociraptor DFIR tool in LockBit and Babuk ransomware attacks

## Threat Actor Activities

- **Storm-2657**: Conducting "payroll pirate" attacks targeting university HR employees to divert salary payments since March 2025
- **CL0P-Linked Hackers**: Exploiting Oracle EBS zero-day vulnerability affecting dozens of organizations since August 2025
- **UTA0388**: China-aligned threat actor conducting spear-phishing campaigns across North America, Asia, and Europe using GOVERSHELL malware
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks before FBI takedown
- **RondoDox Operators**: Managing large-scale botnet targeting 56 n-day vulnerabilities across 30+ device types worldwide
- **Stealit Campaign**: Distributing Node.js-based malware through compromised game and VPN installers
- **ClayRat Operators**: Targeting Russian Android users through Telegram channels and phishing websites