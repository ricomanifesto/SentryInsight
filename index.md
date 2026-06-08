# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with threat actors targeting enterprise infrastructure and popular software systems. The most significant active exploits include a Check Point VPN zero-day being exploited by the Qilin ransomware gang, a critical Gogs Git service vulnerability enabling remote code execution, and widespread attacks against WordPress sites through an Everest Forms Pro flaw. Additional concerns include active exploitation of SolarWinds Serv-U servers for denial-of-service attacks and a Cisco SD-WAN Manager vulnerability with no available patch. Supply chain attacks are also proliferating through GitHub repositories and npm packages, while various APT groups continue deploying sophisticated backdoors to maintain persistent access to compromised networks.

## Active Exploitation Details

### Check Point VPN Zero-Day
- **Description**: Critical vulnerability in Check Point Remote Access VPN and Mobile Access deployments configured to use the deprecated IKEv1 key exchange protocol that allows password bypass
- **Impact**: Attackers can bypass authentication mechanisms and gain unauthorized access to VPN networks
- **Status**: Currently being exploited in zero-day attacks; patches have been released by Check Point

### Gogs Git Service Zero-Day
- **Description**: Critical zero-day vulnerability in the Gogs Git service platform that enables remote code execution
- **Impact**: Attackers can compromise Internet-facing instances and access any repositories, including private ones
- **Status**: Critical zero-day flaw that has been patched by Gogs

### Everest Forms Pro WordPress Plugin
- **Description**: Critical vulnerability in the Everest Forms Pro plugin for WordPress that allows complete website takeover
- **Impact**: Hackers can gain full administrative control of WordPress websites
- **Status**: Currently being actively exploited
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service
- **Description**: High-severity security flaw in SolarWinds Serv-U multi-protocol file server software that can cause system crashes
- **Impact**: Attackers can crash servers and disrupt file transfer services
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog; actively being exploited

### Cisco Catalyst SD-WAN Manager
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager with active exploitation
- **Impact**: Potential for unauthorized access and system compromise
- **Status**: Currently under active exploitation with no patch available
- **CVE ID**: CVE-2026-20245

### UniFi OS Server Vulnerabilities
- **Description**: Chain of three previously fixed vulnerabilities in Ubiquiti UniFi OS server that can be combined for exploitation
- **Impact**: Remote code execution with root privileges without authentication
- **Status**: Vulnerabilities are already fixed but can be chained together for attack

## Affected Systems and Products

- **Check Point VPN Systems**: Remote Access VPN and Mobile Access deployments using IKEv1 protocol
- **Gogs Git Service**: Internet-facing instances of the self-hosted Git service
- **WordPress Sites**: Websites using the Everest Forms Pro plugin
- **SolarWinds Infrastructure**: Servers running Serv-U multi-protocol file server software
- **Cisco Network Equipment**: Catalyst SD-WAN Manager deployments
- **Ubiquiti Network Devices**: UniFi OS server installations
- **DD-WRT Routers**: Router firmware vulnerable to C0XMO botnet attacks
- **GitHub Repositories**: Microsoft repositories and other GitHub projects affected by Miasma worm
- **npm Ecosystem**: Over 50 legitimate packages compromised in supply chain attacks
- **Meta AI Systems**: Instagram accounts accessed through AI support system exploitation

## Attack Vectors and Techniques

- **VPN Protocol Exploitation**: Targeting deprecated IKEv1 implementations to bypass authentication
- **Remote Code Execution**: Exploiting web application vulnerabilities for system compromise
- **Supply Chain Attacks**: Compromising legitimate software packages and repositories with malicious code
- **Social Engineering**: Using fake IT support calls and vishing techniques to gain initial access
- **Botnet Propagation**: Spreading malware through router firmware vulnerabilities
- **AI System Manipulation**: Exploiting AI-powered support systems to reset user passwords
- **Physical Intrusion**: Combining vishing with physical access attempts for data theft
- **Repository Worm Attacks**: Self-replicating malware spreading through Git repositories

## Threat Actor Activities

- **Qilin Ransomware Gang**: Actively exploiting Check Point VPN zero-day vulnerabilities for network infiltration
- **UNC3753**: Conducting financially motivated data theft extortion campaigns targeting professional services using vishing and physical intrusion techniques
- **VerdantBamboo (Chinese APT)**: Deploying BSD variants of BRICKSTORM backdoor along with PLENET and AGENTPSD malware on Linux appliances
- **UNC5221 (Chinese Espionage Group)**: Accessing Microsoft 365 environments using Brickstorm backdoor and undocumented malware for persistent access
- **Silent Ransom Group**: Targeting U.S. law firms with fake IT support calls leading to rapid data theft within hours
- **C0XMO Botnet Operators**: Spreading Gafgyt botnet variants through DD-WRT router vulnerabilities while eliminating competing malware
- **Supply Chain Attackers**: Distributing IronWorm and Miasma worm variants through npm packages and GitHub repositories for information stealing