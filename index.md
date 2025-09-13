# Exploitation Report

Current cybersecurity threats are dominated by several critical exploitation activities targeting different platforms and systems. Apple devices continue to face sophisticated spyware campaigns, with French authorities confirming the fourth such campaign in 2025 targeting users with advanced surveillance capabilities. Samsung has addressed a critical zero-day vulnerability **CVE-2025-21043** that was actively exploited in Android attacks. Additionally, a new ransomware strain called HybridPetya has emerged with the capability to bypass UEFI Secure Boot protections using **CVE-2024-7344**, while CISA has warned of active exploitation of a remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing software. These incidents highlight the ongoing threat landscape affecting mobile devices, enterprise systems, and critical infrastructure.

## Active Exploitation Details

### Apple Spyware Campaign
- **Description**: Sophisticated spyware attacks targeting Apple device users in France, representing the fourth confirmed campaign in 2025
- **Impact**: Unauthorized surveillance and data collection from targeted individuals' devices
- **Status**: Active exploitation confirmed by CERT-FR following Apple's user notifications

### Samsung Android Zero-Day Vulnerability
- **Description**: Critical security vulnerability in Samsung Android devices that was exploited in zero-day attacks
- **Impact**: Attackers could gain unauthorized access and control over affected Samsung Android devices
- **Status**: Patched in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware strain that exploits a vulnerability to bypass UEFI Secure Boot protections
- **Impact**: Ability to install malicious applications on the EFI System Partition, bypassing critical security measures
- **Status**: Active exploitation using existing vulnerability
- **CVE ID**: CVE-2024-7344

### Dassault DELMIA Apriso RCE Vulnerability
- **Description**: Critical remote code execution flaw in DELMIA Apriso manufacturing operations management software
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Actively exploited according to CISA warning

### Cursor Security Flaw
- **Description**: Critical security vulnerability in Cursor code editor that could expose user code to malware
- **Impact**: Potential compromise of developer environments and source code exposure
- **Status**: Feature disabled by default leaves users vulnerable to automatic command execution

## Affected Systems and Products

- **Apple Devices**: iPhones and other Apple products targeted by sophisticated spyware campaigns
- **Samsung Android Devices**: Affected by critical zero-day vulnerability requiring monthly security updates
- **UEFI Systems**: Devices with UEFI Secure Boot vulnerable to HybridPetya ransomware bypass techniques
- **DELMIA Apriso**: Manufacturing operations management software with critical RCE vulnerability
- **Cursor Code Editor**: Development environment with security flaw affecting code protection
- **Solar-Powered Highway Infrastructure**: Devices containing undocumented radios raising security concerns

## Attack Vectors and Techniques

- **Spyware Deployment**: Sophisticated targeting of specific individuals through Apple device compromise
- **Zero-Day Exploitation**: Immediate exploitation of unpatched Samsung Android vulnerabilities
- **UEFI Secure Boot Bypass**: Exploitation of CVE-2024-7344 to circumvent boot-level security protections
- **Remote Code Execution**: Network-based attacks against manufacturing software systems
- **Supply Chain Concerns**: Undocumented radio components in critical infrastructure devices

## Threat Actor Activities

- **Apple-Targeting Groups**: Continued sophisticated campaigns against high-value targets using advanced spyware techniques
- **Android Exploit Actors**: Groups actively exploiting zero-day vulnerabilities in Samsung devices before patches become available
- **Ransomware Operators**: Development and deployment of HybridPetya with advanced UEFI bypass capabilities
- **Manufacturing Sector Threats**: Targeting of industrial systems through DELMIA Apriso exploitation
- **Infrastructure Threats**: Potential state-level concerns regarding undocumented capabilities in solar-powered highway devices