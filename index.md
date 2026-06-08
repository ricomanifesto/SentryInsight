# Exploitation Report

Current threat landscape demonstrates significant exploitation activity across multiple attack vectors, with attackers focusing on WordPress plugins, network infrastructure, and supply chain attacks. Critical zero-day vulnerabilities in Cisco Catalyst SD-WAN Manager and WordPress Everest Forms Pro plugin are being actively exploited in the wild, while threat actors are leveraging router firmware flaws and social engineering tactics to compromise enterprise environments. The C0XMO botnet continues spreading through DD-WRT router vulnerabilities, and sophisticated supply chain attacks like Miasma worm are targeting major repositories including Microsoft's GitHub infrastructure. Additionally, SolarWinds Serv-U servers face active exploitation for denial-of-service attacks, and Meta's AI support system was compromised to hijack thousands of Instagram accounts.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: High-severity unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager allowing privilege escalation
- **Impact**: Attackers can achieve root privilege escalation on affected systems
- **Status**: Currently being exploited in active attacks with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution, allowing attackers full control of WordPress websites
- **Status**: Actively exploited by threat actors for complete site takeover
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial-of-Service Vulnerability
- **Description**: High-severity security flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers through denial-of-service attacks
- **Status**: Recently patched but actively exploited, added to CISA's Known Exploited Vulnerabilities catalog

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Router compromise and botnet recruitment across various CPU architectures
- **Status**: Actively exploited for botnet propagation with capability to eliminate rival malware

## Affected Systems and Products

- **WordPress Sites**: Websites using Everest Forms Pro plugin (approximately 4,000 installations)
- **Cisco Network Infrastructure**: Catalyst SD-WAN Manager deployments
- **SolarWinds Serv-U**: Multi-protocol file server installations
- **DD-WRT Routers**: Various router models running DD-WRT firmware
- **Instagram Accounts**: Over 20,000 accounts compromised through Meta AI support system
- **Microsoft GitHub Repositories**: 73 repositories across four organizations affected by Miasma worm
- **npm Ecosystem**: Over 50 legitimate packages targeted in supply chain attacks
- **Cloud Infrastructure**: 230 AWS, Google Cloud, and Azure servers compromised by PCPJack
- **Fuel Tank Monitoring Systems**: Over 900 automatic tank gauge systems exposed across US infrastructure

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in network management systems
- **WordPress Plugin Exploitation**: Targeting critical flaws in popular plugins for site takeover
- **Botnet Propagation**: Automated spreading through router firmware vulnerabilities
- **Social Engineering**: Fake IT support calls targeting law firms and professional services
- **AI System Abuse**: Exploitation of Meta's AI-powered support system for account hijacking
- **Supply Chain Attacks**: Self-replicating worms targeting software repositories and package managers
- **Cloud Infrastructure Hijacking**: Compromising cloud servers to create covert SMTP relay networks
- **Polyfill Injection**: Malicious code injection on legitimate websites to display fake login prompts

## Threat Actor Activities

- **C0XMO Botnet Operators**: Deploying Gafgyt botnet variant through DD-WRT router vulnerabilities while eliminating competing malware
- **Silent Ransom Group**: Conducting targeted social engineering campaigns against US law firms using fake IT support calls
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor and new malware variants (Plenet, AgentPSD) to maintain persistence in Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack**: Hijacking cloud infrastructure to establish covert SMTP relay networks across major cloud providers
- **Miasma Worm Campaign**: Self-replicating supply chain attacks affecting Microsoft GitHub repositories and npm ecosystem
- **Meta AI Support Attackers**: Sophisticated exploitation of AI-powered support systems for large-scale account compromise