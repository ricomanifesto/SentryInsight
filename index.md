# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by several high-severity flaws being actively exploited in the wild. WatchGuard Fireware OS VPN systems are under active attack through CVE-2025-14733, a critical remote code execution vulnerability with a CVSS score of 9.3. Meanwhile, SonicWall's SMA1000 Edge Access devices face ongoing zero-day attacks where threat actors are chaining a newly discovered vulnerability with previously disclosed flaws. Cisco AsyncOS Email Security Appliances are being targeted through an unpatched maximum-severity zero-day actively exploited by Chinese APT group UAT-9686. Additionally, CISA has flagged CVE-2025-5387, a critical ASUS Live Update vulnerability, for active exploitation and added it to their Known Exploited Vulnerabilities catalog. Fortinet systems are also experiencing active attacks targeting critical flaws, while UEFI vulnerabilities affect multiple motherboard vendors including ASRock, ASUS, GIGABYTE, and MSI.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical remote code execution vulnerability in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Allows attackers to execute arbitrary code remotely on affected firewall systems
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall SMA1000 Zero-Day Vulnerability Chain
- **Description**: New zero-day vulnerability being chained with previously disclosed critical vulnerability in SonicWall Edge Access devices
- **Impact**: Enables comprehensive compromise of SonicWall SMA1000 devices through exploitation chain
- **Status**: Actively exploited, zero-day remains unpatched

### Cisco AsyncOS Email Security Zero-Day
- **Description**: Maximum-severity zero-day vulnerability in Cisco AsyncOS software for Email Security Appliances
- **Impact**: Allows remote code execution and system compromise
- **Status**: Actively exploited by Chinese APT group UAT-9686, currently unpatched

### ASUS Live Update Critical Flaw
- **Description**: Critical vulnerability in ASUS Live Update software component
- **Impact**: Enables unauthorized system access and potential code execution
- **Status**: Actively exploited, added to CISA KEV catalog
- **CVE ID**: CVE-2025-5387

### HPE OneView Remote Code Execution
- **Description**: Maximum severity vulnerability in HPE OneView Software enabling unauthenticated remote code execution
- **Impact**: Allows complete system compromise without authentication
- **Status**: Patches available, CVSS 10.0 rating

### Fortinet Critical Vulnerabilities
- **Description**: Multiple critical flaws in Fortinet systems being actively targeted
- **Impact**: Admin account compromise and device configuration export including credentials
- **Status**: Under active attack

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS VPN components affected by critical RCE vulnerability
- **SonicWall SMA1000 Devices**: Edge Access devices vulnerable to zero-day exploitation chains
- **Cisco Email Security Appliances**: AsyncOS software vulnerable to maximum-severity zero-day
- **ASUS Systems**: Live Update software component across multiple ASUS products
- **HPE OneView Software**: Infrastructure management platform with unauthenticated RCE
- **Fortinet Products**: Multiple Fortinet systems experiencing active exploitation
- **Motherboards**: ASRock, ASUS, GIGABYTE, and MSI motherboards affected by UEFI DMA attack vulnerabilities
- **Gladinet CentreStack**: File servers being targeted by Clop ransomware for data theft

## Attack Vectors and Techniques

- **VPN Exploitation**: Direct attacks against WatchGuard VPN services through critical RCE vulnerability
- **Zero-Day Chaining**: SonicWall attackers combining new zero-day with known vulnerabilities for enhanced impact
- **Email Security Bypass**: Cisco AsyncOS exploitation enabling compromise of email security infrastructure
- **Software Update Hijacking**: ASUS Live Update vulnerability exploitation for system compromise
- **Unauthenticated Access**: HPE OneView attacks requiring no authentication for maximum impact
- **Password Spraying**: Automated campaigns targeting Cisco SSL VPN and Palo Alto GlobalProtect gateways
- **UEFI DMA Attacks**: Early-boot direct memory access attacks against motherboard UEFI implementations
- **Phishing and Social Engineering**: RaccoonO365 toolkit used for Microsoft 365 credential theft
- **QR Code Phishing**: Kimsuky using QR codes to distribute DocSwap Android malware
- **Ransomware Data Theft**: Clop targeting Internet-exposed file servers for extortion

## Threat Actor Activities

- **UAT-9686 (Chinese APT)**: Actively exploiting Cisco AsyncOS zero-day vulnerability in targeted attacks against email security infrastructure
- **Kimsuky (North Korean APT)**: Deploying DocSwap Android malware via QR code phishing campaigns mimicking delivery applications
- **LongNosedGoblin (Chinese APT)**: Using Windows Group Policy to deploy espionage malware targeting government entities in Southeast Asia and Japan
- **Prince of Persia (Iranian APT)**: Conducting surveillance operations against dissidents with advanced operational security and cryptographic C2 communications
- **North Korean Threat Groups**: Leading global cryptocurrency theft with $2.02 billion stolen in 2025 across multiple campaigns
- **Clop Ransomware Gang**: Targeting Gladinet CentreStack file servers in new data theft extortion operations
- **RaccoonO365 Developers**: Nigerian cybercriminals creating phishing toolkits for Microsoft 365 attacks against major corporations