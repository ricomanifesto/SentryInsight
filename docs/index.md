# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple enterprise platforms, with threat actors focusing heavily on VPN gateways, cloud authentication systems, and network infrastructure. The most concerning activity includes active exploitation of WatchGuard Fireware OS VPN vulnerability CVE-2025-14733, zero-day attacks targeting SonicWall Edge Access devices, and large-scale OAuth phishing campaigns against Microsoft 365 accounts. Nation-state actors, particularly China-aligned and Russia-linked groups, are conducting sophisticated campaigns targeting government entities and critical infrastructure, while North Korean groups continue their record-breaking cryptocurrency theft operations.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Remote code execution allowing attackers to gain unauthorized access to network infrastructure
- **Status**: Actively exploited in real-world attacks; patches have been released
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: Newly discovered vulnerability in SonicWall SMA1000 Edge Access devices
- **Impact**: Threat actors are chaining this zero-day with previously disclosed critical vulnerabilities for enhanced attack capabilities
- **Status**: Zero-day exploitation ongoing; affects SMA1000 devices

### UEFI DMA Attack Vulnerability
- **Description**: UEFI firmware implementation vulnerability enabling direct memory access attacks that bypass early-boot memory protections
- **Impact**: Pre-boot attacks allowing attackers to compromise systems before operating system security measures are active
- **Status**: Affects multiple major motherboard manufacturers; enables sophisticated firmware-level attacks

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity security flaw in HPE OneView Software
- **Impact**: Unauthenticated remote code execution allowing complete system compromise
- **Status**: Critical vulnerability with CVSS score of 10.0; patches available

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS VPN components actively targeted
- **SonicWall SMA1000**: Edge Access devices under zero-day exploitation
- **Microsoft 365**: OAuth authentication systems targeted in widespread phishing campaigns
- **Cisco VPN Gateways**: SSL VPN platforms under credential-based attacks
- **Palo Alto GlobalProtect**: VPN gateways targeted in password spraying campaigns
- **Motherboards**: ASUS, Gigabyte, MSI, and ASRock UEFI implementations vulnerable to DMA attacks
- **HPE OneView Software**: Infrastructure management platform with critical RCE vulnerability
- **Fortinet FortiCloud SSO**: Over 25,000 devices exposed with authentication bypass vulnerabilities

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Microsoft 365 accounts compromised through device code authentication workflows
- **ATM Jackpotting**: Ploutus malware deployment for physical cash extraction from ATMs
- **Password Spraying**: Automated credential attacks against VPN platforms
- **Cracked Software Distribution**: CountLoader and GachiLoader malware spread through compromised software sites
- **Group Policy Abuse**: Windows Group Policy mechanisms used for malware deployment in government networks
- **DMA Attacks**: Direct memory access exploitation during early boot phases
- **Ransomware Extortion**: Clop targeting Gladinet CentreStack servers for data theft

## Threat Actor Activities

- **Russia-Aligned Groups**: Conducting sophisticated phishing campaigns using Microsoft 365 device code authentication for account takeovers
- **LongNosedGoblin (China-Aligned)**: Deploying espionage malware through Windows Group Policy, targeting Southeast Asian and Japanese government entities
- **North Korean Groups**: Record-breaking cryptocurrency theft totaling $2.02 billion in 2025, focusing on larger payouts through patient targeting strategies
- **Clop Ransomware Gang**: Targeting Internet-exposed Gladinet CentreStack file servers in data theft extortion campaigns
- **RaccoonO365 Operators**: Nigerian-based phishing-as-a-service platform targeting Microsoft 365 credentials; three suspects arrested
- **Russian State Actors**: Attributed to destructive cyberattacks against Danish critical infrastructure, specifically water utility systems