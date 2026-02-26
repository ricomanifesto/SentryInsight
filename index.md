# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation, with the most severe being a maximum-severity authentication bypass flaw in Cisco SD-WAN systems (CVE-2026-20127) that has been exploited since 2023 to grant unauthorized administrative access. Additionally, CISA has confirmed active exploitation of a FileZen vulnerability (CVE-2026-25108), while multiple critical remote code execution flaws have been discovered in SolarWinds Serv-U and Zyxel router systems. Beyond traditional vulnerabilities, threat actors are increasingly leveraging AI development tools and conducting sophisticated social engineering campaigns targeting developers and organizations globally.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: A maximum-severity authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage)
- **Impact**: Allows remote attackers to gain unauthorized administrative access to affected systems
- **Status**: Actively exploited in zero-day attacks since 2023, patches now available
- **CVE ID**: CVE-2026-20127

### FileZen Vulnerability
- **Description**: A vulnerability in FileZen file transfer software that has been confirmed as actively exploited
- **Impact**: Allows unauthorized access and potential data compromise
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog due to confirmed active exploitation
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software
- **Impact**: Successful exploitation could result in remote code execution with root privileges
- **Status**: Patches released by SolarWinds to address all four vulnerabilities

### Zyxel Router Remote Code Execution
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models
- **Impact**: Allows unauthenticated attackers to gain remote command execution capabilities
- **Status**: Security updates released by Zyxel

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controller**: Formerly known as vSmart, affected by authentication bypass vulnerability
- **Cisco Catalyst SD-WAN Manager**: Formerly known as vManage, vulnerable to unauthorized access
- **FileZen File Transfer Software**: Confirmed active exploitation by threat actors
- **SolarWinds Serv-U 15.5**: File transfer software with four critical remote code execution vulnerabilities
- **Zyxel Router Models**: Over a dozen router models affected by critical RCE flaw
- **Anthropic Claude Code**: AI-powered coding assistant with multiple security vulnerabilities
- **Next.js Development Environment**: Targeted through malicious repositories in fake job interviews
- **NuGet Package Ecosystem**: Four malicious packages targeting ASP.NET developers
- **npm Package Repository**: Malicious packages designed to drop malware on developer systems

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of Cisco SD-WAN vulnerability since 2023 before disclosure
- **Social Engineering**: Fake job interviews targeting developers with malicious Next.js repositories
- **Supply Chain Attacks**: Malicious NuGet and npm packages designed to compromise developer environments
- **AI Tool Exploitation**: Vulnerabilities in Claude Code allowing remote code execution and API key theft
- **SaaS API Abuse**: UNC2814 group using legitimate SaaS API calls to hide malicious traffic
- **Vishing Operations**: Scattered LAPSUS$ Hunters offering financial incentives for women to conduct social engineering attacks
- **Package Repository Poisoning**: Coordinated campaigns distributing backdoored development tools
- **Telephone-Oriented Attack Delivery (TOAD)**: Email-based attacks that bypass gateways by only containing phone numbers

## Threat Actor Activities

- **UNC2814 (China-nexus)**: Conducted GRIDTIDE campaign resulting in 53 breaches across 42 countries, primarily targeting telecommunications and government agencies
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per call to recruit women for IT help desk vishing attacks
- **North Korean Groups**: Linked to fake job recruitment campaigns using malicious Next.js repositories
- **Diesel Vortex**: Financially motivated group targeting freight and logistics organizations in the US and Europe through phishing campaigns using 52 domains
- **Russian Exploit Brokers**: Sanctioned individuals involved in purchasing stolen zero-day exploits from defense contractor employees
- **Chinese Police Operations**: Using ChatGPT for politically motivated influence operations against Japanese officials
- **ShinyHunters**: Extortion gang responsible for data breaches including Wynn Resorts employee data theft