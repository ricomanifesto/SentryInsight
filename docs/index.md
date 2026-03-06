# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple fronts, with threat actors leveraging AI technologies to enhance traditional attack methods while actively exploiting critical vulnerabilities in enterprise infrastructure. CISA has ordered federal agencies to patch three iOS security flaws being exploited in cyberespionage and crypto-theft attacks using the Coruna exploit kit. Critical vulnerabilities in Cisco Catalyst SD-WAN Manager systems are under active exploitation, while nation-state actors from North Korea, China, Pakistan, and Iran are deploying sophisticated campaigns targeting telecommunications infrastructure, financial institutions, and government agencies. Google's Threat Intelligence Group tracked 90 zero-day vulnerabilities that were actively exploited throughout 2025, with nearly half targeting enterprise software and appliances.

## Active Exploitation Details

### iOS Security Flaws in Coruna Exploit Kit Attacks
- **Description**: Three iOS security vulnerabilities being exploited through the Coruna exploit kit in targeted attacks
- **Impact**: Enables cyberespionage activities and cryptocurrency theft operations
- **Status**: CISA has mandated federal agencies to apply patches immediately

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two critical vulnerabilities in Cisco Catalyst SD-WAN Manager (formerly SD-WAN vManage) systems
- **Impact**: Allows attackers to compromise network management infrastructure
- **Status**: Active exploitation confirmed by Cisco in the wild

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in the User Registration & Membership plugin affecting over 60,000 WordPress sites
- **Impact**: Enables attackers to create administrative accounts and gain full site control
- **Status**: Currently being exploited to compromise WordPress installations

### Hikvision and Rockwell Automation Critical Flaws
- **Description**: Two security flaws with CVSS 9.8 severity ratings affecting industrial and surveillance systems
- **Impact**: Complete system compromise potential due to maximum severity rating
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog indicating active exploitation

## Affected Systems and Products

- **Apple iOS Devices**: Multiple versions affected by three security flaws exploited via Coruna kit
- **Cisco Catalyst SD-WAN Manager**: Network management systems under active attack
- **WordPress Sites**: Over 60,000 installations using vulnerable User Registration & Membership plugin
- **Hikvision Products**: Surveillance and security camera systems with critical vulnerabilities
- **Rockwell Automation Systems**: Industrial control and automation infrastructure
- **Telecommunications Infrastructure**: South American telecom providers targeted by Chinese APT groups
- **U.S. Financial Institutions**: Banks and financial services targeted by Iranian MuddyWater group
- **Wikipedia Platform**: Multiple wikis affected by self-propagating JavaScript worm
- **FBI Surveillance Systems**: Wiretap and surveillance warrant management systems breached

## Attack Vectors and Techniques

- **AI-Enhanced Social Engineering**: North Korean APTs using AI for face swapping and automated communication in IT worker scams
- **ClickFix Social Engineering**: InstallFix variation convincing users to run malicious commands for fake Claude Code installations
- **Multi-Stage Malware Deployment**: VOID#GEIST campaign using batch scripts to deliver encrypted RAT payloads including XWorm, AsyncRAT, and Xeno RAT
- **JavaScript Worm Propagation**: Self-replicating worm vandalizing Wikipedia pages and modifying user scripts
- **Phishing-as-a-Service**: Tycoon 2FA platform bypassing multi-factor authentication before law enforcement takedown
- **Search Engine Poisoning**: Fake GitHub repositories promoted through Microsoft Bing AI to distribute info-stealing malware
- **Network Infrastructure Targeting**: Custom malware toolkits including TernDoor, PeerTime, and BruteEntry for telecom attacks

## Threat Actor Activities

- **North Korean APTs**: Leveraging AI technologies to enhance long-running IT worker infiltration scams with improved face swapping and automated communications
- **Transparent Tribe (APT36)**: Pakistan-aligned group using AI-powered coding tools for mass-producing malware implants targeting Indian organizations
- **Iranian MuddyWater Group**: Deploying new Dindoor backdoor to establish persistence in U.S. corporate networks including banks and airlines
- **Chinese UAT-9244 Group**: Targeting South American telecommunications infrastructure since 2024 with sophisticated malware toolkit affecting Windows, Linux, and network devices
- **Iranian Cyber Operations**: Developing cyber-kinetic warfare capabilities, hacking IP cameras for missile strike planning and targeting physical infrastructure
- **Mexico Government Attackers**: Using Anthropic's Claude and OpenAI's ChatGPT with detailed playbooks to breach government agencies and access citizen data
- **Cryptocurrency Theft Operations**: Coordinated attacks resulting in $46 million theft from U.S. Marshals Service and $100 million fraud ring targeting U.S. businesses through BEC and romance scams