# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, most notably a maximum-severity Cisco SD-WAN zero-day that has been exploited for three years. CVE-2026-20127 represents a significant authentication bypass vulnerability that allowed sophisticated threat actors to gain administrative access to Cisco Catalyst SD-WAN systems since 2023. Additionally, multiple critical vulnerabilities in enterprise security solutions including Trend Micro Apex One and Juniper Networks PTX routers pose immediate risks to organizational infrastructure. The exploitation activity is further compounded by coordinated campaigns targeting developers through malicious repositories and supply chain attacks, alongside a major Chinese espionage operation that compromised 53 organizations across 42 countries.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage) that allows unauthenticated remote attackers to compromise systems
- **Impact**: Remote attackers can gain administrative access to SD-WAN infrastructure, potentially allowing complete network control and data exfiltration
- **Status**: Actively exploited in zero-day attacks since 2023, recently patched by Cisco
- **CVE ID**: CVE-2026-20127

### Trend Micro Apex One Code Execution Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro's Apex One security solution that enable remote code execution on vulnerable Windows systems
- **Impact**: Attackers can achieve remote code execution on enterprise endpoints protected by the security solution
- **Status**: Recently patched by Trend Micro, exploitation status in the wild unclear

### Juniper Networks PTX Router Takeover Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved network operating system running on PTX Series routers that allows complete system compromise
- **Impact**: Unauthenticated attackers can execute code remotely with root privileges, enabling full router takeover
- **Status**: Recently disclosed and patched, active exploitation status unknown

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant affecting developer workflows
- **Impact**: Remote code execution and API key exfiltration on developer systems integrated with the AI assistant
- **Status**: Recently disclosed vulnerabilities highlighting supply chain risks in AI-integrated development environments

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: Controller (vSmart) and Manager (vManage) systems vulnerable to authentication bypass
- **Trend Micro Apex One**: Enterprise endpoint security solution with critical RCE vulnerabilities on Windows systems
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved network operating system
- **Anthropic Claude Code**: AI-powered coding assistant integrated into developer environments
- **Google API Keys**: Previously harmless API keys for services like Maps now expose Gemini AI data
- **Gaming Platforms**: Browser and chat platforms distributing trojanized gaming utilities with Java-based RATs
- **NuGet Gallery**: Malicious StripeApi package targeting financial services developers
- **Next.js Development**: Fake repositories and technical assessment materials targeting software developers

## Attack Vectors and Techniques

- **Authentication Bypass**: Exploitation of CVE-2026-20127 in Cisco SD-WAN systems allowing unauthenticated administrative access
- **Supply Chain Compromise**: Malicious packages on NuGet Gallery and fake Next.js repositories targeting developers
- **Social Engineering**: Fake job interview processes delivering malicious technical assessments to developers
- **Blockchain C2 Infrastructure**: Aeternum C2 botnet using Polygon blockchain to store encrypted commands and evade takedown
- **API Key Abuse**: Exploitation of Google API keys to access Gemini AI data through previously secure client-side implementations
- **SaaS API Abuse**: Chinese threat actors using legitimate SaaS API calls to hide malicious traffic in espionage campaigns
- **Trojanized Gaming Tools**: Distribution of remote access trojans through compromised gaming utilities on browsers and chat platforms

## Threat Actor Activities

- **UNC2814 (China-nexus)**: Conducted the GRIDTIDE campaign compromising 53 organizations across 42 countries, primarily targeting telecommunications firms and government agencies using SaaS API calls to hide malicious traffic
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors since December 2025 using the Dohdoor backdoor
- **Unknown Sophisticated Actor**: Exploited Cisco SD-WAN zero-day CVE-2026-20127 for three years while leaving minimal evidence
- **North Korean-linked Actors**: Connected to fake job recruitment campaigns using malicious Next.js repositories to establish persistent access to developer machines
- **Developer-targeting Campaign**: Coordinated effort using fake technical assessments and job interviews to compromise software developer environments
- **Chinese Police Operations**: Use of ChatGPT in politically motivated influence operations targeting Japanese political figures
- **Financial Threat Actors**: Targeting developers with malicious StripeApi NuGet packages to steal API tokens from financial services firms