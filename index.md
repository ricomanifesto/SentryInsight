# Exploitation Report

Critical exploitation activity is surging across multiple attack vectors, with threat actors leveraging both newly disclosed vulnerabilities and sophisticated evasion techniques. Active exploitation includes a critical authentication bypass flaw in cPanel being mass-exploited for ransomware attacks, a Linux privilege escalation vulnerability enabling root access, and various zero-day activities targeting government and enterprise systems. Attackers are increasingly abusing legitimate services like Remote Monitoring and Management tools, cloud email services, and package repositories to evade detection while conducting large-scale phishing campaigns and credential theft operations.

## Active Exploitation Details

### Weaver E-cology Critical Vulnerability
- **Description**: Critical vulnerability in Weaver E-cology office automation system allowing attackers to execute discovery commands
- **Impact**: Enables reconnaissance and potential system compromise through command execution
- **Status**: Actively exploited in attacks since mid-March 2026
- **CVE ID**: CVE-2026-22679

### cPanel Authentication Bypass Flaw
- **Description**: Critical authentication bypass vulnerability affecting cPanel control panel software with multiple proof-of-concept exploits available
- **Impact**: Complete system compromise, website defacement, and ransomware deployment
- **Status**: Mass-exploited in "Sorry" ransomware attacks with claims of zero-day activity for at least one month
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Privilege Escalation
- **Description**: "Copy Fail" vulnerability affecting various Linux distributions enabling privilege escalation to root access
- **Impact**: Local privilege escalation allowing attackers to gain full system control
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog after active exploitation confirmed
- **CVE ID**: CVE-2026-31431

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation enterprise file transfer application
- **Impact**: Unauthorized access to file transfer systems and potential data exfiltration
- **Status**: Recently patched by Progress Software with critical severity rating

## Affected Systems and Products

- **Weaver E-cology**: Office automation systems compromised since March 2026
- **cPanel Control Panels**: Web hosting control panels targeted by government and MSP-focused threat actors
- **Linux Distributions**: Various distributions affected by Copy Fail vulnerability enabling root access
- **MOVEit Automation**: Enterprise managed file transfer applications with authentication bypass risks
- **PyTorch Lightning**: Malicious package on Python Package Index delivering credential stealers
- **Remote Monitoring Tools**: SimpleHelp and ScreenConnect RMM tools abused in phishing campaigns
- **Amazon SES**: Email service increasingly exploited for phishing bypassing security filters
- **Facebook Accounts**: 30,000 accounts compromised through Google AppSheet phishing relay
- **Telegram Mini Apps**: Platform abused for cryptocurrency scams and Android malware distribution

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of critical authentication flaws in enterprise applications
- **Privilege Escalation**: Linux kernel vulnerabilities exploited for root access within 24 hours of disclosure
- **Supply Chain Attacks**: Malicious packages distributed through legitimate software repositories
- **RMM Tool Abuse**: Legitimate remote management software used to establish persistent access across 80+ organizations
- **Phishing Relay**: Google AppSheet exploited as intermediary platform to evade email security filters
- **Cloud Service Abuse**: Amazon SES leveraged to send convincing phishing emails bypassing reputation filters
- **OAuth Manipulation**: ConsentFix v3 attacks using automated OAuth abuse to compromise Azure environments
- **Ransomware Deployment**: Mass exploitation of cPanel vulnerability for "Sorry" ransomware attacks

## Threat Actor Activities

- **Silver Fox APT**: China-based group deploying ABCDoor malware via tax-themed phishing targeting organizations in India and Russia with over 1,600 socially engineered messages
- **Unknown cPanel Attackers**: Threat actors targeting government, military entities in Southeast Asia, and managed service providers using critical cPanel vulnerabilities
- **Vietnamese Phishing Group**: Operation using Google AppSheet as phishing relay to compromise 30,000 Facebook accounts
- **Sorry Ransomware Operators**: Group mass-exploiting cPanel authentication bypass for website encryption and ransom demands
- **ShinyHunters**: Extortion gang claiming responsibility for Instructure educational platform data breach
- **North Korean Groups**: Responsible for 76% of all cryptocurrency stolen in 2026, leveraging AI-enhanced techniques for historic heists