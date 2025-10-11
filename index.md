# Exploitation Report

The current threat landscape shows active zero-day exploitation across multiple critical systems, with threat actors targeting enterprise file sharing solutions, Oracle software, and abusing legitimate security tools for malicious purposes. Most concerning is the active exploitation of CVE-2025-11371 in Gladinet CentreStack and TrioFox products, allowing local attackers to access system files without authentication. Additionally, zero-day exploitation of Oracle E-Business Suite has impacted dozens of organizations since August 2025, with attacks linked to the CL0P ransomware group. The sophisticated threat group Storm-2603 is notably weaponizing the Velociraptor incident response tool in ransomware campaigns, while Storm-2657 conducts targeted "payroll pirate" attacks against university HR systems to hijack employee salary payments.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication, with exploitation escalating from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Unauthorized access to sensitive system files and potential complete system compromise through remote code execution
- **Status**: Currently unpatched with active in-the-wild exploitation detected by Huntress
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: A critical zero-day vulnerability in Oracle's E-Business Suite (EBS) software that has been actively exploited since August 9, 2025
- **Impact**: Complete organizational compromise with dozens of organizations affected
- **Status**: Zero-day exploitation ongoing with no patch available

### Fortra GoAnywhere Managed File Transfer Vulnerability
- **Description**: A critical security flaw in GoAnywhere Managed File Transfer (MFT) that came under active exploitation
- **Impact**: Potential file transfer system compromise and unauthorized data access
- **Status**: Under investigation with full timeline revealed by Fortra
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to authentication bypass
- **Oracle E-Business Suite (EBS)**: Enterprise resource planning software with zero-day exploitation
- **Fortra GoAnywhere MFT**: Managed file transfer solutions with critical vulnerabilities
- **Consumer Edge Devices**: Targeted by RondoDox botnet using exploit shotgun approach
- **npm Registry**: Compromised with 175 malicious packages containing 26,000 downloads
- **Android Devices**: Targeted by ClayRat spyware impersonating popular applications
- **SonicWall Firewall Backups**: 100% of cloud backup service customers affected in breach

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active targeting of unpatched vulnerabilities in enterprise software
- **Legitimate Tool Abuse**: Storm-2603 weaponizing Velociraptor DFIR tool for persistent network access
- **Supply Chain Attacks**: Malicious npm packages used for credential phishing campaigns
- **Social Engineering**: ClayRat spyware disguising as WhatsApp, TikTok, YouTube, and Google Photos
- **Node.js SEA Abuse**: Stealit malware leveraging Single Executable Application feature via game and VPN installers
- **HR System Targeting**: Direct attacks on payroll systems to redirect salary payments
- **DDoS Amplification**: Aisuru botnet utilizing compromised IoT devices on major US ISPs

## Threat Actor Activities

- **Storm-2603**: Chinese threat group conducting ransomware attacks using legitimate Velociraptor DFIR tool for network persistence and deploying LockBit and Babuk ransomware
- **Storm-2657**: Cybercrime gang conducting "payroll pirate" attacks targeting university HR employees since March 2025 to hijack salary payments
- **CL0P-linked Hackers**: Exploiting Oracle E-Business Suite zero-day to breach dozens of organizations since August 2025
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion activities before FBI takedown
- **RondoDox Botnet Operators**: Employing hit-and-run exploit shotgun tactics against consumer edge devices globally
- **Stealit Campaign**: Active malware distribution through compromised game and VPN installers using Node.js exploitation