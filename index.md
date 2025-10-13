# Exploitation Report

Current security incidents reveal a concerning landscape of active exploitation activities, with threat actors leveraging zero-day vulnerabilities, abusing legitimate security tools, and conducting widespread compromise campaigns. The most critical concerns include active exploitation of CVE-2025-11371 in Gladinet file sharing software allowing unauthorized system access, widespread SonicWall SSL VPN compromises affecting over 100 customer accounts, and the active exploitation of CVE-2025-10035 in Fortra's GoAnywhere MFT platform. Additionally, threat actors are weaponizing legitimate security tools like Velociraptor for ransomware operations and employing sophisticated botnets for record-breaking DDoS attacks against U.S. infrastructure.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication, with exploitation escalating from Local File Inclusion (LFI) to Remote Code Execution (RCE)
- **Impact**: Unauthorized access to sensitive system files and potential full system compromise
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: A critical security flaw in GoAnywhere Managed File Transfer platform under active exploitation
- **Impact**: Potential unauthorized access to file transfer systems and sensitive data
- **Status**: Actively exploited, with complete investigation timeline revealed by vendor
- **CVE ID**: CVE-2025-10035

### Oracle E-Business Suite Unauthorized Access Bug
- **Description**: A fresh security flaw allowing unauthorized access to sensitive data without login credentials
- **Impact**: Direct access to sensitive business data and systems
- **Status**: Security alert issued by Oracle, patch status unclear

### SonicWall SSL VPN Widespread Compromise
- **Description**: Large-scale compromise of SonicWall SSL VPN devices enabling access to multiple customer environments
- **Impact**: Unauthorized access to corporate networks and potential lateral movement
- **Status**: Over 100 customer accounts compromised, ongoing investigation

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and synchronization platforms with zero-day vulnerability
- **Fortra GoAnywhere MFT**: Managed file transfer solutions experiencing active exploitation
- **Oracle E-Business Suite**: Enterprise business applications with unauthorized access vulnerability
- **SonicWall SSL VPN**: Network security appliances with widespread authentication compromise
- **Node.js Applications**: Single Executable Applications feature abused by Stealit malware
- **npm Registry**: 175 malicious packages with 26,000 downloads targeting credential harvesting
- **Consumer Edge Devices**: Various IoT devices compromised by RondoDx botnet exploitation
- **U.S. ISP Infrastructure**: AT&T, Comcast, and Verizon networks affected by Aisuru botnet DDoS attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities for system access
- **Legitimate Tool Abuse**: Weaponization of Velociraptor DFIR tool for ransomware operations
- **Social Engineering**: Fake inflation refund SMS campaigns targeting New York residents
- **Supply Chain Attacks**: Malicious npm packages disguised as legitimate software libraries
- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub for resilient command and control
- **Discord C2 Communications**: ChaosBot malware leveraging Discord channels for victim control
- **VPN Authentication Bypass**: Compromise of SSL VPN authentication mechanisms
- **Payroll Diversion**: Storm-2657 hijacking HR SaaS accounts to redirect salary payments

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Abusing Velociraptor tool in LockBit ransomware campaigns for persistent access
- **Storm-2657**: "Payroll Pirates" targeting HR SaaS platforms to divert employee salary payments
- **GXC Team**: Dismantled cybercrime syndicate led by "GoogleXcoder," 25-year-old Brazilian arrested
- **ShinyHunters**: Salesforce extortion operations disrupted by FBI takedown of BreachForums portal
- **Astaroth Operators**: Banking trojan campaign using GitHub infrastructure for operational resilience
- **ChaosBot Developers**: Rust-based backdoor utilizing Discord for command and control operations
- **Stealit Campaign**: Node.js SEA feature abuse for malware distribution via game and VPN installers
- **RondoDx Botnet**: "Exploit shotgun" approach targeting consumer edge device vulnerabilities
- **Aisuru Botnet**: Record-breaking DDoS attacks leveraging compromised IoT devices on U.S. ISPs