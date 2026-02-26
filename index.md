# Exploitation Report

The current threat landscape reveals a concerning mix of zero-day exploitation, supply chain attacks, and targeted developer compromises. The most critical activity involves a maximum-severity Cisco SD-WAN zero-day vulnerability that has been actively exploited since 2023 to achieve administrative access to enterprise networks. Simultaneously, sophisticated campaigns are targeting software developers through malicious repositories, fake job interviews, and compromised package managers, while threat actors continue to exploit AI coding assistants and leverage social engineering techniques to establish persistent access to development environments.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Zero-Day
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller and Catalyst SD-WAN Manager allowing remote attackers to compromise enterprise network infrastructure
- **Impact**: Remote attackers can gain administrative access and completely compromise SD-WAN deployments
- **Status**: Actively exploited in zero-day attacks since 2023, patches now available
- **CVE ID**: CVE-2026-20127

### Zyxel Router Remote Code Execution
- **Description**: A critical vulnerability affecting over a dozen Zyxel router models that allows unauthenticated remote command execution
- **Impact**: Complete device compromise and potential network lateral movement
- **Status**: Security updates released by Zyxel

### SolarWinds Serv-U Critical Vulnerabilities
- **Description**: Four critical security flaws in SolarWinds Serv-U file transfer software version 15.5
- **Impact**: Remote code execution with root privileges
- **Status**: Patches available from SolarWinds

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security vulnerabilities in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Remote code execution and API key exfiltration from developer environments
- **Status**: Vulnerabilities disclosed to Anthropic

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: SD-WAN Controller (formerly vSmart) and SD-WAN Manager (formerly vManage) systems
- **Zyxel Routers**: Over a dozen router models susceptible to unauthenticated remote code execution
- **SolarWinds Serv-U**: File transfer software version 15.5 with critical root execution flaws
- **Anthropic Claude Code**: AI coding assistant vulnerable to remote code execution
- **NuGet Package Manager**: Malicious packages targeting ASP.NET developers
- **Next.js Development Platform**: Fake repositories used in developer-targeting campaigns
- **npm Package Registry**: Malware-dropping packages in the JavaScript ecosystem

## Attack Vectors and Techniques

- **Malicious Repository Campaigns**: Fake Next.js projects and technical assessments used to trick developers into executing malicious code
- **Package Manager Poisoning**: Malicious NuGet packages impersonating legitimate Stripe libraries to steal API tokens
- **Social Engineering**: Fake job interviews and recruitment processes targeting software developers
- **In-Memory Malware Deployment**: Fileless attacks establishing persistent access on developer machines
- **Supply Chain Infiltration**: Compromising development tools and AI assistants to affect downstream software
- **SaaS API Abuse**: Using legitimate API calls to hide malicious traffic and maintain persistence
- **Telephone-Oriented Attack Delivery (TOAD)**: Bypassing email gateways by including only phone numbers in phishing emails

## Threat Actor Activities

- **UNC2814 (China-nexus)**: Conducted the GRIDTIDE campaign, breaching at least 53 organizations across 42 countries targeting telecommunications firms and government agencies
- **North Korean Groups**: Linked to fake job recruitment campaigns using poisoned Next.js repositories to establish persistent access
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per call to recruit women for IT help desk vishing attacks
- **Chinese Police Operations**: Using ChatGPT for politically motivated influence operations against Japanese officials
- **Russian Exploit Brokers**: Purchasing zero-day exploits from defense contractor employees for potential state-sponsored use
- **Ransomware Operators**: Ecosystem disruption following RAMP forum seizure, forcing groups to reorganize their operations