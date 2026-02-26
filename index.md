# Exploitation Report

Critical exploitation activity is currently dominated by a zero-day vulnerability in Cisco SD-WAN systems that has been actively exploited since 2023, allowing attackers to gain complete administrative access to network infrastructure. Meanwhile, a sophisticated developer-targeting campaign is using malicious repositories and fake job interviews to compromise software developers' systems with in-memory malware. Additional threats include supply chain attacks through malicious packages in software repositories, vulnerabilities in AI coding assistants, and ongoing nation-state activities including Chinese espionage operations that have breached dozens of organizations across 42 countries.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage)
- **Impact**: Allows remote attackers to completely control affected systems with administrative privileges
- **Status**: Actively exploited in zero-day attacks since 2023, recently patched by Cisco
- **CVE ID**: CVE-2026-20127

### Next.js Repository Malware Campaign
- **Description**: Coordinated developer-targeting campaign using malicious repositories disguised as legitimate Next.js projects and technical assessments
- **Impact**: Establishes persistent access to developer machines and delivers in-memory malware
- **Status**: Active campaign linked to North Korean threat actors, ongoing exploitation

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security vulnerabilities in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Could result in remote code execution and API key exfiltration from developer environments
- **Status**: Recently disclosed vulnerabilities affecting AI-integrated development workflows

### SolarWinds Serv-U File Transfer Vulnerabilities
- **Description**: Four critical security flaws in SolarWinds Serv-U 15.5 file transfer software
- **Impact**: Successful exploitation could result in remote code execution with root privileges
- **Status**: Recently patched by SolarWinds, exploitation status unclear

### Zyxel Router Remote Code Execution
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models
- **Impact**: Allows unauthenticated attackers to gain remote command execution on affected devices
- **Status**: Security updates released by Zyxel

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controller and Manager**: Network infrastructure components vulnerable to authentication bypass
- **Next.js Development Environments**: Developers targeted through malicious repositories and fake job assessments
- **NuGet and npm Package Managers**: Supply chain attacks through malicious packages mimicking legitimate libraries
- **Anthropic Claude Code**: AI coding assistant vulnerable to remote code execution and data exfiltration
- **SolarWinds Serv-U 15.5**: File transfer software with critical remote code execution vulnerabilities
- **Zyxel Router Models**: Multiple router models affected by remote code execution vulnerability
- **ASP.NET Development Environments**: Targeted by malicious NuGet packages designed to steal sensitive data

## Attack Vectors and Techniques

- **Social Engineering**: Fake job interviews and technical assessments to trick developers into executing malicious code
- **Supply Chain Attacks**: Malicious packages in software repositories (NuGet, npm) mimicking legitimate libraries
- **Repository Poisoning**: Malicious GitHub repositories disguised as legitimate development projects
- **API Token Theft**: Malicious packages designed to steal authentication tokens and sensitive data
- **In-Memory Malware**: Advanced techniques to avoid detection while maintaining persistence
- **SaaS API Abuse**: Using legitimate SaaS API calls to hide malicious network traffic
- **Authentication Bypass**: Exploiting authentication mechanisms to gain unauthorized administrative access

## Threat Actor Activities

- **UNC2814 (Chinese Nexus)**: Conducted global espionage campaign breaching at least 53 organizations across 42 countries, targeting telecommunications firms and government agencies
- **North Korean Groups**: Linked to fake job recruitment campaigns using poisoned Next.js repositories to establish persistent access
- **Scattered LAPSUS$ Hunters (SLH)**: Offering financial incentives ($500-$1,000 per call) to recruit women for IT help desk vishing attacks
- **Chinese State Actors**: Using ChatGPT and AI tools for politically motivated influence operations and disinformation campaigns
- **Russian Exploit Brokers**: Sanctioned for purchasing stolen zero-day exploits from U.S. defense contractor employees
- **Ransomware Groups**: Ecosystem disruption following RAMP forum seizure, forcing groups to reorganize operations