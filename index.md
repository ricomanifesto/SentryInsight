# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure and cloud services through multiple attack vectors. The most severe threats include a critical WatchGuard Fireware OS VPN vulnerability being actively exploited with a CVSS score of 9.3, a maximum-severity HPE OneView flaw rated CVSS 10.0 enabling unauthenticated remote code execution, and ongoing zero-day attacks against SonicWall Edge Access devices. Additionally, widespread phishing campaigns targeting Microsoft 365 accounts are leveraging OAuth device code authentication mechanisms, while new UEFI vulnerabilities enable pre-boot attacks on major motherboard manufacturers' products.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS that allows exploitation of VPN functionality
- **Impact**: Remote attackers can exploit this vulnerability to gain unauthorized access to network infrastructure
- **Status**: Actively exploited in real-world attacks; patches have been released by WatchGuard
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability affecting SonicWall SMA1000 Edge Access devices, being chained with previously disclosed critical vulnerabilities
- **Impact**: Threat actors can achieve remote code execution and compromise network edge devices
- **Status**: Currently being exploited in active attacks; zero-day status indicates no patch available
- **CVE ID**: Not disclosed

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity vulnerability in HPE OneView Software enabling unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code remotely without authentication on affected systems
- **Status**: Critical vulnerability has been patched by HPE
- **CVE ID**: Not explicitly mentioned

### UEFI DMA Attack Vulnerability
- **Description**: UEFI firmware implementation vulnerability enabling direct memory access (DMA) attacks that bypass early-boot memory protections
- **Impact**: Attackers can perform pre-boot attacks and potentially compromise system integrity at the firmware level
- **Status**: Affects multiple major motherboard vendors; patch status unclear
- **CVE ID**: Not disclosed

### Microsoft 365 OAuth Device Code Exploitation
- **Description**: Ongoing phishing campaigns exploiting OAuth device code authentication workflows to steal Microsoft 365 credentials
- **Impact**: Account takeover attacks leading to unauthorized access to corporate Microsoft 365 environments
- **Status**: Multiple threat actors actively conducting these attacks
- **CVE ID**: Not applicable (exploitation of legitimate feature)

## Affected Systems and Products

- **WatchGuard Fireware OS**: VPN functionality in firewall appliances
- **SonicWall SMA1000**: Edge Access devices used for secure remote access
- **HPE OneView Software**: Infrastructure management platform
- **UEFI Firmware**: Motherboards from ASUS, Gigabyte, MSI, and ASRock
- **Microsoft 365**: Cloud-based productivity and collaboration platform
- **Fortinet FortiCloud SSO**: Over 25,000 devices exposed with authentication bypass vulnerability
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft
- **University Systems**: Online coding repositories and institutional infrastructure

## Attack Vectors and Techniques

- **VPN Exploitation**: Targeting critical vulnerabilities in enterprise VPN solutions for network infiltration
- **Zero-Day Chaining**: Combining new zero-day vulnerabilities with previously disclosed flaws for enhanced attack capabilities
- **OAuth Phishing**: Leveraging legitimate OAuth device code flows to bypass traditional authentication protections
- **UEFI/Firmware Attacks**: Pre-boot exploitation targeting system firmware for persistent access
- **Ransomware Operations**: Data theft and extortion campaigns targeting exposed file servers
- **Social Engineering**: Distribution of malware through cracked software and YouTube videos
- **ATM Jackpotting**: Physical and logical attacks on ATM systems using Ploutus malware
- **Group Policy Abuse**: Using Windows Active Directory Group Policy for malware deployment in government networks

## Threat Actor Activities

- **Iranian Infy APT**: Resurfaced after five years of silence with new malware campaigns targeting victims
- **Russia-Aligned Groups**: Conducting Microsoft 365 device code phishing campaigns for account takeovers and destructive attacks on Danish water utility infrastructure
- **LongNosedGoblin (China-Aligned)**: New threat group targeting government entities in Southeast Asia and Japan using Windows Group Policy for espionage malware deployment
- **RansomHouse**: Upgraded encryption capabilities with multi-layered data processing techniques
- **Clop Ransomware**: Targeting Gladinet CentreStack file servers for data theft extortion campaigns
- **North Korean Cybercriminals**: Shifted strategy to target "bigger fish" for larger payouts using sophisticated attack methods
- **Nigerian Cybercriminals**: Developed and operated Raccoon0365 phishing-as-a-service platform targeting Microsoft 365 users
- **ATM Fraud Networks**: 54 individuals charged in multi-million dollar ATM jackpotting scheme using Ploutus malware