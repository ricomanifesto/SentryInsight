# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, with threat actors targeting enterprise infrastructure through sophisticated attack chains. Most notably, WatchGuard Firebox firewalls are experiencing active exploitation of a critical remote code execution vulnerability, while SonicWall Edge Access devices face coordinated zero-day attacks. Microsoft 365 environments continue to be heavily targeted through OAuth device code phishing campaigns by multiple threat actors, including suspected Russia-aligned groups. Additionally, over 25,000 FortiCloud SSO-enabled devices remain exposed to authentication bypass attacks, and a newly discovered UEFI vulnerability affects major motherboard manufacturers, enabling pre-boot direct memory access attacks.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical remote code execution vulnerability in WatchGuard Firebox firewalls affecting Fireware OS
- **Impact**: Allows attackers to execute arbitrary code remotely on vulnerable firewall devices
- **Status**: Actively exploited in real-world attacks, patches released by WatchGuard
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day Attacks
- **Description**: Zero-day vulnerability affecting SonicWall SMA1000 Edge Access devices
- **Impact**: Threat actors are chaining this new zero-day with previously disclosed critical vulnerabilities for comprehensive device compromise
- **Status**: Active exploitation detected, part of coordinated attack campaigns

### FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting Fortinet devices with FortiCloud SSO enabled
- **Impact**: Enables remote attackers to bypass authentication mechanisms and gain unauthorized access
- **Status**: Over 25,000 devices exposed online amid ongoing attacks targeting this vulnerability

### UEFI Early-Boot DMA Vulnerability
- **Description**: UEFI firmware vulnerability enabling direct memory access attacks during early boot phases
- **Impact**: Attackers can bypass early-boot memory protections and potentially gain persistent system-level access
- **Status**: Affects motherboards from ASUS, Gigabyte, MSI, and ASRock; enables pre-boot attacks

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity vulnerability in HPE OneView Software allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Critical vulnerability resolved with patches from HPE

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Devices running vulnerable Fireware OS versions
- **SonicWall SMA1000 Devices**: Edge Access devices targeted in zero-day attack campaigns
- **Fortinet Infrastructure**: Over 25,000 devices with FortiCloud SSO functionality exposed online
- **Major Motherboard Manufacturers**: ASUS, Gigabyte, MSI, and ASRock motherboards with vulnerable UEFI implementations
- **Microsoft 365 Environments**: Enterprise and organizational accounts targeted through OAuth phishing
- **HPE OneView Software**: Infrastructure management platform with critical RCE vulnerability
- **Cisco VPN and Email Services**: Multiple products affected in separate threat campaigns
- **Gladinet CentreStack Servers**: Internet-exposed file servers targeted by Clop ransomware

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Multiple threat actors leveraging Microsoft 365 device code authentication workflows to steal credentials and conduct account takeovers
- **Zero-Day Chaining**: SonicWall attackers combining new zero-day exploits with previously disclosed vulnerabilities for enhanced compromise capabilities
- **Direct Memory Access (DMA) Attacks**: UEFI vulnerability exploitation enabling early-boot system compromise
- **Ransomware-as-a-Service Evolution**: RansomHouse upgrading encryption methods with multi-layered data processing techniques
- **ATM Jackpotting**: Large-scale deployment of Ploutus malware for ATM cash theft operations
- **Phishing-as-a-Service**: Raccoon0365 platform enabling Microsoft 365 credential theft operations
- **Malware Distribution**: Cracked software and YouTube videos spreading CountLoader and GachiLoader malware
- **Windows Group Policy Abuse**: LongNosedGoblin threat group using Group Policy for espionage malware deployment

## Threat Actor Activities

- **Russia-Aligned Groups**: Conducting sophisticated Microsoft 365 device code phishing campaigns for account takeovers
- **LongNosedGoblin (China-aligned)**: Previously undocumented threat cluster targeting governmental entities in Southeast Asia and Japan using Windows Group Policy for malware deployment
- **RansomHouse Operators**: Upgrading ransomware encryption capabilities with enhanced multi-layered processing techniques
- **Clop Ransomware Gang**: Targeting Internet-exposed Gladinet CentreStack file servers in data theft extortion campaigns
- **ATM Fraud Network**: 54 individuals charged in multi-million dollar ATM jackpotting scheme using Ploutus malware
- **Raccoon0365 Developers**: Nigerian-based phishing-as-a-service operators arrested for Microsoft 365 credential theft platform
- **North Korean Cyber Groups**: Leading global cryptocurrency theft with $2.02 billion stolen in 2025, demonstrating shift toward targeting larger-value victims
- **Multiple OAuth Threat Actors**: Various groups simultaneously exploiting Microsoft 365 OAuth device code mechanisms for credential compromise