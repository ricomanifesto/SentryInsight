# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms with several high-impact vulnerabilities being actively exploited in the wild. The most severe threats include a zero-day vulnerability in Cisco Catalyst SD-WAN Manager that allows root privilege escalation, active exploitation of WordPress sites through the Everest Forms Pro plugin, and ongoing attacks against SolarWinds Serv-U servers causing denial-of-service conditions. Additionally, threat actors are leveraging DD-WRT router vulnerabilities for botnet expansion, conducting sophisticated supply chain attacks against npm packages and GitHub repositories, and exploiting exposed fuel tank gauge systems across critical infrastructure in the United States.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched vulnerability in Cisco Catalyst SD-WAN Manager allowing privilege escalation
- **Impact**: Attackers can gain root-level access to affected systems
- **Status**: Currently unpatched and actively exploited in the wild
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete website compromise through arbitrary code execution
- **Status**: Actively exploited to take full control of WordPress sites
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Server crashes and denial of service attacks
- **Status**: Recently patched but actively exploited by threat actors

### DD-WRT Router Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Router compromise and botnet enrollment with cross-architecture propagation capabilities
- **Status**: Actively exploited for botnet expansion

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions affected by unpatched zero-day vulnerability
- **WordPress Sites**: Sites using Everest Forms Pro plugin with approximately 4,000 installations at risk
- **SolarWinds Serv-U**: Multi-protocol file server software experiencing active DoS attacks
- **DD-WRT Routers**: Firmware vulnerable to botnet recruitment and lateral movement
- **Cloud Infrastructure**: AWS, Google Cloud, and Azure servers compromised by PCPJack for SMTP relay operations
- **NPM Ecosystem**: Over 50 packages affected by IronWorm and Miasma worm supply chain attacks
- **GitHub Repositories**: 73 Microsoft repositories compromised in Miasma worm campaign
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed across US critical infrastructure
- **Microsoft IIS Servers**: Targeted by OP-512 threat cluster using custom web shell frameworks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Cisco SD-WAN Manager vulnerability leveraged for privilege escalation
- **Web Application Attacks**: WordPress plugin exploitation leading to complete site takeover
- **Botnet Propagation**: Multi-architecture malware spreading across router networks
- **Supply Chain Poisoning**: Malicious npm packages and GitHub repository compromise
- **Social Engineering**: Silent Ransom Group using fake IT support calls to target law firms
- **Cloud Server Hijacking**: PCPJack creating covert SMTP relay networks across major cloud platforms
- **Web Shell Deployment**: OP-512 using custom frameworks for persistent IIS server access
- **Industrial System Targeting**: Exposed fuel tank gauges vulnerable to operational disruption

## Threat Actor Activities

- **C0XMO Botnet**: Gafgyt variant targeting DD-WRT routers and eliminating competing malware
- **Silent Ransom Group**: Conducting targeted extortion campaigns against US law firms through social engineering
- **UNC5221 (Chinese APT)**: Deploying Brickstorm, Plenet, and AgentPSD malware for persistent Microsoft 365 access
- **OP-512**: New threat cluster specifically targeting Microsoft IIS servers with custom web shell frameworks
- **PCPJack**: Hijacking cloud infrastructure to establish covert SMTP relay operations
- **IronWorm Operators**: Conducting Rust-based supply chain attacks targeting npm developers
- **Miasma Worm Campaign**: Self-replicating attacks affecting Microsoft GitHub repositories and npm packages