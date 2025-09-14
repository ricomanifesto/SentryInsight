# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with significant security implications. Samsung has addressed a critical zero-day vulnerability affecting Android devices that was actively exploited in the wild. Meanwhile, CISA has issued warnings about ongoing exploitation of a critical remote code execution flaw in Dassault's DELMIA Apriso manufacturing software. Additionally, cybercriminal groups UNC6040 and UNC6395 are conducting sophisticated data theft campaigns targeting Salesforce platforms, while Apple users in France are facing their fourth spyware campaign of 2025. A new ransomware strain called HybridPetya has emerged with capabilities to bypass UEFI Secure Boot protections.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Successful exploitation allows attackers to compromise Android devices, potentially leading to unauthorized access and data theft
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Flaw
- **Description**: A critical remote code execution vulnerability in DELMIA Apriso, a manufacturing operations management (MOM) application
- **Impact**: Attackers can execute arbitrary code remotely on affected systems, potentially compromising manufacturing operations
- **Status**: Actively exploited in the wild, CISA has added it to the Known Exploited Vulnerabilities catalog

### Apple Device Spyware Campaign
- **Description**: Sophisticated spyware attacks targeting Apple device users in France
- **Impact**: Allows attackers to conduct surveillance and data collection on targeted individuals
- **Status**: Fourth spyware campaign identified in 2025, actively targeting French users

## Affected Systems and Products

- **Samsung Android Devices**: Various Samsung Android devices affected by the zero-day vulnerability
- **DELMIA Apriso**: Manufacturing operations management software from Dassault Systèmes
- **Apple Devices**: iPhone and other Apple devices targeted in French spyware campaigns
- **Salesforce Platforms**: Cloud-based CRM and business applications targeted by cybercriminal groups
- **UEFI Systems**: Computer systems with UEFI Secure Boot potentially vulnerable to HybridPetya ransomware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of previously unknown vulnerabilities in Samsung Android devices
- **Remote Code Execution**: Network-based attacks targeting Dassault manufacturing software
- **Spyware Deployment**: Sophisticated surveillance malware targeting specific individuals
- **UEFI Secure Boot Bypass**: Advanced ransomware technique that circumvents boot-level security protections
- **Cloud Platform Compromise**: Targeted attacks against Salesforce infrastructure for data theft

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups conducting data theft operations targeting Salesforce platforms with specific indicators of compromise identified by the FBI
- **HybridPetya Operators**: Ransomware group deploying advanced malware capable of bypassing UEFI Secure Boot and installing malicious applications on EFI System Partitions
- **State-Sponsored Actors**: Suspected involvement in sophisticated spyware campaigns targeting Apple users in France, representing the fourth such campaign in 2025