# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with threat actors targeting web servers, enterprise systems, and development tools. The most severe incidents include CVE-2026-42945 affecting NGINX Plus and NGINX Open causing worker crashes and potential remote code execution, CVE-2026-42897 in Microsoft Exchange Server enabling arbitrary code execution via crafted emails, and CVE-2026-20182 in Cisco SD-WAN Controller allowing authentication bypass for administrative access. Additionally, supply chain attacks are escalating with malicious packages infiltrating npm repositories and WordPress plugins being exploited for credential theft and payment card skimming operations.

## Active Exploitation Details

### NGINX Worker Process Vulnerability
- **Description**: A security flaw in NGINX Plus and NGINX Open that causes worker process crashes and enables potential remote code execution
- **Impact**: Attackers can crash NGINX worker processes and potentially execute arbitrary code on affected systems
- **Status**: Under active exploitation in the wild, recently disclosed
- **CVE ID**: CVE-2026-42945

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: A high-severity vulnerability in on-premise Exchange Server versions that allows arbitrary code execution through crafted email messages
- **Impact**: Threat actors can execute arbitrary code via cross-site scripting (XSS) attacks by sending specially crafted emails
- **Status**: Zero-day vulnerability actively exploited in attacks, mitigations available
- **CVE ID**: CVE-2026-42897

### Cisco SD-WAN Controller Authentication Bypass
- **Description**: A critical authentication bypass flaw in Cisco Catalyst SD-WAN Controller with maximum CVSS 10.0 severity rating
- **Impact**: Attackers can gain administrative access to network control systems without authentication
- **Status**: Exploited in zero-day attacks, added to CISA KEV catalog
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: A critical security flaw in the Funnel Builder plugin for WordPress enabling malicious JavaScript injection
- **Impact**: Attackers inject malicious code into WooCommerce checkout pages to steal credit card information and payment data
- **Status**: Under active exploitation for payment card skimming attacks

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Hackers can obtain admin-level access to WordPress websites without proper authentication
- **Status**: Currently being exploited by threat actors

### Avada Builder WordPress Plugin File Read Vulnerabilities
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting an estimated one million WordPress installations
- **Impact**: Attackers can read arbitrary files and extract sensitive information including credentials from affected websites
- **Status**: Publicly disclosed vulnerabilities enabling credential theft

## Affected Systems and Products

- **NGINX Plus and NGINX Open**: Web server platforms experiencing worker crashes and potential RCE
- **Microsoft Exchange Server**: On-premise versions vulnerable to XSS-based code execution
- **Cisco Catalyst SD-WAN Controller**: Network management systems with authentication bypass
- **WordPress Sites**: Multiple plugins including Funnel Builder, Burst Statistics, and Avada Builder
- **WooCommerce Platforms**: E-commerce sites targeted for payment card skimming
- **npm Package Repository**: Node.js packages compromised in supply chain attacks
- **TanStack Development Tools**: JavaScript/TypeScript libraries targeted in supply chain attacks

## Attack Vectors and Techniques

- **Crafted Email Exploitation**: Attackers sending specially crafted emails to trigger Exchange Server vulnerabilities
- **JavaScript Injection**: Malicious scripts injected into WordPress checkout pages for payment data theft
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in network controllers
- **Supply Chain Compromise**: Malicious code injection into popular development packages and libraries
- **Device Code Phishing**: Tycoon2FA phishing kit using device-code attacks against Microsoft 365 accounts
- **Session Token Theft**: REMUS infostealer focusing on browser session hijacking over traditional password theft
- **Arbitrary File Reading**: Exploitation of file inclusion vulnerabilities to extract sensitive data

## Threat Actor Activities

- **Secret Blizzard/Turla**: Russian state-sponsored group transforming Kazuar backdoor into modular P2P botnet for persistent access and stealth operations
- **TeamPCP**: Hacker group advertising stolen Mistral AI source code repositories for sale after successful breach
- **Tycoon2FA Operators**: Cybercriminals deploying advanced phishing kits with device-code attacks and Trustifi URL abuse for Microsoft 365 account hijacking
- **WordPress Plugin Attackers**: Multiple threat actors exploiting WordPress plugin vulnerabilities for admin access and payment card theft
- **Supply Chain Attackers**: Groups compromising npm packages like node-ipc with credential-stealing malware and targeting TanStack development tools affecting major companies including OpenAI