# Exploitation Report

Critical active exploitation campaigns are currently targeting enterprise environments across multiple vectors. Zero-day vulnerabilities are being exploited in Gladinet file sharing software (CVE-2025-11371) and Oracle E-Business Suite software, with the latter linked to CL0P ransomware operations affecting dozens of organizations. SonicWall SSL VPN devices are experiencing widespread compromise with over 100 accounts impacted, while threat actors are weaponizing legitimate DFIR tools like Velociraptor in ransomware attacks. Additionally, GoAnywhere Managed File Transfer systems have been actively exploited (CVE-2025-10035), and sophisticated malware campaigns are leveraging Node.js features and compromised npm packages for credential harvesting operations.

## Active Exploitation Details

### Gladinet Zero-Day Vulnerability
- **Description**: Local file inclusion vulnerability in Gladinet CentreStack and TrioFox products allowing local attackers to access system files without authentication, escalating to remote code execution
- **Impact**: Attackers can access sensitive system files and potentially achieve full system compromise through RCE capabilities
- **Status**: Active in-the-wild exploitation detected, currently unpatched zero-day
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: Security flaw in Oracle's E-Business Suite (EBS) software enabling unauthorized access and system compromise
- **Impact**: Complete organizational breach with potential data exfiltration and system control
- **Status**: Active exploitation since August 9, 2025, affecting dozens of organizations

### GoAnywhere MFT Critical Vulnerability
- **Description**: Critical security flaw in GoAnywhere Managed File Transfer system allowing unauthorized access
- **Impact**: Compromise of file transfer systems and potential data theft
- **Status**: Active exploitation confirmed, patch timeline revealed by vendor
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread authentication bypass affecting SSL VPN devices enabling unauthorized network access
- **Impact**: Complete network infiltration and access to internal systems across multiple customer environments
- **Status**: Active widespread compromise affecting over 100 accounts

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to zero-day exploitation
- **Oracle E-Business Suite**: Enterprise resource planning software targeted in zero-day attacks
- **GoAnywhere Managed File Transfer**: Secure file transfer solutions under active exploitation
- **SonicWall SSL VPN Devices**: Network security appliances experiencing widespread compromise
- **Consumer Edge Devices**: IoT and networking equipment targeted by RondoDox botnet
- **npm Registry**: JavaScript package repository compromised with 175 malicious packages
- **HR SaaS Platforms**: Human resources software targeted in payroll diversion attacks
- **University Systems**: Educational institutions specifically targeted in payroll pirate campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple unpatched vulnerabilities actively exploited including file sharing software and Oracle EBS
- **Legitimate Tool Abuse**: Velociraptor DFIR tool weaponized for persistent access and ransomware deployment
- **VPN Device Compromise**: SSL VPN authentication bypass enabling network infiltration
- **Supply Chain Attacks**: Malicious npm packages with 26,000+ downloads used for credential phishing
- **Social Engineering**: Game and VPN installer distribution for Stealit malware delivery
- **Account Takeover**: HR system compromise for salary payment diversion
- **Node.js SEA Abuse**: Single Executable Application feature exploited for malware distribution
- **Botnet Operations**: RondoDox and Aisuru botnets targeting edge devices and conducting massive DDoS attacks

## Threat Actor Activities

- **CL0P-Linked Groups**: Exploiting Oracle EBS zero-day since August 2025 affecting dozens of organizations
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group using Velociraptor tool in LockBit and Babuk ransomware operations
- **Storm-2657**: "Payroll Pirates" targeting university HR employees for salary payment hijacking since March 2025
- **ShinyHunters**: Operating BreachForums portal for Salesforce extortion before FBI takedown
- **RondoDox Operators**: Conducting "exploit shotgun" attacks against consumer edge devices globally
- **Aisuru Botnet**: Executing record-breaking DDoS attacks using compromised US ISP-hosted IoT devices
- **Stealit Campaign**: Distributing Node.js-based malware through gaming and VPN installers
- **npm Package Attackers**: Deploying 175 malicious packages for large-scale credential harvesting operations