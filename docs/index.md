# Exploitation Report

Critical zero-day vulnerabilities are actively being exploited across multiple enterprise infrastructure components, with threat actors targeting network security appliances and enterprise software systems. The most concerning activities include active exploitation of a critical WatchGuard Fireware OS VPN vulnerability (CVE-2025-14733), zero-day attacks against Cisco AsyncOS email security appliances, ongoing exploitation of SonicWall Edge Access devices, and CISA's addition of an ASUS Live Update flaw to the Known Exploited Vulnerabilities catalog. Additionally, ransomware groups are targeting exposed file servers while state-sponsored actors continue sophisticated espionage campaigns using legitimate Windows features for persistence.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Enables remote code execution with high severity impact
- **Status**: Actively exploited in real-world attacks, patches available from WatchGuard
- **CVE ID**: CVE-2025-14733

### Cisco AsyncOS Email Security Zero-Day
- **Description**: Maximum-severity zero-day vulnerability in Cisco AsyncOS software for email security appliances
- **Impact**: Allows unauthorized access and potential system compromise
- **Status**: Currently being exploited by China-nexus APT group UAT-9686, no patch available yet

### SonicWall Edge Access Zero-Day Chain
- **Description**: New zero-day flaw being chained with a previously disclosed critical vulnerability in SMA1000 devices
- **Impact**: Enables comprehensive compromise of edge access infrastructure
- **Status**: Active exploitation by threat actors targeting SonicWall devices

### ASUS Live Update Critical Flaw
- **Description**: Critical vulnerability in ASUS Live Update software
- **Impact**: Allows unauthorized system access and potential code execution
- **Status**: Added to CISA KEV catalog due to evidence of active exploitation

### HPE OneView Maximum Severity Vulnerability
- **Description**: Critical unauthenticated remote code execution flaw in HPE OneView Software
- **Impact**: Complete system compromise without authentication required
- **Status**: Recently patched, CVSS score of 10.0

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS installations with VPN functionality
- **Cisco Email Security Appliances**: AsyncOS software deployments
- **SonicWall SMA1000 Devices**: Edge access and VPN gateway systems
- **ASUS Systems**: Devices utilizing ASUS Live Update software
- **HPE OneView Software**: Enterprise infrastructure management platforms
- **UEFI Motherboards**: ASRock, ASUS, GIGABYTE, and MSI motherboard models vulnerable to early-boot DMA attacks
- **Gladinet CentreStack Servers**: Internet-exposed file servers targeted by ransomware
- **VPN Gateways**: Palo Alto Networks GlobalProtect and Cisco SSL VPN platforms

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of unpatched vulnerabilities in network appliances and enterprise software
- **Zero-Day Chaining**: Combining multiple vulnerabilities for enhanced system access
- **Password Spraying**: Automated credential attacks against VPN platforms
- **Phishing Campaigns**: QR code-based attacks distributing Android malware
- **Group Policy Abuse**: China-aligned groups using legitimate Windows features for persistence
- **Early-Boot DMA Attacks**: Hardware-level exploitation targeting UEFI implementations
- **Ransomware Deployment**: Targeting exposed file servers for data theft and extortion

## Threat Actor Activities

- **UAT-9686 (China-nexus APT)**: Actively exploiting Cisco AsyncOS zero-day in targeted attacks
- **LongNosedGoblin (China-aligned)**: Using Windows Group Policy for espionage malware deployment targeting Southeast Asian and Japanese government entities
- **Kimsuky (North Korean)**: Distributing DocSwap Android malware via QR phishing campaigns mimicking delivery applications
- **Clop Ransomware Group**: Conducting data theft extortion campaigns against Gladinet CentreStack file servers
- **RaccoonO365 Developers**: Nigerian threat actors developing phishing tools targeting Microsoft 365 environments
- **Prince of Persia (Iranian APT)**: Conducting surveillance operations against dissidents with advanced operational security
- **North Korean Cryptocurrency Thieves**: Stealing $2.02 billion in cryptocurrency throughout 2025, leading global crypto theft activities