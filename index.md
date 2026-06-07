# Exploitation Report

Critical exploitation activity is occurring across multiple attack vectors, with threat actors actively targeting enterprise infrastructure and consumer applications. The most severe incidents include active exploitation of a zero-day vulnerability in Cisco Catalyst SD-WAN Manager enabling root privilege escalation, a critical WordPress plugin flaw allowing complete site compromise, and widespread botnet campaigns targeting DD-WRT router firmware. Additional concerning activities include supply chain attacks compromising NPM packages and Microsoft GitHub repositories, sophisticated social engineering campaigns against law firms, and the compromise of consumer browsers to deliver cryptocurrency miners. These attacks demonstrate threat actors' continued focus on high-value targets and critical infrastructure components.

## Active Exploitation Details

### Cisco Catalyst SD-WAN Manager Zero-Day
- **Description**: High-severity zero-day vulnerability in Cisco Catalyst SD-WAN Manager
- **Impact**: Allows attackers to gain root privilege escalation on affected systems
- **Status**: Currently being exploited in the wild with no patch available
- **CVE ID**: CVE-2026-20245

### Everest Forms Pro WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Everest Forms Pro WordPress plugin affecting approximately 4,000 active installations
- **Impact**: Enables complete site takeover and arbitrary code execution
- **Status**: Actively exploited by threat actors to compromise WordPress websites
- **CVE ID**: CVE-2026-3300

### SolarWinds Serv-U Denial of Service Vulnerability
- **Description**: High-severity security flaw in SolarWinds Serv-U multi-protocol file server software
- **Impact**: Allows attackers to crash servers and disrupt service availability
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

### DD-WRT Router Firmware Vulnerability
- **Description**: Security flaw in DD-WRT router firmware being exploited by the C0XMO botnet variant
- **Impact**: Enables botnet recruitment and lateral movement to devices with various CPU architectures
- **Status**: Actively exploited to spread malware and eliminate rival botnet infections

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Manager**: Enterprise network management systems vulnerable to privilege escalation
- **WordPress Sites**: Websites using Everest Forms Pro plugin (~4,000 active installations)
- **SolarWinds Serv-U**: Multi-protocol file server deployments across enterprise environments
- **DD-WRT Routers**: Consumer and small business routers running DD-WRT firmware
- **NPM Ecosystem**: JavaScript developers and applications using compromised packages
- **Microsoft GitHub**: 73 Microsoft repositories affected by Miasma worm campaign
- **Gas Station Infrastructure**: Over 900 automatic tank gauge systems exposed online
- **Hola Browser**: Windows users of the compromised browser application
- **Microsoft 365**: Enterprise environments targeted by Chinese APT group UNC5221

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched Cisco SD-WAN vulnerability for privilege escalation
- **Web Application Attacks**: Exploitation of WordPress plugin vulnerabilities for site compromise
- **Social Engineering**: Silent Ransom Group using fake IT support calls to target law firms
- **Supply Chain Compromise**: IronWorm and Miasma worm variants targeting NPM package repositories
- **Botnet Operations**: C0XMO variant spreading through router vulnerabilities and eliminating competitors
- **Browser Compromise**: Hola Browser supply chain attack delivering cryptocurrency miners
- **Malicious Web Shells**: OP-512 threat cluster deploying custom frameworks on IIS servers
- **Credential Harvesting**: Suspicious polyfill scripts collecting login credentials on legitimate websites

## Threat Actor Activities

- **Silent Ransom Group**: Conducting social engineering campaigns against U.S. law firms using fake IT support calls, achieving data theft within hours
- **C0XMO Botnet Operators**: Deploying Gafgyt botnet variant to compromise DD-WRT routers and expand to multi-architecture devices
- **UNC5221 (Chinese APT)**: Maintaining persistent access to Microsoft 365 environments using Brickstorm backdoor and custom malware (Plenet and AgentPSD)
- **OP-512 Threat Cluster**: Targeting Microsoft IIS servers with sophisticated web shell frameworks for persistent access
- **PCPJack**: Hijacking cloud infrastructure from AWS, Google Cloud, and Azure to establish covert SMTP relay networks
- **Supply Chain Attackers**: Coordinated campaigns using IronWorm and Miasma variants to compromise NPM packages and propagate across development environments
- **Miasma Operators**: Successfully infiltrating 73 Microsoft GitHub repositories in major supply chain attack campaign