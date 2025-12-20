# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure through multiple attack vectors. WatchGuard Firebox firewalls are under active attack via CVE-2025-14733, a critical remote code execution vulnerability with a CVSS score of 9.3. Meanwhile, SonicWall Edge Access devices are being compromised through a chained zero-day attack targeting SMA1000 devices. Additional threats include widespread Microsoft 365 OAuth phishing campaigns, UEFI firmware vulnerabilities affecting major motherboard manufacturers, and sophisticated state-sponsored campaigns by China-aligned and Russia-linked threat groups targeting government entities and critical infrastructure.

## Active Exploitation Details

### WatchGuard Fireware OS VPN Vulnerability
- **Description**: Critical remote code execution vulnerability in WatchGuard Firebox firewall systems
- **Impact**: Complete system compromise with remote code execution capabilities
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733

### SonicWall Edge Access Zero-Day Attack
- **Description**: New zero-day vulnerability chained with previously disclosed critical vulnerability targeting SMA1000 devices
- **Impact**: Complete device compromise and potential network infiltration
- **Status**: Active exploitation ongoing, leveraging both new zero-day and existing critical flaw

### UEFI Firmware DMA Attack
- **Description**: UEFI firmware implementation vulnerability enabling direct memory access attacks that bypass early-boot memory protections
- **Impact**: Pre-boot system compromise and complete control over affected systems
- **Status**: Vulnerability disclosed, affects multiple major motherboard manufacturers

### Microsoft 365 OAuth Phishing Exploitation
- **Description**: Multiple threat actors exploiting OAuth device code authorization mechanism for account takeovers
- **Impact**: Complete Microsoft 365 account compromise and corporate data access
- **Status**: Active campaigns ongoing with sophisticated phishing-as-a-service platforms

## Affected Systems and Products

- **WatchGuard Firebox Firewalls**: All versions running vulnerable Fireware OS
- **SonicWall SMA1000 Devices**: Edge Access devices exposed to internet
- **Motherboards**: ASUS, ASRock, Gigabyte, and MSI motherboards with vulnerable UEFI implementations
- **Microsoft 365**: Enterprise accounts targeted through OAuth authentication flows
- **Cisco VPN Systems**: SSL VPN platforms under password spraying attacks
- **Palo Alto Networks**: GlobalProtect VPN gateways targeted in credential attacks
- **Fortinet FortiCloud**: Over 25,000 devices exposed with SSO enabled amid authentication bypass attacks
- **Gladinet CentreStack**: File servers targeted by Clop ransomware for data theft

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of critical firewall vulnerabilities for system compromise
- **Zero-Day Chaining**: Combining new zero-day with existing vulnerabilities for enhanced impact
- **DMA Attacks**: Pre-boot direct memory access to bypass security protections
- **OAuth Phishing**: Device code authentication abuse for Microsoft 365 account takeovers
- **Password Spraying**: Automated credential attacks against VPN infrastructure
- **Ransomware Deployment**: Data theft extortion campaigns targeting file servers
- **Group Policy Abuse**: Windows Group Policy manipulation for malware deployment
- **Phishing-as-a-Service**: Professional phishing platforms like Raccoon0365 for scalable attacks

## Threat Actor Activities

- **China-Aligned APT (LongNosedGoblin)**: Deploying espionage malware through Windows Group Policy to target governmental entities across Southeast Asia and Japan
- **Russia-Linked Groups**: Conducting Microsoft 365 device code phishing campaigns for account takeovers and credential theft
- **North Korean Cybercriminals**: Leading global cryptocurrency theft with $2.02 billion stolen in 2025 using sophisticated attack methods
- **Iranian APT (Prince of Persia)**: Targeting dissidents with advanced operational security and cryptographic communications
- **Clop Ransomware Gang**: Executing data theft extortion campaigns against Internet-exposed file servers
- **Nigerian Cybercriminals**: Operating Raccoon0365 phishing-as-a-service platform for Microsoft 365 attacks
- **Russian State Actors**: Orchestrating destructive cyberattacks against Danish critical infrastructure, including water utilities