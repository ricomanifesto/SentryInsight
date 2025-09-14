# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems, with several zero-day vulnerabilities and recently patched flaws being actively exploited in the wild. The most significant threats include a Samsung Android zero-day vulnerability that has been exploited in targeted attacks, ongoing spyware campaigns targeting Apple users in France, cybercriminal groups conducting data theft operations against Salesforce platforms, a critical Dassault manufacturing system vulnerability being actively exploited, a newly discovered ransomware strain capable of bypassing UEFI security protections, and a critical security flaw in the popular Cursor code editor. Additionally, infrastructure security concerns have emerged with undocumented radio communications discovered in solar-powered highway devices.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Allows attackers to compromise Samsung Android devices through undisclosed attack vectors
- **Status**: Patched in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Apple Spyware Campaign Targeting French Users
- **Description**: Fourth spyware campaign in 2025 targeting Apple device users in France with sophisticated attack methods
- **Impact**: Enables surveillance and data collection from targeted Apple devices
- **Status**: Actively ongoing with Apple issuing user notifications and warnings

### Dassault DELMIA Apriso RCE Vulnerability
- **Description**: Critical remote code execution flaw in DELMIA Apriso manufacturing operations management software
- **Impact**: Allows attackers to execute arbitrary code remotely on affected manufacturing systems
- **Status**: Actively being exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware strain capable of bypassing UEFI Secure Boot protections
- **Impact**: Can install malicious applications on the EFI System Partition, compromising system integrity at the firmware level
- **Status**: Recently discovered and actively being deployed by threat actors

### Cursor Code Editor Critical Security Flaw
- **Description**: Critical vulnerability in the popular Cursor code editor that could expose user code to malware
- **Impact**: Allows automatic execution of malicious commands, potentially compromising developer environments and source code
- **Status**: Feature disabled by default leaves users vulnerable to automatic command execution

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices prior to the latest monthly security update
- **Apple Devices**: iPhones, iPads, and other Apple devices used by targeted individuals in France
- **Dassault DELMIA Apriso**: Manufacturing operations management software installations
- **UEFI-enabled Systems**: Computers with UEFI firmware and Secure Boot functionality
- **Cursor Code Editor**: Development environments using the Cursor AI-powered code editor
- **Salesforce Platforms**: Enterprise Salesforce deployments and associated data systems
- **Solar-Powered Highway Infrastructure**: Transportation department devices with undocumented radio capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Samsung vulnerability exploited before patches were available
- **Spyware Deployment**: Sophisticated spyware campaigns targeting specific user groups
- **Remote Code Execution**: Network-based attacks against manufacturing software
- **Firmware-Level Attacks**: UEFI Secure Boot bypass techniques for persistent malware installation
- **Supply Chain Compromise**: Targeting development environments through code editor vulnerabilities
- **Data Theft Operations**: Systematic extraction of data from cloud-based enterprise platforms
- **Infrastructure Infiltration**: Undocumented communication channels in critical infrastructure devices

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups conducting systematic data theft attacks against Salesforce platforms, with FBI releasing indicators of compromise for both groups
- **State-Sponsored Actors**: Sophisticated spyware campaigns targeting Apple users in France, representing the fourth such campaign in 2025
- **Ransomware Operators**: HybridPetya ransomware group developing advanced techniques to bypass modern security protections
- **Infrastructure Threat Actors**: Unknown actors potentially leveraging undocumented radio capabilities in solar-powered highway infrastructure devices