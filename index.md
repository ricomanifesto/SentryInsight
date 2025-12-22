# Exploitation Report

Multiple critical vulnerabilities are under active exploitation, with threat actors targeting enterprise infrastructure and authentication systems. Most concerning are zero-day attacks against SonicWall Edge Access devices and a critical WatchGuard Fireware OS vulnerability (CVE-2025-14733) enabling remote code execution. Additionally, sophisticated phishing campaigns are targeting Microsoft 365 environments using device code authentication workflows, while a new UEFI flaw affects major motherboard manufacturers. The activity spans nation-state actors, ransomware groups, and cybercriminal operations targeting government entities, critical infrastructure, and enterprise systems.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Remote code execution allowing attackers to gain unauthorized access to network infrastructure
- **Status**: Actively exploited in real-world attacks; patches have been released
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability affecting SonicWall SMA1000 Edge Access devices
- **Impact**: Threat actors are chaining this zero-day with previously disclosed critical vulnerabilities for enhanced attack capabilities
- **Status**: Currently being exploited in active attacks; patches not yet available

### UEFI Firmware DMA Vulnerability
- **Description**: Direct Memory Access (DMA) vulnerability in UEFI firmware implementations
- **Impact**: Enables pre-boot attacks that can bypass early-boot memory protections
- **Status**: Vulnerability disclosed; affects multiple major motherboard manufacturers

### Fortinet FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiCloud SSO
- **Impact**: Allows remote attackers to bypass authentication mechanisms
- **Status**: Over 25,000 devices exposed online; ongoing attacks detected

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS installations with VPN components
- **SonicWall SMA1000**: Edge Access devices in enterprise environments
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed online
- **Major Motherboards**: ASUS, Gigabyte, MSI, and ASRock motherboards with vulnerable UEFI firmware
- **Microsoft 365**: Enterprise accounts targeted through OAuth device code authentication
- **ATM Systems**: Financial institutions using vulnerable ATM infrastructure

## Attack Vectors and Techniques

- **Device Code Phishing**: Russia-linked actors exploiting Microsoft 365 OAuth device code authentication workflows for account takeovers
- **ATM Jackpotting**: Large-scale deployment of Ploutus malware targeting ATM networks for cash extraction
- **UEFI Pre-boot Attacks**: Direct memory access attacks bypassing early-boot security protections
- **Group Policy Abuse**: China-aligned threat actors using Windows Group Policy for malware deployment
- **Ransomware Data Theft**: Clop ransomware targeting Gladinet CentreStack file servers for data exfiltration
- **Malware Distribution**: CountLoader and GachiLoader spread through cracked software and YouTube videos

## Threat Actor Activities

- **Iranian Infy APT**: Resurged after five years of silence with new malware campaigns targeting victims
- **Russia-linked Groups**: Conducting sophisticated Microsoft 365 device code phishing campaigns for credential theft
- **LongNosedGoblin**: China-aligned APT group targeting governmental entities in Southeast Asia and Japan using Windows Group Policy for espionage malware deployment
- **RansomHouse**: Upgraded encryption techniques with multi-layered data processing capabilities
- **Clop Ransomware**: Active data theft extortion campaign targeting Internet-exposed file servers
- **RaccoonO365 Operators**: Nigerian cybercriminals arrested for developing phishing-as-a-service platform targeting Microsoft 365