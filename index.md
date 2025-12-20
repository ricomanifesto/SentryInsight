# Exploitation Report

Current threat landscape reveals significant exploitation activity across multiple vectors, with critical vulnerabilities being actively exploited in enterprise environments. The most pressing concerns include a critical WatchGuard Fireware OS VPN vulnerability being exploited in real-world attacks, zero-day attacks targeting SonicWall Edge Access devices, and widespread OAuth phishing campaigns against Microsoft 365 accounts. Additionally, over 25,000 FortiCloud SSO devices remain exposed to remote attacks, while threat actors continue leveraging UEFI vulnerabilities for pre-boot attacks across major motherboard manufacturers.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality with remote code execution capabilities
- **Impact**: Attackers can achieve complete system compromise and establish persistent access to network infrastructure
- **Status**: Actively exploited in real-world attacks; patches have been released by WatchGuard
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day Attacks
- **Description**: New zero-day vulnerability in SonicWall SMA1000 devices being chained with previously disclosed critical vulnerabilities
- **Impact**: Complete device compromise and potential lateral movement within enterprise networks
- **Status**: Active exploitation ongoing; attackers combining multiple vulnerabilities for enhanced impact

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity vulnerability in HPE OneView Software allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Critical vulnerability resolved by HPE with patches available

### UEFI DMA Attack Vulnerability
- **Description**: UEFI firmware implementation vulnerability enabling direct memory access (DMA) attacks that bypass early-boot memory protections
- **Impact**: Pre-boot compromise allowing attackers to establish persistent, low-level system access
- **Status**: Affects multiple motherboard manufacturers; early-boot attack vector confirmed

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS VPN components experiencing active exploitation
- **SonicWall SMA1000 Devices**: Edge Access devices targeted in zero-day attack campaigns
- **Microsoft 365 Platforms**: Accounts targeted through OAuth device code phishing attacks
- **FortiCloud SSO Devices**: Over 25,000 devices exposed online with authentication bypass vulnerabilities
- **UEFI Motherboards**: ASRock, ASUS, Gigabyte, and MSI motherboards vulnerable to DMA attacks
- **HPE OneView Software**: Infrastructure management platform affected by critical RCE vulnerability
- **Cisco VPN Gateways**: SSL VPN platforms targeted in password spraying campaigns
- **Palo Alto Networks GlobalProtect**: VPN solutions under credential-based attacks
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft extortion

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Microsoft 365 credential theft through device code authentication workflow exploitation
- **Password Spraying Campaigns**: Automated attacks against VPN platforms using credential-based techniques
- **Zero-Day Chaining**: Combining new zero-day vulnerabilities with previously disclosed critical flaws
- **DMA Pre-Boot Attacks**: Direct memory access attacks bypassing early-boot security protections
- **Group Policy Deployment**: Windows Group Policy abuse for espionage malware distribution
- **Phishing-as-a-Service**: Raccoon0365 platform facilitating Microsoft 365 targeted attacks
- **Malware Distribution**: Cracked software and YouTube videos spreading CountLoader and GachiLoader
- **Data Theft Extortion**: Ransomware operations targeting exposed file servers for data exfiltration

## Threat Actor Activities

- **Russia-Aligned Groups**: Conducting Microsoft 365 device code phishing campaigns for account takeovers
- **LongNosedGoblin (China-Aligned)**: Targeting Asian governments using Windows Group Policy for espionage malware deployment
- **Clop Ransomware Gang**: Targeting Internet-exposed Gladinet CentreStack servers in data theft campaigns
- **North Korean Groups**: Leading global cryptocurrency theft with $2.02 billion stolen in 2025
- **Prince of Persia (Iran APT)**: Conducting surveillance operations against dissidents with advanced operational security
- **Nigerian Cybercriminals**: Operating Raccoon0365 phishing-as-a-service platform targeting Microsoft 365
- **Russian State Actors**: Orchestrating destructive cyberattacks against Danish critical infrastructure