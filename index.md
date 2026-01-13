# Exploitation Report

The current threat landscape reveals several critical exploitation activities spanning zero-day vulnerabilities, social engineering attacks, and sophisticated supply chain compromises. Most notably, CISA has ordered federal agencies to patch a high-severity Gogs vulnerability that was actively exploited in zero-day attacks, while threat actors are increasingly leveraging advanced social engineering techniques like browser-in-browser attacks to steal credentials. Additionally, multiple supply chain attacks targeting development platforms and a maximum-severity vulnerability affecting nearly 60,000 n8n instances highlight the persistent risks to automation and workflow platforms.

## Active Exploitation Details

### Gogs Remote Code Execution Vulnerability
- **Description**: A high-severity remote code execution vulnerability in the Gogs Git service platform
- **Impact**: Allows attackers to achieve remote code execution on vulnerable systems
- **Status**: Actively exploited in zero-day attacks; CISA has mandated federal agencies to patch their systems

### Ni8mare Vulnerability in n8n Workflow Platform
- **Description**: A maximum-severity vulnerability affecting n8n workflow automation instances
- **Impact**: Critical security compromise of workflow automation systems
- **Status**: Nearly 60,000 n8n instances remain unpatched and vulnerable to exploitation

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi hypervisor platform
- **Impact**: Allows attackers to escape virtual machine isolation and compromise hypervisor systems
- **Status**: Actively exploited by Chinese-speaking threat actors, potentially developed years ago

### Instagram Password Reset Bug
- **Description**: A vulnerability allowing mass-requesting of password reset emails
- **Impact**: Enabled threat actors to scrape data from over 17 million Instagram accounts
- **Status**: Fixed by Instagram, but data was already extracted and leaked online

## Affected Systems and Products

- **Gogs Git Service**: Self-hosted Git service installations vulnerable to remote code execution
- **n8n Workflow Platform**: Nearly 60,000 publicly exposed instances affected by maximum-severity vulnerability
- **VMware ESXi**: Hypervisor systems vulnerable to virtual machine escape exploits
- **Instagram**: Social media platform affected by password reset exploitation leading to mass data scraping
- **SonicWall VPN**: Used as initial access vector in VMware ESXi exploitation campaigns
- **Telegram**: Proxy link functionality exposing user IP addresses through malicious links
- **Target Corporation**: Development servers compromised with source code theft claims
- **University of Hawaii Cancer Center**: Ransomware attack affecting systems and data from 1990s onwards

## Attack Vectors and Techniques

- **Browser-in-Browser (BitB) Attacks**: Sophisticated social engineering technique mimicking legitimate browser windows to steal Facebook credentials
- **Supply Chain Poisoning**: Malicious npm packages masquerading as n8n integrations to steal OAuth tokens from developers
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Gogs and VMware ESXi systems
- **QR Code Phishing (Quishing)**: North Korean APT using QR codes in spear-phishing campaigns targeting government and academic institutions
- **Credential Brute-Forcing**: GoBruteforcer botnet targeting cryptocurrency project databases with weak authentication
- **Spear-Phishing**: Targeted email campaigns delivering malware such as RustyWater RAT
- **Game Service Exploitation**: Character hijacking in Apex Legends live matches through unknown vulnerabilities
- **Proxy Link Manipulation**: Exploitation of Telegram proxy handling to reveal user IP addresses

## Threat Actor Activities

- **Chinese-Speaking Groups**: Exploiting VMware ESXi zero-days using compromised SonicWall VPN appliances as initial access vectors
- **North Korean APT (Kimsuky)**: Conducting quishing attacks against US and foreign government agencies, NGOs, and academic institutions using QR code-embedded phishing emails
- **Iranian MuddyWater APT**: Launching spear-phishing campaigns with RustyWater RAT targeting diplomatic, maritime, financial, and telecom entities across the Middle East
- **Russian APT28**: Running credential-stealing campaigns targeting Turkish energy and nuclear research agencies, as well as strategic policy organizations
- **GoBruteforcer Operators**: Targeting cryptocurrency and blockchain project databases to build botnet infrastructure for password brute-forcing attacks
- **Black Axe Criminal Organization**: 34 members arrested in Spain for organized fraud schemes totaling €5.9 million
- **Unknown Ransomware Group**: Breached University of Hawaii Cancer Center, stealing participant data including historical records with Social Security numbers