# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with threat actors targeting enterprise file sharing systems, Oracle E-Business Suite installations, and VPN infrastructure. The most severe activity involves CVE-2025-11371 affecting Gladinet CentreStack and TrioFox products, where attackers achieve remote code execution through local file inclusion vulnerabilities. Additionally, threat actors linked to CL0P ransomware have exploited Oracle E-Business Suite since August 2025, impacting dozens of organizations. Chinese threat group Storm-2603 has weaponized legitimate forensics tools for persistent access in ransomware campaigns, while widespread SonicWall VPN compromises have affected over 100 accounts across multiple organizations.

## Active Exploitation Details

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: A zero-day vulnerability allowing local attackers to access system files without authentication through local file inclusion (LFI) that escalates to remote code execution (RCE)
- **Impact**: Attackers can gain unauthorized system access and execute arbitrary code remotely
- **Status**: Actively exploited in the wild, currently unpatched
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: A zero-day security flaw in Oracle's E-Business Suite (EBS) software that has been exploited by CL0P-linked threat actors
- **Impact**: Dozens of organizations compromised through exploitation of this vulnerability
- **Status**: Actively exploited since August 9, 2025, linked to CL0P ransomware operations

### Fortra GoAnywhere Managed File Transfer Vulnerability
- **Description**: A critical security flaw in GoAnywhere Managed File Transfer (MFT) system
- **Impact**: Allows attackers to compromise file transfer systems and potentially access sensitive data
- **Status**: Under active exploitation with full timeline revealed by Fortra
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices allowing unauthorized access to corporate networks
- **Impact**: Over 100 customer accounts compromised with threat actors gaining authenticated access to multiple environments
- **Status**: Actively compromised across multiple organizations

## Affected Systems and Products

- **Gladinet CentreStack and TrioFox**: File sharing and collaboration platforms vulnerable to zero-day exploitation
- **Oracle E-Business Suite (EBS)**: Enterprise resource planning software targeted by CL0P-linked attackers
- **Fortra GoAnywhere MFT**: Managed file transfer solution with critical vulnerability under exploitation
- **SonicWall SSL VPN Devices**: Network security appliances experiencing widespread authentication bypasses
- **Consumer Edge Devices**: Various IoT and networking equipment targeted by RondoDox botnet
- **npm Package Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise software systems
- **Legitimate Tool Abuse**: Weaponization of Velociraptor DFIR tool by Storm-2603 for persistent network access
- **VPN Authentication Bypass**: Compromise of SSL VPN devices to gain authenticated network access
- **Supply Chain Attacks**: Distribution of malicious npm packages for credential phishing campaigns
- **Social Engineering**: Payroll piracy attacks targeting HR employees at universities
- **Malware Distribution**: Stealit malware campaign using Node.js Single Executable Applications via game and VPN installers

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Chinese threat group using Velociraptor DFIR tool in LockBit and Babuk ransomware attacks for persistent network access
- **Storm-2657**: Cybercrime gang conducting "payroll pirate" attacks targeting university HR employees to hijack salary payments since March 2025
- **CL0P-Linked Hackers**: Exploiting Oracle E-Business Suite zero-day vulnerability since August 2025, compromising dozens of organizations
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks and Salesforce extortion campaigns until FBI takedown
- **RondoDox Botnet Operators**: Conducting "exploit shotgun" attacks against consumer edge devices worldwide
- **Aisuru Botnet**: Leveraging compromised IoT devices from major US ISPs (AT&T, Comcast, Verizon) for record-breaking DDoS attacks