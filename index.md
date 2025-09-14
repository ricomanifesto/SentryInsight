# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities being actively exploited in targeted attacks. Samsung has addressed a critical zero-day vulnerability (CVE-2025-21043) that was exploited in Android attacks, while Apple users in France face ongoing spyware campaigns targeting iOS devices. Additionally, CISA has warned of active exploitation of a critical remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing operations management platform. New ransomware variants like HybridPetya demonstrate advanced capabilities to bypass security measures, and threat actors UNC6040 and UNC6395 continue targeting Salesforce platforms for data theft operations.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: Critical security vulnerability in Samsung Android devices that was exploited in zero-day attacks before patches were available
- **Impact**: Attackers can gain unauthorized access and control over Samsung Android devices
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Apple iOS Spyware Campaign
- **Description**: Fourth spyware campaign in 2025 targeting Apple iOS devices in France, involving sophisticated attacks against targeted individuals
- **Impact**: Unauthorized surveillance and data collection from targeted iPhone users
- **Status**: Active exploitation confirmed by CERT-FR and Apple notifications sent to affected users

### Dassault DELMIA Apriso RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in DELMIA Apriso manufacturing operations management platform
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited according to CISA warning

### HybridPetya Ransomware UEFI Bypass
- **Description**: Advanced ransomware variant capable of bypassing UEFI Secure Boot protection mechanisms
- **Impact**: Complete system compromise and ransomware deployment even on systems with Secure Boot enabled
- **Status**: Recently discovered and actively deployed in attacks

### Cursor Code Editor Security Flaw
- **Description**: Critical security vulnerability in Cursor code editor that could expose user code to malware
- **Impact**: Automatic execution of malicious commands in development environments
- **Status**: Users vulnerable due to feature being disabled by default

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices prior to monthly security update installation
- **Apple iOS Devices**: iPhone users in France targeted by sophisticated spyware campaigns
- **Dassault DELMIA Apriso**: Manufacturing operations management platforms actively targeted
- **UEFI Systems**: Windows systems with Secure Boot vulnerable to HybridPetya ransomware bypass
- **Cursor Code Editor**: Development environments at risk of automatic malware execution
- **Salesforce Platforms**: Enterprise Salesforce implementations targeted by cybercriminal groups
- **Solar-Powered Infrastructure Devices**: Highway infrastructure with undocumented radio components

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Targeting unpatched vulnerabilities in Samsung Android and Apple iOS devices
- **Spyware Deployment**: Sophisticated campaigns using advanced persistent threat techniques against high-value targets
- **Remote Code Execution**: Network-based attacks against manufacturing management systems
- **UEFI Secure Boot Bypass**: Advanced ransomware techniques to circumvent boot-level security protections
- **Malicious Code Injection**: Automatic command execution in development environments through compromised editors
- **Data Theft Operations**: Systematic targeting of cloud-based business platforms for data exfiltration

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups systematically targeting Salesforce platforms for data theft operations, with FBI releasing indicators of compromise
- **Spyware Operators**: Unknown threat actors conducting fourth spyware campaign in 2025 against French Apple users with sophisticated targeting capabilities
- **HybridPetya Operators**: Ransomware group deploying advanced variants capable of bypassing modern security protections
- **Manufacturing Sector Attackers**: Threat actors actively exploiting Dassault systems for potential industrial espionage or disruption