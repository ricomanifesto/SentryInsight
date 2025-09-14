# Exploitation Report

The current cybersecurity landscape reveals several critical exploitation activities, with particular focus on zero-day vulnerabilities affecting major platforms. Samsung has addressed a critical zero-day vulnerability (CVE-2025-21043) that was actively exploited in Android attacks, while CISA has warned of active exploitation targeting Dassault's DELMIA Apriso manufacturing systems. Additionally, Apple users in France have been targeted by a fourth spyware campaign in 2025, demonstrating the persistent threat of sophisticated surveillance attacks. The emergence of HybridPetya ransomware with UEFI Secure Boot bypass capabilities represents a significant evolution in ransomware tactics, while FBI warnings about UNC6040 and UNC6395 groups highlight ongoing threats to Salesforce platforms.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Attackers can compromise Samsung Android devices through active exploitation before patches were available
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Flaw
- **Description**: A critical remote code execution vulnerability in DELMIA Apriso, a manufacturing operations management application
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited according to CISA warnings

### Apple Spyware Campaign
- **Description**: Sophisticated spyware attacks targeting Apple device users in France
- **Impact**: Surveillance and data theft from targeted individuals' Apple devices
- **Status**: Fourth campaign identified in 2025, with Apple issuing user notifications

### HybridPetya Ransomware UEFI Bypass
- **Description**: A newly discovered ransomware strain capable of bypassing UEFI Secure Boot protections
- **Impact**: Can install malicious applications on the EFI System Partition, compromising boot security
- **Status**: Recently discovered and actively spreading

### Cursor Security Flaw
- **Description**: A critical security vulnerability in the Cursor code editor that could expose user code to malware
- **Impact**: Malicious commands can run automatically, potentially compromising development environments
- **Status**: Requires user action to enable security features that are disabled by default

## Affected Systems and Products

- **Samsung Android Devices**: Various Samsung Android models affected by the zero-day vulnerability
- **Dassault DELMIA Apriso**: Manufacturing operations management systems vulnerable to remote code execution
- **Apple iOS Devices**: French users targeted in sophisticated spyware campaigns
- **UEFI Secure Boot Systems**: Devices with UEFI Secure Boot potentially vulnerable to HybridPetya ransomware bypass
- **Cursor Code Editor**: Development environments using Cursor IDE at risk from malware injection
- **Salesforce Platforms**: Enterprise Salesforce implementations targeted by cybercriminal groups

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched Samsung Android vulnerability before disclosure
- **Remote Code Execution**: Network-based attacks against Dassault manufacturing systems
- **Spyware Deployment**: Sophisticated surveillance malware targeting specific Apple device users
- **UEFI Boot Process Manipulation**: Ransomware bypassing hardware-level security protections
- **Social Engineering**: Targeting of Salesforce platforms through credential compromise and platform manipulation
- **Supply Chain Concerns**: Undocumented radio components in solar-powered infrastructure devices

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups actively targeting Salesforce platforms for data theft operations, with FBI releasing indicators of compromise
- **Advanced Persistent Threat Groups**: Sophisticated actors conducting targeted spyware campaigns against Apple users in France
- **Ransomware Operators**: HybridPetya ransomware groups developing advanced techniques to bypass modern security protections
- **Nation-State Actors**: Likely involvement in sophisticated Apple device surveillance campaigns based on targeting patterns