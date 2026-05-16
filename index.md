# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple critical vulnerabilities, with threat actors actively targeting enterprise infrastructure, WordPress plugins, and supply chain components. The most severe ongoing exploitations include a maximum-severity authentication bypass vulnerability in Cisco's SD-WAN Controller being exploited for administrative access, a critical Microsoft Exchange Server zero-day flaw allowing arbitrary code execution through crafted emails, and widespread attacks on WordPress plugins affecting millions of installations. Additionally, sophisticated supply chain attacks are targeting npm packages and AI development environments, while multiple zero-day vulnerabilities were demonstrated at Pwn2Own Berlin 2026, highlighting the evolving threat landscape across Windows, Exchange, and other enterprise platforms.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: A high-severity vulnerability in Microsoft Exchange Server that allows threat actors to execute arbitrary code through cross-site scripting (XSS) attacks
- **Impact**: Attackers can execute arbitrary code on vulnerable Exchange servers, potentially leading to complete system compromise
- **Status**: Actively exploited in attacks, Microsoft has shared mitigations
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: A maximum-severity authentication bypass flaw in Cisco Catalyst SD-WAN Controller systems
- **Impact**: Attackers can gain administrative access to network control systems, potentially compromising entire network infrastructure
- **Status**: Actively exploited in limited zero-day attacks, patches available
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Critical Vulnerability
- **Description**: A critical vulnerability in the Funnel Builder plugin for WordPress that allows malicious code injection
- **Impact**: Attackers can inject malicious JavaScript snippets into WooCommerce checkout pages to steal credit card information
- **Status**: Actively exploited for credit card theft attacks

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in the Burst Statistics WordPress plugin
- **Impact**: Hackers can obtain admin-level access to WordPress websites
- **Status**: Currently being exploited to gain unauthorized administrative access

### Avada Builder WordPress Plugin Vulnerabilities
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting approximately one million WordPress installations
- **Impact**: Allows attackers to read arbitrary files and extract sensitive information including credentials
- **Status**: Actively exploited for credential theft

### Node-IPC NPM Package Supply Chain Attack
- **Description**: Credential-stealing malware injected into newly published versions of the node-ipc package
- **Impact**: Steals developer credentials and sensitive information from development environments
- **Status**: Active supply chain attack targeting three different versions

### TanStack Supply Chain Attack
- **Description**: The "Mini Shai-Hulud" supply chain attack targeting TanStack packages
- **Impact**: Compromised employee devices at major organizations including OpenAI
- **Status**: Active attack affecting hundreds of npm and PyPI packages

### 18-Year-Old NGINX Vulnerability
- **Description**: A long-standing vulnerability in the NGINX open-source web server discovered using autonomous scanning
- **Impact**: Can be exploited for denial of service attacks and potentially remote code execution under certain conditions
- **Status**: Recently discovered, active exploitation potential

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to zero-day exploitation via crafted emails
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure components with maximum-severity authentication bypass
- **WordPress Plugins**: Multiple popular plugins including Funnel Builder, Burst Statistics, and Avada Builder affecting millions of installations
- **Node.js Development Environments**: npm package ecosystem through node-ipc supply chain compromise
- **NGINX Web Servers**: 18-year-old vulnerability affecting widespread web server deployments
- **Windows 11**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own Berlin 2026
- **Microsoft Edge**: Browser vulnerabilities exploited during security research events
- **TanStack Development Tools**: Supply chain compromise affecting development environments

## Attack Vectors and Techniques

- **Crafted Email Exploitation**: Microsoft Exchange vulnerability exploited through specially crafted email messages
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in Cisco SD-WAN controllers
- **Malicious Code Injection**: JavaScript injection into WordPress checkout pages for payment card theft
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages and dependencies
- **Zero-Day Exploitation**: Multiple previously unknown vulnerabilities exploited before patches became available
- **Cross-Site Scripting (XSS)**: Web-based attacks allowing arbitrary code execution in vulnerable applications
- **Arbitrary File Reading**: Exploitation of file system access vulnerabilities to extract sensitive data

## Threat Actor Activities

- **Cisco SD-WAN Attackers**: Limited but active exploitation of maximum-severity authentication bypass for administrative access
- **WordPress Plugin Exploiters**: Widespread attacks targeting millions of WordPress installations for credential theft and payment card fraud
- **Supply Chain Attackers**: Sophisticated actors compromising npm packages and development tools to target developer environments
- **Pwn2Own Researchers**: Security researchers demonstrated 24 unique zero-day vulnerabilities on day one, with 15 additional zero-days exploited on day two, collecting over $900,000 in total awards
- **TeamPCP Hacker Group**: Threatening to leak Mistral AI source code repositories
- **Turla APT Group**: Russian state-sponsored actors transforming Kazuar backdoor into modular P2P botnet infrastructure
- **FrostyNeighbor APT**: Belarussian nation-state group targeting government organizations in Poland and Ukraine with carefully crafted spear-phishing campaigns