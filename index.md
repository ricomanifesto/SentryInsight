# Exploitation Report

The cybersecurity landscape is witnessing significant exploitation activity across multiple critical vulnerabilities. A Microsoft Exchange Server zero-day vulnerability tracked as CVE-2026-42897 is being actively exploited through crafted emails to enable cross-site scripting attacks and arbitrary code execution. Simultaneously, a maximum severity authentication bypass flaw in Cisco Catalyst SD-WAN Controller (CVE-2026-20182) has been exploited in zero-day attacks, allowing attackers to gain administrative access to network infrastructure. WordPress ecosystems are under siege with the Funnel Builder plugin experiencing active exploitation for WooCommerce checkout skimming, while the Burst Statistics plugin faces authentication bypass attacks. Supply chain attacks are also escalating, with the TanStack compromise affecting OpenAI employees and the node-ipc npm package being weaponized with credential-stealing malware.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: A high-severity vulnerability in on-premise Microsoft Exchange Server versions that allows threat actors to execute arbitrary code through cross-site scripting (XSS) attacks via specially crafted emails
- **Impact**: Attackers can execute malicious code in the context of Exchange Server, potentially leading to full system compromise
- **Status**: Actively exploited in the wild, Microsoft has released mitigations
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: A maximum severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller that allows attackers to circumvent authentication mechanisms
- **Impact**: Unauthorized administrative access to network infrastructure, potential for complete network compromise
- **Status**: Actively exploited in limited zero-day attacks, patches available
- **CVE ID**: CVE-2026-20182

### WordPress Funnel Builder Plugin Critical Vulnerability
- **Description**: A critical security vulnerability in the Funnel Builder plugin for WordPress that enables injection of malicious JavaScript code
- **Impact**: Credit card skimming attacks targeting WooCommerce checkout pages, theft of customer payment information
- **Status**: Under active exploitation for checkout skimming attacks

### WordPress Burst Statistics Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in the Burst Statistics WordPress plugin
- **Impact**: Admin-level access to WordPress websites, complete site compromise
- **Status**: Actively exploited by threat actors

### TanStack Supply Chain Attack
- **Description**: Supply chain compromise affecting the TanStack ecosystem, dubbed "Mini Shai-Hulud"
- **Impact**: Device compromise and potential code-signing certificate theft
- **Status**: Confirmed breach of OpenAI employee devices, forced security updates

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to XSS attacks via email
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure systems with authentication bypass
- **WordPress Funnel Builder Plugin**: E-commerce sites using WooCommerce integration
- **WordPress Burst Statistics Plugin**: WordPress sites with analytics functionality
- **Avada Builder Plugin**: WordPress installations with file reading vulnerabilities
- **node-ipc npm Package**: JavaScript applications using inter-process communication
- **TanStack Ecosystem**: Development environments using TanStack libraries
- **OpenClaw Software**: Systems with data theft and privilege escalation vulnerabilities

## Attack Vectors and Techniques

- **Email-Based Exploitation**: Crafted emails targeting Exchange Server XSS vulnerabilities
- **Authentication Bypass**: Direct circumvention of SD-WAN Controller login mechanisms
- **JavaScript Injection**: Malicious code injection into WordPress checkout pages
- **Supply Chain Compromise**: Package poisoning in npm and PyPI repositories
- **Credential Harvesting**: Malware injection for authentication token theft
- **Cross-Site Scripting**: Web application attacks enabling arbitrary code execution
- **File System Access**: Unauthorized reading of sensitive configuration files

## Threat Actor Activities

- **Secret Blizzard/Turla**: Evolution of Kazuar backdoor into modular P2P botnet for persistent access and stealth operations
- **TeamPCP Group**: Threatening to leak Mistral AI source code repositories for financial gain
- **ShinyHunters**: Cybercriminal group involved in Canvas platform attacks prompting congressional attention
- **Unknown Attackers**: Exploiting Exchange zero-day and Cisco SD-WAN vulnerabilities in targeted campaigns
- **Supply Chain Attackers**: Compromising popular development packages for credential theft and infrastructure access