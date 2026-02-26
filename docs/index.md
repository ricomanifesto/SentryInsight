# Exploitation Report

Several critical vulnerabilities are currently under active exploitation, presenting significant risks to enterprise and infrastructure systems. The most severe threat involves a Cisco SD-WAN authentication bypass vulnerability (CVE-2026-20127) that has been actively exploited since 2023, allowing attackers to gain administrative access to network infrastructure. Additional critical threats include newly disclosed remote code execution vulnerabilities in Trend Micro Apex One security software and Zyxel routers, along with a sophisticated campaign targeting software developers through malicious repositories and AI coding assistant vulnerabilities. Chinese-linked threat actors continue to conduct widespread espionage campaigns, successfully breaching dozens of organizations across telecommunications and government sectors.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: Maximum-severity authentication bypass flaw in Cisco Catalyst SD-WAN Controller and Manager systems
- **Impact**: Allows remote attackers to completely compromise SD-WAN infrastructure and gain administrative access without authentication
- **Status**: Actively exploited in zero-day attacks since 2023, patches now available
- **CVE ID**: CVE-2026-20127

### Trend Micro Apex One Remote Code Execution Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro's Apex One security platform allowing remote code execution
- **Impact**: Attackers can execute arbitrary code on vulnerable Windows systems running the security software
- **Status**: Patches released by Trend Micro, exploitation status unclear

### Zyxel Router Remote Code Execution Flaw
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models enabling remote command execution
- **Impact**: Unauthenticated attackers can gain remote command execution on vulnerable network devices
- **Status**: Security updates released, active exploitation potential

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical flaw in Junos OS Evolved running on PTX Series routers
- **Impact**: Unauthenticated attackers can execute code remotely with root privileges, allowing complete router takeover
- **Status**: Newly disclosed, patch availability unclear

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Remote code execution and API key exfiltration from developer environments
- **Status**: Recently disclosed, poses supply chain risks to software development

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: Controller (formerly vSmart) and Manager (formerly vManage) systems
- **Trend Micro Apex One**: Windows-based security platform installations
- **Zyxel Routers**: Over a dozen router models across product lines
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved
- **Anthropic Claude Code**: AI coding assistant platform
- **NuGet Gallery**: Malicious StripeApi package targeting financial services integration
- **Next.js Development Environment**: Fake repositories targeting software developers

## Attack Vectors and Techniques

- **Network Infrastructure Exploitation**: Direct attacks on SD-WAN controllers and routers to gain network access
- **Supply Chain Attacks**: Malicious packages in software repositories and fake technical assessments
- **Social Engineering**: Fake job interview processes targeting developers with malicious repositories
- **AI-Assisted Exploitation**: Leveraging AI coding assistants to execute malicious code and exfiltrate credentials
- **SaaS API Abuse**: Using legitimate SaaS API calls to hide malicious traffic in espionage campaigns
- **Telephone-Oriented Attack Delivery (TOAD)**: Email campaigns containing only phone numbers to bypass security gateways
- **Vishing Campaigns**: Recruiting women for IT help desk social engineering attacks with financial incentives

## Threat Actor Activities

- **UNC2814/GRIDTIDE Campaign**: China-linked espionage group that breached 53 organizations across 42 countries, targeting telecommunications and government agencies through SaaS API abuse
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **Scattered LAPSUS$ Hunters (SLH)**: Cybercrime collective offering $500-$1,000 per call to recruit women for vishing attacks against IT help desks
- **North Korean Threat Groups**: Conducting fake job recruitment campaigns using poisoned Next.js repositories to establish persistent access to developer machines
- **Chinese State-Sponsored Groups**: Ongoing espionage operations against telecommunications firms and government agencies using advanced persistent threat techniques