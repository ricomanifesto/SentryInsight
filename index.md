# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities under active exploitation, with particular concern around Oracle E-Business Suite attacks linked to CL0P ransomware group, widespread SonicWall VPN compromises affecting over 100 accounts, and a zero-day in Gladinet file sharing software (CVE-2025-11371). Additionally, threat actors are leveraging legitimate tools like Velociraptor DFIR software for ransomware attacks, while new malware campaigns including Stealit and ClayRat Android spyware are actively targeting users through deceptive distribution methods. The exploitation of CVE-2025-10035 in GoAnywhere Managed File Transfer systems demonstrates the ongoing threat to enterprise file transfer solutions.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: A critical security flaw in Oracle's E-Business Suite (EBS) software that allows unauthorized access to sensitive data without authentication
- **Impact**: Attackers can access sensitive organizational data without proper login credentials; dozens of organizations have been impacted
- **Status**: Zero-day vulnerability actively exploited since August 9, 2025, by CL0P-linked hackers

### Gladinet CentreStack and TrioFox Zero-Day
- **Description**: Local file inclusion vulnerability that can be escalated to remote code execution in Gladinet CentreStack and TrioFox products
- **Impact**: Local attackers can access system files without authentication and potentially achieve remote code execution
- **Status**: Currently unpatched and under active exploitation
- **CVE ID**: CVE-2025-11371

### GoAnywhere Managed File Transfer Vulnerability
- **Description**: Critical security flaw in Fortra's GoAnywhere Managed File Transfer (MFT) solution
- **Impact**: Enables attackers to compromise file transfer systems and potentially access sensitive data
- **Status**: Under active exploitation with full timeline investigation completed by Fortra
- **CVE ID**: CVE-2025-10035

### SonicWall SSL VPN Compromise
- **Description**: Widespread compromise of SonicWall SSL VPN devices enabling unauthorized access to customer environments
- **Impact**: Threat actors are authenticating into multiple accounts and accessing customer environments
- **Status**: Over 100 accounts confirmed compromised with ongoing exploitation

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software affected by zero-day vulnerability
- **Gladinet CentreStack and TrioFox**: File sharing and storage solutions vulnerable to local file inclusion attacks
- **GoAnywhere Managed File Transfer**: Enterprise file transfer solution with actively exploited vulnerability
- **SonicWall SSL VPN Devices**: Network security appliances experiencing widespread compromise
- **Node.js Applications**: Single Executable Application feature being abused by Stealit malware
- **Android Devices**: Targeted by ClayRat spyware through malicious app distribution
- **npm Registry**: 175 malicious packages with 26,000 downloads used for credential harvesting

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities being exploited before patches are available
- **VPN Compromise**: Authentication bypass or credential compromise on SonicWall VPN systems
- **Malicious Package Distribution**: npm registry abuse with 175 malicious packages for credential phishing
- **Social Engineering**: Android malware disguised as popular apps like WhatsApp, TikTok, and YouTube
- **Tool Abuse**: Legitimate DFIR tool Velociraptor weaponized for ransomware operations
- **Node.js SEA Abuse**: Single Executable Application feature exploited for malware distribution through game and VPN installers
- **Smishing Campaigns**: Text message scams targeting New Yorkers with fake inflation refund offers

## Threat Actor Activities

- **CL0P Ransomware Group**: Exploiting Oracle E-Business Suite zero-day to breach dozens of organizations since August 2025
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group using Velociraptor DFIR tool in LockBit ransomware attacks for persistent network access
- **Storm-2657**: "Payroll Pirates" hijacking HR SaaS accounts to divert employee salary payments to attacker-controlled accounts
- **ShinyHunters Group**: Operating BreachForums portal for corporate data leaks and Salesforce extortion (recently dismantled by FBI)
- **GXC Team Syndicate**: Brazilian-led cybercrime group dismantled by Spanish authorities, leader "GoogleXcoder" arrested
- **RondoDox Botnet Operators**: Using "exploit shotgun" approach targeting consumer edge device vulnerabilities
- **Aisuru Botnet**: Launching record-breaking DDoS attacks primarily from compromised IoT devices on US ISPs including AT&T, Comcast, and Verizon