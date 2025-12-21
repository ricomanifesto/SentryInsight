# Exploitation Report

Critical vulnerabilities are currently being actively exploited across multiple vendor platforms, with attackers targeting everything from enterprise firewalls to UEFI firmware and cloud authentication systems. The most severe active exploitation involves CVE-2025-14733, a critical WatchGuard Fireware OS vulnerability with a CVSS score of 9.3 that enables remote code execution on VPN devices. Simultaneously, threat actors are leveraging zero-day vulnerabilities in SonicWall SMA1000 Edge Access devices and exploiting UEFI firmware flaws that enable pre-boot attacks on major motherboard manufacturers. Advanced persistent threat groups from Iran, Russia, and China are conducting sophisticated campaigns using novel attack vectors including Microsoft 365 OAuth phishing, Windows Group Policy abuse, and ATM jackpotting schemes.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical remote code execution vulnerability in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Attackers can execute arbitrary code remotely on affected firewall devices
- **Status**: Actively exploited in real-world attacks; patches have been released by WatchGuard
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: Zero-day vulnerability affecting SonicWall SMA1000 Edge Access devices, chained with previously disclosed critical vulnerabilities
- **Impact**: Complete compromise of edge access infrastructure and potential lateral movement
- **Status**: Actively exploited in the wild; zero-day status indicates no patches available

### UEFI Firmware DMA Attack Vulnerability
- **Description**: UEFI firmware implementation flaw enabling direct memory access (DMA) attacks that bypass early-boot memory protections
- **Impact**: Pre-boot system compromise allowing attackers to persist below the operating system level
- **Status**: Affects multiple major motherboard vendors; exploitation capability confirmed

### FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiCloud SSO functionality
- **Impact**: Complete bypass of single sign-on authentication mechanisms
- **Status**: Over 25,000 devices exposed online with ongoing active attacks

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS with VPN functionality affected by CVE-2025-14733
- **SonicWall SMA1000**: Edge Access devices vulnerable to zero-day exploitation
- **UEFI Firmware**: Motherboards from ASUS, Gigabyte, MSI, and ASRock affected by DMA attack vulnerabilities
- **Fortinet FortiCloud**: Over 25,000 devices with SSO enabled exposed to authentication bypass attacks
- **Microsoft 365**: Widespread targeting through OAuth device code phishing campaigns
- **ATM Systems**: Various ATM models vulnerable to Ploutus malware jackpotting attacks
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Russia-linked actors exploiting Microsoft 365 device code authentication workflows for account takeovers
- **Windows Group Policy Abuse**: China-aligned LongNosedGoblin APT using Group Policy to deploy espionage malware across government networks
- **ATM Jackpotting**: Physical deployment of Ploutus malware to force ATMs to dispense cash through coordinated multi-million dollar schemes
- **Phishing-as-a-Service**: Raccoon0365 platform enabling widespread Microsoft 365 credential harvesting operations
- **UEFI Pre-Boot Attacks**: Early-boot DMA attacks bypassing traditional security controls through firmware exploitation
- **Ransomware Evolution**: RansomHouse upgrading to multi-layered encryption processing for enhanced data destruction capabilities

## Threat Actor Activities

- **Iranian Infy APT (Prince of Persia)**: Resurfaced after five years of silence with new malware campaigns targeting Swedish and other international victims
- **Russia-Linked Groups**: Conducting sophisticated Microsoft 365 OAuth phishing campaigns using device code authentication abuse for account takeovers
- **LongNosedGoblin (China-aligned)**: New APT group targeting government entities across Southeast Asia and Japan using Windows Group Policy for espionage malware deployment
- **RansomHouse**: Ransomware-as-a-Service operation upgrading encryption capabilities with multi-layered data processing techniques
- **Clop Ransomware**: Actively targeting Gladinet CentreStack file servers in coordinated data theft extortion campaigns
- **ATM Fraud Networks**: 54 individuals charged in coordinated ATM jackpotting scheme using Ploutus malware across multiple financial institutions
- **Raccoon0365 Operators**: Nigerian-based phishing-as-a-service developers arrested for creating platforms enabling widespread Microsoft 365 attacks