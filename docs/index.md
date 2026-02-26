# Exploitation Report

Critical zero-day exploitation continues to plague enterprise networks, with the most severe being a Cisco SD-WAN authentication bypass vulnerability (CVE-2026-20127) that has been actively exploited since 2023. Additionally, CISA has confirmed active exploitation of a FileZen vulnerability (CVE-2026-25108), while threat actors are leveraging sophisticated supply chain attacks targeting developers through malicious repositories and AI-powered tools. Chinese state-sponsored groups have conducted widespread espionage campaigns against telecommunications and government organizations across 42 countries, demonstrating the continued evolution of advanced persistent threat activities.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Cisco Catalyst SD-WAN allowing remote attackers to compromise systems
- **Impact**: Remote attackers can gain unauthorized access to SD-WAN infrastructure
- **Status**: Zero-day exploitation confirmed since 2023, patches now available
- **CVE ID**: CVE-2026-20127

### FileZen Vulnerability
- **Description**: Security flaw in FileZen file transfer software enabling unauthorized access
- **Impact**: Attackers can compromise file transfer operations and potentially access sensitive data
- **Status**: Active exploitation confirmed by CISA, added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-25108

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Remote code execution and API key exfiltration on developer machines
- **Status**: Vulnerabilities disclosed, patches required

### Zyxel Router Remote Code Execution
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models
- **Impact**: Unauthenticated attackers can achieve remote command execution
- **Status**: Security updates released by Zyxel

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U file transfer software
- **Impact**: Remote code execution with root privileges
- **Status**: Updates released to address vulnerabilities

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: Authentication bypass vulnerability affecting SD-WAN infrastructure
- **FileZen**: File transfer software with confirmed active exploitation
- **Anthropic Claude Code**: AI-powered coding assistant with RCE vulnerabilities
- **Zyxel Routers**: Over a dozen router models affected by critical RCE flaw
- **SolarWinds Serv-U 15.5**: File transfer software with four critical vulnerabilities
- **Next.js Projects**: Malicious repositories targeting developers
- **NuGet Packages**: Four malicious packages targeting ASP.NET developers
- **UFP Technologies**: Medical device manufacturer systems compromised

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious Next.js repositories and NuGet packages targeting developers
- **Fake Job Interviews**: North Korean-linked campaigns using fraudulent technical assessments
- **AI Tool Exploitation**: Vulnerabilities in AI coding assistants enabling code execution
- **Social Engineering**: Telephone-oriented attack delivery (TOAD) bypassing email gateways
- **API Abuse**: SaaS API calls used to hide malicious traffic in espionage campaigns
- **Vishing Attacks**: Scattered LAPSUS$ Hunters recruiting women for IT help desk social engineering
- **Malicious Ads**: 1Campaign platform helping threat actors evade Google Ads detection

## Threat Actor Activities

- **UNC2814 (Chinese APT)**: Conducted global espionage campaign with 53 breaches across 42 countries targeting telecommunications and government agencies
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per call to recruit women for vishing attacks against IT help desks
- **Diesel Vortex**: Financially motivated group targeting freight and logistics organizations in US and Europe through phishing campaigns using 52 domains
- **North Korean Groups**: Linked to fake job interview campaigns targeting developers with malicious repositories
- **ShinyHunters**: Extortion gang responsible for Wynn Resorts employee data breach
- **Chinese Police**: Using ChatGPT for politically motivated influence operations against Japanese officials
- **Russian Exploit Brokers**: Purchasing stolen zero-day exploits from defense contractor employees