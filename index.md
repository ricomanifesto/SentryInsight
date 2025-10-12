# Exploitation Report

Current threat intelligence reveals multiple active exploitation campaigns targeting critical enterprise systems. Most concerning are zero-day vulnerabilities in Gladinet CentreStack and TrioFox products (CVE-2025-11371), Oracle E-Business Suite systems, and widespread SonicWall SSL VPN compromises affecting over 100 accounts. Additionally, threat actors are weaponizing legitimate security tools like Velociraptor DFIR for ransomware operations, while the RondoDox botnet continues exploiting edge device vulnerabilities globally. These campaigns demonstrate sophisticated adversary tactics targeting both unpatched systems and abusing trusted security infrastructure.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: Local file inclusion (LFI) vulnerability that can be escalated to remote code execution (RCE)
- **Impact**: Allows local attackers to access system files without authentication and achieve code execution
- **Status**: Currently being exploited in the wild, unpatched zero-day
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: Critical security flaw in Oracle's E-Business Suite (EBS) software
- **Impact**: Enables unauthorized access to enterprise systems and data exfiltration
- **Status**: Zero-day exploitation ongoing since August 9, 2025, targeting dozens of organizations

### Fortra GoAnywhere Managed File Transfer Vulnerability
- **Description**: Critical security flaw in GoAnywhere MFT platform
- **Impact**: Allows attackers to compromise file transfer systems and access sensitive data
- **Status**: Actively exploited, patch timeline and investigation details revealed
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread authentication bypass affecting SSL VPN devices
- **Impact**: Unauthorized access to corporate networks and customer environments
- **Status**: Active exploitation with over 100 compromised accounts confirmed

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and cloud storage solutions vulnerable to LFI/RCE attacks
- **Oracle E-Business Suite**: Enterprise resource planning software targeted by CL0P-linked hackers
- **SonicWall SSL VPN Devices**: Network security appliances compromised for unauthorized access
- **Fortra GoAnywhere MFT**: Managed file transfer platform with critical vulnerability
- **Consumer Edge Devices**: Various IoT and networking equipment targeted by RondoDox botnet
- **npm Registry**: Package repository containing 175 malicious packages with 26,000+ downloads
- **Windows 11 23H2**: Home and Pro editions approaching end of support, creating security risks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities being actively exploited across enterprise software
- **Tool Weaponization**: Legitimate DFIR tool Velociraptor repurposed for ransomware deployment and persistent access
- **Supply Chain Attacks**: Malicious npm packages used for credential harvesting campaigns
- **Social Engineering**: Payroll pirate attacks targeting university HR employees to redirect salary payments
- **VPN Compromise**: SSL VPN authentication bypass enabling network infiltration
- **Malware Distribution**: Node.js Single Executable Application feature abused for Stealit malware delivery
- **Shotgun Approach**: RondoDx botnet using broad exploitation tactics against edge devices

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group abusing Velociraptor DFIR tool in LockBit and Babuk ransomware attacks
- **Storm-2657**: Cybercrime gang conducting "payroll pirate" attacks against US universities since March 2025
- **CL0P-Linked Hackers**: Exploiting Oracle EBS zero-day to breach dozens of organizations
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion (recently disrupted by FBI)
- **RondoDox Botnet Operators**: Conducting widespread exploitation campaigns against consumer edge devices
- **Aisuru Botnet**: Leveraging compromised IoT devices on US ISPs for record-breaking DDoS attacks