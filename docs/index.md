# Exploitation Report

Critical zero-day and recently disclosed vulnerabilities are experiencing active exploitation across multiple platforms, with threat actors targeting Microsoft Exchange servers, Cisco SD-WAN controllers, and popular WordPress plugins. Notable activities include CVE-2026-42897 affecting Microsoft Exchange Server being exploited via crafted emails, CVE-2026-20182 in Cisco Catalyst SD-WAN Controller allowing authentication bypass for administrative access, and supply chain attacks targeting npm packages. Russian state-sponsored groups have evolved their tools into sophisticated modular botnets, while WordPress sites face ongoing attacks through plugin vulnerabilities that enable credential theft and malicious code injection.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: High-severity Exchange Server vulnerability that allows arbitrary code execution through cross-site scripting (XSS) attacks
- **Impact**: Threat actors can execute arbitrary code on vulnerable Exchange servers
- **Status**: Actively exploited in the wild, Microsoft has shared mitigations
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum-severity authentication bypass flaw in Catalyst SD-WAN Controller
- **Impact**: Attackers can gain administrative access to SD-WAN infrastructure
- **Status**: Actively exploited in limited attacks, patches available
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress
- **Impact**: Injection of malicious JavaScript snippets into WooCommerce checkout pages to steal credit card information
- **Status**: Actively exploited to compromise e-commerce sites

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress plugin Burst Statistics
- **Impact**: Hackers can obtain admin-level access to WordPress websites
- **Status**: Actively exploited for unauthorized administrative access

### Avada Builder WordPress Plugin Vulnerabilities
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting an estimated one million WordPress installations
- **Impact**: Allows hackers to read arbitrary files and extract sensitive information including credentials
- **Status**: Vulnerabilities disclosed, exploitation potential high

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to crafted email attacks
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure components allowing authentication bypass
- **WordPress Sites**: Multiple plugins including Funnel Builder, Burst Statistics, and Avada Builder affecting millions of installations
- **Node.js Applications**: npm packages using compromised node-ipc versions (multiple versions affected)
- **Windows 11 and Microsoft Edge**: Zero-day vulnerabilities demonstrated at Pwn2Own Berlin 2026
- **OpenAI Infrastructure**: Two employee devices impacted by TanStack supply chain attack
- **TanStack Ecosystem**: Multiple npm and PyPI packages compromised in supply chain attack

## Attack Vectors and Techniques

- **Email-based Exploitation**: Crafted emails targeting Microsoft Exchange Server vulnerabilities
- **Supply Chain Attacks**: Compromised npm packages including node-ipc and TanStack components
- **Plugin Exploitation**: WordPress plugin vulnerabilities allowing code injection and credential theft
- **Authentication Bypass**: Direct bypass of authentication mechanisms in network infrastructure
- **Modular Botnet Operations**: Evolution of traditional backdoors into peer-to-peer botnet architectures
- **Session Theft**: Focus on stealing browser sessions and authentication tokens rather than passwords
- **Zero-day Demonstrations**: Multiple zero-day vulnerabilities showcased at security conferences

## Threat Actor Activities

- **Russian Secret Blizzard/Turla**: Developed Kazuar backdoor into modular P2P botnet for long-term persistence and stealth operations
- **TeamPCP**: Threatening to leak Mistral AI source code repositories unless buyers are found
- **FrostyNeighbor APT**: Belarussian nation-state group targeting government organizations in Poland and Ukraine with fingerprinted spear-phishing campaigns
- **Pwn2Own Researchers**: Demonstrated 24 unique zero-day vulnerabilities on first day, 15 additional zero-days on second day
- **Supply Chain Attackers**: Compromising popular development packages to steal credentials and establish persistence
- **WordPress Plugin Attackers**: Systematic exploitation of plugin vulnerabilities for credential theft and malicious code injection