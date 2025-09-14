# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems through sophisticated attacks. Samsung has disclosed a zero-day vulnerability being actively exploited in Android attacks, while Apple continues to face spyware campaigns targeting French users. Additionally, threat actors UNC6040 and UNC6395 are conducting data theft operations against Salesforce platforms, and CISA has warned of active exploitation of a critical remote code execution flaw in Dassault manufacturing systems. A new ransomware strain called HybridPetya has also emerged with the capability to bypass UEFI Secure Boot protections.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Attackers can successfully compromise Samsung Android devices through active exploitation
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Apple Spyware Campaign
- **Description**: Fourth spyware campaign in 2025 targeting Apple devices, specifically affecting French users
- **Impact**: Enables sophisticated surveillance and data collection from targeted Apple devices
- **Status**: Apple has issued warnings to affected users; CERT-FR has confirmed the campaign

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: Critical remote code execution vulnerability in DELMIA Apriso manufacturing operations management application
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited according to CISA warning

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware strain capable of bypassing UEFI Secure Boot feature to install malicious applications on EFI System Partition
- **Impact**: Can compromise systems even with Secure Boot enabled, leading to complete system encryption and ransom demands
- **Status**: Recently discovered and actively spreading

### Cursor Security Flaw
- **Description**: Critical security vulnerability in Cursor code editor that could expose user code to malware
- **Impact**: Automatic command execution vulnerability that could compromise development environments and source code
- **Status**: Fix available by disabling vulnerable feature

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices vulnerable to CVE-2025-21043 zero-day exploitation
- **Apple iOS Devices**: French users specifically targeted in ongoing spyware campaigns
- **DELMIA Apriso**: Manufacturing operations management systems facing active RCE exploitation
- **UEFI-enabled Systems**: Devices with UEFI Secure Boot vulnerable to HybridPetya ransomware bypass techniques
- **Cursor Code Editor**: Development environments using Cursor with default configurations at risk
- **Salesforce Platforms**: Organizations using Salesforce targeted by UNC6040 and UNC6395 threat groups

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Samsung Android vulnerability
- **Spyware Deployment**: Sophisticated spyware installation on Apple devices for surveillance operations
- **Remote Code Execution**: Network-based attacks against Dassault manufacturing systems
- **UEFI Secure Boot Bypass**: Advanced technique allowing ransomware installation despite security protections
- **Automatic Command Execution**: Exploitation of default configurations in development tools
- **Salesforce Platform Compromise**: Targeted attacks against cloud-based business platforms

## Threat Actor Activities

- **UNC6040**: Conducting data theft attacks specifically targeting Salesforce platforms with established indicators of compromise
- **UNC6395**: Operating alongside UNC6040 in coordinated Salesforce targeting campaigns with FBI-released IoCs
- **Spyware Operators**: Conducting fourth campaign of 2025 against French Apple users with sophisticated targeting capabilities
- **HybridPetya Authors**: Developing advanced ransomware with UEFI bypass capabilities for maximum system compromise
- **Samsung Android Attackers**: Successfully exploiting zero-day vulnerability before patch availability