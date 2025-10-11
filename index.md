# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities under active exploitation, with threat actors targeting enterprise file sharing systems, Oracle business applications, and consumer edge devices. The most severe activity involves CVE-2025-11371 affecting Gladinet CentreStack and Triofox products, which allows local attackers to access system files without authentication. Additionally, CL0P-linked hackers have been exploiting an Oracle E-Business Suite zero-day since August 2025, impacting dozens of organizations. The RondoDox botnet continues its aggressive "exploit shotgun" campaign against consumer edge devices, while sophisticated threat groups like Storm-2603 and Storm-2657 are leveraging legitimate tools for ransomware deployment and payroll theft operations.

## Active Exploitation Details

### Gladinet Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Gladinet CentreStack and Triofox file sharing products that allows local file inclusion (LFI) leading to remote code execution (RCE)
- **Impact**: Allows local attackers to access system files without authentication, potentially leading to complete system compromise
- **Status**: Currently being actively exploited in the wild, unpatched
- **CVE ID**: CVE-2025-11371

### Oracle E-Business Suite Zero-Day
- **Description**: A critical security flaw in Oracle's E-Business Suite (EBS) software being exploited by CL0P-linked threat actors
- **Impact**: Enables unauthorized access to enterprise business applications and data exfiltration
- **Status**: Active exploitation detected since August 9, 2025, affecting dozens of organizations
- **CVE ID**: CVE-2025-10035

### GoAnywhere MFT Critical Vulnerability
- **Description**: A critical security flaw in Fortra's GoAnywhere Managed File Transfer solution
- **Impact**: Enables attackers to compromise file transfer operations and potentially access sensitive data
- **Status**: Actively exploited, full investigation timeline released by Fortra
- **CVE ID**: CVE-2025-10035

## Affected Systems and Products

- **Gladinet CentreStack and Triofox**: File sharing and synchronization products vulnerable to authentication bypass
- **Oracle E-Business Suite (EBS)**: Enterprise resource planning software targeted by CL0P-linked actors
- **GoAnywhere Managed File Transfer**: Fortra's file transfer solution experiencing active exploitation
- **Consumer Edge Devices**: Various IoT and network devices targeted by RondoDox botnet
- **Node.js Applications**: Single Executable Application (SEA) feature abused for malware distribution
- **npm Registry**: 175 malicious packages with 26,000 downloads used in credential phishing
- **Android Devices**: ClayRat spyware targeting mobile users through fake popular apps
- **SonicWall Firewall Systems**: 100% of cloud backup configurations compromised

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in enterprise software for initial access
- **Local File Inclusion (LFI) to RCE**: Escalating file inclusion vulnerabilities to achieve remote code execution
- **Exploit Shotgun Approach**: RondoDx botnet using hit-and-run tactics against multiple edge device vulnerabilities
- **Legitimate Tool Abuse**: Storm-2603 group using Velociraptor DFIR tool for persistent access and ransomware deployment
- **Node.js SEA Abuse**: Stealit malware campaign leveraging Single Executable Application feature for payload distribution
- **Supply Chain Compromise**: Malicious npm packages used for credential harvesting operations
- **Social Engineering**: ClayRat spyware masquerading as legitimate popular applications
- **HR System Targeting**: Payroll pirate attacks focusing on university HR employees and SaaS account hijacking

## Threat Actor Activities

- **CL0P-Linked Actors**: Actively exploiting Oracle E-Business Suite zero-day since August 2025, targeting multiple organizations for data theft and extortion
- **Storm-2603 (Chinese APT)**: Using Velociraptor DFIR tool to maintain persistent access and deploy LockBit and Babuk ransomware in enterprise environments
- **Storm-2657 (Payroll Pirates)**: Conducting sophisticated social engineering campaigns against university HR employees to redirect salary payments since March 2025
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaking and Salesforce extortion until FBI takedown
- **RondoDox Operators**: Deploying widespread botnet attacks against consumer edge devices using automated exploitation techniques
- **Stealit Campaign**: Distributing malware through fake game and VPN installers using Node.js exploitation techniques
- **npm Package Attackers**: Publishing 175 malicious packages for large-scale credential harvesting operations
- **ClayRat Developers**: Creating Android spyware campaigns targeting users through fake versions of popular applications