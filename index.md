# Exploitation Report

Critical exploitation activity is currently centered around multiple zero-day and recently patched vulnerabilities across various platforms. The most severe threats include active exploitation of a critical cPanel authentication bypass vulnerability (CVE-2026-41940) being mass-exploited in "Sorry" ransomware attacks, and a Linux privilege escalation flaw (CVE-2026-31431) known as "Copy Fail" that CISA has confirmed is being exploited to gain root access. Additionally, threat actors are leveraging legitimate services like RMM tools and cloud platforms for sophisticated phishing campaigns, while supply chain attacks target software repositories and developer environments.

## Active Exploitation Details

### cPanel Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in cPanel that allows unauthorized access to control panels
- **Impact**: Complete system compromise, data encryption in ransomware attacks, unauthorized administrative access
- **Status**: Actively exploited in mass attacks, patches available but widespread exploitation continues
- **CVE ID**: CVE-2026-41940

### Linux "Copy Fail" Privilege Escalation
- **Description**: Security vulnerability in Linux distributions that enables privilege escalation to root access
- **Impact**: Full system compromise, root-level access to affected Linux systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation enterprise file transfer application
- **Impact**: Unauthorized access to file transfer systems, potential data exfiltration
- **Status**: Recently patched by Progress Software, exploitation status being monitored

## Affected Systems and Products

- **cPanel Control Panels**: Web hosting control panels vulnerable to authentication bypass attacks
- **Linux Distributions**: Multiple Linux distributions affected by privilege escalation vulnerability
- **MOVEit Automation**: Enterprise-grade managed file transfer applications
- **PyTorch Lightning Package**: Malicious version published on Python Package Index (PyPI)
- **Remote Monitoring and Management (RMM) Tools**: SimpleHelp and ScreenConnect being abused for persistent access
- **Amazon SES**: Email service being abused for phishing campaigns
- **Telegram Mini Apps**: Platform being exploited for crypto scams and malware delivery
- **Facebook Accounts**: Over 30,000 accounts compromised through Google AppSheet phishing
- **Azure OAuth Services**: Targeted by automated ConsentFix v3 attacks

## Attack Vectors and Techniques

- **RMM Tool Abuse**: Attackers leveraging legitimate SimpleHelp and ScreenConnect tools to establish persistent remote access while evading detection
- **Supply Chain Attacks**: Backdoored PyTorch Lightning package distributing credential-stealing malware targeting browsers and cloud services
- **Phishing as a Service**: Google AppSheet being used as phishing relay infrastructure to compromise Facebook accounts
- **Ransomware Deployment**: "Sorry" ransomware being deployed through exploited cPanel vulnerabilities
- **OAuth Abuse**: ConsentFix v3 attacks using automated techniques to abuse Azure OAuth mechanisms
- **Tax-Themed Social Engineering**: Phishing campaigns using tax-related lures to deploy ABCDoor backdoor and ValleyRAT
- **Cloud Service Abuse**: Amazon SES being leveraged to bypass email security filters in phishing campaigns

## Threat Actor Activities

- **Silver Fox APT Group**: China-backed group conducting tax-themed phishing campaigns targeting organizations in India and Russia, deploying ABCDoor backdoor, ValleyRAT, and other malware tools
- **Vietnamese Threat Actors**: Operating sophisticated phishing campaigns using Google AppSheet infrastructure to compromise over 30,000 Facebook accounts
- **Unknown Threat Actor**: Targeting government, military entities in Southeast Asia, and MSPs using critical cPanel vulnerability for network infiltration
- **ShinyHunters Extortion Gang**: Claimed responsibility for data breach at educational technology company Instructure
- **North Korean APT Groups**: Responsible for 76% of all cryptocurrency theft in 2026, utilizing AI-assisted attack techniques
- **Ransomware Operators**: Mass-exploiting cPanel vulnerabilities to deploy "Sorry" ransomware across multiple websites and systems