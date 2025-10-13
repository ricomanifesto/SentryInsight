# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple critical vulnerabilities. Most notably, Oracle E-Business Suite has been targeted through a zero-day vulnerability that allows unauthenticated remote attackers to access sensitive data, leading to confirmed breaches including Harvard University. Additionally, the RondoDox botnet is conducting widespread "exploit shotgun" campaigns targeting over 50 vulnerabilities across 30+ vendors, while threat actors are exploiting a zero-day in Gladinet file sharing software. The situation is further complicated by widespread SonicWall VPN compromises affecting over 100 accounts and the weaponization of legitimate security tools like Velociraptor for ransomware attacks.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Vulnerability
- **Description**: A critical security flaw in Oracle's E-Business Suite that allows unauthorized access to sensitive data without authentication
- **Impact**: Remote unauthenticated attackers can access and compromise sensitive organizational data, leading to data breaches and potential ransomware attacks
- **Status**: Oracle has issued emergency patches over the weekend; actively exploited in the wild with confirmed victims including Harvard University

### Gladinet CentreStack and Triofox Zero-Day
- **Description**: A zero-day vulnerability in Gladinet file sharing software that allows local attackers to access system files without authentication
- **Impact**: Unauthorized access to system files and potential data exfiltration
- **Status**: Currently being actively exploited; no patch information provided
- **CVE ID**: CVE-2025-11371

### RondoDox Botnet Multi-Vendor Exploitation
- **Description**: A comprehensive "exploit shotgun" campaign targeting vulnerabilities across multiple vendors and products
- **Impact**: Widespread botnet recruitment and system compromise across diverse infrastructure
- **Status**: Active campaign exploiting over 50 flaws across 30+ vendors

### SonicWall SSL VPN Compromise
- **Description**: Widespread authentication bypass allowing threat actors to access multiple customer environments through compromised VPN devices
- **Impact**: Unauthorized network access and potential lateral movement across customer infrastructure
- **Status**: Over 100 accounts confirmed compromised; ongoing investigation

## Affected Systems and Products

- **Oracle E-Business Suite**: All versions affected by the zero-day vulnerability requiring emergency patching
- **Gladinet CentreStack and Triofox**: File sharing software products vulnerable to local privilege escalation
- **SonicWall SSL VPN Devices**: Multiple customer environments compromised through authentication bypass
- **Consumer Edge Devices**: Over 30 vendors targeted by RondoDox botnet exploitation campaigns
- **Microsoft Internet Explorer Mode**: Legacy compatibility feature in Edge browser exploited as backdoor mechanism
- **IoT Devices**: Compromised devices on major US ISPs including AT&T, Comcast, and Verizon used in DDoS attacks

## Attack Vectors and Techniques

- **Unauthenticated Remote Exploitation**: Oracle E-Business Suite attacks allowing direct access without credentials
- **Local Privilege Escalation**: Gladinet zero-day enabling system file access without authentication
- **VPN Authentication Bypass**: SonicWall devices compromised to provide persistent network access
- **Legitimate Tool Weaponization**: Velociraptor DFIR tool abused for ransomware deployment and persistence
- **Legacy Feature Exploitation**: Internet Explorer mode in Edge browser used as backdoor mechanism
- **Botnet Recruitment**: Mass exploitation campaigns using automated tools to compromise edge devices
- **GitHub Infrastructure Abuse**: Astaroth banking trojan using GitHub repositories for command and control resilience

## Threat Actor Activities

- **Clop Ransomware Gang**: Actively exploiting Oracle zero-day vulnerability with Harvard University listed on their leak site
- **Storm-2603 (CL-CRI-1040)**: Chinese threat group weaponizing Velociraptor DFIR tool for LockBit ransomware attacks and persistent network access
- **RondoDox Operators**: Conducting widespread botnet campaigns with "exploit shotgun" approach across multiple vendor ecosystems
- **Astaroth Banking Trojan Operators**: Leveraging GitHub infrastructure for command and control resilience following previous takedowns
- **GXC Team Cybercrime Syndicate**: Brazilian-led operation dismantled by Spanish authorities with leader "GoogleXcoder" arrested
- **ShinyHunters**: Extortion group targeting Salesforce customers before federal takedown of their operations site
- **Unknown Advanced Threat Actors**: Exploiting Internet Explorer mode in Edge browser as backdoor mechanism, prompting Microsoft security enhancements