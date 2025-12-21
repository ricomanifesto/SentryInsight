# Exploitation Report

Current exploitation activities reveal a concerning landscape of active attacks targeting critical infrastructure and enterprise systems. Notable incidents include the active exploitation of WatchGuard Fireware OS vulnerability enabling remote code execution, zero-day attacks against SonicWall Edge Access devices, and sophisticated phishing campaigns targeting Microsoft 365 accounts through OAuth device code authentication. State-sponsored threat actors, including Iranian APT groups and China-aligned clusters, are conducting espionage operations while ransomware groups continue evolving their encryption techniques. Critical vulnerabilities in UEFI firmware and HPE OneView systems present additional attack surfaces requiring immediate attention.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Actively exploited in real-world attacks; patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day Vulnerability
- **Description**: New zero-day flaw affecting SMA1000 Edge Access devices
- **Impact**: Threat actors chaining this with previously disclosed critical vulnerabilities for system compromise
- **Status**: Actively exploited; zero-day status indicates no patch currently available

### HPE OneView Remote Code Execution Vulnerability
- **Description**: Maximum-severity security flaw in HPE OneView Software
- **Impact**: Unauthenticated remote code execution with complete system control
- **Status**: Recently patched; maximum CVSS score of 10.0 indicates critical severity

### UEFI Firmware DMA Vulnerability
- **Description**: UEFI firmware implementation vulnerability enabling direct memory access attacks
- **Impact**: Pre-boot attacks that bypass early-boot memory protections
- **Status**: Affects multiple major motherboard vendors; patches required from individual manufacturers

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS versions with VPN functionality
- **SonicWall SMA1000 Devices**: Edge Access devices with chained vulnerability exploitation
- **HPE OneView Software**: Infrastructure management platform with unauthenticated RCE exposure
- **UEFI Motherboards**: ASRock, ASUS, GIGABYTE, and MSI motherboard models vulnerable to DMA attacks
- **Microsoft 365 Accounts**: Targeted through OAuth device code phishing campaigns
- **Fortinet FortiCloud SSO**: Over 25,000 devices exposed online with authentication bypass vulnerability
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft
- **University Systems**: Sydney University coding repositories compromised with student/staff data exposure

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Microsoft 365 credential theft through device code authentication workflows
- **ATM Jackpotting**: Ploutus malware deployment for cash dispensing attacks
- **DMA Attacks**: Direct memory access exploitation bypassing early-boot protections
- **Group Policy Abuse**: Windows Group Policy manipulation for espionage malware deployment
- **Malware Distribution**: Cracked software and YouTube videos spreading CountLoader and GachiLoader
- **Ransomware Evolution**: RansomHouse upgrading to multi-layered encryption processing
- **Infrastructure Targeting**: Cyberattacks against critical water utility systems

## Threat Actor Activities

- **Iranian Infy APT**: Resurfaced after five years of silence with new malware activity
- **Russia-Linked Groups**: Microsoft 365 device code phishing for account takeovers and infrastructure attacks against Denmark
- **LongNosedGoblin**: China-aligned APT targeting Southeast Asian and Japanese government entities
- **RaccoonO365 Developers**: Nigerian arrests related to Microsoft 365 phishing-as-a-service platform
- **Clop Ransomware Gang**: Data theft extortion campaigns targeting CentreStack file servers
- **RansomHouse Group**: Ransomware-as-a-service operations with upgraded encryption capabilities
- **ATM Fraud Networks**: 54 individuals charged in multi-million dollar jackpotting scheme
- **North Korean Groups**: Sophisticated targeting of "bigger fish" for larger cryptocurrency payouts