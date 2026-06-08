# Exploitation Report

Critical exploitation activity is currently affecting multiple enterprise systems, with attackers leveraging both zero-day vulnerabilities and recently patched flaws to compromise networks. The most severe incidents include active exploitation of an unpatched Cisco SD-WAN Manager zero-day (CVE-2026-20245) enabling root privilege escalation, widespread attacks against WordPress sites through the Everest Forms Pro plugin (CVE-2026-3300), and ongoing campaigns targeting SolarWinds Serv-U file servers for denial-of-service attacks. Additionally, sophisticated threat actors are deploying new malware variants, conducting supply chain attacks against major repositories, and exploiting critical infrastructure systems including fuel tank monitoring systems across the United States.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day Vulnerability
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager that allows attackers to escalate privileges to root level
- **Impact**: Complete system compromise with administrative access, enabling full control over SD-WAN infrastructure
- **Status**: Actively exploited in the wild with no patch currently available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Critical Flaw
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Complete site compromise through arbitrary code execution, allowing attackers full control over WordPress websites
- **Status**: Actively exploited by threat actors to take over websites
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software that can cause server crashes
- **Impact**: Service disruption through denial-of-service attacks, potentially affecting file transfer operations
- **Status**: Recently added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Device compromise and inclusion in botnet operations, with capability to spread across different CPU architectures
- **Status**: Actively exploited for botnet recruitment and malware distribution

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: All versions affected by unpatched zero-day vulnerability
- **WordPress Sites**: Websites using Everest Forms Pro plugin with approximately 4,000 installations at risk
- **SolarWinds Serv-U**: Multi-protocol file server software vulnerable to denial-of-service attacks
- **DD-WRT Routers**: Router firmware susceptible to botnet infection and malware distribution
- **Microsoft GitHub Repositories**: 73 Microsoft repositories compromised by Miasma supply chain attack
- **npm Ecosystem**: Over 50 legitimate packages poisoned in supply chain attacks
- **Fuel Tank Monitoring Systems**: Over 900 automatic tank gauge systems exposed across US critical infrastructure
- **Meta AI Support Systems**: Instagram accounts vulnerable through AI-powered support system exploitation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Cisco SD-WAN Manager for immediate system compromise
- **Supply Chain Attacks**: Self-replicating worms targeting software repositories and package managers including npm and GitHub
- **Social Engineering**: UNC3753 using vishing (voice phishing) and physical intrusions for data theft extortion
- **Web Shell Deployment**: OP-512 threat cluster deploying custom web shell frameworks on Microsoft IIS servers
- **Botnet Operations**: C0XMO malware spreading through router vulnerabilities and eliminating competing malware
- **Plugin Exploitation**: WordPress plugin vulnerabilities being exploited for complete site takeover
- **AI System Abuse**: Meta AI support system manipulation for password reset attacks on Instagram accounts

## Threat Actor Activities

- **UNC3753**: Conducting financially motivated data theft extortion campaigns targeting professional, legal, and financial services organizations through vishing and physical intrusions
- **Silent Ransom Group**: Actively targeting US law firms and professional services with fake IT support calls leading to rapid data theft
- **UNC5221**: Chinese espionage group maintaining persistent access to Microsoft 365 environments using Brickstorm backdoor and new malware variants Plenet and AgentPSD
- **OP-512**: Previously unreported threat cluster targeting Microsoft IIS servers with custom web shell frameworks for persistent access
- **C0XMO Botnet Operators**: Deploying Gafgyt botnet variant targeting DD-WRT routers and eliminating competing malware
- **Miasma Campaign**: Self-replicating supply chain attack affecting Microsoft GitHub repositories and npm packages with information-stealing capabilities