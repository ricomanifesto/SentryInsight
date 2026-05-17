# Exploitation Report

Critical exploitation activity is currently underway across multiple platforms, with attackers targeting both enterprise infrastructure and consumer-facing applications. The most severe threats include zero-day attacks against Microsoft Exchange Server and Cisco SD-WAN systems, where threat actors are achieving administrative access and code execution. Supply chain attacks are also prominent, with compromised npm packages and WordPress plugins being actively exploited to steal credentials and inject malicious code. Notable incidents include the TanStack supply chain attack affecting OpenAI employees and widespread exploitation of WordPress plugins for credit card skimming operations.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: High-severity vulnerability in on-premise Exchange Server allowing arbitrary code execution via cross-site scripting when processing crafted emails
- **Impact**: Threat actors can execute arbitrary code on Exchange servers through malicious email messages
- **Status**: Actively exploited in the wild, mitigations available from Microsoft
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum severity authentication bypass flaw allowing unauthorized access to SD-WAN management systems
- **Impact**: Attackers can gain administrative access to network control systems without valid credentials
- **Status**: Actively exploited in zero-day attacks, patches available
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Funnel Builder plugin for WordPress enabling injection of malicious JavaScript
- **Impact**: Attackers can inject code into WooCommerce checkout pages to steal credit card information and payment data
- **Status**: Under active exploitation for checkout skimming attacks

### Avada Builder WordPress Plugin Vulnerabilities
- **Description**: Two security flaws in the Avada Builder plugin allowing arbitrary file reads and sensitive data extraction
- **Impact**: Hackers can access configuration files, database credentials, and other sensitive site information
- **Status**: Vulnerabilities discovered, patch status unclear

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability allowing unauthorized administrative access
- **Impact**: Attackers can obtain admin-level access to WordPress websites without valid credentials
- **Status**: Actively exploited by threat actors

### Node-IPC npm Package Compromise
- **Description**: Popular inter-process communication package compromised with credential-stealing malware
- **Impact**: Developers using affected versions have their credentials and secrets harvested
- **Status**: Supply chain attack affecting multiple published versions

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise installations vulnerable to email-based XSS attacks
- **Cisco Catalyst SD-WAN Controller**: Network management systems exposed to authentication bypass
- **WordPress Sites**: Multiple plugins including Funnel Builder (WooCommerce integration), Avada Builder (1M+ installations), and Burst Statistics
- **Node.js Development Environment**: npm packages using node-ipc library versions containing malicious code
- **OpenAI Corporate Infrastructure**: Employee devices compromised through TanStack supply chain attack
- **Windows 11 and Microsoft Edge**: Demonstrated vulnerabilities at Pwn2Own Berlin 2026 security conference

## Attack Vectors and Techniques

- **Email-Based Exploitation**: Crafted email messages triggering XSS vulnerabilities in Exchange Server
- **Authentication Bypass**: Direct exploitation of authentication flaws to gain administrative access without credentials
- **Supply Chain Attacks**: Injection of malicious code into legitimate software packages and dependencies
- **JavaScript Injection**: Insertion of malicious scripts into e-commerce checkout processes for payment data theft
- **Zero-Day Exploitation**: Active use of previously unknown vulnerabilities before patches are available
- **Botnet Infrastructure**: Evolution of existing backdoors into modular peer-to-peer networks for persistence

## Threat Actor Activities

- **Secret Blizzard/Turla**: Russian state-sponsored group developing Kazuar backdoor into modular P2P botnet for long-term persistence and stealth operations
- **TeamPCP**: Hacker group threatening to leak Mistral AI source code repositories unless buyers are found
- **Unknown Threat Actors**: Multiple groups exploiting WordPress plugin vulnerabilities for credit card skimming and site compromise
- **Supply Chain Attackers**: Targeting npm ecosystem and TanStack packages to compromise developer environments and corporate infrastructure
- **Pwn2Own Researchers**: Security researchers demonstrating zero-day vulnerabilities in Windows 11, Microsoft Edge, and other enterprise systems during controlled competitions