# Exploitation Report

Critical cybersecurity threats are actively targeting multiple platforms with sophisticated exploitation campaigns. Samsung has addressed a critical zero-day vulnerability (CVE-2025-21043) that was being exploited in Android attacks, while Apple continues to face targeted spyware campaigns affecting French users in what CERT-FR confirms as the fourth such campaign in 2025. Additionally, the U.S. CISA has issued warnings about active exploitation of a critical remote code execution vulnerability in Dassault DELMIA Apriso manufacturing systems. Criminal groups UNC6040 and UNC6395 are conducting data theft operations targeting Salesforce platforms, and a new ransomware strain called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that allows attackers to compromise system security
- **Impact**: Enables attackers to execute arbitrary code and potentially gain full control over affected Android devices
- **Status**: Fixed in Samsung's monthly security update; previously exploited as zero-day
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Flaw
- **Description**: Critical remote code execution vulnerability in DELMIA Apriso manufacturing operations management application
- **Impact**: Allows attackers to execute arbitrary code remotely on affected manufacturing systems
- **Status**: Actively exploited in the wild according to CISA warning

### Apple iOS Spyware Exploitation
- **Description**: Sophisticated spyware campaigns targeting Apple device users in France
- **Impact**: Enables surveillance and data collection from targeted individuals' devices
- **Status**: Fourth confirmed campaign in 2025; Apple has sent security notifications to affected users

### Cursor Security Vulnerability
- **Description**: Critical security flaw in the Cursor code editor that could expose source code to malware
- **Impact**: Automatic execution of malicious commands that could compromise development environments
- **Status**: Feature disabled by default leaves users vulnerable; fix available

## Affected Systems and Products

- **Samsung Android Devices**: All devices running affected Samsung Android versions prior to security update
- **Dassault DELMIA Apriso**: Manufacturing operations management software used in industrial environments
- **Apple iOS Devices**: iPhones and iPads belonging to targeted individuals in France
- **Salesforce Platforms**: Enterprise Salesforce implementations targeted by UNC6040 and UNC6395 groups
- **Cursor Code Editor**: Development environments using Cursor with default security configurations
- **UEFI Systems**: Computers with UEFI Secure Boot affected by HybridPetya ransomware
- **Solar-Powered Infrastructure**: Highway infrastructure devices with undocumented radio components

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Samsung Android vulnerability before public disclosure
- **Remote Code Execution**: Network-based attacks targeting Dassault manufacturing systems
- **Spyware Installation**: Sophisticated malware deployment targeting specific individuals on Apple devices
- **Data Theft Operations**: Systematic extraction of sensitive information from Salesforce platforms
- **UEFI Bypass**: Advanced ransomware technique circumventing Secure Boot protections to install malicious EFI applications
- **Supply Chain Infiltration**: Undocumented radio components embedded in critical infrastructure devices

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups conducting coordinated data theft attacks against Salesforce platform users with FBI releasing indicators of compromise for detection
- **HybridPetya Operators**: Ransomware group deploying advanced techniques to bypass UEFI Secure Boot and install persistent malware on EFI System Partitions
- **State-Sponsored Spyware Campaigns**: Sophisticated actors targeting French Apple users in sustained surveillance operations throughout 2025
- **Manufacturing Sector Attackers**: Threat actors specifically targeting industrial control systems through Dassault DELMIA Apriso vulnerabilities