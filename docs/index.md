# Exploitation Report

Current threat activity reveals multiple critical vulnerabilities under active exploitation, with supply chain attacks emerging as a dominant attack vector. Most concerning are the ongoing exploits of Weaver E-cology enterprise software (CVE-2026-22679) and MetInfo CMS (CVE-2026-29014), both enabling remote code execution. Supply chain compromises have affected major software platforms including DAEMON Tools and gaming platforms, while sophisticated malware campaigns target developers and enterprise systems through trojanized installers and malicious packages.

## Active Exploitation Details

### Weaver E-cology Remote Code Execution
- **Description**: Critical vulnerability in Weaver (Fanwei) E-cology enterprise office automation platform allowing remote code execution via debug API
- **Impact**: Attackers can execute arbitrary commands and gain full system control on affected enterprise systems
- **Status**: Actively exploited in the wild since mid-March 2026, with attackers running discovery commands
- **CVE ID**: CVE-2026-22679

### MetInfo CMS Remote Code Execution
- **Description**: Critical security flaw in MetInfo open-source content management system enabling remote code execution
- **Impact**: Complete system compromise allowing attackers to execute arbitrary code on web servers
- **Status**: Under active exploitation by threat actors targeting CMS installations
- **CVE ID**: CVE-2026-29014

### Apache HTTP/2 Server Vulnerability
- **Description**: Severe vulnerability in Apache HTTP Server that could potentially lead to remote code execution and denial of service attacks
- **Impact**: Remote code execution capabilities and service disruption on web servers
- **Status**: Security updates released by Apache Software Foundation
- **CVE ID**: CVE-2026-23918

### DAEMON Tools Supply Chain Compromise
- **Description**: Trojanized installers for DAEMON Tools software delivering backdoor malware through official distribution channels
- **Impact**: Backdoor installation on thousands of systems downloading from legitimate sources
- **Status**: Active since April 8, affecting official website downloads

## Affected Systems and Products

- **Weaver E-cology**: Enterprise office automation and collaboration platforms
- **MetInfo CMS**: Open-source content management systems and web applications
- **Apache HTTP Server**: Web servers running vulnerable HTTP/2 implementations
- **DAEMON Tools**: Software installation packages from official distribution channels
- **Gaming Platforms**: Video game platforms compromised in supply chain attacks
- **PyTorch Lightning**: Python machine learning packages on PyPI repository
- **Microsoft Edge**: Enterprise environments with stored credentials in process memory
- **Android and Windows Systems**: Devices targeted by BirdCall malware through compromised gaming platforms
- **Linux Developer Systems**: Software development environments targeted by Quasar Linux malware

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of legitimate software distribution channels and official installers
- **Trojanized Package Distribution**: Malicious packages published on official repositories like PyPI
- **Remote Code Execution via Debug APIs**: Exploitation of debugging interfaces in enterprise applications
- **Phishing with RMM Tools**: Use of legitimate remote monitoring tools (SimpleHelp, ScreenConnect) for persistence
- **Memory-Based Credential Theft**: Extraction of stored passwords from application process memory
- **OAuth Token Persistence**: Exploitation of persistent OAuth tokens with no expiration dates
- **TETRA Communication System Interference**: Unauthorized access to critical infrastructure communication systems
- **Microsoft Phone Link Hijacking**: Abuse of legitimate connectivity features to steal SMS and OTPs

## Threat Actor Activities

- **China-Linked UAT-8302**: Advanced persistent threat group targeting government entities in South America and other regions using shared APT malware infrastructure
- **ScarCruft/APT37**: North Korean state-sponsored group conducting supply chain attacks through compromised gaming platforms to distribute BirdCall malware
- **Quasar Linux Operators**: Targeting software developers with sophisticated Linux implants featuring rootkit, backdoor, and credential-stealing capabilities
- **ShinyHunters**: Extortion gang responsible for Vimeo breach affecting 119,000 individuals and other high-profile data thefts
- **Karakurt Ransomware Group**: Russian ransomware operation with "cold case" negotiators conducting extortion campaigns
- **CloudZ RAT Operators**: Deploying advanced remote access tools with new plugins to hijack Microsoft Phone Link connections