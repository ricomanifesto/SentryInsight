# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise and infrastructure systems. Most significantly, attackers are actively exploiting an unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager that enables root privilege escalation, with no patch currently available. CISA has added a high-severity SolarWinds Serv-U denial-of-service vulnerability to its Known Exploited Vulnerabilities catalog, indicating active exploitation causing server crashes. Additionally, threat actors are exploiting a critical WordPress plugin vulnerability in Everest Forms Pro to achieve complete site compromise, while sophisticated supply chain attacks including the Miasma worm campaign have targeted major repositories and npm packages.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched vulnerability allowing attackers to escalate privileges to root level
- **Impact**: Complete system compromise with root access enabling full control of SD-WAN infrastructure
- **Status**: Currently being actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Denial of Service Flaw
- **Description**: High-severity vulnerability in SolarWinds Serv-U multi-protocol file server software causing system crashes
- **Impact**: Attackers can crash servers and cause service disruption
- **Status**: Actively exploited and added to CISA KEV catalog, patch available

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in WordPress plugin with approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited by threat actors

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library
- **Impact**: Potential compromise of systems using FFmpeg for video processing
- **Status**: Newly discovered vulnerabilities requiring assessment

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management infrastructure vulnerable to privilege escalation
- **SolarWinds Serv-U**: Multi-protocol file server software susceptible to denial of service attacks
- **Everest Forms Pro WordPress Plugin**: Approximately 4,000 active installations at risk of complete compromise
- **FFmpeg Media Library**: Widely deployed media processing component with newly discovered vulnerabilities
- **Chrome Browser**: Record 429 security bugs patched in recent update
- **Microsoft GitHub Repositories**: 73 repositories compromised by Miasma worm supply chain attack
- **NPM Package Repository**: Multiple packages compromised by IronWorm and Miasma worm variants
- **Automatic Tank Gauge Systems**: Over 900 fuel monitoring systems exposed online across US critical infrastructure
- **Hola Browser for Windows**: Supply chain compromise delivering cryptocurrency mining malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched Cisco SD-WAN vulnerability for immediate system access
- **Supply Chain Poisoning**: Miasma worm self-replicating across GitHub repositories and npm packages
- **WordPress Plugin Exploitation**: Direct targeting of vulnerable form processing plugins for site takeover
- **Infrastructure Targeting**: Exploitation of exposed industrial control systems including fuel tank gauges
- **Web Shell Deployment**: OP-512 threat cluster using custom frameworks against Microsoft IIS servers
- **Credential Harvesting**: Polyfill-based attacks displaying fake login prompts on legitimate websites
- **Browser Supply Chain**: Compromise of browser distributions to deliver hidden cryptocurrency miners

## Threat Actor Activities

- **Miasma Worm Campaign**: Self-replicating supply chain attack compromising 73 Microsoft repositories and multiple npm packages
- **OP-512 Threat Cluster**: Previously unreported group targeting Microsoft IIS servers with custom web shell frameworks
- **UNC5221 Chinese APT**: Deploying new malware including Brickstorm, Plenet, and AgentPSD to maintain access to Microsoft 365 environments
- **PCPJack**: Hijacking 230 cloud servers across AWS, Google Cloud, and Azure to create covert SMTP relay networks
- **TA4922**: Chinese cybercrime group expanding operations globally beyond traditional East Asian targets
- **IronWorm Operators**: Rust-based information stealing campaign targeting npm developers and supply chain