# Exploitation Report

Critical cybersecurity threats are actively targeting multiple platforms with sophisticated attack campaigns. The most significant exploitation activity involves zero-day attacks against Android devices through Samsung systems, spyware campaigns targeting Apple users in France, and ransomware operations bypassing UEFI security measures. Threat actors UNC6040 and UNC6395 are conducting extensive data theft operations against Salesforce platforms, while CISA has issued warnings about active exploitation of Dassault systems. Additionally, infrastructure concerns have emerged regarding undocumented radio capabilities in solar-powered devices used in transportation systems.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android systems that has been actively exploited in zero-day attacks
- **Impact**: Attackers can compromise Android devices through sophisticated exploitation techniques
- **Status**: Samsung has released monthly security updates including a fix for this actively exploited vulnerability
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: A critical remote code execution flaw in DELMIA Apriso manufacturing operations management software
- **Impact**: Attackers can achieve remote code execution on affected manufacturing systems
- **Status**: CISA has issued warnings about active exploitation of this vulnerability

### Apple Spyware Campaign Targeting French Users
- **Description**: Fourth spyware campaign in 2025 targeting Apple device users in France with sophisticated attack techniques
- **Impact**: Targeted individuals face potential device compromise and data exfiltration through spyware installation
- **Status**: Apple has sent notifications to affected users; CERT-FR has confirmed the campaign

### HybridPetya Ransomware UEFI Bypass
- **Description**: A recently discovered ransomware strain capable of bypassing UEFI Secure Boot protection mechanisms
- **Impact**: Attackers can install malicious applications on the EFI System Partition, compromising system integrity at the firmware level
- **Status**: Active ransomware strain with advanced evasion capabilities

### Cursor Security Flaw
- **Description**: A critical security vulnerability in Cursor code editor that could expose user code to malware
- **Impact**: Organizations and users may be vulnerable to automatically executing malicious commands
- **Status**: Security flaw identified with potential for code exposure

## Affected Systems and Products

- **Samsung Android Devices**: Multiple Android devices affected by zero-day exploitation
- **DELMIA Apriso**: Manufacturing operations management software with critical RCE vulnerability
- **Apple iOS Devices**: French users targeted by sophisticated spyware campaigns
- **UEFI Systems**: Devices with UEFI Secure Boot potentially vulnerable to HybridPetya ransomware bypass
- **Cursor Code Editor**: Development environments at risk of malware exposure
- **Salesforce Platforms**: Enterprise platforms targeted by UNC6040 and UNC6395 threat groups
- **Solar-Powered Infrastructure Devices**: Highway infrastructure systems with undocumented radio capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Sophisticated attacks targeting unpatched Samsung Android vulnerabilities
- **Spyware Deployment**: Advanced persistent threat techniques used against targeted Apple users in France
- **UEFI Secure Boot Bypass**: Ransomware techniques that circumvent firmware-level security protections
- **Remote Code Execution**: Network-based attacks targeting manufacturing management systems
- **Data Theft Operations**: Coordinated campaigns against enterprise Salesforce implementations
- **Automatic Command Execution**: Vulnerability exploitation through disabled security features in development tools

## Threat Actor Activities

- **UNC6040**: Conducting data theft attacks targeting Salesforce platforms with FBI-identified indicators of compromise
- **UNC6395**: Collaborating in sophisticated data theft operations against Salesforce enterprise environments
- **HybridPetya Operators**: Deploying advanced ransomware with UEFI bypass capabilities
- **Apple Spyware Campaigns**: Fourth confirmed spyware operation in 2025 targeting French Apple users with sophisticated attack methods
- **Dassault System Attackers**: Actively exploiting critical RCE vulnerabilities in manufacturing environments