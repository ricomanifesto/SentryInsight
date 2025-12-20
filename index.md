# Exploitation Report

Current exploitation activity reveals several critical vulnerabilities being actively targeted across network infrastructure and enterprise platforms. Most notably, WatchGuard Fireware OS systems are experiencing active exploitation through a critical VPN vulnerability rated CVSS 9.3, while SonicWall Edge Access devices face sophisticated zero-day attacks. Additionally, widespread credential-based attacks are targeting Cisco and Palo Alto Networks VPN platforms, and a new UEFI vulnerability enables pre-boot attacks across major motherboard manufacturers. The threat landscape is further complicated by sophisticated phishing campaigns targeting Microsoft 365 accounts and advanced persistent threat activities from state-sponsored actors.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality
- **Impact**: Allows attackers to execute remote code and gain unauthorized access to network infrastructure
- **Status**: Actively exploited in real-world attacks, patches have been released
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Device Zero-Day
- **Description**: Previously unknown vulnerability in SonicWall SMA1000 Edge Access devices
- **Impact**: Threat actors chain this zero-day with previously disclosed critical vulnerabilities for advanced network compromise
- **Status**: Active zero-day exploitation ongoing, chained with existing vulnerabilities

### UEFI Pre-Boot Attack Vulnerability
- **Description**: Direct Memory Access (DMA) vulnerability in UEFI firmware implementations that bypasses early-boot memory protections
- **Impact**: Enables pre-boot attacks that can compromise system integrity before operating system loads
- **Status**: Affects multiple major motherboard manufacturers, exploitation potential confirmed

### HPE OneView Remote Code Execution Flaw
- **Description**: Maximum-severity security vulnerability in HPE OneView Software allowing unauthenticated access
- **Impact**: Successful exploitation results in remote code execution on management infrastructure
- **Status**: Critical vulnerability with CVSS 10.0 rating, patches available

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS systems with VPN functionality affected by active exploitation
- **SonicWall SMA1000 Devices**: Edge Access devices targeted in sophisticated zero-day attack chains
- **Motherboard Systems**: ASUS, Gigabyte, MSI, and ASRock motherboards vulnerable to UEFI-based DMA attacks
- **Microsoft 365 Platforms**: Enterprise accounts targeted through OAuth device code phishing mechanisms
- **Cisco VPN Systems**: SSL VPN gateways experiencing automated credential spraying attacks
- **Palo Alto Networks**: GlobalProtect VPN platforms under targeted password spraying campaigns
- **HPE OneView Software**: Management platform affected by critical unauthenticated RCE vulnerability
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed to remote authentication bypass attacks

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Sophisticated campaigns leveraging Microsoft 365 device authorization workflows to steal credentials
- **VPN Password Spraying**: Automated credential-based attacks targeting multiple VPN platforms simultaneously
- **Zero-Day Chaining**: Advanced attackers combining new zero-day exploits with previously disclosed vulnerabilities
- **UEFI Firmware Exploitation**: Pre-boot DMA attacks bypassing traditional security controls at the hardware level
- **Group Policy Abuse**: China-aligned actors using Windows Group Policy mechanisms to deploy espionage malware
- **Phishing-as-a-Service**: Criminal platforms like Raccoon0365 providing turnkey phishing infrastructure for Microsoft 365 attacks
- **Malware Distribution via Cracked Software**: CountLoader and GachiLoader malware spread through compromised software distribution sites

## Threat Actor Activities

- **Russia-Aligned Groups**: Conducting sophisticated Microsoft 365 device code phishing campaigns for account takeovers and targeting Danish critical infrastructure with destructive cyberattacks
- **LongNosedGoblin (China-Aligned)**: New APT group deploying Windows Group Policy mechanisms to conduct espionage against Southeast Asian and Japanese government entities
- **North Korean Cybercriminals**: Responsible for $2.02 billion in cryptocurrency theft in 2025, shifting strategy to target larger payouts with sophisticated attack methods
- **Prince of Persia (Iran APT)**: Resumed operations with enhanced operational security, targeting Iranian dissidents with advanced cryptographic communication methods
- **Clop Ransomware Gang**: Targeting Internet-exposed Gladinet CentreStack file servers in new data theft extortion campaigns
- **Nigerian Cybercriminals**: Three individuals arrested for developing and operating Raccoon0365 phishing-as-a-service platform targeting Microsoft 365 accounts