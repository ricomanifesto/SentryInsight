# Exploitation Report

Critical zero-day vulnerabilities are being actively exploited across multiple enterprise platforms, with threat actors targeting SonicWall SMA devices, Cisco AsyncOS email security appliances, and ASUS Live Update software. China-aligned threat groups are leading sophisticated campaigns while North Korean actors have stolen over $2 billion in cryptocurrency through various attack vectors. The exploitation landscape shows a concerning trend of chaining multiple vulnerabilities and targeting enterprise infrastructure through credential-based attacks and supply chain compromises.

## Active Exploitation Details

### SonicWall SMA 100 Series Zero-Day
- **Description**: Critical vulnerability in Secure Mobile Access (SMA) 100 series appliances being actively exploited by threat actors
- **Impact**: Attackers can chain this zero-day with previously disclosed critical vulnerabilities for complete device compromise
- **Status**: Actively exploited in the wild, patches have been released
- **CVE ID**: CVE-2025-40602

### Cisco AsyncOS Email Security Zero-Day
- **Description**: Maximum-severity zero-day flaw in Cisco AsyncOS software for email security appliances
- **Impact**: Complete compromise of email security infrastructure, allowing attackers to bypass email protections
- **Status**: Actively exploited by China-nexus APT actor UAT-9686, currently unpatched
- **CVE ID**: Not specified in articles

### ASUS Live Update Critical Flaw
- **Description**: Critical vulnerability in ASUS Live Update software added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: System compromise through software update mechanism abuse
- **Status**: Evidence of active exploitation confirmed by CISA

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity security flaw in HPE OneView Software rated CVSS 10.0
- **Impact**: Unauthenticated remote code execution allowing complete system takeover
- **Status**: Patched by HPE, critical severity requiring immediate attention

### Fortinet Critical Vulnerabilities
- **Description**: Multiple critical flaws in Fortinet products under active attack
- **Impact**: Attackers targeting admin accounts to export device configurations including hashed credentials and sensitive information
- **Status**: Under active exploitation

## Affected Systems and Products

- **SonicWall SMA 100 Series**: Edge Access devices and Secure Mobile Access appliances
- **Cisco AsyncOS**: Email Security Appliances running AsyncOS software
- **ASUS Live Update**: Software update mechanism on ASUS systems
- **HPE OneView**: Infrastructure management software across HPE environments
- **Fortinet Products**: Network security appliances and management systems
- **Gladinet CentreStack**: Internet-exposed file servers targeted by ransomware
- **Android Devices**: 1.8 million Android TVs, set-top boxes, and tablets compromised by Kimwolf botnet
- **AWS Infrastructure**: EC2 and ECS services targeted in cryptomining campaigns
- **VPN Gateways**: Palo Alto Networks GlobalProtect and Cisco SSL VPN platforms

## Attack Vectors and Techniques

- **Zero-Day Chaining**: Combining new zero-days with previously disclosed critical vulnerabilities for maximum impact
- **Password Spraying**: Automated credential-based attacks targeting VPN platforms
- **Supply Chain Attacks**: Compromising software update mechanisms and legitimate applications
- **QR Code Phishing**: Distribution of Android malware through QR codes on phishing sites
- **Device Linking Abuse**: Hijacking WhatsApp accounts through legitimate pairing code features
- **Credential Stuffing**: Using compromised AWS credentials for cryptomining operations
- **Windows Group Policy Abuse**: Deploying espionage malware through legitimate system administration tools
- **Botnet Operations**: Large-scale DDoS attacks using compromised IoT devices

## Threat Actor Activities

- **UAT-9686 (China-nexus APT)**: Actively exploiting Cisco AsyncOS zero-day in targeted attacks against email security infrastructure
- **LongNosedGoblin (China-aligned)**: Using Windows Group Policy to deploy espionage malware against governmental entities in Southeast Asia and Japan
- **Clop Ransomware**: Targeting Gladinet CentreStack file servers in data theft extortion campaigns
- **Kimsuky (North Korea)**: Distributing DocSwap Android malware via QR phishing campaigns posing as delivery applications
- **Prince of Persia (Iran APT)**: Continuing surveillance operations against dissidents with advanced operational security
- **North Korean Threat Actors**: Responsible for $2.02 billion in cryptocurrency theft in 2025, leading global crypto crime statistics
- **Kimwolf Botnet Operators**: Managing 1.8 million compromised Android devices for large-scale DDoS operations