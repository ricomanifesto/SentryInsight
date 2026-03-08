# Exploitation Report

Current threat landscape shows significant exploitation activity across multiple attack vectors, with threat actors leveraging AI-enhanced techniques and targeting critical infrastructure. Most concerning are the active exploitation campaigns targeting iOS devices through the Coruna exploit kit for crypto-theft and cyberespionage, DNS-based phishing attacks abusing .arpa domains and IPv6, and sophisticated social engineering campaigns using ClickFix techniques. State-sponsored actors, particularly from China and Iran, are deploying advanced malware toolkits against telecommunications infrastructure and U.S. networks. Additionally, CISA has added critical vulnerabilities in Hikvision and Rockwell Automation products to the Known Exploited Vulnerabilities catalog, indicating active in-the-wild exploitation.

## Active Exploitation Details

### iOS Security Flaws via Coruna Exploit Kit
- **Description**: Three iOS security vulnerabilities being actively exploited through the Coruna exploit kit in targeted attacks
- **Impact**: Enables cyberespionage operations and cryptocurrency theft from mobile devices
- **Status**: CISA has ordered federal agencies to patch these flaws immediately due to active exploitation

### Hikvision Critical Vulnerability
- **Description**: Critical security flaw in Hikvision products with maximum CVSS score of 9.8
- **Impact**: Allows remote code execution and complete system compromise
- **Status**: Added to CISA KEV catalog, indicating confirmed exploitation in the wild

### Rockwell Automation Critical Vulnerability
- **Description**: Critical industrial control system vulnerability with CVSS 9.8 rating
- **Impact**: Enables unauthorized access to industrial automation systems
- **Status**: Added to CISA KEV catalog due to active exploitation

### Wikipedia JavaScript Worm
- **Description**: Self-propagating JavaScript worm that automatically vandalizes pages and modifies user scripts
- **Impact**: Widespread vandalism across multiple wiki platforms and potential user data compromise
- **Status**: Currently active, affecting Wikimedia Foundation infrastructure

## Affected Systems and Products

- **iOS Devices**: Multiple versions affected by Coruna exploit kit targeting
- **Hikvision Products**: Network cameras and surveillance systems with critical vulnerabilities
- **Rockwell Automation Systems**: Industrial control and automation platforms
- **Firefox Browser**: 22 newly discovered vulnerabilities (14 high-severity, 7 medium-severity)
- **Telecommunications Infrastructure**: Windows and Linux systems at South American telecom providers
- **TriZetto Provider Solutions**: Healthcare IT systems exposing 3.4 million patient records
- **FBI Surveillance Systems**: Wiretap and surveillance warrant management systems
- **Wikipedia/Wikimedia**: Multiple wiki platforms affected by JavaScript worm

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Legitimate Windows utilities used to deploy DonutLoader malware and CastleRAT backdoor
- **InstallFix Variation**: Fake installation guides for legitimate software (Claude Code) to deliver infostealers
- **DNS Abuse**: .arpa domain and IPv6 reverse DNS exploitation to evade security controls
- **AI-Enhanced Malware Development**: Automated malware generation using AI coding tools
- **Multi-Stage Malware Deployment**: VOID#GEIST campaign delivering XWorm, AsyncRAT, and Xeno RAT through batch scripts
- **Search Engine Poisoning**: Fake GitHub repositories promoted through Bing AI search results
- **Phishing-as-a-Service**: Tycoon 2FA platform bypassing multifactor authentication (recently disrupted)

## Threat Actor Activities

- **Velvet Tempest**: Deploying Termite ransomware through ClickFix techniques and CastleRAT backdoor
- **Transparent Tribe (APT36)**: Pakistan-aligned group using AI to mass-produce malware implants targeting India
- **MuddyWater**: Iran-linked group deploying new Dindoor backdoor against U.S. networks including banks and airlines
- **UAT-9244**: China-linked APT targeting South American telecommunications with TernDoor, PeerTime, and BruteEntry malware
- **North Korean IT Worker Scams**: Enhanced operations using AI for face-swapping and improved social engineering
- **Iranian Cyber-Kinetic Operations**: Hacking IP cameras for missile strike planning and targeting physical infrastructure
- **Mexican Government Attackers**: Using AI tools (Claude, ChatGPT) with detailed playbooks to breach government agencies