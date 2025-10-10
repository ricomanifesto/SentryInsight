# Exploitation Report

Critical vulnerability exploitation activity has intensified across multiple platforms and technologies. The RondoDox botnet is conducting large-scale attacks targeting 56 known vulnerabilities across more than 30 device types, including flaws previously disclosed at Pwn2Own competitions. Meanwhile, threat actors are actively exploiting a critical authentication bypass vulnerability in WordPress Service Finder themes to gain unauthorized administrator access. Advanced persistent threat groups like UTA0388 continue sophisticated espionage campaigns using evolving malware, while ransomware operators are leveraging legitimate security tools like Velociraptor for attack deployment. The threat landscape is further complicated by emerging social engineering campaigns, including ClayRat Android spyware and FileFix cache smuggling attacks that evade traditional security controls.

## Active Exploitation Details

### WordPress Service Finder Theme Authentication Bypass
- **Description**: Critical security flaw in WordPress Service Finder theme allowing threat actors to bypass authentication mechanisms
- **Impact**: Unauthorized access to any account including administrator privileges, potentially leading to complete website compromise
- **Status**: Actively exploited in the wild

### RondoDox Botnet Vulnerability Campaign
- **Description**: Large-scale botnet targeting 56 known vulnerabilities across multiple device manufacturers and platforms
- **Impact**: Device compromise, botnet enrollment, and potential data theft across diverse infrastructure
- **Status**: Active worldwide attacks targeting vulnerabilities disclosed at Pwn2Own competitions

### Framelink Figma MCP Server Remote Code Execution
- **Description**: Vulnerability in third-party Figma Model Context Protocol server enabling remote code execution
- **Impact**: Complete system compromise through agentic AI integration channels
- **Status**: Patch available, active exploitation risk
- **CVE ID**: CVE-2025-53967

## Affected Systems and Products

- **WordPress Websites**: Service Finder theme installations vulnerable to authentication bypass
- **Network Infrastructure**: Over 30 distinct device types targeted by RondoDox botnet operations
- **Android Mobile Devices**: Russian users targeted by ClayRat spyware masquerading as popular applications
- **Enterprise Networks**: Organizations using Velociraptor DFIR tool being weaponized for ransomware deployment
- **SonicWall Cloud Services**: All customers using cloud backup services affected by configuration file theft
- **University Systems**: HR and payroll systems targeted in Storm-2657 "payroll pirate" campaigns
- **Discord Users**: 5.5 million users potentially affected by claimed Zendesk support system breach
- **Figma Integration Environments**: Organizations using Framelink MCP server for AI agent connectivity

## Attack Vectors and Techniques

- **Cache Smuggling**: FileFix attack variant bypassing security software through malicious ZIP archive delivery
- **Social Engineering**: ClayRat spyware distribution through fake WhatsApp, TikTok, and YouTube applications
- **Legitimate Tool Abuse**: Velociraptor DFIR platform weaponized for LockBit and Babuk ransomware deployment
- **Supply Chain Compromise**: WordPress site injections redirecting users to malicious ClickFix phishing campaigns
- **Spear Phishing**: UTA0388 targeting North America, Asia, and Europe with Go-based GOVERSHELL implants
- **AI-Enhanced Attacks**: Russian threat actors incorporating artificial intelligence into cyber operations against Ukraine
- **Cloud Service Exploitation**: Unauthorized access to SonicWall's cloud backup infrastructure
- **Academic Targeting**: University HR employees targeted for payroll redirection attacks

## Threat Actor Activities

- **RondoDox Operators**: Conducting worldwide vulnerability exploitation campaigns targeting diverse infrastructure
- **Storm-2657**: Cybercrime gang executing "payroll pirate" attacks against U.S. universities since March 2025
- **UTA0388**: China-aligned threat actor conducting espionage campaigns with evolved GOVERSHELL malware
- **ClayRat Developers**: Android spyware campaign targeting Russian users through social media and phishing sites
- **TwoNet Hacktivists**: Pro-Russian group escalating from DDoS attacks to critical infrastructure targeting
- **Ransomware Cartel**: LockBit, Qilin, and DragonForce forming collaborative extortion alliance
- **BatShadow Group**: Vietnamese cybercrime organization deploying Vampire Bot malware against job seekers
- **Crimson Collective**: Red Hat attackers collaborating with Scattered Lapsus$ collective
- **Russian State Actors**: Leveraging AI technologies for enhanced cyber operations in Ukraine conflict