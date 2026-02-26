# Exploitation Report

Critical vulnerability exploitation activity continues across multiple technology platforms with significant focus on zero-day attacks and supply chain compromises. The most severe incidents include a critical Cisco SD-WAN authentication bypass vulnerability (CVE-2026-20127) that has been actively exploited since 2023, and active exploitation of a FileZen vulnerability (CVE-2026-25108) confirmed by CISA. Additionally, multiple critical remote code execution flaws in SolarWinds Serv-U and Zyxel routers pose immediate threats to enterprise infrastructure. Supply chain attacks targeting developers through malicious packages and fake job interviews demonstrate sophisticated social engineering tactics, while Chinese espionage groups continue large-scale operations against telecommunications and government organizations globally.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass vulnerability in Cisco Catalyst SD-WAN allowing remote attackers to compromise systems
- **Impact**: Remote attackers can bypass authentication controls and gain unauthorized access to SD-WAN infrastructure
- **Status**: Actively exploited in zero-day attacks since 2023, patches now available
- **CVE ID**: CVE-2026-20127

### FileZen Vulnerability
- **Description**: Recently disclosed vulnerability in FileZen file transfer software
- **Impact**: Allows attackers to exploit file transfer systems for unauthorized access
- **Status**: Active exploitation confirmed by CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software
- **Impact**: Successful exploitation could result in remote code execution with root privileges
- **Status**: Critical patches released, immediate patching required

### Zyxel Router Remote Code Execution Flaw
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models
- **Impact**: Allows unauthenticated attackers to gain remote command execution capabilities
- **Status**: Security updates released by Zyxel

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Could result in remote code execution and API key exfiltration from developer environments
- **Status**: Vulnerabilities disclosed, poses risk to software development workflows

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: Authentication bypass affecting SD-WAN infrastructure
- **FileZen**: File transfer software with active exploitation
- **SolarWinds Serv-U 15.5**: File transfer software with four critical RCE vulnerabilities
- **Zyxel Routers**: Over a dozen router models affected by critical RCE flaw
- **Anthropic Claude Code**: AI coding assistant with RCE and data exfiltration risks
- **Next.js Projects**: Malicious repositories targeting developers
- **NuGet Packages**: Four malicious packages targeting ASP.NET developers
- **npm Packages**: Malware-dropping packages in JavaScript ecosystem

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched vulnerabilities in critical infrastructure
- **Supply Chain Attacks**: Malicious packages in software repositories targeting developers
- **Social Engineering**: Fake job interviews and technical assessments to compromise developer machines
- **SaaS API Abuse**: Using legitimate API calls to hide malicious traffic in espionage campaigns
- **Phishing Campaigns**: Telephone-oriented attack delivery (TOAD) bypassing email gateways
- **Credential Theft**: Targeting freight and logistics organizations through phishing domains
- **Malicious Advertising**: Using 1Campaign service to evade detection in Google Ads

## Threat Actor Activities

- **UNC2814 (Chinese APT)**: GRIDTIDE campaign breached 53 organizations across 42 countries, targeting telecommunications and government agencies
- **Chinese Espionage Groups**: Large-scale operations against telecom firms and government agencies using SaaS API calls to hide activities
- **North Korean Groups**: Fake job recruitment campaigns using malicious Next.js repositories for persistent access
- **Scattered LAPSUS$ Hunters (SLH)**: Recruiting women for IT help desk vishing attacks, offering $500-$1,000 per successful call
- **Diesel Vortex**: Financially motivated group targeting freight and logistics operators in the US and Europe
- **ShinyHunters**: Extortion gang responsible for Wynn Resorts employee data breach
- **Russian Exploit Brokers**: Purchasing stolen zero-day exploits from defense contractor employees