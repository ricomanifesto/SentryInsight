# Exploitation Report

The current threat landscape reveals significant exploitation activity across multiple attack vectors, with threat actors leveraging both known vulnerabilities and sophisticated social engineering techniques. Notable campaigns include the RondoDox botnet actively exploiting 56 n-day vulnerabilities across 30+ device types, critical authentication bypass flaws in WordPress themes being exploited in the wild, and the emergence of advanced spyware campaigns like ClayRat targeting Android users. Additionally, ransomware groups are demonstrating increased collaboration and sophistication, while threat actors are weaponizing legitimate security tools like Velociraptor in their attacks. The SonicWall breach affecting all cloud backup customers highlights the ongoing risks to critical infrastructure and security appliances.

## Active Exploitation Details

### WordPress Service Finder Theme Authentication Bypass
- **Description**: Critical security flaw in the WordPress Service Finder theme that allows threat actors to bypass authentication mechanisms
- **Impact**: Unauthorized access to any account, including administrator accounts, leading to complete site compromise
- **Status**: Currently being actively exploited by threat actors in the wild

### RondoDox Botnet Multi-Vulnerability Campaign
- **Description**: Large-scale botnet targeting 56 different vulnerabilities across more than 30 distinct device types, including flaws first disclosed during Pwn2Own competitions
- **Impact**: Device compromise, botnet recruitment, and potential lateral movement across networks
- **Status**: Active worldwide attacks ongoing

### WordPress Site JavaScript Injections
- **Description**: Malicious campaign targeting WordPress sites to inject JavaScript code that redirects users to malicious sites
- **Impact**: Site visitors redirected to sketchy domains for phishing and malware distribution
- **Status**: Active exploitation campaign using ClickFix phishing techniques

### FileFix Cache Smuggling Attack
- **Description**: Evolved variant of FileFix social engineering attack using cache smuggling techniques
- **Impact**: Secret download of malicious ZIP archives while bypassing security software detection
- **Status**: New attack variant actively being deployed

### Framelink Figma MCP Server Vulnerability
- **Description**: Bug in third-party Figma Model Context Protocol server enabling agentic AI compromise
- **Impact**: Remote code execution (RCE) capabilities against organizations using the affected component
- **Status**: Patch available, active exploitation possible
- **CVE ID**: CVE-2025-53967

## Affected Systems and Products

- **WordPress Sites**: Service Finder theme users vulnerable to authentication bypass; multiple sites targeted for JavaScript injection campaigns
- **Android Devices**: Users targeted by ClayRat spyware through fake WhatsApp, TikTok, YouTube, and Google Photos applications
- **Network Devices**: Over 30 distinct device types affected by RondoDox botnet attacks, including Pwn2Own-disclosed vulnerabilities
- **SonicWall Firewall Users**: All customers using cloud backup service affected by configuration file theft
- **Enterprise Networks**: Organizations using Velociraptor DFIR tool at risk of ransomware deployment
- **University Systems**: HR employees and payroll systems targeted in Storm-2657 campaigns
- **Figma Integration Users**: Organizations using Framelink MCP server vulnerable to RCE attacks

## Attack Vectors and Techniques

- **Social Engineering**: ClayRat spyware distributed through fake popular app installations and Telegram channels
- **Botnet Operations**: RondoDox leveraging multiple n-day vulnerabilities for large-scale device compromise
- **Supply Chain Attacks**: Legitimate DFIR tools like Velociraptor repurposed for ransomware deployment
- **Phishing Campaigns**: University employees targeted through sophisticated payroll redirection schemes
- **Cache Smuggling**: FileFix attacks using browser cache manipulation to bypass security controls
- **JavaScript Injection**: WordPress sites compromised to serve malicious redirects through injected code
- **Authentication Bypass**: Direct exploitation of WordPress theme vulnerabilities for administrative access
- **AI-Enhanced Attacks**: Russian threat actors incorporating AI tools in cyber operations against Ukraine
- **Token Theft**: OAuth and API token compromise leading to SaaS platform breaches

## Threat Actor Activities

- **Storm-2657**: Conducting "payroll pirate" attacks against US universities since March 2025, targeting HR employees to hijack salary payments
- **UTA0388**: China-aligned actor running spear-phishing campaigns across North America, Asia, and Europe using Go-based GOVERSHELL implant
- **ClayRat Operators**: Targeting Russian users through fake app distribution via Telegram and phishing sites
- **RondoDox Group**: Operating large-scale botnet with worldwide reach, exploiting 56 vulnerabilities across multiple device types
- **LockBit, Qilin, DragonForce**: Ransomware groups forming collaborative "cartel" to share attack information and resources
- **TwoNet Hacktivists**: Pro-Russian group pivoted from DDoS attacks to critical infrastructure targeting
- **BatShadow**: Vietnamese cybercrime group behind Vampire Bot malware targeting job seekers
- **Crimson Collective**: Recently breached Red Hat Consulting's GitLab instance and partnered with Scattered Lapsus$ group
- **Russian State Actors**: Increasingly using AI tools in cyber operations against Ukrainian targets during H1 2025