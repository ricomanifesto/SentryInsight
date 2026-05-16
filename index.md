# Exploitation Report

Critical exploitation activity is escalating across multiple attack vectors, with threat actors actively targeting enterprise infrastructure, supply chain components, and web applications. The most severe incidents include active exploitation of Microsoft Exchange Server vulnerabilities allowing arbitrary code execution, a maximum-severity Cisco SD-WAN authentication bypass flaw (CVE-2026-20182) being exploited for administrative access, and widespread supply chain attacks targeting npm packages and developer environments. WordPress plugins continue to face active exploitation for credential theft and site compromise, while zero-day vulnerabilities demonstrated at security conferences highlight ongoing risks in Windows 11, Microsoft Exchange, and other enterprise systems. State-sponsored groups like Turla are evolving their tactics with modular peer-to-peer botnets, and emerging threats include AI-assisted vulnerability discovery and exploitation of legacy infrastructure components.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: High-severity vulnerability in on-premise Exchange Server allowing arbitrary code execution through cross-site scripting attacks
- **Impact**: Threat actors can execute arbitrary code and gain unauthorized access to Exchange environments
- **Status**: Actively exploited in the wild, Microsoft has shared mitigations
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability in Cisco's SD-WAN Controller system
- **Impact**: Attackers can gain complete administrative access to network control systems
- **Status**: Actively exploited in limited attacks, patches available, added to CISA KEV catalog
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Critical Vulnerability
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress allowing malicious code injection
- **Impact**: Attackers inject malicious JavaScript into WooCommerce checkout pages to steal credit card information
- **Status**: Actively exploited for payment data theft

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in the WordPress Burst Statistics plugin
- **Impact**: Hackers obtain admin-level access to WordPress websites
- **Status**: Actively exploited in the wild

### Avada Builder WordPress Plugin Vulnerabilities
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting approximately one million active installations
- **Impact**: Allows hackers to read arbitrary files and extract sensitive credentials and configuration data
- **Status**: Actively exploited for credential theft

### Node-IPC Supply Chain Attack
- **Description**: Malicious backdoor injected into three versions of the popular node-ipc npm package
- **Impact**: Steals developer credentials, environment variables, and other sensitive information from development systems
- **Status**: Active supply chain attack targeting developer environments

### TanStack Supply Chain Attack (Mini Shai-Hulud)
- **Description**: Supply chain compromise affecting hundreds of npm and PyPI packages through TanStack
- **Impact**: Compromised developer devices and forced certificate rotations at affected organizations
- **Status**: Ongoing investigation, confirmed impact at OpenAI and other organizations

### 18-Year-Old NGINX Vulnerability
- **Description**: Legacy vulnerability in NGINX web server discovered through autonomous scanning
- **Impact**: Enables denial of service attacks and potential remote code execution under certain conditions
- **Status**: Recently disclosed, affects long-term installations

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise installations vulnerable to XSS-based code execution
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure systems with authentication bypass risks
- **WordPress Plugins**: Funnel Builder, Burst Statistics, and Avada Builder plugins affecting millions of installations
- **Node.js Ecosystem**: npm packages and development environments using node-ipc
- **NGINX Web Servers**: 18-year-old installations potentially vulnerable to DoS and RCE
- **Windows 11**: Multiple zero-day vulnerabilities demonstrated at Pwn2Own Berlin 2026
- **Microsoft Edge**: Browser vulnerabilities exploited in security competitions
- **Red Hat Enterprise Linux**: Zero-day vulnerabilities shown at security conferences

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exchange Server vulnerability exploited via crafted emails
- **Authentication Bypass**: Direct access to administrative interfaces without proper credentials
- **Supply Chain Compromise**: Injection of malicious code into trusted package repositories
- **Plugin Exploitation**: WordPress plugin vulnerabilities enabling site takeover
- **Session Theft**: Advanced techniques using infostealers like REMUS to capture authentication tokens
- **P2P Botnet Evolution**: Turla's transformation of Kazuar backdoor into modular peer-to-peer network
- **Zero-Day Exploitation**: Multiple vulnerabilities demonstrated at security conferences
- **Software-Defined Radio Attacks**: Novel attack vector targeting transportation infrastructure

## Threat Actor Activities

- **Turla Group**: Russian state-sponsored actors evolving Kazuar backdoor into modular P2P botnet for persistent access and stealth operations
- **TeamPCP**: Cybercriminal group threatening to leak Mistral AI source code unless buyers are found
- **FrostyNeighbor APT**: Belarussian nation-state group conducting targeted espionage campaigns against government organizations in Poland and Ukraine using sophisticated fingerprinting techniques
- **ShinyHunters**: Cybercriminal group responsible for Canvas platform attacks affecting educational institutions
- **Supply Chain Attackers**: Unknown actors conducting sophisticated attacks against npm ecosystem and developer toolchains
- **WordPress Threat Actors**: Coordinated exploitation campaigns targeting multiple WordPress plugins for credential theft and payment data compromise