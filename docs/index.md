# Exploitation Report

Critical active exploitation activity continues to target enterprise infrastructure with several high-severity vulnerabilities being exploited in the wild. WatchGuard Fireware OS devices are under active attack through CVE-2025-14733, a critical remote code execution vulnerability with a CVSS score of 9.3. SonicWall Edge Access devices are being compromised through zero-day attacks that chain new vulnerabilities with previously disclosed flaws. Multiple threat actors are conducting sophisticated phishing campaigns targeting Microsoft 365 accounts using OAuth device code authentication workflows, while ransomware operations have evolved with more complex encryption methods. State-sponsored actors from Iran, Russia, and China have resurged with new malware variants and espionage campaigns targeting government entities and critical infrastructure.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in Fireware OS that allows remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected firewall devices
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability targeting SMA1000 devices, chained with previously disclosed critical vulnerabilities
- **Impact**: Complete compromise of edge access devices
- **Status**: Active exploitation ongoing, zero-day status indicates no patch currently available

### UEFI Firmware DMA Vulnerability
- **Description**: Direct memory access vulnerability in UEFI firmware implementation affecting multiple motherboard manufacturers
- **Impact**: Pre-boot attacks that can bypass early-boot memory protections
- **Status**: Vulnerability disclosed, affects ASUS, Gigabyte, MSI, and ASRock motherboards

### HPE OneView Critical Flaw
- **Description**: Maximum-severity security flaw allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Patches available, CVSS score of 10.0

## Affected Systems and Products

- **WatchGuard Fireware OS**: VPN functionality in firewall devices
- **SonicWall SMA1000**: Edge access devices vulnerable to chained zero-day attacks
- **ASUS, Gigabyte, MSI, ASRock Motherboards**: UEFI firmware implementations susceptible to DMA attacks
- **HPE OneView Software**: Infrastructure management platform with maximum-severity RCE flaw
- **Microsoft 365**: Accounts targeted through OAuth device code phishing campaigns
- **FortiCloud SSO Devices**: Over 25,000 devices exposed online with authentication bypass vulnerability
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft
- **Danish Water Utilities**: Critical infrastructure targeted in Russian state-sponsored attacks

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Multiple threat actors leveraging Microsoft 365 device code authentication workflows for account takeovers
- **Ransomware-as-a-Service Evolution**: RansomHouse upgraded to multi-layered encryption processing from simple linear techniques
- **ATM Jackpotting**: Ploutus malware deployed in large-scale conspiracy affecting multiple financial institutions
- **Windows Group Policy Abuse**: LongNosedGoblin APT using legitimate Windows functionality for malware deployment
- **Cracked Software Distribution**: CountLoader and GachiLoader malware spread through compromised software and YouTube videos
- **Direct Memory Access Attacks**: Pre-boot DMA attacks targeting UEFI firmware implementations
- **Supply Chain Targeting**: Attacks on file server platforms to compromise multiple downstream victims

## Threat Actor Activities

- **Iranian Infy APT (Prince of Persia)**: Resumed malware operations after five-year dormancy period targeting unspecified victims
- **RansomHouse**: Upgraded ransomware-as-a-service platform with enhanced multi-layered encryption capabilities
- **Russia-Aligned Groups**: Conducting OAuth phishing campaigns against Microsoft 365 accounts and destructive attacks on Danish critical infrastructure
- **LongNosedGoblin**: China-aligned APT group targeting Southeast Asian and Japanese government entities using Windows Group Policy for espionage malware deployment
- **Clop Ransomware**: Targeting Internet-exposed Gladinet CentreStack file servers in new data theft extortion campaigns
- **ATM Jackpotting Consortium**: 54 individuals indicted for multi-million dollar scheme using Ploutus malware
- **RaccoonO365 Operators**: Nigerian-based phishing-as-a-service targeting Microsoft 365 through sophisticated social engineering