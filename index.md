# Exploitation Report

Current threat activity reveals a diverse range of exploitation tactics targeting enterprise platforms, consumer devices, and development environments. The most critical developments include Samsung's disclosure of CVE-2025-21043, a zero-day vulnerability actively exploited in Android attacks, and ongoing campaigns by threat actors UNC6040 and UNC6395 compromising Salesforce environments for data theft and extortion. Additional concerning activities include the emergence of VoidProxy phishing-as-a-service targeting Microsoft 365 and Google accounts, WhiteCobra's cryptocurrency-stealing extensions flooding VSCode marketplaces, and the new HybridPetya ransomware capable of bypassing UEFI Secure Boot protections. CISA has also issued warnings about active exploitation of a Dassault RCE vulnerability and Apple spyware activity following zero-day disclosures.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: Critical security vulnerability in Samsung Android devices being actively exploited in zero-day attacks
- **Impact**: Enables attackers to compromise Android devices through unknown attack vectors
- **Status**: Patched in Samsung's monthly security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso RCE Vulnerability
- **Description**: Critical remote code execution flaw in DELMIA Apriso manufacturing operations management application
- **Impact**: Allows attackers to execute arbitrary code remotely on affected systems
- **Status**: Actively exploited in the wild, CISA warning issued

### Apple Zero-Day Spyware Activity
- **Description**: Sophisticated zero-day vulnerability used in targeted spyware attacks against individuals
- **Impact**: Enables deployment of sophisticated spyware on Apple devices
- **Status**: Previously disclosed, French advisory provides additional details on ongoing activity

## Affected Systems and Products

- **Samsung Android Devices**: All devices running vulnerable Android versions prior to monthly security update
- **DELMIA Apriso**: Manufacturing operations management application by Dassault
- **Apple Devices**: Targeted devices affected by sophisticated spyware campaigns
- **Salesforce Environments**: Enterprise platforms targeted by UNC6040 and UNC6395 threat groups
- **Microsoft 365 Accounts**: Targeted by VoidProxy phishing service
- **Google Accounts**: Targeted by VoidProxy phishing service including SSO-protected accounts
- **VSCode/Cursor/Windsurf**: Development environments targeted by malicious extensions
- **UEFI Secure Boot Systems**: Systems vulnerable to HybridPetya ransomware bypass techniques

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Samsung Android and Apple devices
- **Phishing-as-a-Service**: VoidProxy platform providing turnkey phishing capabilities targeting cloud accounts
- **Supply Chain Attacks**: Malicious extensions planted in legitimate development tool marketplaces
- **UEFI Bypass Techniques**: HybridPetya ransomware bypassing Secure Boot protections to install malicious EFI applications
- **Cloud Platform Compromise**: Direct targeting of Salesforce environments for data theft
- **Remote Code Execution**: Exploitation of RCE vulnerabilities in enterprise manufacturing applications

## Threat Actor Activities

- **UNC6040**: Actively compromising Salesforce environments to steal data and conduct extortion operations
- **UNC6395**: Parallel threat cluster also targeting Salesforce platforms for data theft and extortion campaigns
- **VoidProxy Operators**: Running phishing-as-a-service platform targeting Microsoft 365 and Google accounts with SSO bypass capabilities
- **WhiteCobra**: Cryptocurrency-focused threat actor flooding development tool marketplaces with 24 malicious extensions across VSCode, Cursor, and Windsurf platforms
- **HybridPetya Operators**: Ransomware group deploying advanced techniques to bypass UEFI Secure Boot protections
- **Sophisticated Spyware Groups**: Advanced persistent threat actors conducting targeted surveillance operations against high-value individuals using Apple zero-days