# Exploitation Report

Current threat landscape reveals several critical vulnerabilities under active exploitation, with attackers leveraging both newly disclosed flaws and established attack vectors. Most notably, the "Copy Fail" Linux vulnerability (CVE-2026-31431) has been added to CISA's Known Exploited Vulnerabilities catalog just one day after public disclosure, indicating rapid weaponization by threat actors. Additionally, a critical cPanel authentication bypass flaw (CVE-2026-41940) is being mass-exploited in "Sorry" ransomware campaigns targeting websites globally. Chinese-backed APT groups continue sophisticated campaigns using tax-themed phishing to deploy previously undocumented malware, while various threat actors exploit normal business processes and OAuth mechanisms for unauthorized access.

## Active Exploitation Details

### Copy Fail Linux Root Access Vulnerability
- **Description**: A security flaw affecting various Linux distributions that allows attackers to gain root access to systems
- **Impact**: Complete system compromise and root-level privileges on affected Linux systems
- **Status**: Actively exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### cPanel Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in cPanel web hosting control panel software
- **Impact**: Complete compromise of web hosting environments, data encryption in ransomware attacks
- **Status**: Mass exploitation ongoing in "Sorry" ransomware campaigns targeting websites
- **CVE ID**: CVE-2026-41940

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress Software's MOVEit Automation enterprise managed file transfer application
- **Impact**: Unauthorized access to sensitive file transfer systems and data
- **Status**: Critical vulnerability requiring immediate patching; exploitation potential high given MOVEit's history of being targeted

## Affected Systems and Products

- **Linux Distributions**: Various distributions affected by Copy Fail vulnerability enabling root access
- **cPanel Web Hosting**: Control panel software targeted in mass ransomware exploitation campaigns
- **MOVEit Automation**: Enterprise managed file transfer application with critical authentication bypass flaw
- **Windows Systems**: April 2026 security updates causing backup failures due to vulnerable driver blocking
- **Facebook Accounts**: Over 30,000 accounts compromised via Google AppSheet phishing campaigns
- **Azure Environments**: Targeted by ConsentFix v3 automated OAuth abuse attacks

## Attack Vectors and Techniques

- **Tax-Themed Phishing**: China-backed Silver Fox APT group using over 1,600 socially engineered messages to deliver ABCDoor backdoor and ValleyRAT
- **Google AppSheet Phishing Relay**: Vietnamese threat actors using Google's low-code platform to distribute phishing emails targeting Facebook accounts
- **OAuth Abuse**: ConsentFix v3 attacks targeting Azure with automated OAuth consent manipulation
- **Telegram Mini Apps Abuse**: Large-scale fraud operation using Telegram's Mini App feature for crypto scams and Android malware distribution
- **Vishing and SSO Abuse**: Cybercrime groups conducting rapid SaaS extortion attacks with minimal traces
- **Structured Loan Fraud**: Fraudsters exploiting normal credit union business processes using stolen identities

## Threat Actor Activities

- **Silver Fox (China-backed APT)**: Conducting extensive tax-themed phishing campaigns targeting organizations in India and Russia with new ABCDoor malware, ValleyRAT, and over 1,600 socially engineered messages
- **Unknown cPanel Threat Actor**: Targeting government and military entities in Southeast Asia, MSPs, and hosting providers using weaponized cPanel vulnerabilities
- **Vietnamese Phishing Group**: Compromising 30,000+ Facebook accounts using Google AppSheet as phishing relay infrastructure
- **Sorry Ransomware Operators**: Mass-exploiting cPanel authentication bypass vulnerability for website encryption attacks
- **China-Aligned Espionage Groups**: Targeting government and defense sectors across South, East, and Southeast Asia, plus European government entities
- **North Korean Groups**: Responsible for 76% of all cryptocurrency stolen in 2026, conducting historic heists with potential AI assistance
- **ShinyHunters Extortion Gang**: Claiming responsibility for Instructure data breach affecting educational technology platforms