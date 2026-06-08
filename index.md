# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms and systems. The most significant threats include a high-severity zero-day vulnerability in Cisco Catalyst SD-WAN Manager that enables root privilege escalation, and a critical flaw in the Everest Forms Pro WordPress plugin allowing complete website takeover. Additional concerning exploitation activity includes the deployment of the C0XMO botnet targeting DD-WRT router firmware vulnerabilities, active exploitation of SolarWinds Serv-U denial-of-service flaws, and sophisticated supply chain attacks including the Miasma worm targeting GitHub repositories and the IronWorm campaign affecting npm packages.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: A high-severity unpatched vulnerability in Cisco Catalyst SD-WAN Manager that allows privilege escalation to root level
- **Impact**: Attackers can gain complete administrative control of affected SD-WAN management systems
- **Status**: Currently being actively exploited in the wild with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: A critical vulnerability in the Everest Forms Pro plugin affecting WordPress installations with approximately 4,000 active deployments
- **Impact**: Enables arbitrary code execution leading to complete website compromise and takeover
- **Status**: Under active exploitation by threat actors targeting WordPress sites
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: A high-severity flaw in SolarWinds Serv-U multi-protocol file server software that can cause server crashes
- **Impact**: Attackers can crash affected servers, causing denial of service conditions
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Allows botnet infection and can spread to devices with various CPU architectures
- **Status**: Currently being exploited to build botnet infrastructure that also eliminates rival malware

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Network management systems vulnerable to privilege escalation attacks
- **WordPress Sites with Everest Forms Pro Plugin**: Approximately 4,000 active installations at risk of complete compromise
- **SolarWinds Serv-U**: Multi-protocol file server software susceptible to denial of service attacks
- **DD-WRT Router Firmware**: Network infrastructure devices being compromised for botnet operations
- **FFmpeg Media Library**: 21 newly discovered zero-day vulnerabilities affecting video processing systems
- **GitHub Repositories**: 73 Microsoft repositories compromised in Miasma worm supply chain attack
- **npm Package Ecosystem**: Over 50 legitimate packages poisoned in IronWorm and Miasma variant attacks
- **Gas Station Tank Gauge Systems**: Over 900 automatic tank gauge systems exposed online across US critical infrastructure

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Cisco SD-WAN systems for privilege escalation
- **WordPress Plugin Exploitation**: Code injection attacks through vulnerable form processing functionality
- **Botnet Propagation**: Automated scanning and exploitation of router firmware vulnerabilities for malware distribution
- **Supply Chain Poisoning**: Injection of malicious code into legitimate software packages and repositories
- **Social Engineering**: Fake IT support calls targeting law firms and professional services organizations
- **AI-Powered Support System Abuse**: Exploitation of Meta's AI support system to reset Instagram account passwords
- **Credential Phishing**: Suspicious login prompts deployed through compromised polyfill services on legitimate websites

## Threat Actor Activities

- **C0XMO Botnet Operators**: Targeting DD-WRT routers while actively removing competing malware from infected systems
- **Silent Ransom Group**: Conducting sophisticated social engineering campaigns against US law firms with rapid data exfiltration capabilities
- **UNC5221 (Chinese APT)**: Deploying new malware including Brickstorm backdoor, Plenet, and AgentPSD to maintain persistent access to Microsoft 365 environments
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **PCPJack**: Hijacking cloud servers from AWS, Google Cloud, and Azure to create covert SMTP relay networks for email-based attacks
- **Miasma Worm Operators**: Executing self-replicating supply chain attacks affecting major repositories including Microsoft's GitHub presence
- **Meta AI Support Attackers**: Successfully compromising over 20,000 Instagram accounts through AI support system manipulation