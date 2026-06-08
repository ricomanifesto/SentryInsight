# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with attackers targeting network infrastructure, web applications, and development environments. Most concerning are zero-day attacks against Check Point VPN solutions linked to the Qilin ransomware gang, active exploitation of Cisco Catalyst SD-WAN Manager systems (CVE-2026-20245), and ongoing attacks against WordPress sites through the Everest Forms Pro plugin (CVE-2026-3300). Additionally, threat actors are exploiting SolarWinds Serv-U systems to crash servers, while supply chain attacks are targeting npm repositories and GitHub platforms. Chinese APT groups are deploying new malware variants to maintain persistent access, and various botnets are spreading through router vulnerabilities.

## Active Exploitation Details

### Check Point VPN Zero-Day Vulnerability
- **Description**: Critical security flaw affecting Remote Access VPN and Mobile Access deployments
- **Impact**: Complete system compromise allowing ransomware deployment
- **Status**: Zero-day exploitation confirmed, security updates released by Check Point

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager
- **Impact**: System compromise and potential network infiltration
- **Status**: Actively exploited with no patch currently available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin
- **Impact**: Complete WordPress website takeover and administrative access
- **Status**: Active exploitation confirmed, hackers gaining full site control
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Server crashes and denial of service attacks
- **Status**: Added to CISA KEV catalog due to active exploitation

### DD-WRT Router Vulnerability
- **Description**: Security flaw in DD-WRT router firmware
- **Impact**: Botnet recruitment and device compromise
- **Status**: Actively exploited by C0XMO botnet variant

## Affected Systems and Products

- **Check Point Systems**: Remote Access VPN and Mobile Access deployments
- **Cisco Catalyst**: SD-WAN Manager systems across enterprise networks
- **WordPress Sites**: Websites using Everest Forms Pro plugin
- **SolarWinds Serv-U**: Multi-protocol file server installations
- **DD-WRT Routers**: Various models running DD-WRT firmware
- **Microsoft GitHub**: 73 repositories affected by Miasma worm
- **npm Ecosystem**: Over 50 legitimate packages poisoned in supply chain attacks
- **Gas Station Infrastructure**: Over 900 automatic tank gauge systems across the US
- **Android Devices**: Arabic-speaking users targeted by Asin spyware
- **Instagram Accounts**: 20,225 accounts compromised through Meta AI support system

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in VPN and network management systems
- **Supply Chain Attacks**: Malicious code injection into legitimate software packages and repositories
- **Social Engineering**: Vishing and fake IT support calls targeting law firms and professional services
- **Botnet Propagation**: Automated spreading through router vulnerabilities with rival malware elimination
- **Mobile Malware**: Distribution through fake news, PDF, and war map applications
- **AI-Powered Support Abuse**: Manipulation of Meta's AI support system for password resets
- **Physical Intrusion**: Combined cyber and physical attack methods for data theft

## Threat Actor Activities

- **Qilin Ransomware Gang**: Linked to Check Point VPN zero-day attacks, targeting enterprise networks for ransomware deployment
- **VerdantBamboo (China-nexus)**: Deploying BSD variant of BRICKSTORM backdoor along with PLENET and AGENTPSD malware on Linux appliances
- **UNC3753**: Conducting financially motivated data theft extortion campaigns using vishing and physical intrusions against US professional services
- **UNC5221 (Chinese APT)**: Accessing Microsoft 365 environments using Brickstorm backdoor and new malware variants for persistent access
- **Silent Ransom Group**: Targeting US law firms with fake IT support social engineering attacks leading to rapid data theft
- **C0XMO Botnet Operators**: Spreading through DD-WRT router vulnerabilities while eliminating competing malware
- **Supply Chain Attackers**: Deploying IronWorm and Miasma worm variants across npm ecosystem and GitHub repositories