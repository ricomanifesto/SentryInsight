# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, posing significant risks to WordPress sites, enterprise networks, and cloud infrastructure. The most severe incidents include active exploitation of a critical WordPress plugin flaw (CVE-2026-3300) that enables complete site takeover, an unpatched Cisco SD-WAN zero-day (CVE-2026-20245) being exploited for root privilege escalation, and widespread attacks targeting SolarWinds Serv-U servers for denial of service. Additionally, sophisticated supply chain attacks are targeting npm packages and Microsoft GitHub repositories, while threat actors are leveraging compromised cloud servers and exposed industrial systems to establish covert operations.

## Active Exploitation Details

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Everest Forms Pro WordPress plugin that allows arbitrary code execution
- **Impact**: Attackers can achieve complete website takeover and control
- **Status**: Actively exploited in the wild against sites using the plugin
- **CVE ID**: CVE-2026-3300

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched vulnerability in Cisco Catalyst SD-WAN Manager
- **Impact**: Enables root privilege escalation on affected systems
- **Status**: Currently being exploited as a zero-day with no patch available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Denial of Service Flaw
- **Description**: High-severity vulnerability in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers and cause service disruption
- **Status**: Recently patched but actively exploited; added to CISA KEV catalog

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library
- **Impact**: Potential code execution and system compromise in applications using FFmpeg
- **Status**: Recently discovered by AI security analysis

## Affected Systems and Products

- **WordPress Sites**: Approximately 4,000 active installations of Everest Forms Pro plugin vulnerable to complete takeover
- **Cisco SD-WAN Infrastructure**: Enterprise network management systems at risk of root compromise
- **SolarWinds Serv-U**: File server installations vulnerable to denial of service attacks
- **Smart TV Platforms**: Consumer devices being converted into web-scraping proxy networks
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure
- **Cloud Servers**: 230 AWS, Google Cloud, and Azure servers compromised for SMTP relay operations
- **Microsoft GitHub Repositories**: 73 repositories affected by Miasma worm supply chain attacks
- **NPM Ecosystem**: Over 50 legitimate packages compromised in IronWorm and Miasma supply chain attacks
- **Hola Browser**: Windows version compromised to deliver cryptocurrency miners

## Attack Vectors and Techniques

- **Plugin Exploitation**: Direct exploitation of WordPress plugin vulnerabilities for immediate site control
- **Zero-Day Exploitation**: Targeting unpatched Cisco infrastructure for privilege escalation
- **Supply Chain Attacks**: Self-replicating worms targeting software repositories and package managers
- **IoT Device Compromise**: Converting smart TVs into proxy networks without user knowledge
- **Industrial System Targeting**: Exploiting exposed fuel tank monitoring systems in critical infrastructure
- **Cloud Infrastructure Hijacking**: Compromising cloud servers to establish covert SMTP relay networks
- **Browser Supply Chain**: Compromising legitimate browser distributions to deliver malware

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor and new malware (Plenet, AgentPSD) to maintain persistence in Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack**: Operating covert SMTP relay networks using hijacked cloud infrastructure across major providers
- **Miasma Worm Operators**: Conducting widespread supply chain attacks against GitHub repositories and npm packages
- **IronWorm Campaign**: Rust-based information stealing operations targeting npm ecosystem developers
- **TA4922 (Chinese Group)**: Expanding global cybercrime operations with diverse attack methodologies targeting multiple regions
- **Asin Spyware Operators**: Targeting Arabic-speaking users through fake news, PDF, and war map applications
- **FIFA 2026 Scammers**: Launching early fraudulent campaigns with fake websites and banking malware ahead of the World Cup