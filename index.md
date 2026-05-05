# Exploitation Report

Current cybersecurity landscape shows intense exploitation activity across multiple fronts, with several critical vulnerabilities being actively exploited in the wild. The most concerning developments include mass exploitation of a critical cPanel authentication bypass flaw being used in ransomware campaigns, active exploitation of the Linux "Copy Fail" vulnerability for root access escalation, and ongoing attacks against Weaver E-cology office automation systems. Additionally, sophisticated phishing campaigns are leveraging legitimate services like Amazon SES, Google AppSheet, and RMM tools to evade detection, while threat actors continue to exploit trusted platforms for credential theft and malware distribution.

## Active Exploitation Details

### Weaver E-cology Critical Vulnerability
- **Description**: Critical vulnerability in Weaver E-cology office automation system allowing attackers to execute discovery commands
- **Impact**: Enables unauthorized access and reconnaissance within enterprise environments
- **Status**: Actively exploited since mid-March 2026
- **CVE ID**: CVE-2026-22679

### cPanel Authentication Bypass Flaw
- **Description**: Critical authentication bypass vulnerability in cPanel web hosting control panel
- **Impact**: Complete system compromise allowing attackers to deploy ransomware and encrypt data
- **Status**: Mass-exploited in "Sorry" ransomware attacks, with proof-of-concept exploits publicly available
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Vulnerability
- **Description**: Security flaw affecting various Linux distributions enabling privilege escalation
- **Impact**: Allows attackers to gain root access to compromised Linux systems
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog, actively exploited in the wild
- **CVE ID**: CVE-2026-31431

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress Software's MOVEit Automation managed file transfer application
- **Impact**: Potential unauthorized access to file transfer systems and sensitive data
- **Status**: Recently patched by Progress Software, customers warned to apply updates immediately

## Affected Systems and Products

- **Weaver E-cology**: Office automation systems vulnerable to command execution attacks
- **cPanel**: Web hosting control panels across government, MSP, and hosting provider networks
- **Linux Distributions**: Various distributions affected by Copy Fail privilege escalation vulnerability
- **MOVEit Automation**: Enterprise managed file transfer applications
- **PyTorch Lightning Package**: Backdoored version distributed via Python Package Index (PyPI)
- **Facebook Accounts**: Over 30,000 accounts compromised via Google AppSheet phishing relay
- **SimpleHelp and ScreenConnect**: RMM tools abused in legitimate software-based attacks
- **Amazon SES**: Increasingly exploited for phishing email distribution
- **Telegram Mini Apps**: Platform abused for crypto scams and Android malware delivery

## Attack Vectors and Techniques

- **Authentication Bypass Exploitation**: Direct exploitation of cPanel and MOVEit authentication flaws
- **Privilege Escalation**: Linux Copy Fail vulnerability used for root access
- **Supply Chain Attacks**: Backdoored PyTorch Lightning package delivering credential stealers
- **RMM Tool Abuse**: Legitimate remote management software used for persistent access
- **Phishing Relay Attacks**: Google AppSheet used as intermediary for Facebook account theft
- **Email Service Abuse**: Amazon SES leveraged to bypass security filters
- **Social Engineering**: Tax-themed phishing campaigns targeting organizations in India and Russia
- **OAuth Abuse**: ConsentFix v3 attacks using automated Azure OAuth exploitation
- **Platform Exploitation**: Telegram Mini Apps abused for crypto fraud and malware distribution

## Threat Actor Activities

- **Silver Fox (China-backed APT)**: Conducting tax-themed phishing campaigns targeting organizations in India and Russia, deploying ABCDoor backdoor, ValleyRAT, and other malware through over 1,600 socially engineered messages
- **Sorry Ransomware Operators**: Mass-exploiting cPanel vulnerability to encrypt victim data and deploy ransomware payloads
- **Vietnamese-linked Operation**: Using Google AppSheet phishing relay to compromise over 30,000 Facebook accounts
- **ShinyHunters Extortion Gang**: Claiming responsibility for Instructure educational technology company data breach
- **Unknown Government Targeting Group**: Exploiting cPanel vulnerability to specifically target government, military, and MSP networks in Southeast Asia
- **RMM-based Campaign Operators**: Targeting over 80 organizations using legitimate SimpleHelp and ScreenConnect tools for persistent access
- **PyPI Package Attackers**: Distributing backdoored Python packages targeting browser credentials, environment files, and cloud services