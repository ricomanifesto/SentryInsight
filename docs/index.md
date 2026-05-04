# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure with several high-impact vulnerabilities being actively weaponized. The most severe threats include the "Copy Fail" Linux privilege escalation vulnerability being exploited for root access across various Linux distributions, a critical cPanel authentication bypass flaw being mass-exploited in "Sorry" ransomware campaigns, and a MOVEit Automation authentication bypass vulnerability affecting enterprise file transfer systems. Threat actors are also leveraging sophisticated techniques including automated OAuth abuse against Azure environments, tax-themed phishing campaigns deploying ABCDoor malware, and large-scale Facebook account compromises through Google AppSheet phishing relays. These exploitation campaigns demonstrate a concerning trend toward rapid, high-impact attacks that target both government entities and critical infrastructure providers.

## Active Exploitation Details

### Copy Fail Linux Privilege Escalation
- **Description**: A critical security vulnerability affecting various Linux distributions that allows attackers to gain root access to compromised systems
- **Impact**: Complete system compromise with root-level privileges, enabling full control over affected Linux systems
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### Critical cPanel Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in cPanel that is being mass-exploited by threat actors
- **Impact**: Unauthorized access to web hosting control panels, leading to website compromise and data encryption in ransomware attacks
- **Status**: Actively exploited in "Sorry" ransomware campaigns targeting websites
- **CVE ID**: CVE-2026-41940

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress Software's MOVEit Automation enterprise managed file transfer application
- **Impact**: Unauthorized access to enterprise file transfer systems, potential data theft and system compromise
- **Status**: Recently disclosed, patch available from Progress Software

### cPanel Government and MSP Targeting
- **Description**: Previously unknown threat actors exploiting a critical cPanel vulnerability to target government and military entities in Southeast Asia
- **Impact**: Compromise of government networks, military systems, and managed service provider infrastructure
- **Status**: Active targeting campaign against high-value government and MSP networks

## Affected Systems and Products

- **MOVEit Automation**: Enterprise-grade managed file transfer application by Progress Software
- **Linux Distributions**: Various Linux distributions affected by the Copy Fail vulnerability
- **cPanel Systems**: Web hosting control panel systems targeted in mass exploitation campaigns
- **Azure Environments**: Microsoft Azure platforms targeted through automated OAuth abuse techniques
- **Facebook Accounts**: Over 30,000 accounts compromised through phishing campaigns
- **Government Networks**: Southeast Asian government and military entities
- **MSP Infrastructure**: Managed service providers and hosting providers

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of critical authentication flaws in MOVEit Automation and cPanel systems
- **Privilege Escalation**: Copy Fail vulnerability enabling root access on Linux systems
- **Automated OAuth Abuse**: ConsentFix v3 attacks targeting Azure with automated OAuth manipulation
- **Tax-Themed Phishing**: Silver Fox group using tax-themed phishing emails to deploy ABCDoor malware
- **Google AppSheet Phishing Relay**: Vietnamese-linked operation using Google AppSheet as intermediary for Facebook account compromise
- **Ransomware Deployment**: "Sorry" ransomware attacks following cPanel exploitation
- **Vishing and SSO Abuse**: Rapid SaaS extortion attacks combining voice phishing with single sign-on abuse

## Threat Actor Activities

- **Silver Fox**: China-based cybercrime group deploying ABCDoor malware via tax-themed phishing campaigns targeting organizations in Russia and India
- **"Sorry" Ransomware Operators**: Mass exploitation of cPanel vulnerabilities to encrypt website data in ransomware attacks
- **Vietnamese-Linked Group**: Large-scale Facebook account compromise operation using Google AppSheet phishing relays, affecting over 30,000 accounts
- **Unknown Southeast Asian Targeting Group**: Previously unidentified threat actor exploiting cPanel vulnerabilities to target government, military, and MSP networks in Southeast Asia
- **ConsentFix v3 Operators**: Cybercriminals using automated OAuth abuse techniques to target Azure environments
- **SaaS Extortion Groups**: Two cybercrime groups conducting rapid, high-impact attacks within SaaS environments using vishing and SSO abuse techniques
- **China-Aligned Espionage Campaign**: Targeting government and defense sectors across South, East, and Southeast Asia, plus one European government entity