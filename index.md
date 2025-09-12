# Exploitation Report

Critical security threats are actively targeting users across multiple platforms and sectors. A significant zero-day vulnerability in Samsung Android devices has been exploited in targeted attacks, while advanced ransomware is bypassing fundamental security measures like UEFI Secure Boot. Additionally, a critical remote code execution vulnerability in industrial manufacturing systems is under active exploitation, and sophisticated spyware campaigns continue targeting high-profile users. These incidents highlight the evolving threat landscape where attackers are successfully circumventing modern security protections and exploiting both known and unknown vulnerabilities.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Attackers can compromise Android devices through targeted exploitation
- **Status**: Samsung has released monthly security updates that include a fix for this actively exploited vulnerability
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: A critical remote code execution flaw in DELMIA Apriso, a manufacturing operations management (MOM) application
- **Impact**: Attackers can execute arbitrary code remotely on affected manufacturing systems
- **Status**: CISA has issued warnings about active exploitation in the wild

### HybridPetya UEFI Secure Boot Bypass
- **Description**: A new ransomware strain that exploits a vulnerability to bypass UEFI Secure Boot protections and install malicious applications on the EFI System Partition
- **Impact**: Complete system compromise, encryption of data, and persistence at the firmware level
- **Status**: Active ransomware campaigns utilizing this technique have been discovered
- **CVE ID**: CVE-2024-7344

## Affected Systems and Products

- **Samsung Android Devices**: Various Samsung Android models affected by the zero-day vulnerability
- **DELMIA Apriso**: Manufacturing operations management applications in industrial environments
- **UEFI Systems**: Computers with UEFI firmware vulnerable to Secure Boot bypass techniques
- **Apple iOS Devices**: French users targeted in ongoing spyware campaigns
- **Windows 11 23H2**: Home and Pro editions approaching end of support, creating potential security risks
- **Solar-Powered Infrastructure**: Highway infrastructure devices with undocumented radio capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of previously unknown vulnerabilities in Samsung Android devices
- **Remote Code Execution**: Network-based attacks against manufacturing management systems
- **UEFI Firmware Manipulation**: Advanced ransomware bypassing Secure Boot protections through firmware-level exploitation
- **Spyware Deployment**: Targeted campaigns against specific user groups using sophisticated surveillance tools
- **Infrastructure Compromise**: Potential risks from undocumented communication capabilities in critical infrastructure

## Threat Actor Activities

- **Mobile Device Attackers**: Conducting zero-day attacks against Samsung Android users with targeted exploitation campaigns
- **Industrial System Attackers**: Actively exploiting manufacturing operations management systems for unauthorized access and potential operational disruption
- **Ransomware Operators**: Deploying HybridPetya ransomware with advanced UEFI bypass capabilities for maximum system compromise and persistence
- **State-Sponsored Groups**: Conducting sophisticated spyware campaigns targeting French users through multiple waves of attacks in 2025
- **Infrastructure Threat Actors**: Potential exploitation of undocumented radio capabilities in solar-powered highway infrastructure devices