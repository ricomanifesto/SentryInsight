# Exploitation Report

Multiple critical vulnerabilities are currently under active exploitation by sophisticated threat actors across various platforms and infrastructure components. The most significant threats include a zero-day flaw in Cisco AsyncOS Email Security Appliances being exploited by China-nexus APT group UAT-9686, a maximum-severity remote code execution vulnerability in HPE OneView software, and actively exploited vulnerabilities in SonicWall SMA appliances. Additionally, CISA has flagged critical flaws in ASUS Live Update and Fortinet systems based on evidence of active exploitation, while North Korea-linked groups continue their cryptocurrency theft operations totaling $2.02 billion in 2025.

## Active Exploitation Details

### Cisco AsyncOS Email Security Zero-Day
- **Description**: Maximum-severity zero-day vulnerability in Cisco AsyncOS software for Email Security Appliances
- **Impact**: Enables complete compromise of email security infrastructure by China-nexus threat actors
- **Status**: Currently being exploited in the wild with no patch available
- **CVE ID**: No specific CVE mentioned in the available information

### SonicWall SMA 100 Series Vulnerability
- **Description**: Critical security flaw in Secure Mobile Access (SMA) 100 series appliances
- **Impact**: Allows unauthorized access to secure network infrastructure
- **Status**: Actively exploited in the wild, patch now available
- **CVE ID**: CVE-2025-40602

### HPE OneView Remote Code Execution
- **Description**: Maximum-severity vulnerability in HPE OneView Software enabling unauthenticated remote code execution
- **Impact**: Complete system compromise with arbitrary code execution capabilities
- **Status**: Recently patched by HPE, CVSS score of 10.0

### ASUS Live Update Critical Flaw
- **Description**: Critical vulnerability in ASUS Live Update software
- **Impact**: System compromise through software update mechanism
- **Status**: Added to CISA KEV catalog due to evidence of active exploitation

### Fortinet Infrastructure Vulnerabilities
- **Description**: Critical vulnerabilities in Fortinet systems targeting administrative accounts
- **Impact**: Attackers can export device configurations including hashed credentials and sensitive information
- **Status**: Under active attack with focus on credential harvesting

## Affected Systems and Products

- **Cisco Email Security Appliances**: AsyncOS software running on email security infrastructure
- **SonicWall SMA 100 Series**: Secure Mobile Access appliances used for VPN and secure remote access
- **HPE OneView Software**: Infrastructure management platform for server and storage systems
- **ASUS Live Update**: Software update mechanism for ASUS devices
- **Fortinet Systems**: Network security appliances with administrative access
- **Gladinet CentreStack**: Internet-exposed file servers targeted by Clop ransomware
- **VPN Gateways**: Palo Alto Networks GlobalProtect and Cisco SSL VPN platforms
- **AWS Infrastructure**: EC2 and ECS services targeted in cryptocurrency mining campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Cisco AsyncOS vulnerability being exploited before patches are available
- **Credential-Based Attacks**: Password spraying campaigns targeting VPN gateways and administrative accounts
- **Supply Chain Attacks**: Targeting software update mechanisms like ASUS Live Update
- **Social Engineering**: WhatsApp device linking abuse for account hijacking through GhostPairing campaign
- **QR Code Phishing**: Distribution of DocSwap Android malware via malicious QR codes
- **Configuration Export**: Exploitation of administrative access to extract sensitive device configurations
- **Cryptomining Deployment**: Use of compromised AWS credentials to deploy cryptocurrency mining operations

## Threat Actor Activities

- **UAT-9686 (China-nexus APT)**: Actively exploiting Cisco AsyncOS zero-day vulnerability in targeted attacks against email security infrastructure
- **LongNosedGoblin (China-aligned)**: Using Windows Group Policy to deploy espionage malware targeting governmental entities in Southeast Asia and Japan
- **Clop Ransomware Group**: Targeting Gladinet CentreStack file servers in data theft extortion campaigns
- **North Korea-linked Groups**: Leading global cryptocurrency theft with $2.02 billion stolen in 2025 through various attack methods
- **Kimsuky (North Korean APT)**: Distributing DocSwap Android malware via QR phishing campaigns mimicking delivery applications
- **Prince of Persia (Iranian APT)**: Continuing surveillance operations against dissidents with advanced operational security measures
- **Automated Campaign Operators**: Conducting widespread password spraying attacks against Cisco and Palo Alto Networks VPN gateways