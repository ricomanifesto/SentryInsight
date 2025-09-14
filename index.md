# Exploitation Report

The current threat landscape shows critical active exploitation across multiple platforms and devices. Samsung has confirmed a zero-day vulnerability being exploited in Android attacks, while Apple continues to face targeted spyware campaigns affecting French users. Meanwhile, CISA has issued warnings about active exploitation of a Dassault manufacturing system vulnerability, and new ransomware variants are bypassing security protections. Additional concerns include vulnerabilities in popular development tools and undocumented communication capabilities in infrastructure devices.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: Critical zero-day vulnerability in Samsung Android devices being actively exploited in targeted attacks
- **Impact**: Allows attackers to compromise Android devices and potentially gain elevated privileges
- **Status**: Fixed in Samsung's latest monthly security update
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: Critical remote code execution vulnerability in DELMIA Apriso manufacturing operations management application
- **Impact**: Enables attackers to execute arbitrary code remotely on affected manufacturing systems
- **Status**: Actively exploited in the wild, CISA has added to Known Exploited Vulnerabilities catalog

### Apple Spyware Campaign
- **Description**: Fourth spyware campaign in 2025 targeting Apple device users in France
- **Impact**: Allows sophisticated surveillance and data collection from targeted individuals
- **Status**: Active exploitation confirmed by Apple user notifications and CERT-FR advisory

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware strain capable of bypassing UEFI Secure Boot protections
- **Impact**: Can install malicious applications on EFI System Partition, compromising boot-level security
- **Status**: Recently discovered and actively deployed by threat actors

### Cursor IDE Security Vulnerability
- **Description**: Critical security flaw in Cursor development environment that could expose source code
- **Impact**: Potential exposure of sensitive code and automatic execution of malicious commands
- **Status**: Vulnerability disclosed with mitigation steps available

## Affected Systems and Products

- **Samsung Android Devices**: Devices running affected Android versions prior to latest security update
- **DELMIA Apriso**: Manufacturing operations management systems across industrial environments
- **Apple iOS Devices**: iPhones and iPads belonging to targeted French users
- **UEFI Systems**: Computers with UEFI Secure Boot that may be vulnerable to HybridPetya
- **Cursor IDE**: Development environments using Cursor code editor
- **Solar-Powered Infrastructure**: Highway infrastructure devices with undocumented radio capabilities
- **Salesforce Platforms**: Customer relationship management systems targeted by UNC6040 and UNC6395

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of previously unknown vulnerabilities in Samsung Android systems
- **Remote Code Execution**: Network-based attacks against manufacturing management systems
- **Spyware Deployment**: Sophisticated surveillance tools deployed against high-value targets
- **UEFI Compromise**: Boot-level infection bypassing traditional security measures
- **Supply Chain Infiltration**: Undocumented radio capabilities in infrastructure devices
- **Platform Abuse**: Misuse of legitimate Salesforce platforms for data theft operations

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups actively targeting Salesforce platforms for data theft operations, with FBI releasing indicators of compromise
- **HybridPetya Operators**: Ransomware group deploying advanced techniques to bypass UEFI security protections
- **State-Sponsored Actors**: Sophisticated threat actors conducting targeted spyware campaigns against French Apple users
- **Manufacturing Sector Attackers**: Threat actors specifically targeting industrial manufacturing operations management systems through Dassault vulnerabilities