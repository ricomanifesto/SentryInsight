# Exploitation Report

The current threat landscape reveals significant supply chain attacks targeting developer ecosystems, critical infrastructure vulnerabilities in mail systems and enterprise applications, and ongoing extortion campaigns against educational institutions. The most notable activity includes the Mini Shai-Hulud worm compromising hundreds of npm and PyPI packages from major organizations like TanStack and Mistral AI, critical remote code execution vulnerabilities in Fortinet products and Exim mail servers, and the ShinyHunters extortion group's massive Canvas platform breach affecting educational institutions worldwide. These incidents demonstrate sophisticated attack vectors ranging from package repository compromises to enterprise application vulnerabilities, with attackers increasingly targeting supply chain components and critical infrastructure systems.

## Active Exploitation Details

### Mini Shai-Hulud Supply Chain Attack
- **Description**: A self-propagating worm compromising npm and PyPI packages across multiple major organizations including TanStack, Mistral AI, Guardrails AI, UiPath, and OpenSearch
- **Impact**: Credential theft targeting developers, compromise of signed packages, and potential widespread supply chain contamination
- **Status**: Active ongoing campaign with hundreds of compromised packages identified

### Fortinet FortiSandbox and FortiAuthenticator RCE Vulnerabilities
- **Description**: Critical remote code execution flaws in Fortinet's security appliances allowing attackers to run arbitrary commands
- **Impact**: Complete system compromise of enterprise security infrastructure
- **Status**: Security patches released, exploitation capability confirmed

### Exim BDAT Vulnerability
- **Description**: Severe memory corruption vulnerability in Exim mail server affecting GnuTLS builds
- **Impact**: Potential remote code execution on mail servers
- **Status**: Security updates released to address the vulnerability

### ShinyHunters Canvas Platform Breach
- **Description**: Massive cyberattack targeting Instructure's Canvas learning management system
- **Impact**: 3.65TB of data compromised affecting educational institutions globally, ransom agreement reached to prevent data leak
- **Status**: Data breach concluded with ransom payment, Congressional testimony requested

### CheckMarx Jenkins Plugin Compromise
- **Description**: Official Jenkins Application Security Testing plugin compromised with malicious infostealer
- **Impact**: Credential theft from development environments using the compromised security plugin
- **Status**: Rogue version identified and warned about by CheckMarx

### RubyGems Malicious Package Campaign
- **Description**: Hundreds of malicious packages uploaded to RubyGems package repository
- **Impact**: Supply chain compromise targeting Ruby developers
- **Status**: New account signups suspended, cleanup operations underway

## Affected Systems and Products

- **Fortinet Security Appliances**: FortiSandbox and FortiAuthenticator products with critical RCE vulnerabilities
- **Exim Mail Servers**: GnuTLS builds affected by BDAT vulnerability enabling memory corruption
- **Package Repositories**: npm, PyPI, and RubyGems repositories compromised with malicious packages
- **Educational Platforms**: Canvas LMS affecting millions of students and educators globally
- **Enterprise Development Tools**: Jenkins AST plugin and various AI/ML packages from major vendors
- **SAP Enterprise Applications**: Commerce Cloud and S/4HANA with critical vulnerabilities requiring patching
- **Hugging Face AI Models**: Tokenizer libraries vulnerable to manipulation for data exfiltration
- **Microsoft Products**: 120 vulnerabilities patched in May 2026 Patch Tuesday, including critical flaws

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Compromise of legitimate package repositories and injection of malicious code into trusted packages
- **Package Typosquatting**: Creation of malicious packages with names similar to popular legitimate packages
- **Signed Package Abuse**: Compromise of legitimate packages while maintaining valid digital signatures
- **Remote Code Execution**: Exploitation of memory corruption and input validation flaws in enterprise applications
- **Credential Harvesting**: Deployment of infostealers through compromised development tools and packages
- **Social Engineering**: Targeting of developers through compromised legitimate software distribution channels
- **Network Pivoting**: Use of SOCKS5 proxies and TON networks for command and control communications

## Threat Actor Activities

- **ShinyHunters**: Conducted massive extortion campaign against Instructure's Canvas platform, compromising 3.65TB of educational data and reaching ransom agreement
- **TeamPCP**: Orchestrated the Mini Shai-Hulud supply chain campaign, compromising hundreds of packages across npm and PyPI repositories targeting major tech companies
- **TrickMo Operators**: Deployed new Android banking trojan variant using The Open Network for C2 communications and SOCKS5 for network pivoting
- **Unknown APT Groups**: Targeted automotive manufacturer Škoda's online shop and UK water supplier South Staffordshire Water, demonstrating continued interest in critical infrastructure and consumer data