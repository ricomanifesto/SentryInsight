# Exploitation Report

Current threat activity demonstrates a concerning escalation in sophisticated exploitation techniques, with multiple zero-day vulnerabilities under active attack and threat actors increasingly weaponizing legitimate security tools. Critical zero-day exploitations are occurring in Gladinet file sharing software and Oracle's E-Business Suite, while threat actors are exploiting SonicWall SSL VPN devices for widespread network compromises. Particularly alarming is the trend of cybercriminals repurposing legitimate digital forensics tools like Velociraptor for ransomware operations, and the emergence of botnet operations targeting consumer edge devices and IoT infrastructure.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion (LFI) vulnerability that escalates to remote code execution, allowing attackers to access system files without authentication
- **Impact**: Unauthorized access to sensitive system files and potential complete system compromise through RCE escalation
- **Status**: Currently under active in-the-wild exploitation with no patch available
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: Critical security flaw in Oracle's EBS software that has been exploited by CL0P-linked threat actors
- **Impact**: Mass compromise of organizations with potential data exfiltration and ransomware deployment
- **Status**: Active exploitation since August 9, 2025, affecting dozens of organizations

### Fortra GoAnywhere Managed File Transfer
- **Description**: Critical security vulnerability in file transfer software that came under active exploitation
- **Impact**: Potential unauthorized access to managed file transfer systems and sensitive data exposure
- **Status**: Patch timeline and investigation details revealed by Fortra
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Devices
- **Description**: Widespread compromise allowing threat actors to authenticate into multiple customer environments
- **Impact**: Unauthorized network access affecting over 100 accounts across multiple organizations
- **Status**: Active exploitation with evidence of systematic targeting

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and cloud storage solutions vulnerable to zero-day LFI/RCE attacks
- **Oracle E-Business Suite**: Enterprise resource planning software targeted in mass exploitation campaign
- **SonicWall SSL VPN**: Network security appliances compromised for unauthorized access
- **Fortra GoAnywhere MFT**: Managed file transfer solutions affected by critical vulnerability
- **Consumer Edge Devices**: IoT devices and routers targeted by RondoDox botnet operations
- **npm Registry**: JavaScript package repository contaminated with 175 malicious packages
- **Android Devices**: Mobile platforms targeted by ClayRat spyware masquerading as popular apps

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched vulnerabilities in enterprise software for immediate access
- **Tool Weaponization**: Abuse of legitimate DFIR tools like Velociraptor for persistent access and ransomware deployment
- **Supply Chain Contamination**: Distribution of malicious npm packages with 26,000+ downloads for credential harvesting
- **Social Engineering**: ClayRat spyware deployment through fake popular applications on Android platforms
- **VPN Compromise**: Systematic exploitation of SSL VPN infrastructure for multi-tenant access
- **Botnet Operations**: RondoDox employing "shotgun approach" for mass exploitation of edge device vulnerabilities
- **IoT Device Exploitation**: Aisuru botnet leveraging compromised IoT devices on major US ISPs for record DDoS attacks

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor DFIR tool in LockBit and Babuk ransomware campaigns
- **CL0P-linked Actors**: Mass exploitation of Oracle EBS zero-day affecting dozens of organizations since August 2025
- **Storm-2657**: "Payroll pirates" targeting university HR employees to hijack salary payments through SaaS account compromise
- **ShinyHunters**: Operating BreachForums portal for Salesforce extortion before FBI takedown, warning of law enforcement crackdowns
- **Unknown Actors**: Systematic compromise of SonicWall VPN devices affecting 100+ customer accounts
- **RondoDox Operators**: Conducting widespread botnet operations targeting consumer edge devices globally
- **Aisuru Botnet**: Orchestrating record-breaking DDoS attacks using compromised IoT devices on US ISP networks