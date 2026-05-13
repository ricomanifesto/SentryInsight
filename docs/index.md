# Exploitation Report

The current threat landscape shows significant supply chain compromise activity with multiple package repositories under attack, alongside critical vulnerabilities in enterprise systems. Notable incidents include the Shai-Hulud worm campaign targeting npm and PyPI packages with credential-stealing malware, and critical remote code execution vulnerabilities discovered in Fortinet's security products. While Microsoft's latest patch cycle notably contains no zero-day vulnerabilities for the first time in two years, threat actors continue to exploit organizational trust relationships and software supply chains to achieve widespread compromise.

## Active Exploitation Details

### Shai-Hulud Supply Chain Attack
- **Description**: A self-propagating worm targeting npm and PyPI package repositories, compromising legitimate packages from major organizations including TanStack, Mistral AI, UiPath, OpenSearch, and Guardrails AI
- **Impact**: Credential theft and potential supply chain poisoning affecting developers who install compromised packages
- **Status**: Active campaign with hundreds of packages compromised across multiple repositories

### RubyGems Malicious Package Campaign
- **Description**: Mass upload of malicious packages to the RubyGems repository forcing temporary suspension of new account registrations
- **Impact**: Potential compromise of Ruby development environments and applications using affected gems
- **Status**: RubyGems has paused new signups to address the attack

### CheckMarx Jenkins Plugin Compromise
- **Description**: Official CheckMarx Jenkins Application Security Testing plugin compromised with information-stealing malware
- **Impact**: Credential theft and potential compromise of CI/CD pipelines using the affected plugin
- **Status**: Rogue version published on Jenkins Marketplace, users advised to verify plugin integrity

### Fortinet FortiSandbox and FortiAuthenticator RCE Vulnerabilities
- **Description**: Critical remote code execution vulnerabilities in Fortinet's security products
- **Impact**: Attackers can execute arbitrary commands or code on affected systems
- **Status**: Security patches released by Fortinet

### Exim BDAT Memory Corruption Vulnerability
- **Description**: Severe security issue in Exim mail transfer agent affecting GnuTLS builds
- **Impact**: Memory corruption leading to potential code execution on mail servers
- **Status**: Security updates released by Exim

## Affected Systems and Products

- **npm and PyPI Package Repositories**: Hundreds of packages compromised including TanStack, Mistral AI, UiPath, OpenSearch, and Guardrails AI packages
- **RubyGems Repository**: Multiple malicious packages uploaded targeting Ruby developers
- **Jenkins CI/CD Platform**: CheckMarx AST plugin compromised with infostealer malware
- **Fortinet Products**: FortiSandbox and FortiAuthenticator systems vulnerable to remote code execution
- **Exim Mail Servers**: GnuTLS builds affected by memory corruption vulnerability
- **Hugging Face AI Models**: Tokenizer library files can be manipulated to hijack model outputs
- **SAP Enterprise Systems**: Commerce Cloud and S/4HANA platforms with critical vulnerabilities
- **Android Banking Applications**: TrickMo banking trojan using TON blockchain for C2 communications

## Attack Vectors and Techniques

- **Package Repository Compromise**: Threat actors uploading malicious versions of legitimate packages to npm, PyPI, and RubyGems repositories
- **Supply Chain Worm Propagation**: Self-replicating malware spreading through package dependencies and development environments
- **Plugin Marketplace Abuse**: Compromising official plugin repositories to distribute malicious code through trusted channels
- **AI Model Manipulation**: Weaponizing tokenizer library files in Hugging Face models to hijack outputs and exfiltrate data
- **Memory Corruption Exploitation**: Leveraging buffer overflow vulnerabilities in mail transfer agents for code execution
- **Blockchain C2 Infrastructure**: Using The Open Network (TON) blockchain for command and control communications in mobile malware

## Threat Actor Activities

- **TeamPCP**: Behind the Shai-Hulud supply chain attack campaign targeting multiple package repositories with credential-stealing worms
- **ShinyHunters**: Extortion group that breached Instructure (Canvas LMS) and reached a ransom agreement to prevent leak of 3.65TB of data
- **TrickMo Operators**: Android banking trojan developers implementing advanced techniques including SOCKS5 proxies and blockchain-based C2 infrastructure
- **Unknown Supply Chain Attackers**: Groups targeting RubyGems repository with mass malicious package uploads and compromising official Jenkins plugins