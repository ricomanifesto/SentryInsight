# Exploitation Report

Critical vulnerabilities are currently under active exploitation across multiple platforms, with particularly concerning activity targeting enterprise infrastructure and gaming platforms. The most severe exploitation involves CVE-2026-22679, a critical remote code execution vulnerability in Weaver E-cology that has been actively exploited since March through debug API abuse. Additionally, threat actors are weaponizing CVE-2026-31431, a Linux privilege escalation flaw dubbed "Copy Fail," and CVE-2026-41940, a critical cPanel authentication bypass vulnerability that is being mass-exploited in ransomware campaigns. State-sponsored groups including North Korean ScarCruft and Chinese Silver Fox are conducting sophisticated supply chain attacks, while cybercriminals are leveraging legitimate services like Amazon SES and RMM tools to evade detection in widespread phishing campaigns.

## Active Exploitation Details

### Weaver E-cology RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in Weaver E-cology enterprise office automation platform exploitable through debug API
- **Impact**: Allows attackers to execute arbitrary commands and gain unauthorized access to enterprise systems
- **Status**: Under active exploitation since mid-March 2026, with discovery commands being executed against vulnerable systems
- **CVE ID**: CVE-2026-22679

### Linux Copy Fail Privilege Escalation
- **Description**: Security vulnerability affecting various Linux distributions that enables privilege escalation to root access
- **Impact**: Allows attackers to gain complete administrative control over compromised Linux systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### cPanel Authentication Bypass
- **Description**: Critical authentication bypass vulnerability affecting cPanel web hosting control panel software
- **Impact**: Enables complete compromise of hosting infrastructure and deployment of ransomware
- **Status**: Mass exploitation ongoing with "Sorry" ransomware attacks targeting compromised systems
- **CVE ID**: CVE-2026-41940

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation managed file transfer application
- **Impact**: Could allow unauthorized access to sensitive file transfer systems and data
- **Status**: Recently patched by Progress Software, potential for active exploitation given historical MOVEit targeting

## Affected Systems and Products

- **Weaver E-cology**: Enterprise office automation and collaboration platforms widely used in corporate environments
- **Linux Distributions**: Various Linux distributions affected by Copy Fail vulnerability, particularly targeting systems with vulnerable kernel components
- **cPanel Hosting Infrastructure**: Web hosting providers and managed service providers using cPanel control panels
- **Gaming Platforms**: Video game platforms compromised in ScarCruft supply chain attacks
- **PyTorch Lightning**: Python Package Index packages containing backdoored versions targeting developer environments
- **MOVEit Automation**: Enterprise managed file transfer systems used by organizations for secure file sharing
- **Amazon SES**: Simple Email Service being abused for phishing campaigns to bypass security filters
- **RMM Tools**: SimpleHelp and ScreenConnect remote monitoring and management platforms used in legitimate operations
- **Telegram Mini Apps**: Platform feature abused for cryptocurrency scams and Android malware distribution

## Attack Vectors and Techniques

- **Supply Chain Compromise**: ScarCruft trojanizing gaming platform components to deliver BirdCall malware across Android and Windows systems
- **Debug API Exploitation**: Weaver E-cology vulnerabilities exploited through exposed debug interfaces allowing remote command execution
- **Privilege Escalation**: Linux Copy Fail vulnerability used to escalate from user to root privileges on compromised systems
- **Authentication Bypass**: cPanel and MOVEit vulnerabilities allowing complete bypass of authentication mechanisms
- **Phishing with Legitimate Services**: Amazon SES abuse to send convincing phishing emails that bypass reputation-based security filters
- **RMM Tool Abuse**: Legitimate remote monitoring tools used to establish persistent remote access after initial compromise
- **Package Repository Poisoning**: Backdoored PyTorch Lightning packages delivering credential stealers through trusted repositories
- **OAuth Abuse Automation**: ConsentFix v3 attacks targeting Azure environments with automated OAuth consent abuse techniques
- **Ransomware Deployment**: Mass exploitation of cPanel vulnerabilities followed by "Sorry" ransomware encryption
- **Tax-Themed Social Engineering**: Silver Fox using seasonal tax themes to deliver ABCDoor backdoor and ValleyRAT malware

## Threat Actor Activities

- **ScarCruft (North Korean APT)**: Conducting supply chain attacks against gaming platforms to deploy cross-platform BirdCall malware targeting both Android and Windows users
- **Silver Fox (Chinese APT)**: Targeting organizations in Russia and India with tax-themed phishing campaigns delivering previously undocumented ABCDoor backdoor and ValleyRAT malware
- **Sorry Ransomware Operators**: Mass-exploiting critical cPanel authentication bypass vulnerability to deploy ransomware across hosting infrastructure
- **Unknown Southeast Asian Threat Actor**: Targeting government, military entities, and managed service providers using weaponized cPanel vulnerabilities
- **ShinyHunters Extortion Gang**: Claiming responsibility for Instructure data breach affecting educational technology systems
- **Multiple Cybercriminal Groups**: Conducting large-scale phishing campaigns targeting over 35,000 users across 26 countries using code of conduct-themed lures and legitimate email services
- **RMM-Based Attack Campaign**: Targeting over 80 organizations since April 2025 using legitimate SimpleHelp and ScreenConnect tools for persistent access
- **Cryptocurrency Fraud Networks**: Operating large-scale scam operations through Telegram Mini Apps, with recent international crackdowns arresting 276 suspects and seizing $701 million