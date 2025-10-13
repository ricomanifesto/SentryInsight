# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting diverse infrastructure components. The RondoDox botnet has emerged as a particularly aggressive threat, weaponizing over 50 vulnerabilities across more than 30 vendors using an "exploit shotgun" approach to compromise consumer edge devices globally. Simultaneously, threat actors are exploiting a zero-day vulnerability in Gladinet file sharing software, allowing unauthorized access to system files without authentication. Additional concerning activities include widespread compromise of SonicWall VPN devices affecting over 100 accounts, and the abuse of legitimate security tools like Velociraptor DFIR by ransomware operators. A critical vulnerability in Oracle E-Business Suite has also been disclosed, enabling unauthorized data access without login credentials.

## Active Exploitation Details

### Gladinet CentreStack and Triofox Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Gladinet CentreStack and Triofox file sharing products that allows local attackers to access system files without authentication
- **Impact**: Unauthorized access to sensitive system files and data without requiring valid credentials
- **Status**: Currently being actively exploited by threat actors; patch status unclear
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Authentication Bypass
- **Description**: A fresh security flaw in Oracle's E-Business Suite that enables unauthorized access to sensitive data
- **Impact**: Attackers can access sensitive business data without requiring login credentials
- **Status**: Oracle has issued a security alert; exploitation potential confirmed

### Fortra GoAnywhere MFT Critical Vulnerability
- **Description**: A critical security flaw in GoAnywhere Managed File Transfer that came under active exploitation
- **Impact**: Compromise of managed file transfer systems and potential data exfiltration
- **Status**: Has been actively exploited; Fortra has provided full timeline of exploitation and remediation
- **CVE ID**: CVE-2025-10035

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: Botnet campaign exploiting over 50 vulnerabilities across 30+ vendors using a "shotgun" approach
- **Impact**: Widespread compromise of consumer edge devices and network infrastructure
- **Status**: Ongoing active exploitation campaign targeting multiple vendor products

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices affecting multiple customer environments
- **Impact**: Unauthorized access to corporate networks and potential lateral movement
- **Status**: Active compromise affecting over 100 accounts across multiple organizations

## Affected Systems and Products

- **Gladinet CentreStack and Triofox**: File sharing and storage platforms vulnerable to authentication bypass
- **Oracle E-Business Suite**: Enterprise resource planning systems at risk of unauthorized data access
- **Fortra GoAnywhere MFT**: Managed file transfer solutions compromised through critical vulnerability
- **SonicWall SSL VPN**: Network access devices experiencing widespread compromise
- **Consumer Edge Devices**: Over 30 vendor products targeted by RondoDox botnet
- **Microsoft Edge IE Mode**: Legacy browser compatibility feature abused as backdoor
- **Velociraptor DFIR Tool**: Legitimate incident response tool weaponized for ransomware attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in file sharing systems
- **Authentication Bypass**: Circumventing login mechanisms to access sensitive data without credentials
- **Botnet Shotgun Approach**: Automated exploitation attempts across multiple vendor products simultaneously
- **VPN Infrastructure Compromise**: Targeting SSL VPN devices for network access and persistence
- **Legitimate Tool Abuse**: Converting security and forensics tools into attack instruments
- **Browser Feature Exploitation**: Using IE Mode backward compatibility as persistence mechanism
- **Node.js SEA Feature Abuse**: Leveraging Single Executable Application feature for malware distribution

## Threat Actor Activities

- **Storm-2603 (CL-CRI-1040)**: Abusing Velociraptor DFIR tool in LockBit ransomware operations for persistent network access
- **Storm-2657 "Payroll Pirates"**: Hijacking HR SaaS accounts to redirect employee salary payments to attacker-controlled accounts
- **RondoDox Operators**: Conducting widespread exploitation campaigns against consumer edge devices using automated attack methods
- **GXC Team Cybercrime Syndicate**: Brazilian-led group dismantled by Spanish authorities, with leader "GoogleXcoder" arrested
- **Astaroth Banking Trojan Group**: Using GitHub as operational backbone for trojan distribution and resilience
- **ChaosBot Operators**: Deploying Rust-based backdoor using Discord channels for command and control communications