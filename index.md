# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation, posing significant threats to enterprise and cloud infrastructures. The most concerning activity includes zero-day exploitation of Cisco Catalyst SD-WAN Manager systems enabling root privilege escalation, active attacks against WordPress sites through a critical Everest Forms Pro plugin vulnerability, and denial-of-service attacks targeting SolarWinds Serv-U file servers. Supply chain attacks are also intensifying with self-replicating worms targeting npm repositories and Microsoft GitHub environments, while threat actors leverage exposed fuel tank gauge systems and compromised cloud servers for malicious operations.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager that allows privilege escalation attacks
- **Impact**: Attackers can gain root-level access to affected systems, potentially compromising entire network infrastructures
- **Status**: Currently being actively exploited with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete website takeover through arbitrary code execution capabilities
- **Status**: Under active exploitation by threat actors
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity security flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers and disrupt file transfer operations
- **Status**: Recently patched but actively exploited, added to CISA's Known Exploited Vulnerabilities catalog

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library
- **Impact**: Potential code execution and system compromise in applications using FFmpeg
- **Status**: Newly discovered vulnerabilities requiring immediate attention

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management systems vulnerable to privilege escalation
- **WordPress Sites**: Websites using Everest Forms Pro plugin vulnerable to complete compromise
- **SolarWinds Serv-U**: File server software susceptible to denial-of-service attacks
- **FFmpeg-based Applications**: Media processing applications containing the vulnerable library
- **Microsoft GitHub Repositories**: 73 repositories compromised by Miasma worm attacks
- **npm Package Ecosystem**: Over 50 legitimate packages targeted by IronWorm and Miasma variants
- **AWS, Google Cloud, Azure Servers**: 230 cloud servers hijacked by PCPJack threat actor
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed across US critical infrastructure
- **Hola Browser for Windows**: Compromised to deliver cryptocurrency mining malware
- **Android Devices**: Arabic-speaking users targeted by Asin spyware through fake applications

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Cisco SD-WAN systems
- **Plugin-based Attacks**: Targeting WordPress websites through vulnerable third-party plugins
- **Supply Chain Attacks**: Self-replicating worms propagating through software repositories and development environments
- **Cloud Infrastructure Hijacking**: Unauthorized access to cloud servers for creating covert SMTP relay networks
- **Critical Infrastructure Targeting**: Exploitation of exposed industrial control systems in fuel storage facilities
- **Social Engineering**: FIFA World Cup 2026-themed scams using fake websites and banking malware
- **Mobile Spyware Distribution**: Malicious Android applications disguised as news, PDF, and mapping tools
- **Browser Compromise**: Supply chain attacks against browser software to deliver cryptocurrency miners

## Threat Actor Activities

- **UNC5221 Chinese APT Group**: Deploying Brickstorm backdoor and new malware (Plenet, AgentPSD) to maintain persistent access to Microsoft 365 environments
- **PCPJack**: Hijacking cloud infrastructure across major providers to establish covert email relay networks
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **Miasma Campaign**: Self-replicating supply chain attacks targeting npm repositories and Microsoft GitHub environments
- **IronWorm Operators**: Rust-based information stealing campaigns targeting software developers through npm package poisoning
- **TA4922 Chinese Group**: Expanding cybercrime operations globally beyond traditional East Asian targets
- **Fuel Infrastructure Attackers**: Actively exploiting exposed automatic tank gauge systems across US critical infrastructure