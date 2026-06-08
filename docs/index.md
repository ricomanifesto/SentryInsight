# Exploitation Report

Current threat landscape shows significant active exploitation across multiple critical vulnerabilities and attack vectors. Check Point VPN solutions are under active zero-day exploitation by the Qilin ransomware gang, while CISA has added a SolarWinds Serv-U denial-of-service vulnerability to its Known Exploited Vulnerabilities catalog due to confirmed active attacks. The Everest Forms Pro WordPress plugin faces critical exploitation allowing complete website takeovers, and Cisco Catalyst SD-WAN Manager systems are being actively targeted with no available patches. Additionally, multiple sophisticated supply chain attacks are targeting GitHub repositories and npm packages, while threat actors are exploiting exposed fuel tank gauge systems across US critical infrastructure.

## Active Exploitation Details

### Check Point VPN Zero-Day Vulnerability
- **Description**: Critical security flaw affecting Check Point Remote Access VPN and Mobile Access deployments
- **Impact**: Enables threat actors to gain unauthorized access to VPN infrastructure and potentially pivot into internal networks
- **Status**: Zero-day exploitation confirmed, security updates released by Check Point

### SolarWinds Serv-U Denial-of-Service Vulnerability
- **Description**: High-severity security flaw in SolarWinds Serv-U multi-protocol file server software causing server crashes
- **Impact**: Attackers can crash servers and cause denial-of-service conditions
- **Status**: Actively exploited, added to CISA KEV catalog, patches available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Everest Forms Pro plugin allowing complete website compromise
- **Impact**: Attackers can take complete control of WordPress websites
- **Status**: Actively exploited in the wild
- **CVE ID**: CVE-2026-3300

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager with CVSS score of 7.8
- **Impact**: Enables unauthorized access and potential network compromise
- **Status**: Actively exploited with no patch currently available
- **CVE ID**: CVE-2026-20245

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Enables botnet recruitment and lateral movement to other device types across various CPU architectures
- **Status**: Actively exploited by C0XMO Gafgyt botnet variant

## Affected Systems and Products

- **Check Point VPN Solutions**: Remote Access VPN and Mobile Access deployments
- **SolarWinds Serv-U**: Multi-protocol file server software installations
- **WordPress Sites**: Websites using Everest Forms Pro plugin
- **Cisco SD-WAN Infrastructure**: Catalyst SD-WAN Manager deployments
- **DD-WRT Routers**: Devices running DD-WRT firmware across multiple CPU architectures
- **GitHub Repositories**: 73 Microsoft repositories affected by Miasma supply chain attacks
- **npm Ecosystem**: Over 50 packages compromised in IronWorm and Miasma worm attacks
- **Fuel Tank Gauge Systems**: Over 900 automatic tank gauge (ATG) systems across US critical infrastructure
- **Instagram Accounts**: 20,225 accounts compromised through Meta AI support system abuse

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Qilin ransomware leveraging unpatched Check Point VPN vulnerabilities
- **Ransomware Operations**: Qilin gang using VPN zero-days for initial access and lateral movement
- **Botnet Propagation**: C0XMO variant spreading through router vulnerabilities and eliminating competing malware
- **Supply Chain Attacks**: Self-replicating Miasma worms targeting GitHub repositories and npm packages
- **Social Engineering**: Silent Ransom Group using fake IT support calls to target law firms
- **Vishing and Physical Intrusions**: UNC3753 combining voice phishing with physical access attempts
- **AI Support System Abuse**: Attackers manipulating Meta's AI-powered support to reset Instagram passwords
- **Malicious Polyfill Injection**: Suspicious login prompts appearing on legitimate websites including Toshiba and Muji
- **Infrastructure Targeting**: Direct attacks on exposed fuel tank monitoring systems

## Threat Actor Activities

- **Qilin Ransomware Gang**: Actively exploiting Check Point VPN zero-days for network infiltration and ransomware deployment
- **VerdantBamboo (Chinese APT)**: Deploying BSD variants of BRICKSTORM backdoor along with PLENET and AGENTPSD malware on Linux appliances
- **UNC3753**: Conducting data theft extortion campaigns against US professional, legal, and financial services using combination of vishing and physical intrusion techniques
- **UNC5221 (Chinese APT)**: Maintaining persistent access to Microsoft 365 environments using Brickstorm backdoor and previously undocumented malware
- **Silent Ransom Group**: Targeting US law firms with sophisticated social engineering attacks involving fake IT support calls
- **C0XMO Botnet Operators**: Spreading Gafgyt botnet variant through DD-WRT router exploits while actively removing competing malware
- **Supply Chain Attackers**: Orchestrating widespread IronWorm and Miasma campaigns targeting npm packages and GitHub repositories with Rust-based information stealers