# Exploitation Report

Critical zero-day exploitation activity is currently targeting multiple enterprise platforms, with threat actors leveraging unpatched vulnerabilities in file sharing software, Oracle E-Business Suite, and consumer edge devices. The most severe incidents include active exploitation of CVE-2025-11371 in Gladinet file sharing products and CVE-2025-10035 in GoAnywhere Managed File Transfer systems. Additionally, CL0P-linked hackers are conducting mass exploitation campaigns against Oracle software, while sophisticated botnets like RondoDox and Aisuru are targeting IoT devices and ISP infrastructure with unprecedented scale attacks.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication, with exploitation paths progressing from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Unauthorized system file access and potential remote code execution capabilities
- **Status**: Currently unpatched with active in-the-wild exploitation observed by Huntress
- **CVE ID**: CVE-2025-11371

### GoAnywhere Managed File Transfer Critical Flaw
- **Description**: A critical security vulnerability in Fortra's GoAnywhere MFT platform that has undergone active exploitation
- **Impact**: Compromise of managed file transfer operations and potential data exfiltration
- **Status**: Patched following detailed investigation and disclosure by Fortra
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: A zero-day vulnerability in Oracle's E-Business Suite software being exploited by CL0P-linked hackers in mass campaigns
- **Impact**: Dozens of organizations compromised with potential for widespread corporate data theft
- **Status**: Active exploitation observed since August 9, 2025, by Google Threat Intelligence Group

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and cloud storage platforms vulnerable to authentication bypass
- **Fortra GoAnywhere MFT**: Managed file transfer solutions experiencing critical exploitation
- **Oracle E-Business Suite (EBS)**: Enterprise business applications targeted in mass exploitation campaigns
- **Consumer Edge Devices**: IoT devices and network equipment targeted by RondoDox botnet operations
- **U.S. ISP Infrastructure**: AT&T, Comcast, and Verizon networks compromised by Aisuru botnet for DDoS attacks
- **SonicWall Cloud Backup Service**: 100% of firewall configuration backups breached affecting all customers
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited before vendor patches
- **Shotgun Approach**: RondoDox botnet using hit-and-run tactics against edge device vulnerabilities
- **Supply Chain Attacks**: Malicious npm packages masquerading as legitimate development tools
- **Social Engineering**: Stealit malware distributed through fake game and VPN installers using Node.js SEA features
- **Tool Abuse**: Velociraptor DFIR tool weaponized for persistent access in ransomware campaigns
- **Credential Harvesting**: Mass phishing campaigns targeting developer credentials through malicious packages
- **AI Agent Exploitation**: CamoLeak attacks targeting GitHub Copilot for code and secret exfiltration

## Threat Actor Activities

- **CL0P-Linked Group**: Conducting mass exploitation of Oracle E-Business Suite affecting dozens of organizations since August 2025
- **Storm-2657**: "Payroll Pirates" targeting university HR employees to hijack salary payments in ongoing campaigns
- **Storm-2603**: Chinese threat group abusing Velociraptor IR tools for persistent access in LockBit and Babuk ransomware deployments
- **ShinyHunters**: Operating BreachForums portal for Salesforce extortion until FBI takedown, with continued extortion threats remaining active
- **RondoDox Operators**: Running global botnet campaigns with hit-and-run exploitation tactics against consumer edge devices
- **Aisuru Botnet**: Orchestrating record-breaking DDoS attacks primarily using compromised IoT devices on major U.S. ISP networks