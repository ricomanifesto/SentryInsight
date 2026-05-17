# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by several high-severity flaws under active attack. Most notably, Microsoft Exchange Server is facing zero-day exploitation through CVE-2026-42897, allowing arbitrary code execution via crafted emails. Cisco's SD-WAN infrastructure is also under siege with CVE-2026-20182, a maximum-severity authentication bypass flaw being exploited to gain administrative access. WordPress ecosystems are experiencing widespread attacks through the Funnel Builder plugin vulnerability enabling credit card theft, and the Burst Statistics plugin authentication bypass granting admin-level access. Supply chain attacks are escalating with malicious code injected into the popular node-ipc npm package and the TanStack compromise affecting even OpenAI employees. Additionally, Russian state-sponsored group Turla has evolved their Kazuar backdoor into a sophisticated peer-to-peer botnet for persistent access.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: A high-severity cross-site scripting vulnerability in on-premise Exchange Server installations that allows arbitrary code execution
- **Impact**: Attackers can execute arbitrary code on Exchange servers through specially crafted emails
- **Status**: Currently being exploited in the wild, mitigations provided by Microsoft
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco's SD-WAN Controller
- **Impact**: Complete administrative access to SD-WAN infrastructure without authentication
- **Status**: Actively exploited in zero-day attacks, patches released
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: A critical security flaw in the Funnel Builder plugin for WordPress affecting WooCommerce checkout processes
- **Impact**: Injection of malicious JavaScript code into checkout pages to steal credit card information and customer data
- **Status**: Under active exploitation for payment card skimming attacks

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Admin-level access to WordPress websites without proper authentication
- **Status**: Actively exploited to gain unauthorized administrative access

### Node-IPC NPM Package Supply Chain Attack
- **Description**: Malicious code injected into three versions of the popular node-ipc npm package for inter-process communication
- **Impact**: Credential theft and unauthorized access to developer secrets and environments
- **Status**: Active supply chain attack targeting development environments

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise installations vulnerable to email-based code execution attacks
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure components allowing unauthorized administrative access
- **WordPress Websites**: Sites using Funnel Builder plugin experiencing payment card theft, sites with Burst Statistics plugin facing authentication bypass
- **Node.js Development Environments**: Applications using compromised node-ipc package versions subject to credential theft
- **TanStack Ecosystem**: JavaScript development tools compromised in supply chain attack
- **Windows 11**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own Berlin 2026
- **Microsoft Edge**: Browser vulnerabilities exploited during security research demonstrations
- **Avada Builder WordPress Plugin**: One million installations potentially affected by file read vulnerabilities
- **OpenClaw**: Four security flaws enabling data theft, privilege escalation, and persistence

## Attack Vectors and Techniques

- **Email-Based Exploitation**: Crafted emails targeting Exchange Server vulnerabilities for code execution
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in network infrastructure
- **JavaScript Injection**: Malicious code insertion into e-commerce checkout processes for payment theft
- **Supply Chain Compromise**: Injection of malicious code into popular development packages and tools
- **Peer-to-Peer Botnet**: Evolution of traditional backdoors into distributed, persistent network architectures
- **Cross-Site Scripting**: Web application vulnerabilities enabling arbitrary code execution
- **Package Repository Attacks**: Compromise of npm and PyPI packages for widespread distribution

## Threat Actor Activities

- **Turla (Secret Blizzard)**: Russian state-sponsored group transforming Kazuar backdoor into modular P2P botnet for long-term persistence and stealth operations
- **TeamPCP**: Hacker group threatening to leak Mistral AI source code repositories unless buyers are found
- **ShinyHunters**: Cybercriminal group involved in Canvas cyberattack affecting educational technology systems
- **Unknown Actors**: Multiple threat groups actively exploiting WordPress plugin vulnerabilities for credential theft and unauthorized access
- **Supply Chain Attackers**: Sophisticated actors targeting development tools and package repositories to compromise downstream applications and organizations