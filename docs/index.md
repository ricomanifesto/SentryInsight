# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, with several zero-day and recently patched flaws posing significant threats. The most severe activity involves a critical WordPress plugin vulnerability in Everest Forms Pro (CVE-2026-3300) allowing complete site takeover, an unpatched Cisco Catalyst SD-WAN Manager zero-day (CVE-2026-20245) enabling root privilege escalation, and a SolarWinds Serv-U flaw being exploited for denial-of-service attacks. Supply chain attacks are also escalating with the Miasma worm campaign targeting Microsoft GitHub repositories and multiple npm package compromises through IronWorm malware. Additionally, over 900 gas station fuel tank monitoring systems are exposed to attacks, and threat actors are leveraging compromised cloud infrastructure for covert operations.

## Active Exploitation Details

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Everest Forms Pro WordPress plugin that allows attackers to execute arbitrary code
- **Impact**: Complete site compromise and takeover of WordPress websites
- **Status**: Actively exploited in the wild, affects approximately 4,000 active installations
- **CVE ID**: CVE-2026-3300

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity unpatched vulnerability in Cisco Catalyst SD-WAN Manager systems
- **Impact**: Root privilege escalation allowing full system compromise
- **Status**: Zero-day actively exploited with no patch currently available
- **CVE ID**: CVE-2026-20245

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Server crashes and denial of service attacks
- **Status**: Recently patched but actively exploited, added to CISA's Known Exploited Vulnerabilities catalog

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library through AI-powered analysis
- **Impact**: Potential code execution and system compromise in applications using FFmpeg
- **Status**: Newly discovered zero-days requiring immediate attention across multimedia applications

## Affected Systems and Products

- **WordPress Sites**: Everest Forms Pro plugin installations vulnerable to complete takeover
- **Cisco SD-WAN Manager**: Network infrastructure systems exposed to privilege escalation
- **SolarWinds Serv-U**: File server software vulnerable to denial-of-service attacks
- **FFmpeg Applications**: Widespread impact across video processing and multimedia applications
- **Gas Station Tank Gauges**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure
- **Microsoft GitHub Repositories**: 73 repositories compromised in Miasma worm supply chain attack
- **npm Package Ecosystem**: Multiple legitimate packages compromised with IronWorm malware
- **Cloud Infrastructure**: 230+ AWS, Google Cloud, and Azure servers hijacked for SMTP relay networks
- **Hola Browser**: Windows version compromised to deliver cryptocurrency miners
- **Smart TV Platforms**: Devices converted into web-scraping proxies through malicious apps

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Miasma worm self-replication across GitHub repositories and npm packages
- **Web Application Exploitation**: Direct exploitation of WordPress plugin vulnerabilities for site takeover
- **Zero-Day Exploitation**: Active attacks against unpatched Cisco infrastructure components
- **IoT Device Targeting**: Exploitation of exposed industrial control systems and tank monitoring equipment
- **Cloud Infrastructure Hijacking**: PCPJack campaign compromising cloud servers for covert email operations
- **Browser-Based Attacks**: Credential theft and data exfiltration through compromised browser applications
- **Social Engineering**: FIFA World Cup 2026-themed phishing campaigns and fake websites

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying Brickstorm backdoor, Plenet, and AgentPSD malware for persistent access to Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack Campaign**: Hijacking cloud servers across AWS, Google Cloud, and Azure to create covert SMTP relay networks
- **TA4922 (Chinese Cybercrime Group)**: Expanding global cybercrime operations beyond traditional East Asian targets
- **Miasma Worm Operators**: Conducting large-scale supply chain attacks targeting software repositories and development infrastructure
- **Asin Spyware Campaign**: Targeting Arabic-speaking users through fake news applications, PDF readers, and war mapping tools
- **IronWorm Campaign**: Distributing Rust-based information stealers through compromised npm packages