# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems across various sectors. Threat actors are actively exploiting a zero-day vulnerability in Cisco Catalyst SD-WAN Manager that enables root privilege escalation, with no patch currently available. Simultaneously, attackers are leveraging recently patched flaws in SolarWinds Serv-U to crash servers and exploiting a critical WordPress plugin vulnerability to achieve complete site compromise. Supply chain attacks have intensified with new malware campaigns targeting the npm ecosystem, while Chinese APT groups continue deploying sophisticated backdoors to maintain persistent access to Microsoft 365 environments.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched zero-day vulnerability in Cisco Catalyst SD-WAN Manager allowing privilege escalation
- **Impact**: Attackers can gain root-level access to affected systems
- **Status**: Actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Server Crash Vulnerability
- **Description**: Recently patched high-severity flaw in SolarWinds Serv-U that allows attackers to crash servers
- **Impact**: Service disruption and denial of service attacks
- **Status**: Actively exploited despite patch availability

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical security vulnerability in Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution
- **Status**: Actively exploited in the wild

### Cisco Unified Communications Manager File Write Vulnerability
- **Description**: Bug allowing unauthenticated attackers on the network to write files and escalate to root privileges
- **Impact**: Full system compromise from network-accessible position
- **Status**: Patched after exploit code became public
- **CVE ID**: CVE-2026-20230

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Zero-day vulnerability with active exploitation
- **SolarWinds Serv-U**: Recently patched server crash vulnerability under active attack
- **WordPress Installations**: Sites using Everest Forms Pro plugin (4,000 active installations)
- **Cisco Unified Communications Manager**: Systems vulnerable to file write and privilege escalation
- **Microsoft 365 Environments**: Targeted by Chinese APT groups using custom backdoors
- **npm Ecosystem**: 36+ packages infected with IronWorm malware in supply chain attacks
- **Automatic Tank Gauge Systems**: Over 900 exposed systems across US critical infrastructure
- **Hola Browser for Windows**: Compromised in supply chain attack delivering cryptocurrency miners
- **GitHub Repositories**: Vulnerable to takeover through Claude Code GitHub Action flaw

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN vulnerabilities for privilege escalation
- **Supply Chain Attacks**: Malicious npm packages distributing IronWorm and Miasma worm variants targeting developer credentials
- **Web Shell Deployment**: OP-512 threat cluster deploying custom web shell frameworks on Microsoft IIS servers
- **Browser Compromise**: Hola Browser supply chain attack delivering undeclared cryptocurrency mining executables
- **Credential Theft**: Polyfill-based attacks presenting fake login prompts on legitimate websites like Toshiba and Muji
- **Repository Hijacking**: GitHub Action vulnerabilities allowing single malicious issues to compromise entire repositories
- **SMTP Relay Abuse**: PCPJack hijacking cloud servers to create covert email relay networks

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor alongside previously undocumented Plenet and AgentPSD malware for persistent Microsoft 365 access
- **OP-512**: New threat cluster targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack**: Hijacking 230+ cloud servers across AWS, Google Cloud, and Azure to establish covert SMTP relay networks
- **TA4922 (Chinese Group)**: Expanding cybercrime operations globally beyond traditional East Asian targets with diverse attack methodologies
- **Supply Chain Attackers**: Multiple campaigns targeting npm ecosystem with both malicious and poisoned versions of legitimate packages
- **Asin Spyware Operators**: Targeting Arabic-speaking users through fake news, PDF, and war map applications on Android platforms