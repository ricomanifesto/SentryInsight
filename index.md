# Exploitation Report

The cybersecurity landscape is experiencing significant active exploitation activity, with multiple critical vulnerabilities being exploited in the wild. Most notably, threat actors are actively exploiting zero-day vulnerabilities in Oracle E-Business Suite and Gladinet file sharing software, with the Oracle flaw being linked to CL0P ransomware operations affecting dozens of organizations. Additional concerning developments include widespread SonicWall VPN compromises affecting over 100 accounts, the abuse of legitimate DFIR tools like Velociraptor in ransomware attacks, and sophisticated malware campaigns targeting consumers through fake applications and social engineering tactics.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: A zero-day security flaw in Oracle's E-Business Suite (EBS) software that allows unauthorized access to sensitive data without authentication
- **Impact**: Attackers can access sensitive corporate data and have successfully breached dozens of organizations since exploitation began
- **Status**: Under active exploitation since August 9, 2025, with Oracle issuing a security alert
- **CVE ID**: Not specified in available information

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local file inclusion (LFI) to remote code execution (RCE) attacks in Gladinet file sharing software
- **Impact**: Local attackers can access system files without authentication and potentially achieve remote code execution
- **Status**: Active in-the-wild exploitation detected, currently unpatched
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere Managed File Transfer Vulnerability
- **Description**: A critical security flaw in GoAnywhere Managed File Transfer (MFT) software
- **Impact**: Allows attackers to compromise file transfer systems and access managed data
- **Status**: Previously exploited, with Fortra releasing detailed timeline of exploitation and remediation
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices through authentication bypass
- **Impact**: Threat actors are gaining authenticated access to multiple customer environments
- **Status**: Over 100 accounts confirmed compromised across multiple customer environments

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software affected by zero-day vulnerability enabling unauthorized data access
- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to local file inclusion attacks
- **Fortra GoAnywhere MFT**: Managed file transfer solution with critical vulnerability allowing system compromise
- **SonicWall SSL VPN**: Network security appliances experiencing widespread authentication bypasses
- **Node.js Applications**: Single Executable Application (SEA) feature being abused for malware distribution
- **npm Registry**: 175 malicious packages with 26,000 downloads targeting credential harvesting
- **Android Devices**: ClayRat spyware targeting users through fake popular applications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Oracle EBS and Gladinet software
- **Authentication Bypass**: SonicWall VPN devices compromised through authentication mechanisms
- **Legitimate Tool Abuse**: Velociraptor DFIR tool weaponized for persistent access in ransomware operations
- **Social Engineering**: Fake "Inflation Refund" SMS campaigns targeting New York residents
- **Supply Chain Attacks**: Malicious npm packages disguised as legitimate development tools
- **Application Masquerading**: Android malware posing as popular apps like WhatsApp, TikTok, and YouTube
- **Payroll Diversion**: HR SaaS account hijacking to redirect employee salary payments

## Threat Actor Activities

- **CL0P Ransomware Group**: Linked to Oracle E-Business Suite zero-day exploitation affecting dozens of organizations since August 2025
- **Storm-2603**: Chinese threat group abusing Velociraptor DFIR tool in LockBit ransomware attacks for persistent network access
- **Storm-2657**: "Payroll Pirates" targeting HR SaaS platforms to hijack employee accounts and divert salary payments
- **GXC Team**: Cybercrime syndicate dismantled by Spanish authorities, with leader "GoogleXcoder" arrested
- **ShinyHunters**: Cybercriminal group operating BreachForums portal for Salesforce extortion before FBI takedown
- **RondoDox Botnet**: Operating "exploit shotgun" approach targeting consumer edge devices globally
- **Aisuru Botnet**: Launching record-breaking DDoS attacks primarily from compromised IoT devices on US ISPs