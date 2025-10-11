# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting file sharing software, Oracle business systems, and consumer edge devices. The most significant active exploitation involves CVE-2025-11371 in Gladinet file sharing products, CVE-2025-10035 in GoAnywhere Managed File Transfer systems, and an Oracle E-Business Suite zero-day being leveraged by CL0P-linked hackers. These attacks demonstrate sophisticated techniques ranging from local file inclusion to remote code execution, affecting organizations globally across various sectors including universities, manufacturing, and enterprise infrastructure.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication, with exploitation progressing from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Unauthorized system file access and potential complete system compromise through remote code execution
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### GoAnywhere Managed File Transfer Vulnerability
- **Description**: A critical security flaw in Fortra's GoAnywhere MFT solution that has been under active exploitation
- **Impact**: Compromise of managed file transfer systems, potentially exposing sensitive data transfers
- **Status**: Actively exploited, full investigation timeline revealed by Fortra
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Zero-Day
- **Description**: A zero-day vulnerability in Oracle's E-Business Suite software being exploited since August 9, 2025
- **Impact**: Organizational breaches affecting dozens of entities, with potential data exfiltration and system compromise
- **Status**: Actively exploited by CL0P-linked hackers, affecting multiple organizations globally

## Affected Systems and Products

- **Gladinet CentreStack**: File sharing and collaboration platform vulnerable to authentication bypass
- **Gladinet TrioFox**: Cloud file server solution affected by the same zero-day vulnerability
- **GoAnywhere MFT**: Managed file transfer solutions from Fortra experiencing active exploitation
- **Oracle E-Business Suite**: Enterprise business applications targeted in widespread zero-day attacks
- **Consumer Edge Devices**: Various edge devices targeted by RondoDox botnet exploitation campaigns
- **IoT Devices**: Internet-of-Things devices compromised for DDoS botnet operations, particularly on US ISPs
- **Node.js Applications**: Systems running Node.js Single Executable Applications vulnerable to Stealit malware

## Attack Vectors and Techniques

- **Local File Inclusion to RCE**: Attackers exploiting LFI vulnerabilities to achieve remote code execution in file sharing systems
- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being actively exploited before patches are available
- **Shotgun Approach**: RondoDox botnet using hit-and-run tactics to exploit multiple edge device vulnerabilities
- **Social Engineering**: Stealit malware distributed through game and VPN installers leveraging Node.js SEA features
- **Supply Chain Attacks**: 175 malicious npm packages with 26,000 downloads used for credential phishing
- **DFIR Tool Abuse**: Velociraptor digital forensics tool being weaponized for persistent access in ransomware attacks
- **AI System Exploitation**: CamoLeak attacks targeting GitHub Copilot for data exfiltration

## Threat Actor Activities

- **CL0P-Linked Hackers**: Exploiting Oracle E-Business Suite zero-day to breach dozens of organizations since August 2025
- **Storm-2603**: Chinese threat group using Velociraptor DFIR tool in LockBit and Babuk ransomware attacks
- **Storm-2657**: "Payroll Pirates" targeting university HR employees to hijack salary payments through SaaS account compromise
- **ShinyHunters**: Operating BreachForums portal for Salesforce extortion before FBI takedown
- **RondoDox Operators**: Running botnet campaigns with shotgun approach to edge device exploitation
- **Aisuru Botnet**: Conducting record-breaking DDoS attacks using compromised IoT devices on major US ISPs
- **Stealit Campaign**: Distributing malware through game and VPN installers targeting credential theft