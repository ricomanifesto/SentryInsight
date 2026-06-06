# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems with significant impact across cloud infrastructure, network management platforms, and web applications. Active zero-day exploitation is occurring against Cisco Catalyst SD-WAN Manager systems, enabling root privilege escalation without available patches. Simultaneously, attackers are leveraging recently patched SolarWinds Serv-U vulnerabilities to crash file servers, while WordPress sites face ongoing compromise through critical plugin vulnerabilities. Supply chain attacks are proliferating through sophisticated malware campaigns targeting GitHub repositories and npm packages, with threat actors deploying advanced persistent techniques to maintain access across enterprise environments.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity vulnerability in Cisco Catalyst SD-WAN Manager allowing unauthorized privilege escalation
- **Impact**: Attackers can gain root-level access to SD-WAN management systems, potentially compromising entire network infrastructure
- **Status**: Currently being exploited in the wild with no patch available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software causing system crashes
- **Impact**: Attackers can crash file servers, disrupting file transfer operations and causing service outages
- **Status**: Recently patched but actively exploited; added to CISA's Known Exploited Vulnerabilities catalog

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution, allowing full administrative control
- **Status**: Actively exploited to take over WordPress websites

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library through AI-powered analysis
- **Impact**: Potential code execution and system compromise in applications utilizing FFmpeg for media processing
- **Status**: Newly discovered vulnerabilities requiring immediate patching across affected systems

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management platform vulnerable to privilege escalation attacks
- **SolarWinds Serv-U**: Multi-protocol file server software susceptible to denial of service attacks
- **WordPress Sites**: Websites using Everest Forms Pro plugin facing complete compromise
- **FFmpeg-based Applications**: Media processing applications containing newly discovered vulnerabilities
- **Microsoft GitHub Repositories**: 73 repositories compromised by Miasma worm supply chain attacks
- **npm Package Ecosystem**: Over 50 legitimate packages poisoned with malware in IronWorm campaign
- **Smart TV Devices**: Consumer devices being converted into web-scraping proxies through malicious applications
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN vulnerabilities for privilege escalation
- **Supply Chain Poisoning**: Malicious code injection into legitimate software packages and repositories
- **Web Shell Deployment**: Custom web shell frameworks targeting Microsoft IIS servers through OP-512 threat cluster
- **Credential Harvesting**: Fake login prompts deployed on legitimate websites through polyfill compromise
- **Proxy Network Creation**: Converting smart TVs into web-scraping exit nodes through embedded SDK exploitation
- **Worm Propagation**: Self-replicating malware spreading across GitHub repositories and npm packages
- **Browser-Based Attacks**: Increasing focus on browser-layer exploitation for credential theft and system access

## Threat Actor Activities

- **UNC5221 Chinese APT**: Deploying Brickstorm backdoor, Plenet, and AgentPSD malware for persistent Microsoft 365 access
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for sustained access
- **PCPJack**: Hijacking 230 cloud servers across AWS, Google Cloud, and Azure to establish covert SMTP relay networks
- **TA4922 Chinese Group**: Expanding cybercrime operations globally beyond traditional East Asian targets
- **Miasma Worm Operators**: Conducting large-scale supply chain attacks affecting major technology companies
- **IronWorm Campaign**: Distributing Rust-based information stealers through npm package poisoning
- **Asin Spyware Operators**: Targeting Arabic-speaking users through fake news, PDF, and war map applications