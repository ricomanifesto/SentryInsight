# Exploitation Report

Current threat activity reveals several critical security incidents involving both zero-day vulnerabilities and actively exploited flaws. Most notably, Samsung has addressed a critical zero-day vulnerability (CVE-2025-21043) that was being exploited in Android attacks, while CISA has issued warnings about active exploitation of a remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing software. Additionally, a new ransomware strain called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections using CVE-2024-7344, and Apple has issued its fourth spyware campaign warning to French users in 2025. The security landscape also includes concerns about a critical vulnerability in the popular Cursor code editor and undocumented radio components discovered in solar-powered highway infrastructure devices.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung's Android implementation that was being actively exploited in zero-day attacks
- **Impact**: Allows attackers to compromise Android devices with successful exploitation
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: A critical remote code execution flaw in DELMIA Apriso, a manufacturing operations management (MOM) application
- **Impact**: Enables attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively being exploited in the wild according to CISA warnings
- **CVE ID**: Not specified in the source material

### UEFI Secure Boot Bypass Vulnerability
- **Description**: A vulnerability that allows the HybridPetya ransomware to bypass UEFI Secure Boot protections
- **Impact**: Enables malicious applications to be installed on the EFI System Partition, circumventing security measures
- **Status**: Being exploited by HybridPetya ransomware
- **CVE ID**: CVE-2024-7344

### Cursor Code Editor Security Flaw
- **Description**: A critical security vulnerability in the Cursor code editor that could expose user code to malware
- **Impact**: Potential exposure of source code and automatic execution of malicious commands
- **Status**: Identified as a critical flaw with features disabled by default potentially leaving users vulnerable
- **CVE ID**: Not specified in the source material

## Affected Systems and Products

- **Samsung Android Devices**: Devices running Samsung's Android implementation affected by the zero-day vulnerability
- **DELMIA Apriso**: Manufacturing operations management software experiencing active exploitation
- **UEFI Systems**: Devices with UEFI Secure Boot functionality vulnerable to HybridPetya ransomware bypass
- **Cursor Code Editor**: Popular code editor with critical security vulnerability
- **Apple iOS Devices**: French users targeted by spyware campaigns
- **Solar-Powered Highway Infrastructure**: Devices containing undocumented radio components
- **Windows 11 23H2**: Home and Pro editions approaching end of support in 60 days

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Samsung Android vulnerability exploited before patches were available
- **Remote Code Execution**: Direct exploitation of DELMIA Apriso systems for code execution
- **UEFI Bypass**: HybridPetya ransomware circumventing Secure Boot protections through CVE-2024-7344
- **Ransomware Installation**: Malicious application installation on EFI System Partition
- **Spyware Campaigns**: Targeted attacks against specific user groups (French Apple users)
- **Code Editor Exploitation**: Automatic command execution through disabled security features

## Threat Actor Activities

- **HybridPetya Operators**: Ransomware group deploying new strain capable of bypassing UEFI Secure Boot protections, resembling notorious Petya/NotPetya malware families
- **Android Exploit Actors**: Unknown threat actors conducting sophisticated zero-day attacks against Samsung Android devices
- **Spyware Campaign Operators**: Advanced persistent threat actors targeting French Apple users in ongoing surveillance operations, representing the fourth such campaign in 2025
- **DELMIA Apriso Attackers**: Threat actors actively exploiting manufacturing systems through remote code execution vulnerabilities