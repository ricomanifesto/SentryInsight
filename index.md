# Exploitation Report

Critical exploitation activity spans multiple attack vectors with active zero-day campaigns targeting enterprise infrastructure. WatchGuard Fireware OS firewalls face active exploitation through CVE-2025-14733, while SonicWall Edge Access devices are compromised via chained zero-day attacks. Microsoft 365 environments are under sustained assault through OAuth device code phishing campaigns by Russia-linked actors, complemented by the Raccoon0365 phishing-as-a-service platform. UEFI firmware vulnerabilities enable pre-boot attacks on major motherboard vendors, while ransomware operations like Clop and RansomHouse continue targeting enterprise systems with enhanced encryption techniques. State-sponsored groups including Iranian Infy APT and China-aligned LongNosedGoblin are conducting sophisticated espionage campaigns against government entities across multiple regions.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical security flaw in Fireware OS affecting VPN functionality with remote code execution capabilities
- **Impact**: Attackers can achieve remote code execution on WatchGuard Firebox firewalls
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day Chain
- **Description**: New zero-day vulnerability chained with previously disclosed critical vulnerability in SMA1000 devices
- **Impact**: Complete compromise of SonicWall Edge Access infrastructure
- **Status**: Active zero-day attacks ongoing, targeting SMA1000 devices

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity security flaw allowing unauthenticated remote code execution
- **Impact**: Complete system compromise without authentication requirements
- **Status**: Critical vulnerability resolved with patches available

### UEFI DMA Attack Vulnerability
- **Description**: UEFI firmware implementation vulnerable to direct memory access attacks that bypass early-boot memory protections
- **Impact**: Pre-boot system compromise enabling persistent attacks
- **Status**: Affects motherboards from ASUS, Gigabyte, MSI, and ASRock

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: Fireware OS VPN implementations
- **SonicWall SMA1000**: Edge Access devices and appliances
- **HPE OneView Software**: Infrastructure management platforms
- **Motherboard Vendors**: ASUS, ASRock, GIGABYTE, MSI UEFI firmware
- **Microsoft 365**: Enterprise email and collaboration platforms
- **Fortinet FortiCloud**: Over 25,000 exposed SSO-enabled devices
- **Gladinet CentreStack**: File server platforms targeted by ransomware

## Attack Vectors and Techniques

- **OAuth Device Code Phishing**: Exploitation of Microsoft 365 device code authorization workflows
- **UEFI DMA Attacks**: Direct memory access attacks bypassing boot-time protections
- **VPN Exploitation**: Remote code execution through network appliance vulnerabilities
- **Ransomware Encryption**: Multi-layered data processing techniques by RansomHouse
- **ATM Jackpotting**: Ploutus malware deployment for cash extraction
- **Group Policy Abuse**: Windows Group Policy used for malware distribution by APT groups
- **Phishing-as-a-Service**: Raccoon0365 platform targeting Microsoft 365 credentials

## Threat Actor Activities

- **Iranian Infy APT**: Resurged after five years of silence, targeting Swedish and other international victims
- **Russia-linked Groups**: Multiple actors conducting Microsoft 365 OAuth phishing campaigns
- **LongNosedGoblin**: China-aligned APT targeting governmental entities in Southeast Asia and Japan using Windows Group Policy
- **Clop Ransomware**: Targeting Gladinet CentreStack file servers for data theft extortion
- **RansomHouse**: Upgraded encryption capabilities with multi-layered data processing
- **ATM Criminal Network**: 54 individuals charged in multi-million dollar jackpotting scheme
- **Raccoon0365 Operators**: Nigerian-based phishing-as-a-service developers arrested
- **North Korean Groups**: Sophisticated targeting of high-value cryptocurrency and financial targets