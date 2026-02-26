# Exploitation Report

The current threat landscape shows several critical vulnerabilities under active exploitation, with the most severe being a zero-day authentication bypass flaw in Cisco SD-WAN systems (CVE-2026-20127) that has been exploited since 2023 to gain administrative access. This coincides with heightened activity from Chinese threat actors conducting global espionage campaigns, targeting telecommunications firms and government agencies across 42 countries. Additional concerns include multiple vulnerabilities in development tools and AI-powered coding assistants that could enable remote code execution, as well as ongoing supply chain attacks targeting developers through malicious packages and fake job recruitment schemes.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: A maximum-severity authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage)
- **Impact**: Allows remote attackers to gain complete administrative access to affected systems
- **Status**: Actively exploited in zero-day attacks since 2023, patches now available
- **CVE ID**: CVE-2026-20127

### FileZen Vulnerability
- **Description**: A security flaw in FileZen file transfer software confirmed by CISA for active exploitation
- **Impact**: Enables unauthorized access to file transfer systems
- **Status**: Currently under active exploitation, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-25108

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Could result in remote code execution and API key exfiltration, compromising developer environments
- **Status**: Recently disclosed vulnerabilities affecting AI-integrated development workflows

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software
- **Impact**: Successful exploitation could result in remote code execution with root privileges
- **Status**: Patches released to address the vulnerabilities

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controller and Manager**: Authentication bypass affecting network management systems
- **FileZen File Transfer Software**: Active exploitation targeting file sharing infrastructure
- **Anthropic Claude Code**: AI coding assistant with multiple security flaws
- **SolarWinds Serv-U 15.5**: File transfer software with critical RCE vulnerabilities
- **Zyxel Routers**: Over a dozen router models affected by critical remote command execution flaw
- **Next.js Development Projects**: Malicious repositories used in supply chain attacks
- **NuGet and npm Package Repositories**: Compromised packages targeting ASP.NET developers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched Cisco SD-WAN systems since 2023
- **Supply Chain Attacks**: Malicious packages in NuGet and npm repositories targeting developers
- **Social Engineering**: Fake job interviews and technical assessments to compromise developer systems
- **AI-Powered Attacks**: Exploitation of vulnerabilities in AI coding assistants
- **SaaS API Abuse**: Using legitimate SaaS API calls to hide malicious traffic in espionage campaigns
- **Phishing Campaigns**: Credential theft targeting freight and logistics organizations
- **Vishing Operations**: Telephone-oriented attack delivery (TOAD) bypassing email gateways

## Threat Actor Activities

- **UNC2814 (China-nexus)**: Conducted GRIDTIDE campaign breaching 53 organizations across 42 countries, primarily targeting telecommunications and government agencies
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per call to recruit women for IT help desk social engineering attacks
- **North Korean Groups**: Linked to fake job recruitment campaigns using poisoned Next.js repositories
- **Diesel Vortex**: Financially motivated group targeting freight and logistics operators in the US and Europe through phishing
- **Russian Exploit Brokers**: Involved in purchasing stolen zero-day exploits from defense contractor employees
- **Chinese Police Operations**: Using ChatGPT for politically motivated influence operations targeting Japanese officials
- **ShinyHunters**: Extortion gang targeting major companies including Wynn Resorts for employee data theft