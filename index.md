# Exploitation Report

Several critical security incidents are currently unfolding, with active exploitation targeting major platforms and infrastructure systems. The most significant concerns include a zero-day vulnerability in Samsung Android devices that has been exploited in targeted attacks, ongoing spyware campaigns against French Apple users representing the fourth such incident in 2025, and active exploitation of a critical remote code execution flaw in Dassault's DELMIA Apriso manufacturing software. Additionally, threat actors UNC6040 and UNC6395 are conducting sophisticated data theft operations against Salesforce platforms, while a new ransomware strain called HybridPetya has demonstrated the ability to bypass UEFI Secure Boot protections.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: Critical security vulnerability in Samsung Android devices that has been actively exploited in zero-day attacks
- **Impact**: Allows attackers to compromise Samsung Android devices through unknown attack vectors
- **Status**: Patched in Samsung's monthly security update release
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw affecting DELMIA Apriso manufacturing operations management software
- **Impact**: Enables attackers to execute arbitrary code remotely on affected systems, potentially compromising manufacturing operations
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog

### Apple Spyware Campaign Zero-Day
- **Description**: Sophisticated spyware attacks targeting Apple device users, particularly in France, using advanced exploitation techniques
- **Impact**: Allows state-sponsored or sophisticated attackers to install spyware on targeted Apple devices for surveillance purposes
- **Status**: Fourth spyware campaign identified in 2025, with Apple issuing threat notifications to affected users

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware variant capable of bypassing UEFI Secure Boot protections to install malicious applications on the EFI System Partition
- **Impact**: Complete system compromise, ransomware deployment, and potential persistence through firmware-level installation
- **Status**: Recently discovered and actively deployed in attacks

### Cursor Code Editor Security Vulnerability
- **Description**: Critical security flaw in the Cursor code editor that could expose user code to malware through automatically executing commands
- **Impact**: Potential code exposure, malware injection, and compromise of development environments
- **Status**: Identified as critical risk due to default configuration leaving users vulnerable

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices prior to the latest monthly security update
- **Dassault DELMIA Apriso**: Manufacturing operations management software installations
- **Apple iOS/macOS Devices**: Apple devices owned by targeted individuals, particularly in France
- **UEFI Secure Boot Systems**: Systems running UEFI Secure Boot that can be compromised by HybridPetya
- **Salesforce Platforms**: Enterprise Salesforce deployments targeted by threat groups
- **Cursor Code Editor**: Development environments using the Cursor code editor with default configurations

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unknown vulnerabilities in Samsung Android and Apple devices
- **Remote Code Execution**: Network-based attacks against Dassault DELMIA Apriso installations
- **UEFI Firmware Manipulation**: Advanced technique to bypass Secure Boot protections and establish persistence
- **Spyware Installation**: Sophisticated delivery mechanisms for surveillance software on Apple devices
- **Cloud Platform Infiltration**: Targeted attacks against Salesforce environments for data theft
- **Development Environment Compromise**: Exploitation of code editor vulnerabilities to inject malware

## Threat Actor Activities

- **UNC6040 and UNC6395**: Conducting coordinated data theft operations targeting Salesforce platforms, with FBI releasing indicators of compromise for both groups
- **State-Sponsored Actors**: Likely responsible for the sophisticated spyware campaigns against Apple users in France, representing the fourth such campaign in 2025
- **HybridPetya Operators**: Ransomware group deploying advanced techniques to bypass modern security protections
- **Samsung Android Attackers**: Unknown threat actors exploiting the zero-day vulnerability for targeted attacks on Samsung devices