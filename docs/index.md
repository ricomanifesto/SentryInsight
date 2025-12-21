# Exploitation Report

Current threat landscape shows critical active exploitation targeting enterprise infrastructure and authentication systems. WatchGuard Fireware OS devices are under active attack through CVE-2025-14733, a critical vulnerability with a CVSS score of 9.3. SonicWall Edge Access devices face zero-day exploitation where threat actors are chaining new vulnerabilities with previously disclosed critical flaws. Multiple threat actors are conducting sophisticated phishing campaigns targeting Microsoft 365 accounts using OAuth device code authentication mechanisms. The Clop ransomware group has expanded operations to target Gladinet CentreStack file servers, while new China-aligned APT group LongNosedGoblin is deploying espionage malware through Windows Group Policy mechanisms against Southeast Asian governments.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS that enables remote code execution through VPN services
- **Impact**: Attackers can achieve remote code execution and compromise network security infrastructure
- **Status**: Actively exploited in real-world attacks; patches available from WatchGuard
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability affecting SMA1000 devices being chained with previously disclosed critical vulnerabilities
- **Impact**: Complete compromise of edge access devices and potential network infiltration
- **Status**: Active exploitation ongoing; zero-day status indicates no patch currently available

### Microsoft 365 OAuth Device Code Authentication Bypass
- **Description**: Multiple threat actors exploiting OAuth device code authentication workflows to steal Microsoft 365 credentials
- **Impact**: Complete account takeover, access to corporate email and cloud resources
- **Status**: Active campaigns by Russia-linked groups and multiple other threat actors

### UEFI DMA Attack Vulnerability
- **Description**: UEFI firmware implementation flaw enabling direct memory access attacks that bypass early-boot memory protections
- **Impact**: Pre-boot system compromise, potential for persistent malware installation below operating system level
- **Status**: Affects multiple major motherboard vendors; patches being developed

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS with VPN functionality actively targeted
- **SonicWall SMA1000 Devices**: Edge Access devices under zero-day exploitation
- **Microsoft 365 Accounts**: Enterprise and individual accounts targeted through OAuth phishing
- **Motherboards**: ASUS, ASRock, Gigabyte, and MSI motherboards vulnerable to UEFI DMA attacks
- **Gladinet CentreStack Servers**: Internet-exposed file servers targeted by Clop ransomware
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed to remote attacks
- **HPE OneView Software**: Critical vulnerability with CVSS 10.0 rating allowing unauthenticated RCE

## Attack Vectors and Techniques

- **VPN Exploitation**: Direct targeting of WatchGuard VPN services for initial access
- **Zero-Day Chaining**: Combining new zero-day exploits with previously disclosed vulnerabilities for maximum impact
- **OAuth Device Code Phishing**: Sophisticated phishing campaigns leveraging Microsoft 365 device code authentication flows
- **DMA Attacks**: Pre-boot direct memory access attacks bypassing traditional security controls
- **Group Policy Abuse**: China-aligned actors using Windows Group Policy for malware deployment
- **Ransomware Data Theft**: Clop group targeting file servers for data exfiltration and extortion
- **ATM Jackpotting**: Physical and malware-based attacks using Ploutus malware for cash theft

## Threat Actor Activities

- **Russia-Linked Groups**: Conducting Microsoft 365 account takeover campaigns using device code phishing techniques
- **LongNosedGoblin (China-aligned)**: Targeting Southeast Asian and Japanese government entities with espionage malware deployed via Group Policy
- **Iranian Infy APT**: Resurfaced after years of silence with new malware activity targeting unknown victims
- **Clop Ransomware Group**: Expanded operations to target Gladinet CentreStack servers for data theft extortion
- **RaccoonO365 Operators**: Nigerian-based phishing-as-a-service platform developers arrested for Microsoft 365 attacks
- **ATM Jackpotting Syndicate**: 54 individuals charged in multi-million dollar ATM fraud scheme using Ploutus malware
- **CountLoader/GachiLoader Distributors**: Campaign using cracked software and YouTube videos to distribute modular malware loaders