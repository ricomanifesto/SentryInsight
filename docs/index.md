# Exploitation Report

Current threat landscape shows multiple critical exploitation campaigns targeting enterprise infrastructure and authentication systems. The most severe activity includes active exploitation of a critical WatchGuard Fireware OS VPN vulnerability with a CVSS score of 9.3, zero-day attacks against SonicWall Edge Access devices, and widespread Microsoft 365 OAuth phishing campaigns by Russia-linked threat actors. Additional concerns include a newly discovered UEFI firmware vulnerability affecting major motherboard manufacturers and ongoing password spraying attacks against Cisco and Palo Alto Networks VPN gateways.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability in SonicWall SMA1000 devices being chained with previously disclosed critical flaws
- **Impact**: Complete device compromise and network infiltration
- **Status**: Active exploitation in the wild, zero-day status indicates no patches available

### UEFI Firmware DMA Vulnerability
- **Description**: Direct Memory Access (DMA) vulnerability in UEFI firmware implementations enabling pre-boot attacks
- **Impact**: Bypass of early-boot memory protections and persistent system compromise
- **Status**: Newly discovered vulnerability affecting multiple motherboard vendors

### HPE OneView Critical Flaw
- **Description**: Maximum severity vulnerability in HPE OneView Software enabling unauthenticated access
- **Impact**: Remote code execution without authentication requirements
- **Status**: Patches released by HPE

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS installations with VPN functionality enabled
- **SonicWall SMA1000 Devices**: Edge Access devices exposed to internet-facing attacks
- **Major Motherboard Manufacturers**: ASUS, Gigabyte, MSI, and ASRock motherboards with vulnerable UEFI firmware
- **Microsoft 365 Platforms**: Enterprise and business accounts targeted through OAuth device code phishing
- **Cisco SSL VPN**: VPN gateways under automated password spraying attacks
- **Palo Alto Networks GlobalProtect**: VPN platforms targeted in credential-based attacks
- **Fortinet FortiCloud SSO**: Over 25,000 devices exposed online with SSO enabled
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft
- **HPE OneView Software**: Infrastructure management platforms vulnerable to unauthenticated RCE

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Russia-linked actors exploiting Microsoft 365 device code authentication workflows for account takeovers
- **VPN Password Spraying**: Automated credential-based attacks against Cisco and Palo Alto Networks VPN gateways
- **Zero-Day Chaining**: SonicWall attackers combining new zero-day with previously disclosed vulnerabilities
- **Group Policy Abuse**: LongNosedGoblin APT using Windows Group Policy for malware deployment and persistence
- **Phishing-as-a-Service**: Raccoon0365 platform facilitating Microsoft 365 credential theft operations
- **DMA Exploitation**: Direct memory access attacks bypassing early-boot protections in UEFI firmware
- **Cracked Software Distribution**: CountLoader and GachiLoader malware spread through compromised software sites and YouTube videos

## Threat Actor Activities

- **Russia-Linked Groups**: Conducting sophisticated Microsoft 365 OAuth phishing campaigns targeting enterprise accounts
- **LongNosedGoblin (China-Aligned)**: New APT group targeting government entities in Southeast Asia and Japan using Windows Group Policy for espionage
- **Clop Ransomware**: Targeting Gladinet CentreStack file servers in data theft extortion campaigns
- **North Korean Cybercriminals**: Executed sophisticated cryptocurrency theft operations resulting in $2.02 billion stolen in 2025
- **Prince of Persia (Iran APT)**: Reactivated operations targeting dissidents with advanced operational security and cryptographic C2 communications
- **Nigerian Fraud Syndicate**: Arrested developers behind Raccoon0365 phishing-as-a-service platform targeting Microsoft 365