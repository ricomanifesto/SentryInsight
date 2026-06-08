# Exploitation Report

Current threat activity shows a concerning surge in zero-day exploitation and critical vulnerabilities across enterprise infrastructure. Most notably, threat actors are actively exploiting an unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager (CVE-2026-20245) that enables root privilege escalation with no patch currently available. Additionally, attackers are targeting WordPress sites through a critical flaw in the Everest Forms Pro plugin (CVE-2026-3300), allowing complete site takeover. CISA has added a SolarWinds Serv-U denial-of-service vulnerability to their Known Exploited Vulnerabilities catalog, indicating active exploitation in the wild. The threat landscape is further complicated by sophisticated supply chain attacks, including the Miasma worm campaign that has compromised 73 Microsoft GitHub repositories and new variants targeting the npm ecosystem through IronWorm malware.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager that allows attackers to escalate privileges to root level
- **Impact**: Complete system compromise with administrative access to network management infrastructure
- **Status**: Currently being actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin that allows arbitrary code execution
- **Impact**: Complete website takeover and full site compromise
- **Status**: Actively exploited in the wild against WordPress installations
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial-of-Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software that can be exploited to crash servers
- **Impact**: Service disruption and denial-of-service conditions on file transfer infrastructure
- **Status**: Added to CISA KEV catalog due to active exploitation, patch recently released

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Router compromise leading to botnet recruitment and potential lateral movement to other network devices
- **Status**: Actively exploited by Gafgyt botnet variant across multiple CPU architectures

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management platforms vulnerable to privilege escalation attacks
- **WordPress Sites with Everest Forms Pro**: Approximately 4,000 active installations at risk of complete compromise
- **SolarWinds Serv-U**: Multi-protocol file server software vulnerable to denial-of-service attacks
- **DD-WRT Router Firmware**: Network infrastructure devices susceptible to botnet recruitment
- **Microsoft GitHub Repositories**: 73 repositories compromised in Miasma worm supply chain attack
- **NPM Package Ecosystem**: Over 50 legitimate packages poisoned with IronWorm and Miasma variants
- **Cloud Infrastructure**: 230+ AWS, Google Cloud, and Azure servers hijacked by PCPJack threat actor
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed across US critical infrastructure
- **Microsoft IIS Servers**: Web servers targeted by OP-512 threat cluster with custom web shell frameworks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched Cisco SD-WAN infrastructure for privilege escalation
- **WordPress Plugin Exploitation**: Code injection attacks through vulnerable form processing functionality
- **Supply Chain Compromise**: Self-replicating worm attacks targeting software repositories and development environments
- **Social Engineering**: Fake IT support calls used by Silent Ransom Group against law firms and professional services
- **Botnet Recruitment**: Automated exploitation of router firmware to expand botnet infrastructure
- **Cloud Server Hijacking**: Compromise of cloud instances to create covert SMTP relay networks
- **Web Shell Deployment**: Custom framework deployment on IIS servers for persistent access
- **Credential Theft**: Android spyware campaigns targeting Arabic-speaking users through fake applications

## Threat Actor Activities

- **C0XMO Botnet**: Gafgyt variant targeting DD-WRT routers and expanding to multiple CPU architectures while eliminating rival malware
- **Silent Ransom Group**: Extortion gang conducting social engineering attacks against US law firms with data theft capabilities within hours
- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor and new malware (Plenet, AgentPSD) for persistent access to Microsoft 365 environments
- **OP-512 Threat Cluster**: Previously unreported group targeting Microsoft IIS servers with sophisticated web shell frameworks
- **PCPJack**: Cloud-focused threat actor hijacking major cloud platform servers to establish covert email relay infrastructure
- **IronWorm Campaign**: Supply chain attackers distributing Rust-based information stealers through poisoned NPM packages
- **Miasma Worm Operators**: Conducting large-scale supply chain attacks across GitHub repositories and software ecosystems