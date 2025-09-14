# Exploitation Report

The current threat landscape shows several critical vulnerabilities being actively exploited in the wild, with particular focus on high-profile targets. Most significant is Samsung's disclosure of CVE-2025-21043, a critical zero-day vulnerability that has been exploited in targeted Android attacks. Additionally, CISA has issued warnings about active exploitation of a critical remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing operations management platform. Concurrent spyware campaigns are targeting Apple users in France, representing the fourth such campaign in 2025, while cybercriminal groups UNC6040 and UNC6395 continue their data theft operations against Salesforce platforms. A new ransomware strain called HybridPetya has emerged with the concerning capability to bypass UEFI Secure Boot protections, and a critical security flaw in the Cursor code editor could expose developers' code to malware attacks.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: Critical security vulnerability in Samsung's Android implementation that has been exploited in zero-day attacks targeting users
- **Impact**: Successful exploitation allows attackers to compromise Android devices, potentially gaining unauthorized access to sensitive data and device functionality
- **Status**: Samsung has released monthly security updates including a fix for this vulnerability
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw in DELMIA Apriso, a manufacturing operations management (MOM) application used in industrial environments
- **Impact**: Attackers can execute arbitrary code remotely on affected systems, potentially compromising entire manufacturing operations and gaining access to critical industrial infrastructure
- **Status**: CISA has added this vulnerability to its Known Exploited Vulnerabilities catalog due to active exploitation

### Apple Spyware Campaign Targeting French Users
- **Description**: Sophisticated spyware attacks targeting Apple device users in France, representing the fourth such campaign in 2025
- **Impact**: Successful attacks allow threat actors to deploy spyware on targeted devices, enabling surveillance, data theft, and unauthorized access to personal information
- **Status**: Apple has sent threat notifications to affected users; CERT-FR has confirmed the campaign and issued advisory guidance

### Cursor Code Editor Security Flaw
- **Description**: Critical security vulnerability in the Cursor code editor that could expose developers' source code to malware attacks
- **Impact**: Malicious actors could execute commands automatically and access sensitive source code, potentially compromising development environments and intellectual property
- **Status**: Vulnerability involves a feature being disabled by default, leaving users vulnerable to automatic command execution

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware strain with advanced capabilities to bypass UEFI Secure Boot protections by installing malicious applications on the EFI System Partition
- **Impact**: Attackers can deploy ransomware that persists even through system reinstalls and security measures, encrypting data and demanding ransom payments
- **Status**: Recently discovered variant with enhanced evasion techniques actively being deployed

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices affected by CVE-2025-21043 vulnerability
- **DELMIA Apriso**: Manufacturing operations management software used in industrial environments
- **Apple Devices in France**: iPhone and other Apple devices targeted by spyware campaigns
- **Cursor Code Editor**: Development environment used by software developers and organizations
- **UEFI Secure Boot Systems**: Systems relying on UEFI Secure Boot for security protection
- **Salesforce Platforms**: Enterprise Salesforce implementations targeted by cybercriminal groups

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging previously unknown vulnerabilities in Samsung Android devices before patches were available
- **Remote Code Execution**: Direct exploitation of RCE vulnerabilities in manufacturing software to gain system control
- **Spyware Deployment**: Sophisticated targeting of specific user groups with advanced surveillance tools
- **UEFI Boot Process Manipulation**: Advanced technique to bypass security controls by modifying the boot process at the firmware level
- **Social Engineering**: Targeting of Salesforce platforms through credential theft and unauthorized access techniques
- **Automatic Command Execution**: Exploitation of default configuration weaknesses in development tools

## Threat Actor Activities

- **UNC6040 and UNC6395**: Cybercriminal groups actively targeting Salesforce platforms for data theft operations, with FBI releasing indicators of compromise for these threat actors
- **State-Sponsored Actors**: Sophisticated spyware campaigns targeting Apple users in France suggest advanced persistent threat groups with significant resources and capabilities
- **Ransomware Operators**: HybridPetya ransomware developers demonstrating advanced technical capabilities with UEFI bypass techniques
- **Industrial Espionage Groups**: Actors specifically targeting manufacturing operations through DELMIA Apriso vulnerabilities, indicating potential focus on industrial intelligence gathering