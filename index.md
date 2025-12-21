# Exploitation Report

Current threat activity shows a concerning surge in sophisticated exploitation campaigns targeting enterprise infrastructure and Microsoft 365 environments. Most critical are the active zero-day attacks against SonicWall Edge Access devices, where threat actors are chaining new zero-day vulnerabilities with previously disclosed flaws. Additionally, WatchGuard Firebox firewalls are under active attack exploiting CVE-2025-14733, a critical remote code execution vulnerability. Multiple threat actors are conducting widespread OAuth phishing campaigns against Microsoft 365 accounts, while FortiCloud SSO devices remain exposed to remote attacks through authentication bypass vulnerabilities. The emergence of new APT groups like LongNosedGoblin demonstrates evolving espionage tactics using Windows Group Policy for malware deployment.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS that enables remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected firewall systems
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day Vulnerabilities
- **Description**: New zero-day flaw affecting SMA1000 devices being chained with previously disclosed critical vulnerabilities
- **Impact**: Complete compromise of edge access infrastructure enabling network infiltration
- **Status**: Active zero-day attacks ongoing, no patches mentioned

### FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting Fortinet devices with FortiCloud SSO enabled
- **Impact**: Remote attackers can bypass authentication mechanisms to gain unauthorized access
- **Status**: Over 25,000 devices exposed online, ongoing attacks detected

### UEFI Firmware DMA Attacks
- **Description**: Direct Memory Access vulnerability in UEFI firmware implementations that bypasses early-boot memory protections
- **Impact**: Pre-boot attacks enabling deep system compromise and persistence
- **Status**: Newly disclosed vulnerability affecting multiple motherboard vendors

### HPE OneView Critical Flaw
- **Description**: Maximum-severity vulnerability in HPE OneView Software allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Recently patched critical vulnerability with CVSS 10.0 rating

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS installations vulnerable to remote code execution
- **SonicWall SMA1000 Devices**: Edge access appliances under active zero-day attack
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed online
- **Motherboard Hardware**: ASUS, Gigabyte, MSI, and ASRock motherboards with vulnerable UEFI firmware
- **Microsoft 365 Environments**: Widespread targeting through OAuth device code phishing campaigns
- **HPE OneView Software**: Infrastructure management software with critical RCE vulnerability
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft
- **Cisco VPN Services**: Multiple threat campaigns targeting VPN infrastructure
- **ATM Systems**: Ploutus malware deployment in jackpotting schemes

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Exploitation of Microsoft 365 OAuth authentication workflows to steal credentials
- **Zero-Day Chaining**: Combining new zero-day vulnerabilities with known critical flaws for enhanced impact
- **DMA Attacks**: Direct memory access exploitation during early boot phases to bypass security protections
- **Windows Group Policy Abuse**: Leveraging legitimate Group Policy mechanisms for espionage malware deployment
- **ATM Jackpotting**: Physical and logical attacks using Ploutus malware to dispense cash
- **Phishing-as-a-Service**: Raccoon0365 platform facilitating large-scale Microsoft 365 credential theft
- **Ransomware Data Theft**: Multi-layered encryption techniques combined with data exfiltration for extortion
- **Supply Chain Targeting**: Compromising software distribution sites to spread CountLoader and GachiLoader malware

## Threat Actor Activities

- **LongNosedGoblin (China-aligned APT)**: Conducting espionage operations against Southeast Asian and Japanese government entities using Windows Group Policy for malware deployment
- **Russia-linked Groups**: Executing sophisticated Microsoft 365 device code phishing campaigns for account takeovers and conducting destructive cyberattacks on Danish water utility infrastructure
- **RansomHouse Group**: Upgrading encryption techniques with multi-layered data processing methods to enhance ransomware effectiveness
- **Clop Ransomware Gang**: Targeting Internet-exposed Gladinet CentreStack file servers in data theft extortion campaigns
- **North Korean Cybercriminals**: Stealing $2.02 billion in cryptocurrency through sophisticated attacks, accounting for majority of global crypto theft in 2025
- **ATM Fraud Network**: 54 individuals charged in multi-million dollar ATM jackpotting scheme using coordinated Ploutus malware deployment
- **Raccoon0365 Operators**: Three individuals arrested in Nigeria for developing and operating phishing-as-a-service platform targeting Microsoft 365 environments