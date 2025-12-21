# Exploitation Report

Critical exploitation activity is currently affecting enterprise infrastructure across multiple vectors, with threat actors targeting VPN solutions, UEFI firmware, and cloud authentication systems. The most severe incidents include active exploitation of WatchGuard Fireware OS vulnerabilities, zero-day attacks against SonicWall Edge Access devices, and widespread Microsoft 365 phishing campaigns leveraging OAuth device code authentication. Multiple nation-state actors, including China-aligned and Russia-linked groups, are conducting sophisticated espionage operations while ransomware groups continue evolving their encryption techniques for maximum impact.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability affecting SMA1000 devices, chained with previously disclosed critical vulnerability
- **Impact**: Complete device compromise and network infiltration
- **Status**: Active exploitation ongoing, zero-day status indicates no patch available

### UEFI Firmware DMA Attack Vulnerability
- **Description**: Direct Memory Access (DMA) attack vulnerability in UEFI firmware implementations bypassing early-boot memory protections
- **Impact**: Pre-boot attacks enabling persistent system compromise and bootkit installation
- **Status**: Affects multiple major motherboard vendors, exploitation enables early-boot attacks

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity security flaw allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Critical vulnerability with CVSS score of 10.0, patches released

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS VPN components experiencing active exploitation
- **SonicWall SMA1000 Devices**: Edge Access devices targeted in zero-day attack campaigns
- **Major Motherboard Vendors**: ASUS, Gigabyte, MSI, and ASRock motherboards with vulnerable UEFI implementations
- **Microsoft 365**: Accounts targeted through OAuth device code phishing attacks
- **HPE OneView Software**: Infrastructure management platform with maximum-severity RCE vulnerability
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed to authentication bypass attacks
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft operations

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Microsoft 365 credential theft using legitimate device authentication workflows
- **DMA Attacks**: Direct memory access exploitation during early boot phases to bypass security protections
- **Group Policy Abuse**: Windows Group Policy mechanisms used for malware deployment and persistence
- **ATM Jackpotting**: Physical malware deployment on ATM systems using Ploutus malware for cash dispensing
- **Ransomware-as-a-Service**: Multi-layered encryption techniques with enhanced data processing capabilities
- **Phishing-as-a-Service**: Raccoon0365 platform targeting Microsoft 365 environments
- **VPN Exploitation**: Remote code execution through compromised VPN infrastructure

## Threat Actor Activities

- **Infy APT (Prince of Persia)**: Iranian threat group resurging after five-year dormancy with new malware campaigns
- **LongNosedGoblin**: China-aligned APT group targeting Southeast Asian and Japanese government entities using Windows Group Policy for espionage malware deployment
- **Russia-Linked Groups**: Multiple actors conducting Microsoft 365 device code phishing campaigns for account takeovers
- **RansomHouse**: Ransomware-as-a-Service operation upgrading encryption methods with multi-layered data processing
- **Clop Ransomware**: Targeting Internet-exposed Gladinet CentreStack servers for data theft extortion
- **ATM Fraud Networks**: 54 individuals charged in multi-million dollar ATM jackpotting conspiracy using Ploutus malware
- **CountLoader/GachiLoader Operators**: Malware distribution through cracked software sites and YouTube videos