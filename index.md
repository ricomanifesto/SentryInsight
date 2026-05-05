# Exploitation Report

The current threat landscape reveals intense exploitation activity targeting critical infrastructure and enterprise systems. The most significant threats include active exploitation of a critical cPanel authentication bypass vulnerability (CVE-2026-41940) being mass-exploited in "Sorry" ransomware attacks, and the Linux "Copy Fail" vulnerability (CVE-2026-31431) that CISA has added to its Known Exploited Vulnerabilities catalog after confirming active exploitation for privilege escalation. Additional concerning activity includes ongoing exploitation of a Weaver E-cology office automation vulnerability (CVE-2026-22679) since March, sophisticated phishing campaigns leveraging legitimate RMM tools, and supply chain attacks through backdoored Python packages.

## Active Exploitation Details

### cPanel Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in cPanel web hosting control panel software allowing unauthorized access
- **Impact**: Complete system compromise, mass exploitation for "Sorry" ransomware deployment, targeting of millions of websites
- **Status**: Actively exploited in widespread attacks with proof-of-concept exploits publicly available
- **CVE ID**: CVE-2026-41940

### Linux Copy Fail Privilege Escalation
- **Description**: Security vulnerability in Linux systems allowing privilege escalation to root access
- **Impact**: Complete system compromise, root-level access on affected Linux distributions
- **Status**: Actively exploited in the wild according to CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### Weaver E-cology Office Automation Vulnerability
- **Description**: Critical vulnerability in Weaver E-cology office automation platform
- **Impact**: Unauthorized access and execution of discovery commands on corporate systems
- **Status**: Actively exploited since mid-March 2026
- **CVE ID**: CVE-2026-22679

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation enterprise file transfer application
- **Impact**: Unauthorized access to managed file transfer systems and sensitive data
- **Status**: Recently patched by Progress Software, potential for active exploitation

## Affected Systems and Products

- **cPanel Web Hosting Control Panels**: Millions of websites using cPanel infrastructure globally
- **Linux Distributions**: Various Linux systems vulnerable to Copy Fail privilege escalation
- **Weaver E-cology**: Office automation platforms in corporate environments
- **Progress MOVEit Automation**: Enterprise managed file transfer applications
- **PyTorch Lightning Package**: Python developers using compromised package from PyPI
- **Facebook Accounts**: Over 30,000 accounts compromised via Google AppSheet phishing
- **Government and Military Networks**: Southeast Asian entities targeted via cPanel exploitation
- **Managed Service Providers**: MSP networks targeted in multiple campaigns
- **Amazon SES**: Email service increasingly abused for phishing campaigns

## Attack Vectors and Techniques

- **Authentication Bypass Exploitation**: Direct exploitation of cPanel and MOVEit authentication flaws for unauthorized access
- **Privilege Escalation**: Linux Copy Fail vulnerability exploited for root access elevation
- **RMM Tool Abuse**: Legitimate SimpleHelp and ScreenConnect tools used for persistent remote access in phishing campaigns
- **Supply Chain Attacks**: Backdoored PyTorch Lightning package delivering credential-stealing malware
- **Phishing Relay Techniques**: Google AppSheet used as intermediary to bypass detection in Facebook account compromise
- **Email Service Abuse**: Amazon SES leveraged to send convincing phishing emails that evade standard filters
- **Tax-Themed Social Engineering**: Malicious campaigns using tax season themes to deliver ABCDoor backdoor and ValleyRAT
- **OAuth Abuse**: ConsentFix v3 attacks targeting Azure environments with automated OAuth exploitation

## Threat Actor Activities

- **Unknown Threat Actor**: Targeting government and military entities in Southeast Asia using cPanel vulnerability exploitation
- **Sorry Ransomware Group**: Mass exploitation of cPanel flaw for ransomware deployment across multiple websites
- **Silver Fox (China-based APT)**: Deploying ABCDoor malware via tax-themed phishing campaigns targeting organizations in Russia and India
- **Vietnamese-linked Operation**: Compromising over 30,000 Facebook accounts using Google AppSheet as phishing relay
- **ShinyHunters Extortion Gang**: Claiming responsibility for Instructure data breach affecting educational technology platform
- **Multi-vector Phishing Operators**: Targeting 80+ organizations using legitimate RMM tools for persistent access since April 2025
- **Supply Chain Attackers**: Publishing malicious PyTorch Lightning packages targeting developers and cloud services
- **ConsentFix v3 Operators**: Automated OAuth abuse campaigns targeting Azure environments with scaling capabilities