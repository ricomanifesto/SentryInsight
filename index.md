# Exploitation Report

The current threat landscape reveals critical active exploitation campaigns targeting enterprise infrastructure and development environments. Most notably, Cisco SD-WAN systems have been under sustained zero-day attacks since 2023 through a critical authentication bypass vulnerability, while Chinese threat actors have conducted extensive espionage operations against telecommunications and government agencies globally. Additionally, CISA has confirmed active exploitation of FileZen file transfer systems, and multiple supply chain attacks are targeting developers through malicious packages and fake recruitment campaigns. The rapid exploitation timeframe has decreased to just 29 minutes for network compromise, highlighting the urgent need for enhanced security postures across all organizations.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Cisco Catalyst SD-WAN allowing remote attackers to gain unauthorized access
- **Impact**: Remote attackers can completely bypass authentication mechanisms and gain control of SD-WAN infrastructure
- **Status**: Actively exploited in zero-day attacks since 2023, patch status unclear from available information
- **CVE ID**: CVE-2026-20127

### FileZen File Transfer Vulnerability
- **Description**: Recently disclosed vulnerability in FileZen file transfer software that enables unauthorized access
- **Impact**: Attackers can compromise file transfer operations and potentially access sensitive data
- **Status**: Confirmed active exploitation by CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-25108

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant affecting developer environments
- **Impact**: Remote code execution capabilities and API key exfiltration from development systems
- **Status**: Recently disclosed, exploitation potential confirmed

### Zyxel Router Remote Code Execution
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models allowing unauthenticated remote command execution
- **Impact**: Complete router compromise enabling network infiltration and persistent access
- **Status**: Security updates released, active exploitation risk remains high

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U file transfer software
- **Impact**: Remote code execution with root privileges on affected systems
- **Status**: Patches released for all four critical vulnerabilities

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: All versions affected by authentication bypass vulnerability
- **FileZen**: File transfer software confirmed under active attack
- **Anthropic Claude Code**: AI coding assistant with remote code execution flaws
- **Zyxel Routers**: Over a dozen router models vulnerable to unauthenticated RCE
- **SolarWinds Serv-U 15.5**: File transfer software with four critical vulnerabilities
- **Next.js Repositories**: Malicious repositories targeting developers in supply chain attacks
- **NuGet Packages**: Four malicious packages targeting ASP.NET developers
- **npm Packages**: Malicious packages designed to drop malware on developer systems
- **GitHub Codespaces**: RoguePilot vulnerability enabling token theft through Copilot manipulation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Cisco SD-WAN vulnerability exploited for over a year before discovery
- **Supply Chain Attacks**: Malicious packages in NuGet and npm repositories targeting developers
- **Fake Recruitment Campaigns**: North Korean threat actors using fraudulent job interviews to distribute malware
- **Social Engineering**: SLH group recruiting women for IT help desk vishing attacks with $500-$1,000 per call incentives
- **SaaS API Abuse**: Chinese threat actors hiding malicious traffic through legitimate SaaS API calls
- **Phishing Operations**: Diesel Vortex group using 52 domains to target freight and logistics organizations
- **Malicious Advertising**: 1Campaign platform enabling persistent malicious Google Ads campaigns
- **Telephone-Oriented Attack Delivery (TOAD)**: Email campaigns directing victims to call malicious phone numbers

## Threat Actor Activities

- **Chinese State-Sponsored Groups**: Conducted global espionage campaign against dozens of telecommunications firms and government agencies using SaaS API calls to hide malicious activity
- **North Korean Threat Actors**: Multiple campaigns including fake job recruitment targeting developers and Lazarus Group's adoption of Medusa ransomware
- **Scattered LAPSUS$ Hunters (SLH)**: Recruiting female operatives for IT help desk vishing attacks with significant financial incentives
- **Diesel Vortex**: Financial cybercrime group targeting freight and logistics organizations across US and Europe through credential theft operations
- **ShinyHunters**: Extortion group responsible for major data breaches including Wynn Resorts employee data and CarGurus customer information affecting 12.4 million accounts
- **Russian Exploit Brokers**: Sanctioned individuals involved in purchasing stolen zero-day exploits from US defense contractor employees