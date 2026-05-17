# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across web infrastructure, Microsoft environments, and enterprise networks. The most severe incidents include active exploitation of a maximum severity Cisco SD-WAN authentication bypass vulnerability (CVE-2026-20182) allowing administrative access, a Microsoft Exchange Server zero-day flaw (CVE-2026-42897) being exploited via crafted emails, and an NGINX vulnerability (CVE-2026-42945) causing worker crashes and potential remote code execution. WordPress sites face widespread attacks through the Funnel Builder plugin for credit card theft and the Burst Statistics plugin for admin access compromise. Supply chain attacks have also emerged as a major threat vector, with compromised npm packages and the TanStack attack affecting OpenAI employee devices.

## Active Exploitation Details

### Microsoft Exchange Server Zero-Day
- **Description**: High-severity vulnerability in on-premise Exchange Server versions allowing arbitrary code execution through cross-site scripting (XSS)
- **Impact**: Threat actors can execute arbitrary code on Exchange servers by sending crafted emails
- **Status**: Actively exploited in the wild; mitigations provided by Microsoft
- **CVE ID**: CVE-2026-42897

### Cisco SD-WAN Controller Authentication Bypass
- **Description**: Maximum severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller
- **Impact**: Attackers gain administrative access to network control systems, compromising entire SD-WAN infrastructure
- **Status**: Actively exploited in zero-day attacks; added to CISA KEV catalog
- **CVE ID**: CVE-2026-20182

### NGINX Worker Crash and RCE
- **Description**: Security flaw affecting both NGINX Plus and NGINX Open Source causing worker process crashes
- **Impact**: Worker crashes and possible remote code execution on web servers
- **Status**: Under active exploitation days after public disclosure
- **CVE ID**: CVE-2026-42945

### Funnel Builder WordPress Plugin
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress enabling malicious code injection
- **Impact**: Injection of malicious JavaScript into WooCommerce checkout pages for credit card skimming
- **Status**: Actively exploited for payment card theft operations

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Attackers obtain admin-level access to WordPress websites
- **Status**: Currently being exploited by threat actors

### Avada Builder WordPress Plugin File Read
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting approximately one million installations
- **Impact**: Arbitrary file reading and sensitive information extraction from website databases
- **Status**: Vulnerabilities disclosed, exploitation potential confirmed

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to email-based exploitation
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure systems with administrative access compromise
- **NGINX Plus and Open Source**: Web servers experiencing worker crashes and potential RCE
- **WordPress Sites**: Multiple plugins including Funnel Builder, Burst Statistics, and Avada Builder
- **WooCommerce Platforms**: E-commerce sites targeted for payment card skimming
- **npm Package Ecosystem**: node-ipc package compromised with credential-stealing malware
- **TanStack Library**: Supply chain compromise affecting hundreds of npm and PyPI packages

## Attack Vectors and Techniques

- **Crafted Email Exploitation**: Exchange Server vulnerabilities triggered through malicious email content
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in SD-WAN controllers
- **WordPress Plugin Injection**: Malicious JavaScript injection into e-commerce checkout processes
- **Supply Chain Poisoning**: Compromised development packages delivering credential theft malware
- **Device-Code Phishing**: Tycoon2FA kit utilizing device-code flows and URL shortening services
- **Session Token Theft**: REMUS infostealer focusing on browser session hijacking over password theft

## Threat Actor Activities

- **Russian State-Sponsored Groups**: Turla/Secret Blizzard transforming Kazuar backdoor into modular P2P botnet for persistent access
- **TeamPCP Hacker Group**: Threatening to leak Mistral AI source code repositories unless buyers are found
- **Tycoon2FA Operators**: Enhanced phishing kit supporting Microsoft 365 account hijacking through device-code attacks
- **E-commerce Skimmer Groups**: Active exploitation of WordPress plugins for payment card data theft
- **Supply Chain Attackers**: Targeting development environments through compromised packages and libraries