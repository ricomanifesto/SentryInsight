# Exploitation Report

Critical exploitation activity is currently targeting network infrastructure and enterprise platforms across multiple threat vectors. WatchGuard Firebox firewalls are under active attack through a critical remote code execution vulnerability being exploited in the wild. Simultaneously, multiple sophisticated campaigns are targeting Microsoft 365 environments through OAuth device code phishing mechanisms, while VPN gateways from Cisco and Palo Alto Networks face automated credential-based attacks. Hardware-level threats have emerged with UEFI firmware vulnerabilities affecting major motherboard manufacturers, and SonicWall Edge Access devices are being compromised through zero-day exploits. These concurrent exploitation campaigns demonstrate coordinated efforts by state-sponsored groups and cybercriminal organizations to compromise critical infrastructure and enterprise environments.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical remote code execution vulnerability in WatchGuard Firebox firewall VPN functionality being actively exploited in real-world attacks
- **Impact**: Attackers can execute arbitrary code remotely on affected firewall systems, potentially compromising network perimeter security
- **Status**: Active exploitation confirmed by WatchGuard, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day
- **Description**: Zero-day vulnerability in SonicWall SMA1000 Edge Access devices being chained with previously disclosed critical vulnerabilities
- **Impact**: Complete compromise of edge network security appliances, enabling persistent access to corporate networks
- **Status**: Active zero-day exploitation ongoing, threat actors chaining with existing vulnerabilities

### UEFI Firmware DMA Vulnerability
- **Description**: Direct Memory Access (DMA) vulnerability in UEFI firmware implementations that bypasses early-boot memory protections
- **Impact**: Pre-boot attacks enabling deep system compromise before operating system loads
- **Status**: Vulnerability disclosed affecting multiple major motherboard manufacturers

### Microsoft 365 OAuth Device Code Exploitation
- **Description**: Multiple threat actors exploiting OAuth device code authentication workflows to steal Microsoft 365 credentials
- **Impact**: Complete account takeover of corporate Microsoft 365 environments, enabling data theft and persistent access
- **Status**: Active widespread exploitation by multiple threat groups including Russia-linked actors

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS VPN components actively exploited
- **SonicWall SMA1000 Devices**: Edge Access appliances targeted in zero-day campaigns
- **Microsoft 365 Platforms**: OAuth authentication mechanisms under widespread attack
- **ASUS, Gigabyte, MSI, ASRock Motherboards**: UEFI firmware vulnerable to DMA attacks
- **Cisco SSL VPN Gateways**: Targeted in automated password spraying campaigns
- **Palo Alto Networks GlobalProtect**: Subject to credential-based attacks
- **Gladinet CentreStack Servers**: Internet-exposed file servers targeted by Clop ransomware
- **FortiCloud SSO Devices**: Over 25,000 devices exposed with authentication bypass vulnerabilities

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Russia-linked groups leveraging device code authentication workflows for credential theft
- **DMA Attacks**: Hardware-level exploitation through direct memory access bypassing boot protections
- **Password Spraying**: Automated credential attacks targeting VPN gateways and authentication systems
- **Zero-Day Chaining**: Combining new zero-day vulnerabilities with previously disclosed critical flaws
- **Group Policy Abuse**: China-aligned actors using Windows Group Policy for malware deployment
- **Phishing-as-a-Service**: Raccoon0365 platform enabling large-scale Microsoft 365 targeting
- **Software Supply Chain**: Cracked software distribution for CountLoader and GachiLoader malware delivery

## Threat Actor Activities

- **Russia-Linked Groups**: Conducting sophisticated Microsoft 365 OAuth phishing campaigns for account takeovers
- **LongNosedGoblin (China-aligned)**: Targeting Southeast Asian and Japanese government networks using Group Policy for espionage malware deployment
- **Clop Ransomware Gang**: Launching data theft extortion campaigns against Gladinet CentreStack file servers
- **North Korean Groups**: Leading global cryptocurrency theft with $2.02 billion stolen in 2025 through sophisticated attack methods
- **Prince of Persia (Iran APT)**: Conducting surveillance operations against dissidents with advanced operational security
- **Raccoon0365 Operators**: Nigerian-based phishing-as-a-service platform targeting major corporations through Microsoft 365 attacks