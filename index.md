# Exploitation Report

The current threat landscape reveals a concerning escalation in active exploitation activities, with several critical zero-day vulnerabilities being leveraged by sophisticated threat actors. Most notably, CL0P-linked hackers have exploited a zero-day vulnerability in Oracle's E-Business Suite software since August 2025, impacting dozens of organizations worldwide. Additionally, the RondoDox botnet is conducting large-scale attacks targeting 56 n-day vulnerabilities across more than 30 device types, while threat actors are actively exploiting authentication bypass flaws in WordPress themes and conducting widespread spyware campaigns targeting Android users through social engineering techniques.

## Active Exploitation Details

### Oracle E-Business Suite Zero-Day Exploitation
- **Description**: A zero-day security flaw in Oracle's E-Business Suite (EBS) software has been actively exploited by CL0P-linked hackers since August 9, 2025
- **Impact**: Dozens of organizations have been compromised, allowing attackers to gain unauthorized access to enterprise systems and potentially exfiltrate sensitive data
- **Status**: Active exploitation ongoing since August 2025, affecting multiple organizations globally

### WordPress Service Finder Theme Authentication Bypass
- **Description**: A critical security flaw in the Service Finder WordPress theme allows attackers to bypass authentication mechanisms
- **Impact**: Threat actors can gain unauthorized access to any account, including administrator accounts, providing complete control over WordPress installations
- **Status**: Currently being actively exploited by threat actors

### RondoDox Botnet N-Day Exploitation
- **Description**: A large-scale botnet targeting 56 known vulnerabilities across more than 30 distinct device types, including flaws first disclosed during Pwn2Own hacking competitions
- **Impact**: Worldwide attacks compromising various devices and systems to build an extensive botnet infrastructure
- **Status**: Active exploitation campaign targeting multiple n-day vulnerabilities simultaneously

### Framelink Figma MCP Server Vulnerability
- **Description**: A vulnerability in a third-party option for connecting Figma to agentic AI systems
- **Impact**: Can lead to remote code execution (RCE) and potential compromise of organizations using agentic AI
- **Status**: Patch available, organizations advised to update immediately
- **CVE ID**: CVE-2025-53967

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning software affected by zero-day exploitation
- **WordPress Service Finder Theme**: WordPress theme vulnerable to authentication bypass attacks
- **Various IoT and Network Devices**: Over 30 distinct device types targeted by RondoDox botnet
- **Android Mobile Devices**: Targeted by ClayRat spyware through fake applications
- **SonicWall Cloud Backup Service**: All customers using cloud backup service affected by data breach
- **Figma Integration Systems**: Organizations using Framelink MCP server for AI integration
- **Microsoft Teams and Communication Platforms**: Targeted in social engineering campaigns
- **University HR and Payroll Systems**: Specifically targeted in "payroll pirate" attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unknown vulnerabilities in Oracle EBS software
- **Social Engineering via Fake Applications**: ClayRat spyware distributed through fake WhatsApp, TikTok, YouTube, and Google Photos applications
- **Mass Vulnerability Scanning**: RondoDox botnet systematically targeting 56 different vulnerability types
- **Authentication Bypass**: Direct circumvention of WordPress authentication mechanisms
- **Spear-Phishing Campaigns**: UTA0388 conducting targeted phishing to deliver GOVERSHELL implants
- **Cache Smuggling**: FileFix attack variant using cache smuggling to evade security software detection
- **Legitimate Tool Abuse**: Threat actors weaponizing Velociraptor DFIR tool in ransomware attacks
- **Token Theft**: Exploitation of OAuth and API tokens for SaaS breaches
- **AI-Enhanced Attacks**: Russian hackers incorporating artificial intelligence in cyber operations against Ukraine

## Threat Actor Activities

- **CL0P-Linked Hackers**: Conducting zero-day exploitation of Oracle EBS since August 2025, targeting dozens of organizations
- **RondoDox Operators**: Running large-scale botnet operations targeting 56 vulnerabilities across global infrastructure
- **UTA0388 (China-aligned)**: Conducting spear-phishing campaigns across North America, Asia, and Europe to deploy GOVERSHELL implants
- **Storm-2657**: Targeting university employees in "payroll pirate" attacks since March 2025 to hijack salary payments
- **ClayRat Campaign**: Rapidly evolving Android spyware operation targeting Russian users through Telegram channels and phishing websites
- **ShinyHunters Group**: Operating BreachForums portal (now seized by FBI) for corporate data leaks and extortion
- **TwoNet Hacktivist Group**: Pro-Russian group pivoting from DDoS attacks to critical infrastructure targeting
- **Crimson Collective**: Recently breached Red Hat Consulting's GitLab instance and partnered with Scattered Lapsus$
- **Ransomware Cartel**: LockBit, Qilin, and DragonForce collaborating to share attack information and resources
- **BatShadow (Vietnam-based)**: Operating Vampire Bot malware campaigns targeting job hunters
- **Russian State Actors**: Incorporating AI tools in cyber operations against Ukrainian targets