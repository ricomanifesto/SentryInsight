# Exploitation Report

Critical vulnerabilities are under active exploitation across multiple platforms, with threat actors leveraging zero-day flaws and recently patched vulnerabilities to gain unauthorized access and control over systems. The most severe incidents include active exploitation of a zero-day vulnerability in Cisco Catalyst SD-WAN Manager, enabling root privilege escalation, and attacks against WordPress sites through a critical Everest Forms Pro plugin flaw. Additionally, attackers are targeting SolarWinds Serv-U servers to cause denial of service conditions, while sophisticated supply chain attacks continue to compromise development environments through malicious npm packages and GitHub repositories.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity zero-day vulnerability in Cisco Catalyst SD-WAN Manager enabling privilege escalation
- **Impact**: Attackers can gain root-level privileges on affected systems
- **Status**: Currently unpatched and under active exploitation
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical security flaw in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution, allowing full takeover of WordPress websites
- **Status**: Under active exploitation by threat actors
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Flaw
- **Description**: High-severity vulnerability in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers, causing denial of service conditions
- **Status**: Recently patched but actively exploited, added to CISA's Known Exploited Vulnerabilities catalog

### FFmpeg Zero-Day Vulnerabilities
- **Description**: 21 previously unknown vulnerabilities discovered in FFmpeg media library
- **Impact**: Potential for exploitation in systems using FFmpeg for video processing
- **Status**: Recently discovered through AI-powered security research

## Affected Systems and Products

- **WordPress Sites**: Websites using Everest Forms Pro plugin vulnerable to complete takeover
- **Cisco SD-WAN Infrastructure**: Catalyst SD-WAN Manager systems at risk of privilege escalation
- **SolarWinds Environments**: Serv-U file server deployments subject to denial of service attacks
- **Gas Station Infrastructure**: Over 900 automatic tank gauge systems exposed online across the United States
- **Cloud Platforms**: 230 compromised servers across AWS, Google Cloud, and Microsoft Azure used for SMTP relay networks
- **Microsoft GitHub**: 73 Microsoft repositories compromised in Miasma supply chain attack
- **NPM Ecosystem**: Over 50 legitimate packages poisoned with malicious variants
- **Smart TV Platforms**: Consumer devices converted into web-scraping proxies through malicious apps
- **Hola Browser**: Windows version compromised to deliver cryptocurrency miners

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active targeting of unpatched Cisco SD-WAN vulnerability for privilege escalation
- **WordPress Plugin Attacks**: Exploitation of Everest Forms Pro to achieve arbitrary code execution
- **Supply Chain Poisoning**: Miasma and IronWorm campaigns targeting npm packages and GitHub repositories
- **Infrastructure Targeting**: Attacks against exposed industrial control systems, particularly fuel tank gauges
- **Web Shell Deployment**: OP-512 threat cluster using custom frameworks to maintain persistence on IIS servers
- **Cloud Resource Hijacking**: PCPJack operations compromising cloud servers for covert SMTP relay networks
- **Credential Harvesting**: Polyfill-based attacks displaying fake login prompts on legitimate websites
- **Mobile Spyware**: Asin malware targeting Arabic-speaking users through fake applications

## Threat Actor Activities

- **UNC5221 Chinese APT**: Deploying Brickstorm backdoor and new malware variants (Plenet, AgentPSD) to maintain access to Microsoft 365 environments
- **TA4922 Chinese Group**: Expanding cybercrime operations globally beyond traditional East Asian targets
- **PCPJack**: Creating covert SMTP relay networks by hijacking cloud infrastructure across major providers
- **OP-512 Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **Miasma Campaign**: Self-replicating supply chain attacks affecting Microsoft repositories and npm ecosystem
- **IronWorm Operations**: Rust-based information stealing malware distributed through poisoned npm packages
- **FIFA 2026 Scammers**: Launching early fraud campaigns with fake websites and banking malware ahead of World Cup