# Exploitation Report

Several critical zero-day vulnerabilities are currently being actively exploited in the wild, representing significant threats to organizations and individuals. Samsung has disclosed a critical zero-day vulnerability being exploited in Android attacks, while CISA has issued warnings about active exploitation of a remote code execution flaw in Dassault manufacturing systems. Additionally, Apple has notified French users of ongoing spyware campaigns, and the FBI has released indicators of compromise for cybercriminal groups targeting Salesforce platforms. A new ransomware strain called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections, while security researchers have identified a critical vulnerability in the popular Cursor code editor that could expose development environments to malware.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Attackers can exploit this vulnerability to compromise Samsung Android devices
- **Status**: Samsung has released monthly security updates that include a fix for this actively exploited vulnerability
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: A critical remote code execution flaw in DELMIA Apriso, a manufacturing operations management (MOM) application
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Currently being actively exploited according to CISA warnings
- **CVE ID**: Not specified in the source article

### Apple Spyware Zero-Day Vulnerability
- **Description**: A zero-day flaw that Apple disclosed was being used in sophisticated spyware attacks against targeted individuals
- **Impact**: Enables sophisticated spyware deployment targeting specific individuals
- **Status**: Actively exploited in spyware campaigns, particularly affecting French users
- **CVE ID**: Not specified in the source article

### Cursor Code Editor Security Vulnerability
- **Description**: A critical security flaw in the popular Cursor code editor that could expose development environments to malware
- **Impact**: Allows automatic execution of malicious commands in development environments
- **Status**: Vulnerability present due to a security feature being disabled by default
- **CVE ID**: Not specified in the source article

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung devices running Android are potentially affected by the zero-day vulnerability
- **DELMIA Apriso**: Manufacturing operations management applications used in industrial environments
- **Apple iOS Devices**: French users specifically targeted in recent spyware campaigns
- **Cursor Code Editor**: Development environments using this popular VS Code alternative
- **UEFI Systems**: Devices with UEFI Secure Boot potentially vulnerable to HybridPetya ransomware bypass techniques
- **Salesforce Platforms**: Enterprise CRM and cloud platforms targeted by cybercriminal groups

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being actively exploited across different platforms
- **Spyware Deployment**: Sophisticated targeting of individuals through Apple device compromises
- **UEFI Secure Boot Bypass**: HybridPetya ransomware can circumvent UEFI Secure Boot protections to install malicious applications on EFI System Partitions
- **Remote Code Execution**: Critical RCE vulnerabilities allowing attackers to execute arbitrary commands on target systems
- **Development Environment Targeting**: Malware designed to compromise developer tools and code repositories
- **Cloud Platform Infiltration**: Direct targeting of enterprise Salesforce implementations for data theft

## Threat Actor Activities

- **UNC6040**: Cybercriminal group targeting Salesforce platforms in coordinated data theft attacks
- **UNC6395**: Second cybercriminal group also focusing on Salesforce platform exploitation for data exfiltration
- **HybridPetya Operators**: Ransomware group deploying advanced techniques to bypass modern security protections including UEFI Secure Boot
- **Apple Spyware Campaign Actors**: Sophisticated threat actors conducting targeted spyware campaigns against French users, representing the fourth such campaign in 2025