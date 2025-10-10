# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and systems across the cybersecurity landscape. The RondoDox botnet is conducting large-scale attacks against 56 n-day vulnerabilities across more than 30 device types, exploiting previously disclosed flaws from Pwn2Own competitions. Simultaneously, threat actors are actively exploiting a critical authentication bypass vulnerability in the WordPress Service Finder theme, enabling unauthorized access to administrator accounts. Additional concerning activities include the ClayRat Android spyware campaign targeting users through fake popular applications, ransomware operations leveraging legitimate DFIR tools like Velociraptor, and the SonicWall cloud backup service breach affecting all customers using the service.

## Active Exploitation Details

### RondoDox Botnet Mass Exploitation
- **Description**: Large-scale botnet targeting 56 different n-day vulnerabilities across more than 30 distinct device types, including flaws initially disclosed during Pwn2Own hacking competitions
- **Impact**: Worldwide compromise of vulnerable devices and systems through automated exploitation of known vulnerabilities
- **Status**: Currently active with ongoing exploitation campaigns

### WordPress Service Finder Theme Authentication Bypass
- **Description**: Critical security flaw in the Service Finder WordPress theme allowing attackers to bypass authentication mechanisms
- **Impact**: Unauthorized access to any account including administrator accounts on affected WordPress installations
- **Status**: Actively being exploited by threat actors
- **CVE ID**: CVE-2025-53967

### ClayRat Android Spyware Campaign
- **Description**: Rapidly evolving Android spyware campaign using fake applications that mimic popular services like WhatsApp, Google Photos, TikTok, and YouTube
- **Impact**: Complete device compromise with spyware capabilities including data theft and surveillance
- **Status**: Active targeting of users primarily in Russia through Telegram channels and phishing websites

### Velociraptor DFIR Tool Abuse
- **Description**: Threat actors weaponizing the legitimate Velociraptor digital forensics and incident response tool in ransomware attacks
- **Impact**: Deployment of LockBit and Babuk ransomware using trusted security tools to evade detection
- **Status**: Currently being used in active ransomware campaigns

## Affected Systems and Products

- **WordPress Sites**: Service Finder theme installations vulnerable to authentication bypass
- **Android Devices**: Targeted by ClayRat spyware through malicious app installations
- **Multiple IoT and Network Devices**: Over 30 device types targeted by RondoDx botnet exploitation
- **SonicWall Customers**: All users of SonicWall's cloud backup service affected by data breach
- **Enterprise Networks**: Systems vulnerable to Velociraptor-based ransomware attacks
- **Figma Integrations**: Organizations using Framelink Figma MCP Server vulnerable to remote code execution
- **Discord Users**: 5.5 million users potentially affected by claimed Zendesk support system breach

## Attack Vectors and Techniques

- **Mass Vulnerability Scanning**: RondoDox botnet systematically targeting known n-day vulnerabilities across diverse device types
- **Social Engineering**: ClayRat campaign using fake popular applications distributed through Telegram and phishing sites
- **Living-off-the-Land**: Ransomware operators abusing legitimate DFIR tools like Velociraptor to bypass security controls
- **Cache Smuggling**: FileFix attack variant using cache smuggling techniques to secretly download malicious ZIP archives while evading security software
- **ClickFix Phishing**: WordPress sites compromised with malicious JavaScript injections to redirect users to fraudulent sites
- **AI-Enhanced Attacks**: Russian threat actors incorporating artificial intelligence into cyber operations against Ukraine

## Threat Actor Activities

- **Storm-2657**: Conducting "payroll pirate" attacks targeting university HR employees in the United States to hijack salary payments since March 2025
- **UTA0388**: China-aligned threat actor conducting spear-phishing campaigns across North America, Asia, and Europe to deliver GOVERSHELL Go-based implant
- **TwoNet**: Pro-Russian hacktivist group evolving from DDoS attacks to targeting critical infrastructure systems
- **Crimson Collective**: Recently breached Red Hat Consulting's GitLab instance and has formed partnerships with the notorious Lapsus$ cybercriminal collective
- **LockBit, Qilin & DragonForce**: Three major ransomware groups forming a collaborative "cartel" to share attack information and resources following the release of LockBit 5.0
- **Qilin Ransomware**: Claimed responsibility for attacking Japanese beer maker Asahi and leaked company data on dark web extortion sites
- **BatShadow**: Vietnam-based cybercrime group behind the Vampire Bot malware campaign targeting job hunters