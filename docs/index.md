# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems including Microsoft Exchange Server, Cisco SD-WAN infrastructure, and popular WordPress plugins. Microsoft Exchange Server vulnerabilities CVE-2026-42897 are being actively exploited through crafted emails to achieve arbitrary code execution. Cisco's SD-WAN Controller is under attack via CVE-2026-20182, a maximum severity authentication bypass flaw that grants administrative access. Supply chain attacks have compromised the node-ipc npm package and impacted OpenAI through the TanStack attack vector. WordPress ecosystems face ongoing exploitation through the Funnel Builder plugin for credit card theft and authentication bypass flaws in the Burst Statistics plugin. Zero-day demonstrations at Pwn2Own Berlin 2026 revealed 39 unique vulnerabilities across Windows 11, Microsoft Exchange, and other enterprise systems.

## Active Exploitation Details

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: High-severity vulnerability in on-premise Exchange Server versions allowing arbitrary code execution through cross-site scripting (XSS)
- **Impact**: Threat actors can execute arbitrary code and gain unauthorized access to Exchange environments
- **Status**: Actively exploited in the wild, Microsoft has provided mitigations
- **CVE ID**: CVE-2026-42897

### Cisco Catalyst SD-WAN Controller Authentication Bypass
- **Description**: Maximum severity authentication bypass flaw in Cisco Catalyst SD-WAN Controller
- **Impact**: Attackers gain full administrative access to network infrastructure without authentication
- **Status**: Actively exploited in limited attacks, patches available
- **CVE ID**: CVE-2026-20182

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress allowing malicious JavaScript injection
- **Impact**: Credit card theft through compromised WooCommerce checkout pages
- **Status**: Actively exploited for financial fraud

### Burst Statistics WordPress Plugin Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in WordPress Burst Statistics plugin
- **Impact**: Admin-level access to websites without proper authentication
- **Status**: Currently being exploited by attackers

### Node-IPC Supply Chain Compromise
- **Description**: Malicious code injected into three versions of the popular node-ipc npm package
- **Impact**: Credential theft and unauthorized access to developer environments
- **Status**: Active supply chain attack targeting developer credentials

### Avada Builder WordPress Plugin File Read Vulnerabilities
- **Description**: Two vulnerabilities allowing arbitrary file reading and sensitive information extraction
- **Impact**: Site credential theft and unauthorized access to sensitive data
- **Status**: Disclosed vulnerabilities with one million active installations at risk

## Affected Systems and Products

- **Microsoft Exchange Server**: On-premise versions vulnerable to crafted email attacks
- **Cisco Catalyst SD-WAN Controller**: Network infrastructure systems with authentication bypass
- **WordPress Sites**: Funnel Builder plugin installations processing e-commerce transactions
- **WordPress Sites**: Burst Statistics plugin with over 400,000 active installations
- **Node.js Applications**: Projects using compromised node-ipc package versions
- **WordPress Sites**: Avada Builder plugin with approximately one million installations
- **Windows 11**: Multiple zero-days demonstrated at Pwn2Own Berlin 2026
- **Microsoft Edge**: Browser vulnerabilities exploited in security competitions
- **TanStack Ecosystem**: Supply chain compromise affecting npm and PyPI packages
- **OpenAI Infrastructure**: Two employee devices compromised through supply chain attack

## Attack Vectors and Techniques

- **Crafted Email Exploitation**: Malicious emails targeting Exchange Server XSS vulnerabilities
- **Authentication Bypass**: Direct access to administrative interfaces without credentials
- **JavaScript Injection**: Malicious scripts inserted into e-commerce checkout processes
- **Supply Chain Poisoning**: Compromised packages in npm and PyPI repositories
- **Arbitrary File Reading**: Exploitation of file access controls in WordPress plugins
- **Zero-Day Exploitation**: Advanced techniques demonstrated at security competitions
- **Session Theft**: REMUS infostealer targeting browser sessions and authentication tokens
- **P2P Botnet Operations**: Modular peer-to-peer networks for persistent access

## Threat Actor Activities

- **Exchange Server Attackers**: Actively exploiting CVE-2026-42897 for code execution and system access
- **Cisco Infrastructure Attackers**: Leveraging maximum severity SD-WAN vulnerabilities for network compromise
- **WordPress Threat Actors**: Systematic exploitation of plugin vulnerabilities for financial gain and unauthorized access
- **Supply Chain Attackers**: Sophisticated campaigns targeting developer tools and package repositories
- **Turla Group**: Russian state-sponsored actors deploying modular P2P Kazuar backdoor for persistent access
- **TeamPCP Group**: Threatening to leak Mistral AI source code repositories
- **FrostyNeighbor APT**: Belarussian nation-state group targeting government organizations in Poland and Ukraine with spear-phishing
- **Pwn2Own Researchers**: Security researchers demonstrating 39 unique zero-day vulnerabilities across enterprise systems
- **TanStack Attackers**: Supply chain compromise affecting hundreds of packages and major organizations like OpenAI
- **REMUS Operators**: Advanced infostealer campaigns focusing on session theft and Malware-as-a-Service operations