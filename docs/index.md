# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting enterprise infrastructure, open-source components, and web applications. The most severe incidents include a maximum-severity authentication bypass flaw in Cisco SD-WAN controllers (CVE-2026-20182), a zero-day Exchange Server vulnerability (CVE-2026-42897), and widespread exploitation of WordPress plugins. Supply chain attacks have compromised popular npm packages and TanStack libraries, affecting major organizations including OpenAI. Russian state-sponsored groups continue to evolve their persistent backdoors, while cybercriminals exploit content management systems for financial gain and credential theft.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller that allows attackers to bypass authentication mechanisms
- **Impact**: Attackers can gain administrative access to SD-WAN controllers without valid credentials
- **Status**: Actively exploited in limited attacks, patches available from Cisco
- **CVE ID**: CVE-2026-20182

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: High-severity vulnerability in on-premise Exchange Server allowing arbitrary code execution via crafted email messages
- **Impact**: Threat actors can execute arbitrary code through cross-site scripting (XSS) attacks
- **Status**: Under active exploitation, Microsoft has provided mitigations
- **CVE ID**: CVE-2026-42897

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical security vulnerability in the Funnel Builder plugin for WordPress enabling malicious code injection
- **Impact**: Attackers inject malicious JavaScript into WooCommerce checkout pages to steal credit card information
- **Status**: Actively exploited in the wild for payment card skimming attacks

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the Burst Statistics WordPress plugin
- **Impact**: Hackers obtain admin-level access to WordPress websites
- **Status**: Currently being exploited by threat actors

### node-ipc npm Package Compromise
- **Description**: Popular inter-process communication package compromised with credential-stealing malware
- **Impact**: Supply chain attack targeting npm ecosystems to steal user credentials
- **Status**: Malicious versions published and distributed

### TanStack Supply Chain Attack
- **Description**: Supply chain attack targeting TanStack libraries affecting hundreds of npm and PyPI packages
- **Impact**: Compromise of developer environments and potential code-signing certificate exposure
- **Status**: Active attack affecting major organizations including OpenAI

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controller**: Authentication bypass vulnerability affecting network infrastructure
- **Microsoft Exchange Server**: On-premise versions vulnerable to XSS-based code execution
- **WordPress Plugins**: Funnel Builder, Burst Statistics, and Avada Builder plugins with various vulnerabilities
- **npm Ecosystem**: node-ipc package and TanStack libraries compromised in supply chain attacks
- **Windows 11 and Microsoft Edge**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own Berlin 2026
- **OpenClaw Framework**: Four vulnerabilities enabling data theft and privilege escalation
- **WooCommerce**: Checkout pages targeted for payment card skimming through plugin vulnerabilities

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct exploitation of authentication mechanisms in network controllers
- **Cross-Site Scripting (XSS)**: Crafted email messages targeting Exchange Server installations
- **Malicious JavaScript Injection**: Code injection into e-commerce checkout pages for payment fraud
- **Supply Chain Poisoning**: Compromise of trusted software packages and libraries
- **Peer-to-Peer Botnets**: Evolution of traditional backdoors into distributed P2P networks
- **Session Token Theft**: Advanced infostealer malware targeting browser sessions and authentication tokens
- **Plugin Vulnerabilities**: Exploitation of WordPress plugin flaws for website compromise

## Threat Actor Activities

- **Secret Blizzard/Turla**: Russian state-sponsored group evolving Kazuar backdoor into modular P2P botnet for persistent access and stealth operations
- **TeamPCP**: Hacker group threatening to leak Mistral AI source code and advertising stolen repositories
- **REMUS Operators**: Cybercriminals operating session-theft focused infostealer-as-a-service platform
- **WordPress Plugin Exploiters**: Multiple threat actors targeting various WordPress plugins for website compromise and financial fraud
- **Supply Chain Attackers**: Sophisticated actors compromising popular open-source packages for widespread credential theft