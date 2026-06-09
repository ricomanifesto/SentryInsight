# Exploitation Report

Current threat activity reveals a concerning landscape of active exploitation targeting critical infrastructure, enterprise software, and supply chain components. Several zero-day vulnerabilities are being actively exploited, including a critical Check Point VPN flaw linked to the Qilin ransomware gang and a Gogs zero-day enabling remote code execution. Notable incidents include NSO Group's renewed spear-phishing campaigns against WhatsApp users, widespread exploitation of WordPress plugins, and sophisticated supply chain attacks targeting software repositories. The exploitation of fuel tank monitoring systems and Internet-facing network appliances demonstrates the expanding attack surface threatening critical infrastructure operations.

## Active Exploitation Details

### Check Point VPN Zero-Day Vulnerability
- **Description**: Critical vulnerability affecting Remote Access VPN and Mobile Access deployments configured with deprecated IKEv1 key exchange protocol
- **Impact**: Attackers can bypass password authentication mechanisms in VPN setups
- **Status**: Actively exploited in zero-day attacks, security updates now available
- **CVE ID**: Currently being exploited as zero-day, patches released

### Gogs Remote Code Execution Zero-Day
- **Description**: Critical zero-day flaw in the Gogs Git service that allows remote code execution
- **Impact**: Attackers can compromise Internet-facing instances and access any repositories, including private ones
- **Status**: Zero-day vulnerability, patches have been released

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Attackers can crash servers and cause denial of service
- **Status**: Actively exploited, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: Added to KEV catalog due to active exploitation

### Cisco Catalyst SD-WAN Manager Vulnerability
- **Description**: High-severity security flaw in Cisco Catalyst SD-WAN Manager
- **Impact**: Allows attackers to compromise SD-WAN management infrastructure
- **Status**: Actively exploited with no patch currently available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin
- **Impact**: Complete takeover of WordPress websites
- **Status**: Actively exploited
- **CVE ID**: CVE-2026-3300

### UniFi OS Vulnerability Chain
- **Description**: Three chained vulnerabilities in Ubiquiti UniFi OS server
- **Impact**: Remote code execution with root privileges without authentication
- **Status**: Vulnerabilities have been fixed but can be chained together

## Affected Systems and Products

- **Check Point Remote Access VPN**: IKEv1 configurations specifically vulnerable
- **Gogs Git Service**: Internet-facing instances allowing repository access
- **SolarWinds Serv-U**: Multi-protocol file server installations
- **Cisco Catalyst SD-WAN Manager**: Network management infrastructure
- **WordPress Sites**: Using Everest Forms Pro plugin
- **Ubiquiti UniFi OS**: Network management appliances
- **DD-WRT Routers**: Targeted by C0XMO botnet variant
- **Fuel Tank Monitoring Systems**: Internet-exposed gauge systems in US gas stations
- **GitHub Repositories**: Microsoft repositories affected by Miasma worm
- **PyPI Package Repository**: 37 wheels and 19 code packages compromised
- **Instagram Accounts**: 20,225 accounts compromised through Meta AI support system
- **Oxford University CareerConnect**: Third-party career services platform
- **Smart TVs and Consumer Devices**: Used as proxies for web scraping operations

## Attack Vectors and Techniques

- **VPN Authentication Bypass**: Exploiting deprecated IKEv1 protocol implementations
- **Remote Code Execution**: Direct exploitation of Git service vulnerabilities
- **Supply Chain Attacks**: Poisoning package repositories and software dependencies
- **Social Engineering**: Spear-phishing campaigns and vishing attacks
- **Physical Intrusion**: Combined with digital attacks for data theft extortion
- **AI-Powered Social Engineering**: Enhanced phishing using artificial intelligence
- **Botnet Propagation**: Spreading malware through router firmware vulnerabilities
- **Worm-Based Repository Infection**: Self-replicating attacks targeting code repositories
- **IoT Device Exploitation**: Targeting Internet-exposed industrial control systems

## Threat Actor Activities

- **NSO Group**: Conducting spear-phishing campaigns against WhatsApp users, violating court orders
- **Qilin Ransomware Gang**: Linked to exploitation of Check Point VPN zero-day vulnerabilities
- **VerdantBamboo (China-nexus)**: Deploying BSD variant of BRICKSTORM backdoor on Linux appliances
- **UNC3753**: Conducting data theft extortion campaigns using vishing and physical intrusions against US organizations
- **Silent Ransom Group**: Targeting law firms with fake IT support social engineering calls
- **C0XMO Botnet Operators**: Spreading through DD-WRT router vulnerabilities and eliminating competing malware
- **Hades Campaign Actors**: Targeting PyPI with evolved Shai-Hulud supply chain attacks
- **Miasma Worm Operators**: Conducting self-replicating supply chain attacks against GitHub repositories