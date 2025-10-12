# Exploitation Report

Critical exploitation activity is currently impacting multiple enterprise systems across various sectors. Several zero-day vulnerabilities are under active attack, including a Gladinet CentreStack and TrioFox vulnerability enabling local file inclusion to remote code execution, and an Oracle E-Business Suite flaw exploited by CL0P-linked hackers affecting dozens of organizations. Widespread SonicWall VPN compromises are providing attackers with persistent network access, while threat actors have weaponized the legitimate Velociraptor DFIR tool for ransomware deployment. Additionally, sophisticated malware campaigns are leveraging Node.js features and targeting HR systems in coordinated "payroll pirate" attacks.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability that can be escalated to remote code execution
- **Impact**: Allows local attackers to access system files without authentication and potentially achieve full system compromise
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: Critical security flaw in Oracle's E-Business Suite (EBS) software exploited since August 2025
- **Impact**: Complete system compromise enabling data theft and lateral movement across enterprise networks
- **Status**: Under active exploitation by CL0P-linked threat actors, affecting dozens of organizations
- **CVE ID**: Not specified in source

### SonicWall SSL VPN Device Compromises
- **Description**: Widespread compromise of SonicWall VPN devices allowing unauthorized network access
- **Impact**: Threat actors are authenticating into multiple customer accounts and environments
- **Status**: Active ongoing compromise affecting over 100 accounts

### Fortra GoAnywhere MFT Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer system
- **Impact**: Unauthorized access to file transfer systems and potential data exfiltration
- **Status**: Previously exploited, now patched with full timeline disclosed
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to local file inclusion attacks
- **Oracle E-Business Suite**: Enterprise resource planning software used by large organizations
- **SonicWall SSL VPN Devices**: Network security appliances providing remote access capabilities
- **Fortra GoAnywhere MFT**: Managed file transfer solutions used for secure data exchange
- **Edge Devices**: Consumer networking equipment targeted by RondoDox botnet
- **npm Registry**: JavaScript package repository compromised with 175 malicious packages
- **University HR Systems**: Human resources management platforms targeted in payroll diversion attacks

## Attack Vectors and Techniques

- **Tool Abuse**: Weaponization of legitimate Velociraptor DFIR tool for ransomware deployment and persistent access
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software
- **VPN Compromise**: Authentication bypass and credential compromise on network security devices
- **Supply Chain Attacks**: Distribution of malicious npm packages with over 26,000 downloads for credential harvesting
- **Social Engineering**: Node.js SEA feature abuse through fake game and VPN installers in Stealit malware campaign
- **Account Takeover**: HR system compromise for salary payment redirection
- **Botnet Operations**: Mass exploitation of IoT devices for DDoS attacks via Aisuru botnet

## Threat Actor Activities

- **CL0P-Linked Hackers**: Exploiting Oracle EBS zero-day vulnerability affecting dozens of organizations since August 2025
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group using Velociraptor DFIR tool in LockBit and Babuk ransomware attacks
- **Storm-2657**: "Payroll pirates" targeting university HR employees to hijack salary payments since March 2025
- **ShinyHunters Group**: Operating BreachForums portal for Salesforce extortion before FBI takedown
- **RondoDox Operators**: Managing shotgun-approach botnet targeting edge device vulnerabilities globally
- **Stealit Campaign**: Distributing Node.js-based malware through gaming and VPN installer distribution networks