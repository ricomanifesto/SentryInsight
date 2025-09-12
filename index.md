# Exploitation Report

Critical vulnerabilities are currently being actively exploited in the wild, with several high-impact security issues demanding immediate attention. Samsung has addressed a critical zero-day vulnerability (CVE-2025-21043) that was being exploited in Android attacks, while CISA has issued warnings about active exploitation of a remote code execution flaw in Dassault's DELMIA Apriso manufacturing software. A new ransomware strain called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections using CVE-2024-7344. Additionally, Apple has notified French users of a fourth spyware campaign in 2025, indicating ongoing targeted attacks against iOS devices.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability affecting Samsung Android devices that allows attackers to execute malicious code
- **Impact**: Enables attackers to compromise Android devices and potentially gain unauthorized access to sensitive data
- **Status**: Fixed in Samsung's monthly security updates; previously exploited as zero-day
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: A critical remote code execution vulnerability in DELMIA Apriso, a manufacturing operations management application
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in the wild according to CISA warnings
- **Affected Systems**: Manufacturing operations management systems using DELMIA Apriso

### HybridPetya UEFI Secure Boot Bypass
- **Description**: A vulnerability that allows the HybridPetya ransomware to bypass UEFI Secure Boot protections
- **Impact**: Enables ransomware installation on EFI System Partition, compromising system boot integrity
- **Status**: Actively used by HybridPetya ransomware strain
- **CVE ID**: CVE-2024-7344

## Affected Systems and Products

- **Samsung Android Devices**: Various Samsung Android devices affected by the zero-day vulnerability
- **DELMIA Apriso**: Manufacturing operations management software with RCE vulnerability
- **UEFI-enabled Systems**: Systems with UEFI Secure Boot vulnerable to HybridPetya bypass techniques
- **Apple iOS Devices**: French users targeted by spyware campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Samsung Android devices
- **Remote Code Execution**: Network-based attacks targeting manufacturing systems through DELMIA Apriso
- **UEFI Secure Boot Bypass**: Advanced ransomware techniques to circumvent boot-level security protections
- **Spyware Deployment**: Targeted campaigns against iOS users in France using sophisticated surveillance tools

## Threat Actor Activities

- **Android Attackers**: Unknown threat actors exploiting Samsung zero-day before patch availability
- **Manufacturing Sector Threats**: Cybercriminals targeting industrial systems through DELMIA Apriso vulnerabilities
- **HybridPetya Operators**: Ransomware group utilizing advanced UEFI bypass techniques for system compromise
- **iOS Spyware Campaigns**: Persistent threat actors conducting fourth spyware campaign of 2025 targeting French Apple users