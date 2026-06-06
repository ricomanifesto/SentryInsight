# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and infrastructure systems, with attackers actively exploiting several high-severity vulnerabilities across WordPress plugins, network infrastructure, and supply chain components. The most concerning activities include active exploitation of an unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager that enables root privilege escalation, widespread attacks against WordPress sites through a critical Everest Forms Pro plugin flaw, and ongoing compromise of SolarWinds Serv-U servers causing denial of service conditions. Additionally, sophisticated supply chain attacks are proliferating through npm packages and GitHub repositories, while threat actors are leveraging exposed infrastructure systems including fuel tank gauges and cloud servers for malicious operations.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: A high-severity privilege escalation vulnerability in Cisco Catalyst SD-WAN Manager that allows attackers to gain root-level access
- **Impact**: Complete system compromise with root privileges, enabling full control over network infrastructure
- **Status**: Currently being actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: A critical vulnerability in the Everest Forms Pro WordPress plugin that allows arbitrary code execution
- **Impact**: Complete website takeover and control of WordPress installations
- **Status**: Actively exploited in the wild against sites using the plugin
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: A high-severity flaw in SolarWinds Serv-U multi-protocol file server software that can be exploited to crash servers
- **Impact**: Server crashes leading to denial of service conditions and service disruption
- **Status**: Recently patched but actively exploited, added to CISA KEV catalog

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library through AI analysis
- **Impact**: Potential code execution and system compromise in applications using FFmpeg
- **Status**: Newly discovered vulnerabilities requiring assessment and patching

## Affected Systems and Products

- **WordPress Sites**: Installations using Everest Forms Pro plugin (approximately 4,000 active installations)
- **Cisco SD-WAN Infrastructure**: Catalyst SD-WAN Manager systems across enterprise networks
- **SolarWinds Serv-U**: Multi-protocol file server deployments
- **FFmpeg Applications**: Any software utilizing the FFmpeg media library
- **Cloud Infrastructure**: AWS, Google Cloud, and Microsoft Azure servers targeted by PCPJack
- **Fuel Tank Systems**: Over 900 automatic tank gauge systems across US critical infrastructure
- **GitHub Repositories**: 73 Microsoft repositories affected by Miasma worm attacks
- **NPM Ecosystem**: Multiple packages compromised in IronWorm and Miasma supply chain attacks
- **Smart TV Systems**: Devices running apps with embedded Bright Data SDK
- **Hola Browser**: Windows version compromised with cryptocurrency miner

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN vulnerability for privilege escalation
- **WordPress Plugin Abuse**: Exploitation of critical Everest Forms Pro flaw for site takeover
- **Supply Chain Compromise**: Self-replicating worms targeting npm packages and GitHub repositories
- **Infrastructure Exploitation**: Targeting exposed fuel tank gauge systems for unauthorized access
- **Cloud Server Hijacking**: PCPJack campaign compromising 230 cloud servers for SMTP relay networks
- **Browser Compromise**: Supply chain attack on Hola Browser delivering cryptocurrency miners
- **Web Shell Deployment**: OP-512 threat cluster using custom frameworks against Microsoft IIS servers
- **Social Engineering**: FIFA World Cup 2026-themed scams using fake websites and banking malware

## Threat Actor Activities

- **UNC5221**: Chinese espionage group deploying Brickstorm backdoor, Plenet, and AgentPSD malware for persistent access to Microsoft 365 environments
- **PCPJack**: Threat actor hijacking cloud infrastructure to create covert SMTP email relay networks
- **OP-512**: New threat cluster targeting Microsoft IIS servers with custom web shell frameworks
- **Miasma Campaign**: Self-replicating supply chain attacks affecting GitHub repositories and npm packages
- **IronWorm Operators**: Rust-based information stealer campaign targeting npm ecosystem developers
- **TA4922**: Chinese cybercrime group expanding operations globally beyond East Asia
- **Asin Spyware Authors**: Targeting Arabic-speaking users through fake news, PDF, and war map applications
- **FIFA Scammers**: Multiple threat actors leveraging World Cup 2026 themes for fraud and malware distribution