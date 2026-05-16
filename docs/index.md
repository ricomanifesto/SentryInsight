# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple attack vectors. Most concerning is the active exploitation of Microsoft Exchange Server vulnerabilities, including CVE-2026-42897, which allows remote code execution through crafted emails. Additionally, Cisco Catalyst SD-WAN Controller systems face maximum-severity authentication bypass attacks via CVE-2026-20182, enabling administrative access. WordPress environments are under assault through multiple plugin vulnerabilities in Funnel Builder, Avada Builder, and Burst Statistics plugins. Supply chain attacks have compromised the node-ipc npm package and affected OpenAI through the TanStack attack. Zero-day demonstrations at Pwn2Own Berlin 2026 revealed new vulnerabilities in Windows 11, Microsoft Exchange, and other enterprise systems, with researchers collecting over $900,000 in bounties across multiple products.

## Active Exploitation Details

### Microsoft Exchange Server Vulnerability
- **Description**: A high-severity vulnerability in on-premise Exchange Server versions that allows remote code execution through cross-site scripting (XSS) attacks
- **Impact**: Threat actors can execute arbitrary code on vulnerable Exchange servers when users interact with crafted emails
- **Status**: Actively exploited in the wild; Microsoft has provided mitigations
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability in Cisco's network control system
- **Impact**: Attackers can gain administrative access to SD-WAN controllers without authentication
- **Status**: Actively exploited in limited attacks; patches available
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Funnel Builder plugin allowing injection of malicious JavaScript
- **Impact**: Enables credit card theft through malicious scripts injected into WooCommerce checkout pages
- **Status**: Actively exploited to steal payment information

### Avada Builder WordPress Plugin Flaws
- **Description**: Two vulnerabilities in the popular Avada Builder plugin with over one million active installations
- **Impact**: Allows attackers to read arbitrary files and extract sensitive credentials from affected websites
- **Status**: Under active exploitation for credential theft

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Provides attackers with admin-level access to WordPress websites
- **Status**: Actively exploited by threat actors

### Node-IPC npm Package Compromise
- **Description**: Supply chain attack targeting the popular inter-process communication package
- **Impact**: Credential-stealing malware injected into newly published versions
- **Status**: Three malicious versions identified containing stealer backdoors

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to crafted email attacks
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure systems facing authentication bypass
- **WordPress Plugins**: Funnel Builder, Avada Builder (1M+ installations), and Burst Statistics plugins
- **npm Package Ecosystem**: node-ipc package and dependent applications
- **Windows 11**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own
- **Microsoft Edge**: Browser vulnerabilities exploited during security competitions
- **TanStack**: JavaScript development framework compromised in supply chain attack
- **NGINX Web Server**: 18-year-old vulnerability enabling DoS and potential RCE
- **OpenClaw**: Four security flaws enabling data theft and privilege escalation

## Attack Vectors and Techniques

- **Crafted Email Attacks**: Exploitation of Exchange Server through specially crafted emails triggering XSS
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in SD-WAN controllers
- **JavaScript Injection**: Malicious scripts inserted into WordPress checkout pages for payment theft
- **Supply Chain Compromise**: Injection of malicious code into legitimate software packages
- **File Read Exploitation**: Arbitrary file access leading to credential extraction
- **Zero-Day Exploitation**: Multiple new vulnerabilities demonstrated in controlled environments
- **P2P Botnet Deployment**: Turla's transformation of Kazuar backdoor into modular botnet infrastructure

## Threat Actor Activities

- **Turla Group**: Russian state-sponsored actors deploying enhanced Kazuar backdoor as modular P2P botnet for persistent access
- **TeamPCP**: Hackers advertising stolen Mistral AI source code repositories for sale
- **FrostyNeighbor APT**: Belarussian nation-state group targeting government organizations in Poland and Ukraine with fingerprinted spear-phishing campaigns
- **Unknown Threat Actors**: Multiple groups exploiting WordPress plugin vulnerabilities for financial gain
- **Supply Chain Attackers**: Compromising popular development packages to steal credentials and gain persistent access
- **REMUS Infostealer Operators**: Evolution toward session theft and Malware-as-a-Service models targeting authentication tokens