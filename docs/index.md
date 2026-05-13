# Exploitation Report

This reporting period reveals several critical security developments across multiple platforms and industries. The most significant exploitation activity centers around supply chain attacks, with the Shai-Hulud campaign compromising hundreds of npm and PyPI packages from major organizations including TanStack, Mistral AI, and Guardrails AI. Critical remote code execution vulnerabilities have been disclosed in Fortinet's FortiSandbox and FortiAuthenticator products, while a severe memory corruption flaw affects Exim mail server configurations. Additional notable incidents include the ShinyHunters extortion group's successful breach of Instructure's Canvas platform affecting millions of users, and the compromise of CheckMarx's official Jenkins plugin with credential-stealing malware.

## Active Exploitation Details

### Shai-Hulud Supply Chain Attack
- **Description**: A sophisticated worm-based campaign targeting npm and PyPI package repositories, compromising official packages from major organizations
- **Impact**: Credential theft, potential system compromise for developers using infected packages, and supply chain contamination affecting downstream users
- **Status**: Active exploitation with hundreds of compromised packages identified; TeamPCP threat actor continues operations

### Fortinet FortiSandbox and FortiAuthenticator RCE Vulnerabilities
- **Description**: Critical remote code execution flaws in Fortinet's security products enabling arbitrary code execution
- **Impact**: Attackers can execute commands or arbitrary code on vulnerable systems, potentially leading to complete system compromise
- **Status**: Security patches released; exploitation potential remains high for unpatched systems

### Exim BDAT Memory Corruption Vulnerability
- **Description**: Severe security flaw in Exim mail server affecting GnuTLS builds, leading to memory corruption and potential code execution
- **Impact**: Remote code execution on vulnerable mail servers, potentially allowing complete system takeover
- **Status**: Security updates released to address the vulnerability

### CheckMarx Jenkins Plugin Compromise
- **Description**: Official CheckMarx Jenkins Application Security Testing plugin compromised and published with malicious code
- **Impact**: Information stealing capabilities targeting development environments and CI/CD pipelines
- **Status**: Rogue version identified and reported; users advised to verify plugin integrity

### ShinyHunters Canvas Platform Breach
- **Description**: Successful compromise of Instructure's Canvas learning management system by ShinyHunters extortion group
- **Impact**: Exposure of personal data from millions of students and educators; 3.65TB of data stolen
- **Status**: Instructure reached "agreement" with attackers to prevent data leak

## Affected Systems and Products

- **Fortinet FortiSandbox**: Critical RCE vulnerabilities requiring immediate patching
- **Fortinet FortiAuthenticator**: Critical RCE vulnerabilities with patch available
- **Exim Mail Server**: GnuTLS builds vulnerable to memory corruption attacks
- **npm and PyPI Packages**: Hundreds of packages from TanStack, Mistral AI, Guardrails AI, UiPath, and OpenSearch compromised
- **Jenkins Marketplace**: Official CheckMarx AST plugin compromised with malware
- **Canvas LMS Platform**: Educational platform serving millions of users worldwide
- **SAP Commerce Cloud**: Critical vulnerabilities patched in May 2026 updates
- **SAP S/4HANA**: Critical flaws addressed in security updates
- **Microsoft Products**: 120 vulnerabilities patched in May 2026 Patch Tuesday
- **Android Devices**: TrickMo banking trojan targeting mobile users

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Malicious packages injected into official repositories to target developers
- **Worm Propagation**: Self-replicating malware spreading across package ecosystems
- **Remote Code Execution**: Exploitation of memory corruption and input validation flaws
- **Social Engineering**: Targeting of development teams through compromised tools
- **Credential Harvesting**: Information stealing malware embedded in legitimate-appearing packages
- **Extortion Operations**: Data theft followed by ransom demands and leak threats
- **C2 Infrastructure**: Use of The Open Network (TON) for command and control communications
- **Network Pivoting**: SOCKS5 proxy implementation for lateral movement

## Threat Actor Activities

- **TeamPCP**: Conducting large-scale supply chain attacks through the Shai-Hulud campaign, targeting major open-source projects
- **ShinyHunters**: Successfully breached Instructure's Canvas platform, stealing 3.65TB of data and conducting extortion operations
- **TrickMo Operators**: Deploying enhanced Android banking trojans with improved C2 capabilities and network pivoting features
- **RubyGems Attackers**: Launched major malicious campaign forcing temporary suspension of new account signups on the platform