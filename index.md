# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, with attackers targeting WordPress websites, network infrastructure, and enterprise systems. The most severe activity includes zero-day exploitation of Cisco SD-WAN Manager systems, active attacks against WordPress sites through the Everest Forms Pro plugin, and widespread botnet operations targeting DD-WRT routers. Additionally, supply chain attacks are affecting major platforms including Microsoft GitHub repositories and npm packages, while threat actors continue to leverage social engineering tactics against law firms and other professional services organizations.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager allowing privilege escalation
- **Impact**: Attackers can gain root access to compromised systems
- **Status**: Currently being exploited in the wild with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited by threat actors
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Flaw
- **Description**: High-severity vulnerability in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Server crashes and denial of service attacks
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Security flaw allowing unauthenticated network attackers to write arbitrary files
- **Impact**: File system compromise leading to root privilege escalation
- **Status**: Recently patched with public exploit code available
- **CVE ID**: CVE-2026-20230

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by C0XMO botnet
- **Impact**: Router compromise and botnet recruitment
- **Status**: Actively exploited in botnet campaigns

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Enterprise network management systems vulnerable to zero-day exploitation
- **WordPress Sites**: Websites using Everest Forms Pro plugin (approximately 4,000 installations)
- **SolarWinds Serv-U**: Multi-protocol file server software in enterprise environments
- **DD-WRT Routers**: Consumer and enterprise router firmware across multiple CPU architectures
- **Cisco Unified Communications Manager**: Enterprise communication systems
- **Microsoft GitHub Repositories**: 73 Microsoft repositories affected by Miasma worm supply chain attacks
- **npm Ecosystem**: Over 50 packages affected by IronWorm and Miasma worm variants
- **Smart TVs**: Consumer devices compromised for web-scraping proxy operations
- **Cloud Infrastructure**: 230+ AWS, Google Cloud, and Azure servers hijacked by PCPJack
- **Android Devices**: Arabic-speaking users targeted by Asin spyware through fake applications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN Manager vulnerability for privilege escalation
- **WordPress Plugin Exploitation**: Remote code execution through vulnerable Everest Forms Pro plugin
- **Botnet Propagation**: C0XMO botnet spreading through DD-WRT router vulnerabilities and eliminating competing malware
- **Social Engineering**: Silent Ransom Group using fake IT support calls to target law firms
- **Supply Chain Attacks**: Self-replicating worms (Miasma, IronWorm) targeting GitHub repositories and npm packages
- **Browser Compromise**: Hola Browser supply chain attack delivering cryptocurrency miners
- **Mobile Malware Distribution**: Fake news, PDF, and war map applications distributing Asin spyware
- **Web Shell Deployment**: OP-512 threat cluster targeting Microsoft IIS servers with custom frameworks
- **Cloud Server Hijacking**: PCPJack creating covert SMTP relay networks using compromised cloud infrastructure

## Threat Actor Activities

- **C0XMO Botnet Operators**: Targeting DD-WRT routers for botnet expansion while actively removing competing malware
- **Silent Ransom Group**: Conducting targeted extortion campaigns against U.S. law firms through social engineering
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor, Plenet, and AgentPSD malware for persistent Microsoft 365 access
- **OP-512 Threat Cluster**: Deploying custom web shell frameworks against Microsoft IIS servers
- **Miasma Worm Campaign**: Executing self-replicating supply chain attacks across GitHub and npm ecosystems
- **PCPJack**: Operating covert SMTP relay networks through hijacked cloud infrastructure
- **Asin Spyware Operators**: Targeting Arabic-speaking Android users through malicious applications
- **Magecart Campaign**: Abusing Stripe API infrastructure for credit card theft operations