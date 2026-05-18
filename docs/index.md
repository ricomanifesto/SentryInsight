# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with attackers targeting everything from Microsoft Exchange servers to WordPress plugins. The most severe threats include CVE-2026-42897 affecting Microsoft Exchange Server, CVE-2026-20182 in Cisco SD-WAN controllers, and CVE-2026-42945 impacting NGINX servers. A new Windows privilege escalation zero-day dubbed "MiniPlasma" has emerged with public proof-of-concept code available. Threat actors are also heavily targeting WordPress environments, exploiting vulnerabilities in popular plugins like Funnel Builder, Avada Builder, and Burst Statistics to inject malicious code and steal credentials. Supply chain attacks continue to pose significant risks, with compromises affecting npm packages, GitHub tokens, and various development tools.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: A high-severity vulnerability in on-premise Microsoft Exchange Server that allows arbitrary code execution via cross-site scripting (XSS)
- **Impact**: Threat actors can execute arbitrary code on Exchange servers through crafted emails
- **Status**: Currently being exploited in the wild, mitigations provided by Microsoft
- **CVE ID**: CVE-2026-42897

### Cisco SD-WAN Controller Authentication Bypass
- **Description**: A maximum severity vulnerability (CVSS 10.0) affecting Cisco Catalyst SD-WAN Controller
- **Impact**: Allows unauthorized administrative access to network control systems
- **Status**: Actively exploited and added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-20182

### NGINX Server Vulnerability
- **Description**: A newly disclosed security flaw impacting both NGINX Plus and NGINX Open Source
- **Impact**: Causes worker crashes and potentially enables remote code execution
- **Status**: Under active exploitation in the wild within days of public disclosure
- **CVE ID**: CVE-2026-42945

### Windows MiniPlasma Privilege Escalation Zero-Day
- **Description**: A Windows privilege escalation vulnerability that affects fully patched Windows systems
- **Impact**: Allows attackers to gain SYSTEM privileges on compromised Windows machines
- **Status**: Proof-of-concept exploit code publicly released

### WordPress Funnel Builder Plugin Vulnerability
- **Description**: A critical security vulnerability in the Funnel Builder plugin for WordPress
- **Impact**: Enables injection of malicious JavaScript code into WooCommerce checkout pages for credit card skimming
- **Status**: Under active exploitation for stealing credit card information

### WordPress Burst Statistics Plugin Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in the Burst Statistics WordPress plugin
- **Impact**: Allows hackers to obtain admin-level access to websites
- **Status**: Currently being leveraged by attackers

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to XSS attacks via crafted emails
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure devices with administrative access bypass
- **NGINX Plus and NGINX Open Source**: Web servers experiencing worker crashes and potential RCE
- **Windows Systems**: All versions affected by MiniPlasma privilege escalation vulnerability
- **WordPress Sites**: Installations using vulnerable plugins (Funnel Builder, Avada Builder, Burst Statistics)
- **WooCommerce Stores**: E-commerce sites targeted for checkout page skimming attacks
- **Microsoft 365 Accounts**: Targeted by Tycoon2FA phishing kit using device-code attacks
- **npm Ecosystem**: node-ipc package compromised with credential-stealing malware
- **GitHub Repositories**: Grafana codebase downloaded after token compromise

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploiting Exchange Server vulnerabilities through crafted emails
- **Authentication Bypass**: Circumventing security controls in network infrastructure devices
- **Privilege Escalation**: Using zero-day exploits to gain elevated system permissions
- **JavaScript Injection**: Inserting malicious code into e-commerce checkout pages
- **Device-Code Phishing**: Abusing Microsoft's device authorization flow to hijack accounts
- **Supply Chain Attacks**: Compromising popular software packages and development tools
- **Credit Card Skimming**: Stealing payment information from compromised websites
- **Session Theft**: Using infostealers like REMUS to capture authentication tokens

## Threat Actor Activities

- **Secret Blizzard/Turla**: Russian state-sponsored group developing Kazuar backdoor into modular P2P botnet for persistent access and stealth operations
- **TeamPCP**: Hacker group threatening to leak Mistral AI source code repositories unless buyers are found
- **Tycoon2FA Operators**: Cybercriminals using advanced phishing kits to hijack Microsoft 365 accounts through device-code attacks
- **Unknown Threat Actors**: Multiple groups actively exploiting WordPress plugin vulnerabilities for credential theft and malicious code injection
- **Supply Chain Attackers**: Threat actors compromising development tools and packages, including the TanStack attack affecting OpenAI employees