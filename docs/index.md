# Exploitation Report

The cybersecurity landscape is experiencing significant exploitation activity across multiple fronts, with critical vulnerabilities being actively exploited in enterprise infrastructure and widespread phishing campaigns targeting Microsoft 365 environments. Most notably, WatchGuard's Fireware OS contains a critical vulnerability (CVE-2025-14733) that is being actively exploited in real-world attacks, while SonicWall Edge Access devices face ongoing zero-day exploitation. Additionally, threat actors are leveraging sophisticated OAuth device code phishing techniques and ATM jackpotting malware to conduct large-scale financial crimes and account takeovers.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Remote code execution allowing complete system compromise
- **Status**: Actively exploited in real-world attacks; patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability affecting SonicWall SMA1000 Edge Access devices
- **Impact**: Threat actors chaining this zero-day with previously disclosed critical vulnerabilities for enhanced attack capabilities
- **Status**: Active exploitation ongoing; zero-day status indicates no patch currently available

### UEFI Direct Memory Access Vulnerability
- **Description**: UEFI firmware implementation flaw enabling direct memory access attacks that bypass early-boot memory protections
- **Impact**: Pre-boot attacks allowing deep system compromise before operating system initialization
- **Status**: Affects multiple major motherboard manufacturers; mitigation status unclear

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity security flaw in HPE OneView Software allowing unauthenticated access
- **Impact**: Remote code execution without authentication requirements
- **Status**: Critical vulnerability with patches released

### FortiCloud SSO Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Fortinet devices with FortiCloud SSO enabled
- **Impact**: Remote attacks bypassing authentication mechanisms
- **Status**: Over 25,000 devices exposed online amid ongoing attacks

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Critical RCE vulnerability in Fireware OS affecting VPN components
- **SonicWall SMA1000 Devices**: Edge Access devices targeted by chained zero-day and known vulnerability exploits
- **ASUS, GIGABYTE, MSI, ASRock Motherboards**: UEFI firmware vulnerable to early-boot DMA attacks
- **HPE OneView Software**: Management platform affected by unauthenticated RCE vulnerability
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed to authentication bypass attacks
- **Microsoft 365 Environments**: Targeted by multiple OAuth phishing campaigns and device code authentication attacks
- **Cisco VPN Gateways**: Targeted in password spraying and credential-based attacks
- **Palo Alto Networks GlobalProtect**: Subject to automated credential attacks

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Russia-linked threat actors using Microsoft 365 device code authentication workflows for account takeovers
- **ATM Jackpotting**: Deployment of Ploutus malware for physical ATM compromise and cash theft
- **Password Spraying**: Automated credential attacks against VPN gateways from multiple vendors
- **Phishing-as-a-Service**: Raccoon0365 platform facilitating Microsoft 365 credential theft operations
- **Windows Group Policy Abuse**: LongNosedGoblin threat group leveraging legitimate administrative tools for malware deployment
- **Cracked Software Distribution**: CountLoader and GachiLoader malware spread through compromised software sites and YouTube videos
- **DMA Attacks**: Direct memory access exploitation during system boot processes
- **Zero-Day Chaining**: Combining newly discovered vulnerabilities with previously disclosed flaws for enhanced impact

## Threat Actor Activities

- **Russia-Linked Groups**: Conducting sophisticated Microsoft 365 phishing campaigns using device code authentication bypass techniques
- **LongNosedGoblin (China-Aligned)**: Targeting governmental entities in Southeast Asia and Japan using Windows Group Policy for espionage malware deployment
- **North Korean Cybercriminals**: Generated $2.02 billion in cryptocurrency theft in 2025, shifting strategy to target larger, more valuable organizations with patient, sophisticated attack methods
- **Clop Ransomware Gang**: Actively targeting Internet-exposed Gladinet CentreStack file servers for data theft extortion campaigns
- **Nigerian Cybercriminals**: Three individuals arrested for developing and operating the Raccoon0365 phishing-as-a-service platform targeting Microsoft 365 users
- **Russian State Actors**: Attributed to destructive cyberattacks against Danish water utility infrastructure as part of hybrid warfare campaign
- **Financial Crime Syndicates**: 54 individuals indicted in multi-million dollar ATM jackpotting scheme using Ploutus malware across multiple jurisdictions