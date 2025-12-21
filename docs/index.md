# Exploitation Report

Current cybersecurity landscape shows intense exploitation activity across multiple attack surfaces, with threat actors leveraging zero-day vulnerabilities, advanced phishing techniques, and sophisticated malware campaigns. Critical vulnerabilities in WatchGuard Firebox firewalls (CVE-2025-14733) and HPE OneView (CVE-2025-22205) are being actively exploited, while SonicWall Edge Access devices face zero-day attacks. Microsoft 365 environments are under siege from multiple threat actors using OAuth device code phishing and sophisticated account takeover techniques. Iranian APT groups have resurfaced after years of dormancy, Chinese-aligned actors are deploying espionage malware through Windows Group Policy, and ransomware operations are evolving with advanced encryption methods.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in WatchGuard Fireware OS affecting VPN functionality with remote code execution capabilities
- **Impact**: Attackers can execute arbitrary code remotely, potentially gaining full control over network infrastructure
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity vulnerability in HPE OneView Software allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Critical vulnerability with patches released
- **CVE ID**: CVE-2025-22205

### SonicWall Edge Access Zero-Day
- **Description**: New zero-day vulnerability in SonicWall SMA1000 devices being chained with previously disclosed critical vulnerabilities
- **Impact**: Threat actors achieving persistent access to network edge devices
- **Status**: Actively exploited in targeted attacks, no patch information provided

### UEFI Firmware DMA Attacks
- **Description**: Vulnerability in UEFI firmware implementation allowing direct memory access attacks that bypass early-boot memory protections
- **Impact**: Pre-boot system compromise enabling deep persistence and security control bypass
- **Status**: Affects multiple major motherboard vendors, mitigation status unclear

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: All devices running vulnerable Fireware OS versions
- **HPE OneView Software**: Infrastructure management platforms with unauthenticated access exposure
- **SonicWall SMA1000 Devices**: Edge access appliances under active zero-day exploitation
- **Motherboards**: ASUS, Gigabyte, MSI, and ASRock motherboards with vulnerable UEFI implementations
- **Microsoft 365 Environments**: Accounts and tenants targeted through OAuth device code phishing
- **Fortinet FortiCloud SSO**: Over 25,000 devices exposed online with authentication bypass vulnerabilities
- **Gladinet CentreStack Servers**: File servers targeted by Clop ransomware for data theft operations

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Multi-actor campaigns targeting Microsoft 365 accounts using device code authentication workflows
- **VPN Infrastructure Exploitation**: Direct targeting of enterprise VPN solutions for network access
- **UEFI-Level Attacks**: Pre-boot compromise techniques bypassing traditional security controls
- **Group Policy Abuse**: Windows Group Policy mechanisms used for malware deployment and persistence
- **ATM Jackpotting**: Physical and malware-based attacks using Ploutus malware for cash theft
- **Ransomware-as-a-Service Evolution**: Multi-layered encryption techniques in RansomHouse operations
- **Phishing-as-a-Service Platforms**: Raccoon0365 platform enabling Microsoft 365 credential theft

## Threat Actor Activities

- **Iranian Infy APT (Prince of Persia)**: Resurfaced after five years of dormancy with new malware campaigns targeting Swedish and regional victims
- **LongNosedGoblin (China-aligned)**: Newly identified threat group using Windows Group Policy for espionage malware deployment against Southeast Asian and Japanese government entities
- **Russia-linked Groups**: Conducting sophisticated Microsoft 365 device code phishing campaigns for account takeovers
- **RansomHouse Operators**: Upgraded ransomware operations with multi-layered data processing and encryption techniques
- **Clop Ransomware Gang**: Actively targeting Gladinet CentreStack file servers in data theft extortion campaigns
- **ATM Criminal Networks**: 54 individuals charged in multi-million dollar ATM jackpotting scheme using Ploutus malware
- **Raccoon0365 Developers**: Nigerian-based phishing-as-a-service platform creators arrested for Microsoft 365 attacks
- **State-Sponsored Russian Groups**: Attributed to destructive cyberattacks against Danish water utility infrastructure