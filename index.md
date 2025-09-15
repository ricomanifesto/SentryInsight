# Exploitation Report

Critical security threats are actively targeting organizations through multiple attack vectors, with several high-impact vulnerabilities being exploited in the wild. Samsung has disclosed CVE-2025-21043, a critical zero-day vulnerability that has been actively exploited in Android attacks. Meanwhile, CISA has issued warnings about active exploitation of a remote code execution vulnerability in Dassault's DELMIA Apriso manufacturing systems. Cybercriminal groups UNC6040 and UNC6395 are conducting sophisticated campaigns targeting Salesforce environments for data theft and extortion. Additionally, threat actors are leveraging malicious code editor extensions and phishing-as-a-service platforms to compromise developer environments and cloud accounts. These activities represent significant risks to enterprise systems, mobile devices, and cloud infrastructure.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that has been actively exploited in zero-day attacks
- **Impact**: Attackers can compromise Android devices running vulnerable Samsung software
- **Status**: Patched in Samsung's monthly Android security updates
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution
- **Description**: A critical remote code execution vulnerability in DELMIA Apriso manufacturing operations management application
- **Impact**: Attackers can execute arbitrary code remotely on affected manufacturing systems
- **Status**: Actively exploited according to CISA warnings
- **CVE ID**: Not specified in the source

## Affected Systems and Products

- **Samsung Android Devices**: All devices running vulnerable versions of Samsung's Android implementation
- **DELMIA Apriso**: Manufacturing operations management (MOM) applications used in industrial environments
- **Salesforce Environments**: Cloud-based CRM and business platforms targeted by UNC6040 and UNC6395 groups
- **Visual Studio Code Ecosystem**: VSCode, Cursor, and Windsurf code editors targeted by malicious extensions
- **Microsoft 365 and Google Accounts**: Cloud productivity platforms targeted by VoidProxy phishing service

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Samsung Android devices
- **Remote Code Execution**: Direct exploitation of manufacturing systems through network-accessible services
- **Malicious Extensions**: WhiteCobra threat actor deploying 24 malicious extensions in VSCode marketplace and Open VSX registry to steal cryptocurrency
- **Phishing-as-a-Service**: VoidProxy platform providing turnkey phishing capabilities targeting cloud accounts
- **Data Theft and Extortion**: Sophisticated campaigns combining data exfiltration with extortion tactics
- **UEFI Secure Boot Bypass**: HybridPetya ransomware capable of bypassing UEFI Secure Boot protections

## Threat Actor Activities

- **UNC6040**: Actively compromising Salesforce environments for data theft and extortion operations
- **UNC6395**: Coordinating with UNC6040 in targeting Salesforce platforms and conducting data theft campaigns
- **WhiteCobra**: Flooding code editor marketplaces with cryptocurrency-stealing extensions targeting developers
- **VoidProxy Operators**: Operating phishing-as-a-service platform specifically designed to compromise Microsoft 365 and Google accounts, including those protected by third-party SSO providers
- **HybridPetya Developers**: Creating advanced ransomware with UEFI Secure Boot bypass capabilities for persistent system compromise