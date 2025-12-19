# Exploitation Report

The cybersecurity landscape is currently experiencing a surge of critical zero-day and actively exploited vulnerabilities across multiple enterprise infrastructure components. SonicWall SMA 100 series appliances are under active attack through a chained exploit combining a new zero-day with a previously disclosed critical vulnerability. Cisco AsyncOS Email Security Appliances face maximum-severity zero-day exploitation by China-nexus threat actors, while HPE OneView software contains a CVSS 10.0 rated flaw enabling unauthenticated remote code execution. ASUS Live Update has been added to CISA's Known Exploited Vulnerabilities catalog due to confirmed active exploitation, and Fortinet devices are experiencing ongoing attacks targeting administrative accounts. These incidents represent significant threats to enterprise security infrastructure, with threat actors demonstrating sophisticated chaining techniques and persistent targeting of critical network security appliances.

## Active Exploitation Details

### SonicWall Edge Access Zero-Day Vulnerability
- **Description**: A new zero-day vulnerability in SonicWall SMA1000 devices that attackers are chaining with a critical vulnerability disclosed earlier this year
- **Impact**: Enables threat actors to compromise edge access devices and potentially gain persistent network access
- **Status**: Currently being actively exploited in the wild

### SonicWall SMA 100 Series Vulnerability
- **Description**: Security flaw in Secure Mobile Access (SMA) 100 series appliances actively exploited by attackers
- **Impact**: Allows unauthorized access to secure mobile access infrastructure
- **Status**: Actively exploited in the wild, patches have been released by SonicWall
- **CVE ID**: CVE-2025-40602

### Cisco AsyncOS Zero-Day Vulnerability
- **Description**: Maximum-severity zero-day flaw in Cisco AsyncOS software for Email Security Appliances
- **Impact**: Enables remote code execution and complete compromise of email security infrastructure
- **Status**: Currently unpatched and actively exploited by China-nexus APT group UAT-9686

### ASUS Live Update Critical Vulnerability
- **Description**: Critical flaw in ASUS Live Update utility that has demonstrated active exploitation
- **Impact**: Allows attackers to compromise system update mechanisms and potentially deploy malware
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to confirmed exploitation

### HPE OneView Remote Code Execution Flaw
- **Description**: Maximum-severity vulnerability rated CVSS 10.0 in HPE OneView Software enabling unauthenticated remote code execution
- **Impact**: Allows complete system compromise without authentication requirements
- **Status**: Critical vulnerability has been patched by HPE

### Fortinet Administrative Account Targeting
- **Description**: Critical flaws in Fortinet devices being actively exploited to target administrative accounts
- **Impact**: Once authenticated, attackers can export device configurations including hashed credentials and sensitive information
- **Status**: Under active attack with focus on credential harvesting

## Affected Systems and Products

- **SonicWall SMA1000 Devices**: Edge access appliances vulnerable to chained zero-day exploitation
- **SonicWall SMA 100 Series**: Secure Mobile Access appliances affected by actively exploited vulnerability
- **Cisco AsyncOS Email Security Appliances**: Maximum-severity zero-day affecting email security infrastructure
- **ASUS Live Update Utility**: System update mechanism with confirmed exploitation evidence
- **HPE OneView Software**: Infrastructure management platform with unauthenticated RCE vulnerability
- **Fortinet Network Devices**: Security appliances targeted for administrative credential harvesting
- **Gladinet CentreStack Servers**: File servers targeted by Clop ransomware for data theft operations
- **Palo Alto Networks GlobalProtect**: VPN platform targeted in automated credential-based attacks
- **Cisco SSL VPN**: VPN infrastructure targeted in password spraying campaigns
- **AWS EC2 and ECS**: Cloud services compromised for cryptocurrency mining operations

## Attack Vectors and Techniques

- **Zero-Day Vulnerability Chaining**: Attackers combining new zero-days with previously disclosed vulnerabilities for enhanced exploitation capabilities
- **Password Spraying Attacks**: Automated campaigns targeting VPN gateways with credential-based attacks across multiple platforms
- **Device Linking Abuse**: Exploitation of legitimate WhatsApp device-linking features through pairing codes in GhostPairing campaign
- **Group Policy Deployment**: China-aligned threat actors using Windows Group Policy mechanisms to deploy espionage malware
- **QR Code Phishing**: Distribution of Android malware through QR codes hosted on phishing sites mimicking legitimate delivery applications
- **Cryptocurrency Mining**: Compromise of cloud credentials to deploy mining operations on AWS infrastructure
- **Data Theft Extortion**: Targeting of Internet-exposed file servers for ransomware-based data theft campaigns

## Threat Actor Activities

- **UAT-9686**: China-nexus APT group actively exploiting zero-day vulnerability in Cisco AsyncOS Email Security Appliances
- **LongNosedGoblin**: Previously undocumented China-aligned threat cluster targeting governmental entities in Southeast Asia and Japan using Windows Group Policy for espionage malware deployment
- **Clop Ransomware Gang**: Conducting data theft extortion campaign targeting Internet-exposed Gladinet CentreStack file servers
- **Kimsuky**: North Korean threat actor distributing DocSwap Android malware variant via QR code phishing campaigns posing as Seoul delivery applications
- **Prince of Persia**: Dormant Iranian APT group resuming operations with advanced operational security targeting dissidents through cryptographic command-and-control communications
- **North Korea-Linked Groups**: Responsible for $2.02 billion in cryptocurrency theft in 2025, leading global crypto theft activities
- **E-Note Cryptocurrency Exchange**: Seized by law enforcement for laundering over $70 million in ransomware payments for cybercriminal groups