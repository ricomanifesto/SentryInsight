# Exploitation Report

Critical exploitation activity is currently targeting a diverse range of systems, from enterprise infrastructure to mobile devices and web applications. CISA has issued urgent patching directives for iOS vulnerabilities being exploited through the Coruna exploit kit in cyberespionage and cryptocurrency theft campaigns. Cisco has confirmed active exploitation of two critical Catalyst SD-WAN Manager vulnerabilities, while WordPress sites face ongoing attacks exploiting a critical User Registration & Membership plugin flaw. The threat landscape has been further complicated by the discovery of 90 zero-day vulnerabilities exploited in attacks throughout 2025, with nearly half targeting enterprise software and appliances. Additionally, sophisticated nation-state actors are leveraging AI tools to enhance their attack capabilities and scale malware production.

## Active Exploitation Details

### iOS Security Vulnerabilities
- **Description**: Three iOS security flaws being exploited through the Coruna exploit kit for targeted attacks
- **Impact**: Enables cyberespionage operations and cryptocurrency theft from mobile devices
- **Status**: CISA has ordered federal agencies to patch these vulnerabilities immediately

### Cisco Catalyst SD-WAN Manager Vulnerabilities
- **Description**: Two critical vulnerabilities in Cisco's SD-WAN management platform confirmed under active exploitation
- **Impact**: Allows attackers to compromise network management infrastructure and potentially gain control over SD-WAN deployments
- **Status**: Cisco has confirmed active exploitation in the wild and released patches

### WordPress User Registration & Membership Plugin Vulnerability
- **Description**: Critical vulnerability in a popular WordPress membership plugin affecting over 60,000 sites
- **Impact**: Attackers can create unauthorized administrator accounts, leading to complete site compromise
- **Status**: Currently being exploited to create admin accounts on vulnerable WordPress installations

### Hikvision and Rockwell Automation Critical Flaws
- **Description**: Two security flaws with CVSS 9.8 scores affecting industrial and surveillance systems
- **Impact**: High-severity vulnerabilities that could allow complete system compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, indicating active exploitation

## Affected Systems and Products

- **iOS Devices**: Apple mobile devices targeted through Coruna exploit kit
- **Cisco Catalyst SD-WAN Manager**: Network management platforms vulnerable to critical exploits
- **WordPress Sites**: Over 60,000 sites using User Registration & Membership plugin at risk
- **Hikvision Products**: Surveillance and security camera systems with critical vulnerabilities
- **Rockwell Automation Systems**: Industrial control and automation equipment
- **TriZetto Provider Solutions**: Healthcare IT systems affected by data breach exposing 3.4 million patient records
- **Telecommunications Infrastructure**: South American telecom providers targeted by Chinese APT groups
- **Wikipedia**: Multiple wikis affected by self-propagating JavaScript worm

## Attack Vectors and Techniques

- **Coruna Exploit Kit**: Sophisticated toolkit targeting iOS vulnerabilities for espionage and crypto theft
- **ClickFix Social Engineering**: Enhanced technique called InstallFix using fake Claude Code installation guides
- **AI-Enhanced Malware Development**: Threat actors using artificial intelligence to mass-produce malware implants
- **Multi-Stage VOID#GEIST Campaign**: Complex malware delivery system using batch scripts to deploy encrypted RATs
- **JavaScript Worm**: Self-propagating malware that vandalized Wikipedia pages and modified user scripts
- **Windows Terminal Abuse**: ClickFix campaigns leveraging Windows Terminal to deploy Lumma Stealer
- **Phishing-as-a-Service**: Tycoon 2FA platform enabling bypass of multifactor authentication defenses

## Threat Actor Activities

- **North Korean APTs**: Using AI tools to enhance IT worker infiltration scams with improved face-swapping and communication capabilities
- **Transparent Tribe (APT36)**: Pakistan-aligned group employing AI-powered coding tools to mass-produce malware targeting India
- **MuddyWater**: Iran-linked hackers deploying new Dindoor backdoor against U.S. networks including banks and airlines
- **UAT-9244**: China-linked APT group targeting South American telecommunications with TernDoor, PeerTime, and BruteEntry malware toolkit
- **Iranian Cyber Operations**: Developing cyber-kinetic warfare doctrine by hacking IP cameras for missile strike planning
- **Mexican Government Attackers**: Threat actors using AI tools including Claude and ChatGPT to compromise government agencies and citizen data