# Exploitation Report

The cybersecurity landscape is experiencing intense exploitation activity across multiple attack vectors, with several critical vulnerabilities being actively exploited in the wild. The most severe incidents include mass exploitation of a critical cPanel authentication bypass vulnerability (CVE-2026-41940) being leveraged for "Sorry" ransomware attacks, active exploitation of the "Copy Fail" Linux vulnerability (CVE-2026-31431) that enables root access, and ongoing attacks against Weaver E-cology systems (CVE-2026-22679). Additionally, sophisticated phishing campaigns are abusing legitimate services like Amazon SES and RMM tools to evade detection, while supply chain attacks target PyTorch Lightning packages and threat actors exploit MOVEit Automation vulnerabilities for authentication bypass.

## Active Exploitation Details

### cPanel Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in cPanel web hosting control panel software that allows unauthorized access
- **Impact**: Complete system compromise, website defacement, data encryption in ransomware attacks, targeting of government and MSP networks
- **Status**: Currently being mass-exploited by multiple threat actors including "Sorry" ransomware operators
- **CVE ID**: CVE-2026-41940

### Copy Fail Linux Root Access Vulnerability  
- **Description**: Security flaw in various Linux distributions that allows privilege escalation to root access
- **Impact**: Complete system compromise, unauthorized root-level access to Linux systems
- **Status**: Added to CISA KEV catalog after confirmation of active exploitation one day after public disclosure
- **CVE ID**: CVE-2026-31431

### Weaver E-cology Office Automation Vulnerability
- **Description**: Critical vulnerability in Weaver E-cology office automation platform allowing remote code execution
- **Impact**: Unauthorized system access, execution of discovery commands, potential data theft
- **Status**: Actively exploited since mid-March 2026
- **CVE ID**: CVE-2026-22679

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation enterprise file transfer application
- **Impact**: Unauthorized access to file transfer systems, potential data exfiltration
- **Status**: Recently patched by Progress Software, exploitation status being monitored

## Affected Systems and Products

- **cPanel Web Hosting Control Panel**: Widely deployed web hosting management software affecting millions of websites
- **Linux Distributions**: Various Linux distributions vulnerable to Copy Fail privilege escalation
- **Weaver E-cology**: Office automation platforms used by enterprise organizations
- **MOVEit Automation**: Enterprise-grade managed file transfer applications
- **PyTorch Lightning**: Python machine learning framework packages on PyPI repository
- **Amazon Simple Email Service (SES)**: Cloud email delivery service being abused for phishing
- **Remote Monitoring Tools**: SimpleHelp and ScreenConnect RMM software being weaponized
- **Facebook Accounts**: Over 30,000 accounts compromised via Google AppSheet phishing
- **Telegram Mini Apps**: Platform being abused for crypto scams and malware delivery

## Attack Vectors and Techniques

- **Authentication Bypass Exploitation**: Direct exploitation of authentication flaws in web applications and file transfer systems
- **Privilege Escalation**: Exploiting Linux kernel vulnerabilities to gain root access
- **Supply Chain Compromise**: Backdoored packages distributed through legitimate software repositories
- **Phishing via Legitimate Services**: Abuse of Amazon SES, Google AppSheet, and Telegram Mini Apps to evade detection
- **RMM Tool Weaponization**: Leveraging legitimate remote management software for persistent access
- **Ransomware Deployment**: Mass exploitation followed by data encryption and extortion
- **Social Engineering**: Tax-themed phishing campaigns targeting specific geographic regions
- **OAuth Abuse**: Automated ConsentFix v3 attacks targeting Azure environments

## Threat Actor Activities

- **Sorry Ransomware Group**: Mass-exploiting cPanel vulnerabilities for website encryption and extortion campaigns
- **Silver Fox (China-backed APT)**: Conducting tax-themed phishing campaigns targeting organizations in India and Russia using ABCDoor malware, ValleyRAT, and previously undocumented tools
- **Unknown Southeast Asian Threat Actor**: Targeting government, military, and MSP networks using weaponized cPanel exploits
- **Vietnamese-linked Operation**: Compromising over 30,000 Facebook accounts through Google AppSheet phishing relay campaigns
- **ShinyHunters Extortion Gang**: Claiming responsibility for data breach at educational technology company Instructure
- **Multi-vector Phishing Campaign**: Targeting 80+ organizations using legitimate RMM tools for persistent remote access since April 2025
- **Supply Chain Attackers**: Distributing malicious PyTorch Lightning packages with credential-stealing payloads targeting cloud services and browsers