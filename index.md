# Exploitation Report

Critical security vulnerabilities are being actively exploited across multiple platforms and technologies. The most significant exploitation activities include a zero-day vulnerability in Samsung Android devices that has been actively exploited in attacks, a critical remote code execution flaw in Dassault's DELMIA Apriso manufacturing platform, and sophisticated spyware campaigns targeting Apple users in France. Additionally, threat actors UNC6040 and UNC6395 are conducting data theft operations against Salesforce platforms, while new ransomware strains are developing capabilities to bypass UEFI Secure Boot protections. These exploitation activities demonstrate the evolving threat landscape targeting enterprise platforms, mobile devices, and critical infrastructure systems.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in Samsung Android devices that has been actively exploited in attacks
- **Impact**: Attackers can exploit this vulnerability to compromise Samsung Android devices
- **Status**: Fixed in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: Critical remote code execution vulnerability in DELMIA Apriso, a manufacturing operations management (MOM) application
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in the wild, CISA warning issued

### Apple Spyware Campaign
- **Description**: Sophisticated spyware targeting Apple device users in France
- **Impact**: Allows unauthorized surveillance and data collection from targeted individuals
- **Status**: Fourth spyware campaign identified in 2025, ongoing exploitation confirmed by CERT-FR

### Cursor Security Vulnerability
- **Description**: Critical security flaw in Cursor code editor that could expose user code to malware
- **Impact**: Malicious commands can run automatically, potentially compromising development environments
- **Status**: Feature disabled by default, leaving users vulnerable

## Affected Systems and Products

- **Samsung Android Devices**: Various Samsung Android models affected by zero-day vulnerability
- **DELMIA Apriso**: Manufacturing operations management platform with RCE vulnerability
- **Apple Devices**: iPhone and other Apple devices targeted by spyware campaigns in France
- **Salesforce Platforms**: Enterprise CRM systems targeted by UNC6040 and UNC6395 threat groups
- **Cursor Code Editor**: Popular development tool with security feature disabled by default
- **UEFI Systems**: Systems with Secure Boot feature vulnerable to HybridPetya ransomware bypass
- **Solar-Powered Highway Infrastructure**: Devices containing undocumented radio components

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in Samsung Android devices
- **Remote Code Execution**: Direct exploitation of RCE vulnerabilities in manufacturing systems
- **Spyware Deployment**: Sophisticated surveillance campaigns targeting specific individuals
- **Data Theft Operations**: Targeted attacks against Salesforce platforms for data exfiltration
- **UEFI Secure Boot Bypass**: Advanced ransomware techniques to circumvent boot security measures
- **Supply Chain Concerns**: Undocumented radio components in critical infrastructure devices

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups conducting data theft attacks against Salesforce platforms, with FBI releasing indicators of compromise for these threat actors
- **HybridPetya Operators**: Ransomware group developing advanced capabilities to bypass UEFI Secure Boot protections and install malicious applications on EFI System Partitions
- **Spyware Campaign Actors**: Sophisticated threat actors conducting targeted surveillance operations against Apple users in France, representing the fourth such campaign identified in 2025