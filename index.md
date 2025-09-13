# Exploitation Report

Critical cybersecurity threats are currently manifesting through multiple active exploitation campaigns, including sophisticated spyware attacks targeting Apple devices and new ransomware strains bypassing fundamental security protections. The most severe activities involve a Samsung Android zero-day vulnerability (CVE-2025-21043) being exploited in active attacks, a new HybridPetya ransomware campaign that can bypass UEFI Secure Boot using CVE-2024-7344, and ongoing spyware campaigns against French Apple users. Additionally, CISA has warned of active exploitation of a critical remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing system, highlighting the expanding attack surface across enterprise and consumer platforms.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been exploited in zero-day attacks
- **Impact**: Allows attackers to compromise Samsung Android devices through active exploitation
- **Status**: Samsung has released monthly security updates including a fix for this vulnerability
- **CVE ID**: CVE-2025-21043

### HybridPetya Ransomware UEFI Bypass
- **Description**: A new ransomware strain that can bypass UEFI Secure Boot protection and install malicious applications on the EFI System Partition
- **Impact**: Complete system compromise despite UEFI Secure Boot protections, with ransomware deployment capabilities
- **Status**: Actively being used in attacks, exploiting a known vulnerability
- **CVE ID**: CVE-2024-7344

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: Critical remote code execution vulnerability in DELMIA Apriso manufacturing operations management system
- **Impact**: Remote code execution capabilities allowing complete system compromise
- **Status**: Actively exploited according to CISA warnings

### Apple Spyware Campaign Targeting French Users
- **Description**: Fourth spyware campaign in 2025 targeting Apple device users in France with sophisticated attacks
- **Impact**: Device compromise and surveillance capabilities against targeted individuals
- **Status**: Ongoing campaign with Apple issuing user notifications and CERT-FR confirmation

### Cursor Security Flaw
- **Description**: Critical security vulnerability in Cursor that could expose user code to malware through automatic command execution
- **Impact**: Code exposure and potential malware infection through compromised development environment
- **Status**: Vulnerability disclosed with mitigation measures available

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices vulnerable to CVE-2025-21043 exploitation
- **UEFI Systems**: Systems with UEFI Secure Boot affected by HybridPetya ransomware bypass capabilities
- **Dassault DELMIA Apriso**: Manufacturing operations management systems actively being targeted
- **Apple Devices**: iPhones and other Apple devices in France targeted by spyware campaigns
- **Cursor Development Environment**: Code editor users potentially exposed to malware through security flaw
- **Solar-Powered Highway Infrastructure**: Transportation department devices containing undocumented radio components

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities in Samsung Android devices
- **UEFI Bypass Techniques**: HybridPetya ransomware circumventing Secure Boot protections through CVE-2024-7344
- **Remote Code Execution**: Direct exploitation of manufacturing systems through network-accessible vulnerabilities
- **Spyware Deployment**: Sophisticated targeting of specific user populations through Apple device compromise
- **Supply Chain Concerns**: Undocumented radio components in critical infrastructure devices

## Threat Actor Activities

- **Spyware Operators**: Conducting fourth major campaign in 2025 specifically targeting French Apple users with sophisticated attacks
- **HybridPetya Operators**: Deploying new ransomware variant capable of bypassing fundamental security protections
- **Manufacturing System Attackers**: Actively exploiting Dassault systems according to CISA threat intelligence
- **Mobile Device Attackers**: Leveraging Samsung Android zero-day for device compromise campaigns