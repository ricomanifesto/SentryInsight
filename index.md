# Exploitation Report

Current cybersecurity threats showcase a concerning landscape of active exploitation activities across multiple attack vectors. The most critical concerns include active exploitation of WordPress themes enabling authentication bypass, massive botnet operations targeting 56 known vulnerabilities across 30+ device types, and sophisticated spyware campaigns targeting mobile users through social engineering. Enterprise environments face significant risks from ransomware groups weaponizing legitimate forensic tools, while supply chain attacks affect millions through compromised backup services and AI-powered social engineering campaigns.

## Active Exploitation Details

### Service Finder WordPress Theme Authentication Bypass
- **Description**: Critical security flaw in the Service Finder WordPress theme that allows threat actors to bypass authentication mechanisms
- **Impact**: Attackers can gain unauthorized access to any account, including administrator accounts, leading to complete site compromise
- **Status**: Currently being actively exploited by threat actors

### RondoDox Botnet Multi-Vulnerability Campaign
- **Description**: Large-scale botnet operation targeting 56 different vulnerabilities across more than 30 distinct device types, including vulnerabilities first disclosed during Pwn2Own competitions
- **Impact**: Worldwide attacks enabling device compromise and botnet recruitment across diverse hardware platforms
- **Status**: Active exploitation campaign ongoing globally

### WordPress Sites JavaScript Injection Campaign
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations as part of ClickFix phishing attacks
- **Impact**: Site visitors redirected to sketchy sites for credential harvesting and malware distribution
- **Status**: Active campaign targeting WordPress installations

### Figma MCP Server Remote Code Execution
- **Description**: Security vulnerability in Framelink Figma MCP Server that enables agentic AI compromise
- **Impact**: Remote code execution capabilities that can compromise organizational systems
- **Status**: Patch available - immediate patching required
- **CVE ID**: CVE-2025-53967

## Affected Systems and Products

- **Android Devices**: ClayRat spyware targeting through fake WhatsApp, TikTok, YouTube, and Google Photos applications
- **WordPress Sites**: Service Finder theme and general WordPress installations under active attack
- **SonicWall Cloud Backup**: All customers using cloud backup service affected by firewall configuration theft
- **GitHub Copilot**: Vulnerable to CamoLeak AI attack for data exfiltration
- **University Systems**: HR departments targeted by Storm-2657 in payroll diversion attacks
- **Discord**: Claimed breach affecting 5.5 million users through Zendesk support system
- **Figma MCP Server**: Third-party integration vulnerable to agentic AI compromise
- **30+ Device Types**: Various hardware platforms targeted by RondoDox botnet
- **Asahi Brewery**: Japanese beer manufacturer compromised by Qilin ransomware

## Attack Vectors and Techniques

- **Social Engineering**: ClayRat spyware distributed through fake popular application lookalikes via Telegram channels and phishing websites
- **AI-Powered Attacks**: CamoLeak technique exploiting GitHub Copilot for code and secrets exfiltration
- **Payroll Diversion**: Storm-2657 targeting university HR employees to hijack salary payments
- **Tool Abuse**: Velociraptor DFIR tool weaponized for LockBit and Babuk ransomware deployment
- **Cache Smuggling**: FileFix attack variant using cache smuggling to bypass security software detection
- **Spear-Phishing**: UTA0388 campaigns targeting North America, Asia, and Europe with Go-based implants
- **Supply Chain**: Compromise of backup services affecting all SonicWall cloud backup customers
- **JavaScript Injection**: WordPress sites compromised for malicious redirections in ClickFix campaigns

## Threat Actor Activities

- **Storm-2657**: Cybercrime gang conducting "payroll pirate" attacks against US universities since March 2025, targeting HR employees for salary payment hijacking
- **UTA0388**: China-aligned threat actor conducting spear-phishing campaigns across multiple regions, deploying HealthKick to GOVERSHELL evolution malware
- **ClayRat Operators**: Android spyware campaign targeting Russian users through social engineering and app impersonation
- **RondoDox Botnet**: Large-scale operation targeting 56 vulnerabilities worldwide across diverse device ecosystems
- **TwoNet**: Pro-Russian hacktivist group evolved from DDoS attacks to critical infrastructure targeting
- **Qilin Ransomware**: Claims responsibility for Asahi brewery attack with data leakage threats
- **LockBit, Qilin & DragonForce**: Ransomware cartel formation sharing attack information and resources
- **Crimson Collective**: Red Hat hackers collaborating with Scattered Lapsus$ collective after GitLab breach
- **BatShadow**: Vietnam-based cybercrime group operating Vampire Bot malware targeting job hunters
- **Chaos Ransomware**: Enhanced C++ variant with encryption, wiper, and cryptocurrency-stealing capabilities