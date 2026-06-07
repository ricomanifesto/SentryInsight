# Exploitation Report

Current cybersecurity landscape shows intense active exploitation across multiple critical vulnerabilities spanning network infrastructure, web applications, and supply chain attacks. The most concerning activities include zero-day exploitation of Cisco Catalyst SD-WAN Manager systems enabling root privilege escalation, widespread attacks against WordPress sites through the Everest Forms Pro plugin, and ongoing denial-of-service campaigns targeting SolarWinds Serv-U servers. Additionally, sophisticated supply chain attacks are proliferating through npm packages and GitHub repositories, while threat actors are leveraging social engineering tactics and compromising internet-exposed infrastructure systems.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: High-severity zero-day vulnerability in Cisco Catalyst SD-WAN Manager allowing privilege escalation
- **Impact**: Attackers can gain root-level access to SD-WAN management infrastructure
- **Status**: Currently being exploited in the wild with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete website takeover through arbitrary code execution capabilities
- **Status**: Actively exploited by threat actors for full site compromise
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Server crashes and denial of service attacks against file transfer infrastructure
- **Status**: Recently added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being leveraged for botnet propagation
- **Impact**: Router compromise and integration into the C0XMO botnet for malicious activities
- **Status**: Actively exploited by the C0XMO variant of the Gafgyt botnet

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management systems vulnerable to privilege escalation attacks
- **WordPress Sites**: Websites using Everest Forms Pro plugin vulnerable to complete compromise
- **SolarWinds Serv-U**: File transfer servers experiencing denial of service attacks
- **DD-WRT Routers**: Router firmware vulnerable to botnet recruitment
- **Automatic Tank Gauge Systems**: Over 900 exposed fuel monitoring systems across US critical infrastructure
- **Microsoft IIS Servers**: Web servers targeted by OP-512 threat cluster with custom web shell frameworks
- **AWS, Google Cloud, Azure**: Cloud servers hijacked by PCPJack for covert SMTP relay networks
- **npm Ecosystem**: JavaScript package repository targeted by supply chain attacks
- **Microsoft GitHub Repositories**: 73 repositories compromised by Miasma worm attacks
- **Hola Browser**: Windows version compromised in supply chain attack delivering cryptocurrency miners

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in network infrastructure
- **WordPress Plugin Attacks**: Targeting vulnerable plugins for website takeover
- **Social Engineering**: Silent Ransom Group using fake IT support calls against law firms
- **Supply Chain Attacks**: Multiple campaigns targeting npm packages and GitHub repositories
- **Botnet Operations**: C0XMO botnet spreading through router vulnerabilities and eliminating competing malware
- **Web Shell Deployment**: OP-512 cluster using custom frameworks against IIS servers
- **Cloud Infrastructure Hijacking**: PCPJack compromising cloud servers for email relay networks
- **Browser Compromise**: Supply chain attacks against browser applications
- **Internet-Exposed Systems**: Direct attacks against publicly accessible infrastructure

## Threat Actor Activities

- **Silent Ransom Group**: Actively targeting US law firms and professional services with social engineering attacks leading to rapid data theft
- **C0XMO Botnet Operators**: Expanding botnet infrastructure through DD-WRT router exploitation while eliminating rival malware
- **OP-512 Threat Cluster**: Previously unreported group targeting Microsoft IIS servers with sophisticated web shell frameworks
- **Chinese APT UNC5221**: Deploying new malware including Brickstorm backdoor, Plenet, and AgentPSD to maintain persistent access to Microsoft 365 environments
- **PCPJack**: Cloud infrastructure hijacker creating covert SMTP relay networks across major cloud providers
- **IronWorm Campaign**: Rust-based supply chain attackers targeting npm ecosystem with information stealers
- **Miasma Worm Operators**: Self-replicating malware campaign targeting software repositories including Microsoft's GitHub presence
- **Asin Spyware Developers**: Targeting Arabic-speaking users through fake applications including news, PDF, and war map apps