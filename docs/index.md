# Exploitation Report

Critical zero-day vulnerabilities continue to pose significant threats to enterprise infrastructure, with CVE-2026-20127 in Cisco SD-WAN systems being actively exploited since 2023, allowing remote authentication bypass. Simultaneously, Chinese threat actors have conducted widespread espionage campaigns breaching 53 organizations across 42 countries, while CISA has confirmed active exploitation of CVE-2026-25108 in FileZen systems. The cybersecurity landscape is further complicated by recent discoveries of multiple critical vulnerabilities in SolarWinds Serv-U software and vulnerabilities in AI-powered development tools like Claude Code and GitHub Copilot.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Cisco Catalyst SD-WAN that has been exploited as a zero-day since 2023
- **Impact**: Allows remote attackers to bypass authentication mechanisms and gain unauthorized access to SD-WAN infrastructure
- **Status**: Active zero-day exploitation confirmed, critical severity
- **CVE ID**: CVE-2026-20127

### FileZen Vulnerability
- **Description**: Recently disclosed vulnerability in FileZen file sharing platform confirmed by CISA for active exploitation
- **Impact**: Enables attackers to compromise file sharing systems and potentially access sensitive data
- **Status**: Active exploitation confirmed by CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software
- **Impact**: Successful exploitation could result in remote code execution with root-level privileges
- **Status**: Critical patches released, vulnerabilities allow root code execution

### Claude Code Security Flaws
- **Description**: Multiple security vulnerabilities discovered in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Could result in remote code execution and API key exfiltration from developer environments
- **Status**: Newly disclosed vulnerabilities affecting AI development tools

### GitHub Copilot RoguePilot Flaw
- **Description**: Vulnerability in GitHub Codespaces that could be exploited through malicious Copilot instructions
- **Impact**: Enables attackers to seize control of repositories by injecting malicious instructions and leak GITHUB_TOKEN
- **Status**: Vulnerability allows repository compromise through AI manipulation

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: Critical authentication bypass vulnerability affecting enterprise network infrastructure
- **FileZen Platform**: File sharing systems experiencing confirmed active exploitation
- **SolarWinds Serv-U 15.5**: File transfer software with four critical remote code execution vulnerabilities
- **Anthropic Claude Code**: AI-powered coding assistant vulnerable to remote code execution and data exfiltration
- **GitHub Codespaces/Copilot**: Development platforms vulnerable to malicious instruction injection
- **Zyxel Routers**: Over a dozen router models affected by critical remote command execution vulnerability
- **ASP.NET Applications**: Targeted by malicious NuGet packages designed to steal sensitive data
- **Next.js Repositories**: Poisoned repositories targeting developers through fake job recruitment campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched Cisco SD-WAN systems since 2023
- **SaaS API Abuse**: Chinese threat actors using SaaS API calls to hide malicious traffic in espionage campaigns
- **Supply Chain Attacks**: Malicious packages in NuGet and npm repositories targeting developers
- **Social Engineering**: North Korean groups using fake job interviews to distribute malicious repositories
- **Vishing Operations**: Scattered LAPSUS$ Hunters recruiting women for IT help desk social engineering attacks
- **AI Instruction Injection**: Exploitation of AI development tools through malicious prompt injection
- **Email Gateway Bypass**: Telephone-oriented attack delivery (TOAD) using phone numbers as primary payload

## Threat Actor Activities

- **UNC2814 (Chinese APT)**: Conducted GRIDTIDE campaign resulting in 53 organizational breaches across 42 countries using SaaS API abuse techniques
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per call to recruit women for IT help desk vishing attacks
- **North Korean Groups**: Targeting developers with malicious Next.js repositories through fake job recruitment campaigns
- **Diesel Vortex**: Financially motivated group conducting credential theft against freight and logistics operators across US and Europe using 52 malicious domains
- **Lazarus Group**: North Korean threat group now leveraging Medusa ransomware along with Comebacker backdoor and Blindingcan RAT
- **Russian Exploit Brokers**: Sanctioned individuals involved in purchasing stolen zero-day exploits from US defense contractors
- **ShinyHunters**: Extortion gang responsible for data breaches affecting Wynn Resorts and CarGurus, exposing 12.4 million accounts