# Exploitation Report

Multiple critical zero-day vulnerabilities are currently under active exploitation, with the most severe being CVE-2025-11371 in Gladinet file sharing software and CVE-2025-10035 in Fortra's GoAnywhere Managed File Transfer. These vulnerabilities are being actively exploited by threat actors to gain unauthorized system access and deploy ransomware. Additionally, an Oracle E-Business Suite zero-day has been exploited since August 2025, affecting dozens of organizations. The threat landscape is further complicated by advanced botnet operations like RondoDox targeting edge devices and Aisuru conducting record-breaking DDoS attacks against U.S. ISPs.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: A zero-day vulnerability allowing local file inclusion (LFI) to remote code execution (RCE) escalation in Gladinet CentreStack and Triofox products
- **Impact**: Allows local attackers to access system files without authentication and achieve remote code execution
- **Status**: Currently being exploited in the wild, no patch available
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere Managed File Transfer Critical Flaw
- **Description**: A critical security vulnerability in GoAnywhere MFT that has undergone comprehensive investigation and timeline analysis
- **Impact**: Provides unauthorized access to managed file transfer systems
- **Status**: Under active exploitation with full timeline from detection to patch revealed by Fortra
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Zero-Day
- **Description**: A zero-day vulnerability in Oracle's E-Business Suite (EBS) software exploited by CL0P-linked hackers
- **Impact**: Complete organizational breach and data exfiltration capabilities
- **Status**: Actively exploited since August 9, 2025, affecting dozens of organizations worldwide

## Affected Systems and Products

- **Gladinet Products**: CentreStack and Triofox file sharing platforms vulnerable to authentication bypass
- **Fortra GoAnywhere MFT**: Managed file transfer solutions compromised through critical vulnerability
- **Oracle E-Business Suite**: Enterprise resource planning software targeted in widespread zero-day exploitation
- **Consumer Edge Devices**: Various IoT and network edge devices targeted by RondoDox botnet
- **U.S. Internet Infrastructure**: Major ISPs including AT&T, Comcast, and Verizon affected by Aisuru botnet DDoS attacks
- **Node.js Applications**: Single Executable Application feature abused for malware distribution
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities exploited for initial access and privilege escalation
- **Shotgun Exploit Approach**: RondoDox botnet employs hit-and-run tactics against multiple edge device vulnerabilities simultaneously
- **Digital Forensics Tool Abuse**: Storm-2603 threat group weaponizes Velociraptor DFIR tool for persistent network access
- **Supply Chain Attacks**: Malicious npm packages and Node.js SEA feature abuse for payload distribution
- **Spear-Phishing Campaigns**: UTA0388 delivers Go-based GOVERSHELL implant through targeted email attacks
- **HR Account Hijacking**: Storm-2657 targets university HR employees to divert salary payments
- **DDoS Amplification**: Aisuru botnet leverages compromised IoT devices for record-breaking distributed denial-of-service attacks

## Threat Actor Activities

- **Storm-2657 (Payroll Pirates)**: Actively targeting university HR employees since March 2025 to hijack salary payments through account compromise
- **Storm-2603**: Chinese threat group abusing legitimate Velociraptor DFIR tool to maintain persistent access for LockBit and Babuk ransomware deployment
- **CL0P-Linked Group**: Exploiting Oracle EBS zero-day since August 2025, compromising dozens of organizations in widespread campaign
- **UTA0388**: China-aligned APT conducting spear-phishing operations across North America, Asia, and Europe using evolved GOVERSHELL malware
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks and Salesforce extortion before FBI takedown
- **RondoDox Operators**: Conducting systematic exploitation campaigns against consumer edge devices using automated vulnerability scanning
- **Aisuru Botnet Controllers**: Orchestrating record-breaking DDoS attacks against U.S. internet service providers using compromised IoT infrastructure