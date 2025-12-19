# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple enterprise security platforms, with several maximum-severity flaws posing immediate threats to organizations worldwide. The most alarming developments include zero-day attacks against Cisco AsyncOS Email Security Appliances by China-nexus threat actors, active exploitation of SonicWall Edge Access devices through chained vulnerabilities, and widespread targeting of Fortinet devices amid authentication bypass vulnerabilities. Additional critical threats include a newly discovered WatchGuard Fireware OS vulnerability and an ASUS Live Update flaw that has been added to CISA's Known Exploited Vulnerabilities catalog, all indicating a sustained campaign by advanced persistent threat groups targeting enterprise network security infrastructure.

## Active Exploitation Details

### Cisco AsyncOS Email Security Zero-Day Vulnerability
- **Description**: A maximum-severity zero-day flaw in Cisco AsyncOS software for Email Security Appliances
- **Impact**: Allows threat actors to compromise email security infrastructure and potentially gain unauthorized access to organizational communications
- **Status**: Currently unpatched and actively exploited by China-nexus APT group UAT-9686
- **CVE ID**: Not yet assigned

### SonicWall Edge Access Zero-Day Vulnerability
- **Description**: A new zero-day flaw in SonicWall SMA1000 Edge Access devices being chained with previously disclosed critical vulnerabilities
- **Impact**: Enables threat actors to compromise VPN access points and potentially gain network access
- **Status**: Actively exploited in attacks targeting SonicWall devices
- **CVE ID**: Not disclosed

### WatchGuard Fireware OS Critical RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in WatchGuard Firebox firewalls running Fireware OS
- **Impact**: Allows attackers to execute arbitrary code remotely on affected firewall devices
- **Status**: Actively exploited in real-world attacks, patches available
- **CVE ID**: CVE-2025-14733 (CVSS score: 9.3)

### ASUS Live Update Critical Vulnerability
- **Description**: Critical flaw in ASUS Live Update utility that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Enables attackers to compromise systems through the update mechanism
- **Status**: Evidence of active exploitation confirmed by CISA
- **CVE ID**: Not specified in available information

### Fortinet Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability affecting FortiCloud SSO-enabled devices
- **Impact**: Attackers can target admin accounts and export device configurations including hashed credentials and sensitive information
- **Status**: Under active attack with over 25,000 devices exposed online
- **CVE ID**: Not specified

### HPE OneView Maximum Severity Vulnerability
- **Description**: Critical vulnerability in HPE OneView Software with maximum CVSS score
- **Impact**: Allows unauthenticated remote code execution on affected systems
- **Status**: Recently patched by HPE
- **CVE ID**: Not specified (CVSS score: 10.0)

## Affected Systems and Products

- **Cisco AsyncOS Email Security Appliances**: Email security infrastructure running vulnerable AsyncOS software
- **SonicWall SMA1000 Devices**: Edge Access devices vulnerable to chained zero-day and known vulnerability exploitation
- **WatchGuard Firebox Firewalls**: Network security appliances running vulnerable Fireware OS versions
- **ASUS Systems**: Devices using ASUS Live Update utility across various product lines
- **Fortinet Devices**: Over 25,000 FortiCloud SSO-enabled devices exposed to internet-based attacks
- **HPE OneView Software**: Infrastructure management platforms running vulnerable OneView versions
- **Gladinet CentreStack Servers**: File servers targeted by Clop ransomware in data theft campaigns
- **Various Motherboards**: ASRock, ASUS, GIGABYTE, and MSI motherboards affected by UEFI early-boot DMA attack vulnerabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Advanced persistent threat groups leveraging unpatched vulnerabilities for initial access
- **Authentication Bypass**: Targeting FortiCloud SSO mechanisms to gain unauthorized administrative access
- **Remote Code Execution**: Exploiting critical RCE flaws in network security appliances for system compromise
- **Chained Vulnerability Exploitation**: Combining new zero-days with previously disclosed vulnerabilities for enhanced attack effectiveness
- **Password Spraying**: Automated credential-based attacks against VPN gateways including Palo Alto Networks GlobalProtect and Cisco SSL VPN
- **QR Code Phishing**: Distribution of DocSwap Android malware through QR codes on phishing sites mimicking delivery applications
- **Windows Group Policy Abuse**: Using legitimate Windows administration tools to deploy espionage malware
- **Early-Boot DMA Attacks**: Exploiting UEFI vulnerabilities for direct memory access during system boot process
- **Ransomware Data Theft**: Targeting internet-exposed file servers for data exfiltration and extortion campaigns

## Threat Actor Activities

- **UAT-9686 (China-nexus APT)**: Actively exploiting Cisco AsyncOS zero-day vulnerability in targeted attacks against email security infrastructure
- **LongNosedGoblin (China-aligned)**: Previously undocumented threat group targeting governmental entities in Southeast Asia and Japan using Windows Group Policy for malware deployment
- **North Korean Threat Actors**: Led global cryptocurrency theft in 2025 with $2.02 billion stolen, including Kimsuky group distributing DocSwap Android malware via QR phishing campaigns
- **Clop Ransomware Gang**: Conducting data theft extortion campaigns targeting Gladinet CentreStack file servers
- **Russian State Actors**: Attributed to destructive cyberattacks against Danish critical infrastructure as part of hybrid warfare operations
- **Prince of Persia (Iran APT)**: Resuming operations with advanced operational security to spy on dissidents using cryptographic communication with C2 servers
- **RaccoonO365 Developers**: Nigerian cybercriminals developing phishing tools for Microsoft 365 attacks before recent arrests