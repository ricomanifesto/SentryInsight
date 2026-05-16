# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple enterprise platforms, with Microsoft Exchange Server CVE-2026-42897 allowing remote code execution through crafted emails, and Cisco Catalyst SD-WAN Controller CVE-2026-20182 enabling authentication bypass for administrative access. WordPress ecosystem remains under severe attack with the Funnel Builder plugin vulnerability being exploited to steal credit card data from WooCommerce sites, while supply chain attacks have compromised the node-ipc npm package and affected OpenAI through the TanStack attack. The Pwn2Own Berlin 2026 competition demonstrated 24 unique zero-day vulnerabilities across Windows 11, Microsoft Edge, and Exchange systems, highlighting the widespread nature of current exploitation activity.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: High-severity vulnerability in on-premise Exchange Server that allows arbitrary code execution through cross-site scripting attacks
- **Impact**: Threat actors can execute arbitrary code on vulnerable Exchange servers through specially crafted emails
- **Status**: Actively exploited in the wild, mitigations available but no patch released
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum severity authentication bypass flaw in Cisco's SD-WAN network control system
- **Impact**: Attackers can gain administrative access to network infrastructure without authentication
- **Status**: Actively exploited in limited attacks, patches available
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress enabling malicious code injection
- **Impact**: Attackers inject malicious JavaScript snippets into WooCommerce checkout pages to steal credit card information
- **Status**: Actively exploited to compromise e-commerce sites

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Hackers obtain admin-level access to websites bypassing authentication controls
- **Status**: Actively exploited in attacks against WordPress installations

### Node-IPC NPM Package Supply Chain Attack
- **Description**: Popular inter-process communication package compromised with credential-stealing malware
- **Impact**: Steals developer credentials and secrets from infected systems
- **Status**: Three malicious versions published, actively stealing credentials

### TanStack Supply Chain Attack
- **Description**: Supply chain compromise affecting hundreds of npm and PyPI packages through the Mini Shai-Hulud attack
- **Impact**: Corporate environment infiltration and potential data access
- **Status**: Confirmed breach of OpenAI employee devices

### 18-Year-Old NGINX Vulnerability
- **Description**: Long-standing flaw in NGINX open-source web server discovered through autonomous scanning
- **Impact**: Denial of service attacks and potential remote code execution under certain conditions
- **Status**: Recently discovered, exploitation potential confirmed

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to zero-day cross-site scripting attacks
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure platforms with authentication bypass flaws
- **WordPress Plugins**: Funnel Builder, Burst Statistics, and Avada Builder plugins with critical vulnerabilities
- **NPM Ecosystem**: Node-IPC package versions compromised with malicious code
- **NGINX Web Server**: 18-year-old vulnerability affecting web server installations
- **Windows 11**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own
- **Microsoft Edge**: Browser vulnerabilities exploited during security competitions
- **Red Hat Enterprise Linux**: Zero-day vulnerabilities demonstrated at security events

## Attack Vectors and Techniques

- **Crafted Email Attacks**: Exchange Server compromise through malicious email content triggering XSS vulnerabilities
- **Authentication Bypass**: Direct administrative access to network infrastructure without credentials
- **JavaScript Injection**: Malicious code insertion into e-commerce checkout processes for payment data theft
- **Supply Chain Compromise**: Package repositories infiltrated to distribute credential-stealing malware
- **Zero-Day Exploitation**: Previously unknown vulnerabilities leveraged for system compromise
- **Plugin Vulnerabilities**: WordPress ecosystem targeted through third-party plugin security flaws
- **Session Theft**: Browser session and authentication token stealing through infostealers

## Threat Actor Activities

- **Pwn2Own Competitors**: Security researchers demonstrated 24 unique zero-day vulnerabilities across multiple Microsoft products, earning over $900,000 in awards across two days
- **E-commerce Attackers**: Cybercriminals actively exploiting WordPress plugin vulnerabilities to steal credit card data from online stores
- **Supply Chain Attackers**: Threat actors compromising popular development packages to steal credentials and establish persistent access
- **TeamPCP Group**: Hackers claiming possession of Mistral AI source code repositories and threatening public disclosure
- **Turla APT Group**: Russian state-sponsored actors transforming Kazuar backdoor into modular P2P botnet for persistent access
- **FrostyNeighbor APT**: Belarussian nation-state group conducting targeted espionage campaigns against government organizations in Poland and Ukraine
- **REMUS Operators**: Cybercriminals operating infostealer-as-a-service focusing on session theft and authentication token harvesting