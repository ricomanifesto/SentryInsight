# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple fronts. Critical zero-day vulnerabilities are being actively exploited, with Samsung addressing CVE-2025-21043 in zero-day attacks against Android devices, and CISA warning of active exploitation of a remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing operations management platform. Additionally, a sophisticated new ransomware strain called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections using CVE-2024-7344, while Apple users in France are experiencing their fourth spyware campaign of 2025, following previous zero-day disclosures targeting specific individuals with sophisticated attacks.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability affecting Samsung Android devices that has been exploited in active zero-day attacks
- **Impact**: Attackers can exploit this vulnerability to compromise Android devices, though specific attack outcomes are not detailed in the available information
- **Status**: Samsung has released monthly security updates including a fix for this actively exploited vulnerability
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: A critical remote code execution flaw in DELMIA Apriso, a manufacturing operations management (MOM) application
- **Impact**: Attackers can achieve remote code execution capabilities on affected systems, potentially compromising manufacturing operations and infrastructure
- **Status**: CISA has issued warnings about active exploitation of this vulnerability by threat actors

### HybridPetya UEFI Secure Boot Bypass
- **Description**: A vulnerability that allows the HybridPetya ransomware to bypass UEFI Secure Boot protections and install malicious applications on the EFI System Partition
- **Impact**: Complete system compromise with ransomware deployment, bypassing fundamental boot-level security protections
- **Status**: Actively being exploited by the HybridPetya ransomware strain
- **CVE ID**: CVE-2024-7344

### Apple Spyware Campaign Zero-Day
- **Description**: Sophisticated spyware attacks targeting Apple users, particularly in France, following previous zero-day vulnerability disclosures
- **Impact**: Targeted surveillance and data collection from specific individuals using advanced spyware techniques
- **Status**: Apple has sent notifications to French users about the fourth spyware campaign of 2025, with CERT-FR confirming the alerts

## Affected Systems and Products

- **Samsung Android Devices**: Multiple Android device models affected by the critical zero-day vulnerability
- **Dassault DELMIA Apriso**: Manufacturing operations management platform experiencing active RCE exploitation
- **UEFI Systems**: Systems with UEFI Secure Boot that can be bypassed by HybridPetya ransomware
- **Apple iOS Devices**: iPhones and other Apple devices targeted in French spyware campaigns
- **Cursor Code Editor**: Critical security flaw that could expose code to malware through automatic command execution

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being actively exploited across different platforms including Samsung Android and Apple iOS
- **UEFI Secure Boot Bypass**: Advanced technique allowing ransomware to circumvent boot-level security protections and install on EFI System Partition
- **Spyware Deployment**: Sophisticated targeting of specific individuals using advanced spyware techniques
- **Remote Code Execution**: Critical RCE vulnerabilities in enterprise manufacturing management systems
- **Automatic Code Execution**: Vulnerabilities in development tools that allow malicious commands to run automatically

## Threat Actor Activities

- **HybridPetya Operators**: Deploying advanced ransomware with UEFI Secure Boot bypass capabilities, resembling the notorious Petya/NotPetya campaigns
- **Samsung Android Attackers**: Conducting zero-day attacks against Samsung Android devices with unknown attribution
- **Apple Spyware Campaigns**: Sophisticated threat actors conducting the fourth spyware campaign of 2025 targeting French Apple users, following previous zero-day exploitation patterns
- **Manufacturing Sector Attackers**: Threat actors actively exploiting Dassault DELMIA Apriso systems in manufacturing environments