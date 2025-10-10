# Exploitation Report

Current threat activity demonstrates a diverse landscape of active exploitation targeting multiple platforms and systems. Critical vulnerabilities are being exploited in WordPress themes, with threat actors actively bypassing authentication mechanisms to gain unauthorized administrative access. Meanwhile, large-scale botnets are capitalizing on dozens of known vulnerabilities across various device types, while sophisticated ransomware operations continue to evolve their attack methodologies. Mobile platforms face significant threats from advanced spyware campaigns, and cloud infrastructure breaches are exposing sensitive configuration data for enterprise customers. These developments highlight the ongoing challenges organizations face from both opportunistic cybercriminals and sophisticated threat actors.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical security flaw in the Service Finder WordPress theme allowing unauthorized access to any account, including administrator accounts
- **Impact**: Complete compromise of WordPress sites with full administrative privileges
- **Status**: Actively being exploited by threat actors

### RondoDox Botnet Multi-Vulnerability Campaign
- **Description**: Large-scale botnet operation targeting 56 different vulnerabilities across more than 30 distinct device types, including vulnerabilities originally disclosed at Pwn2Own competitions
- **Impact**: Widespread device compromise and botnet recruitment across multiple vendor platforms
- **Status**: Active worldwide attacks in progress

### Framelink Figma MCP Server Vulnerability
- **Description**: Security vulnerability in third-party connector between Figma and agentic AI systems
- **Impact**: Remote code execution capabilities on affected systems
- **Status**: Patch available, organizations urged to update immediately
- **CVE ID**: CVE-2025-53967

### WordPress Sites JavaScript Injection Campaign
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations as part of ClickFix phishing attacks
- **Impact**: Site visitors redirected to sketchy sites for credential theft and malware distribution
- **Status**: Ongoing campaign affecting multiple WordPress installations

## Affected Systems and Products

- **Service Finder WordPress Theme**: Critical authentication bypass vulnerability affecting all versions
- **Multiple IoT and Network Devices**: Over 30 distinct device types targeted by RondoDox botnet operations
- **Framelink Figma MCP Server**: Third-party integration tool connecting Figma to AI agents
- **WordPress Sites**: Widespread JavaScript injection campaign affecting multiple installations
- **Android Mobile Devices**: ClayRat spyware targeting users through fake popular applications
- **SonicWall Cloud Backup Service**: All customer firewall configuration files compromised
- **University HR Systems**: Targeted by Storm-2657 for payroll redirection attacks
- **Microsoft Defender for Endpoint**: False positive flagging of SQL Server installations

## Attack Vectors and Techniques

- **Social Engineering via Fake Apps**: ClayRat spyware masquerading as WhatsApp, TikTok, YouTube, and Google Photos
- **Spear-Phishing Campaigns**: UTA0388 targeting organizations across North America, Asia, and Europe
- **Cache Smuggling**: FileFix attack variant using advanced evasion techniques to bypass security software
- **Legitimate Tool Abuse**: Threat actors weaponizing Velociraptor DFIR tool in ransomware operations
- **AI-Enhanced Attacks**: Russian threat actors incorporating artificial intelligence into cyber operations against Ukraine
- **Payroll Redirection**: Storm-2657 targeting university HR employees to hijack salary payments
- **Authentication Bypass**: Direct exploitation of WordPress theme vulnerabilities for administrative access

## Threat Actor Activities

- **Storm-2657**: Conducting "pirate payroll" attacks against U.S. universities since March 2025, targeting HR employees for salary payment hijacking
- **UTA0388**: China-aligned threat actor conducting spear-phishing campaigns delivering GOVERSHELL Go-based implant across multiple continents
- **ClayRat Operators**: Rapidly evolving Android spyware campaign targeting Russian users through Telegram channels and phishing websites
- **RondoDox Botnet Operators**: Large-scale vulnerability exploitation campaign targeting 56 different flaws across diverse device ecosystems
- **TwoNet Hacktivist Group**: Pro-Russian collective pivoting from DDoS attacks to critical infrastructure targeting
- **Ransomware Cartel**: LockBit, Qilin, and DragonForce forming collaborative alliance to share attack resources and information
- **Qilin Ransomware**: Claiming responsibility for Asahi brewery attack and data leak operations
- **Crimson Collective**: Recent Red Hat Consulting breach perpetrators collaborating with Scattered Lapsus$ group