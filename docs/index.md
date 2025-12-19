# Exploitation Report

The current threat landscape reveals intense active exploitation across critical infrastructure components, with several maximum-severity vulnerabilities being exploited in the wild. Most concerning are the zero-day attacks targeting Cisco AsyncOS Email Security Appliances by China-nexus threat actors and the active exploitation of HPE OneView Software vulnerabilities. Additional critical exploitation includes ASUS Live Update flaws flagged by CISA and SonicWall SMA 100 appliances being actively targeted. These attacks demonstrate sophisticated threat actors focusing on high-value enterprise infrastructure while simultaneously conducting widespread credential-based attacks against VPN gateways and cloud services.

## Active Exploitation Details

### **Cisco AsyncOS Email Security Appliances Zero-Day**
- **Description**: Maximum-severity zero-day vulnerability in Cisco AsyncOS software affecting email security appliances
- **Impact**: Complete system compromise allowing threat actors to gain unauthorized access to email security infrastructure
- **Status**: Currently being actively exploited by China-nexus APT actor UAT-9686; no patch available
- **CVE ID**: Not specified in articles

### **HPE OneView Software Remote Code Execution**
- **Description**: Maximum-severity vulnerability in HPE OneView Software with CVSS 10.0 rating enabling unauthenticated remote code execution
- **Impact**: Attackers can execute arbitrary code remotely without authentication, leading to complete system compromise
- **Status**: Patched by HPE; previously exploited in the wild

### **ASUS Live Update Critical Flaw**
- **Description**: Critical vulnerability in ASUS Live Update software added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: System compromise through the software update mechanism
- **Status**: Evidence of active exploitation confirmed by CISA

### **SonicWall SMA 100 Series Vulnerability**
- **Description**: Security flaw in SonicWall Secure Mobile Access 100 series appliances
- **Impact**: Unauthorized access to secure network infrastructure and remote access systems
- **Status**: Actively exploited in the wild; patches now available
- **CVE ID**: CVE-2025-40602

### **Critical Fortinet Vulnerabilities**
- **Description**: Multiple critical flaws in Fortinet infrastructure being actively targeted
- **Impact**: Admin account compromise and export of device configurations including hashed credentials
- **Status**: Under active attack with focus on administrative accounts

## Affected Systems and Products

- **HPE OneView Software**: Infrastructure management platform with maximum-severity RCE vulnerability
- **Cisco AsyncOS Email Security Appliances**: Email security infrastructure targeted by zero-day exploitation
- **ASUS Live Update**: Software update mechanism across ASUS hardware ecosystem
- **SonicWall SMA 100 Series**: Secure Mobile Access appliances used for remote connectivity
- **Fortinet Infrastructure**: Network security appliances with admin account targeting
- **Palo Alto Networks GlobalProtect**: VPN platform subject to credential spraying attacks
- **Cisco SSL VPN**: Remote access infrastructure targeted in automated campaigns
- **Gladinet CentreStack**: File server platform targeted by Clop ransomware operations
- **AWS EC2 and ECS**: Cloud infrastructure compromised for cryptocurrency mining operations

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unknown vulnerabilities in enterprise security infrastructure
- **Password Spraying**: Automated credential-based attacks against VPN gateways using common passwords
- **Credential Theft**: Compromise of AWS IAM credentials for cryptomining operations
- **QR Code Phishing**: Distribution of DocSwap Android malware via QR codes on phishing sites
- **Device Linking Abuse**: WhatsApp account hijacking through pairing code manipulation in GhostPairing campaigns
- **Windows Group Policy Manipulation**: LongNosedGoblin threat group using Group Policy for espionage malware deployment
- **Botnet Infrastructure**: Kimwolf botnet utilizing 1.8 million compromised Android TV devices for DDoS attacks
- **Malware Installation**: Physical installation of malware on maritime vessels for remote control capabilities

## Threat Actor Activities

- **UAT-9686 (China-nexus APT)**: Actively exploiting Cisco AsyncOS zero-day vulnerabilities in targeted attacks against email security infrastructure
- **LongNosedGoblin (China-aligned)**: Conducting espionage operations against governmental entities in Southeast Asia and Japan using Windows Group Policy for malware deployment
- **Clop Ransomware Gang**: Targeting Internet-exposed Gladinet CentreStack file servers in data theft extortion campaigns
- **Kimsuky (North Korean APT)**: Distributing DocSwap Android malware via QR phishing campaigns mimicking Seoul delivery applications
- **Prince of Persia (Iranian APT)**: Conducting surveillance operations against dissidents with advanced operational security and cryptographic C2 communications
- **North Korean Threat Actors**: Responsible for $2.02 billion in cryptocurrency theft in 2025, leading global crypto theft operations
- **Kimwolf Botnet Operators**: Controlling 1.8 million infected Android TV devices for large-scale DDoS attack capabilities