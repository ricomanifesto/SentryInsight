# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and services, with threat actors employing sophisticated techniques to compromise organizational data and systems. The most concerning developments include active zero-day exploitation of Samsung Android devices through **CVE-2025-21043**, organized threat clusters **UNC6040** and **UNC6395** systematically compromising Salesforce environments for data theft and extortion, and a new phishing-as-a-service platform **VoidProxy** targeting enterprise cloud accounts. Additionally, CISA has issued warnings about active exploitation of a remote code execution vulnerability in Dassault manufacturing systems, while new ransomware variants are bypassing UEFI security measures, and malicious actors are flooding development platforms with cryptocurrency-stealing extensions.

## Active Exploitation Details

### Samsung Android Zero-Day Vulnerability
- **Description**: A critical security vulnerability in Samsung Android devices that allows attackers to execute zero-day attacks
- **Impact**: Successful exploitation enables attackers to compromise Android devices and potentially gain unauthorized access to sensitive data
- **Status**: Actively exploited in the wild; Samsung has released security patches in their monthly security update
- **CVE ID**: CVE-2025-21043

### Dassault DELMIA Apriso Remote Code Execution Vulnerability
- **Description**: Critical remote code execution flaw affecting DELMIA Apriso manufacturing operations management (MOM) application
- **Impact**: Attackers can achieve remote code execution on affected systems, potentially leading to complete system compromise
- **Status**: Actively exploited according to CISA warning; organizations urged to apply patches immediately

### HybridPetya Ransomware UEFI Bypass
- **Description**: New ransomware variant capable of bypassing UEFI Secure Boot protection mechanisms
- **Impact**: Can install malicious applications on the EFI System Partition, providing persistent access and evading traditional security measures
- **Status**: Recently discovered with active deployment capabilities

## Affected Systems and Products

- **Samsung Android Devices**: All Samsung Android devices affected by the zero-day vulnerability requiring immediate security updates
- **Dassault DELMIA Apriso**: Manufacturing operations management application with critical RCE vulnerability
- **Salesforce Environments**: Enterprise Salesforce deployments targeted by UNC6040 and UNC6395 threat clusters
- **Microsoft 365**: Cloud accounts targeted by VoidProxy phishing service
- **Google Accounts**: Consumer and enterprise Google accounts targeted by VoidProxy platform
- **VSCode and Development Platforms**: Visual Studio Code, Cursor, and Windsurf development environments compromised by malicious extensions
- **UEFI Systems**: Systems with UEFI Secure Boot vulnerable to HybridPetya ransomware bypass techniques

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Samsung Android vulnerability for device compromise
- **Remote Code Execution**: Network-based attacks targeting Dassault manufacturing systems for immediate system control
- **Phishing-as-a-Service**: VoidProxy platform providing turnkey phishing capabilities targeting enterprise cloud authentication
- **Supply Chain Attacks**: WhiteCobra threat actor planting 24 malicious extensions in legitimate development marketplaces
- **UEFI Bypass Techniques**: HybridPetya employing advanced methods to circumvent Secure Boot protections
- **Data Exfiltration and Extortion**: Systematic theft of Salesforce data followed by extortion demands

## Threat Actor Activities

- **UNC6040**: Actively compromising Salesforce environments to steal organizational data and conduct extortion operations against victims
- **UNC6395**: Working in coordination with UNC6040 to target Salesforce platforms for data theft and extortion campaigns
- **VoidProxy Operators**: Deploying new phishing-as-a-service platform specifically designed to bypass third-party SSO protections and compromise Microsoft 365 and Google accounts
- **WhiteCobra**: Conducting supply chain attacks by flooding development platforms with cryptocurrency-stealing extensions targeting developers' digital wallets and sensitive information