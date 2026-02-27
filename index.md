# Exploitation Report

Critical zero-day exploitation activity has been identified across multiple enterprise infrastructure components, with the most severe being a three-year campaign exploiting Cisco SD-WAN systems. CVE-2026-20127, a maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller and Manager, has been under active exploitation since 2023 by sophisticated threat actors who left minimal forensic evidence. Additionally, multiple threat groups are leveraging advanced techniques including blockchain-based command and control infrastructure, AI-powered social engineering campaigns targeting developers, and sophisticated supply chain attacks through malicious package repositories.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass
- **Description**: Maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage)
- **Impact**: Remote attackers can gain administrative access and completely compromise SD-WAN infrastructure
- **Status**: Under active exploitation since 2023, patches recently released
- **CVE ID**: CVE-2026-20127

### Trend Micro Apex One Remote Code Execution
- **Description**: Critical vulnerabilities in Trend Micro Apex One security software allowing remote code execution
- **Impact**: Attackers can gain remote code execution on vulnerable Windows systems
- **Status**: Recently patched, exploitation potential remains high

### Juniper Networks PTX Router Takeover
- **Description**: Critical vulnerability in Junos OS Evolved network operating system running on PTX Series routers
- **Impact**: Unauthenticated attackers can execute code remotely with root privileges, achieving full router takeover
- **Status**: Vulnerability disclosed, patches available

### Google API Key Privilege Escalation
- **Description**: Previously harmless Google API keys for services like Maps can now be used to authenticate to Gemini AI assistant
- **Impact**: Access to private Gemini AI data and unauthorized API usage
- **Status**: Active security concern affecting client-side embedded API keys

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controller and Manager**: All versions prior to latest patches, actively exploited since 2023
- **Trend Micro Apex One**: Windows systems running vulnerable versions with RCE exposure
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved with critical remote code execution vulnerability
- **Google API Services**: Maps API keys embedded in client-side code now exposing Gemini AI access
- **Next.js Development Environment**: Developers targeted through malicious repositories and fake job assessments
- **NuGet Package Ecosystem**: .NET developers exposed through malicious StripeApi package impersonating legitimate Stripe library
- **Claude Code Development Tool**: Security flaws putting developer machines and supply chains at risk

## Attack Vectors and Techniques

- **Blockchain-Based C2**: Aeternum C2 botnet stores encrypted commands on Polygon blockchain to evade takedown efforts
- **Social Engineering via Fake Repositories**: Malicious Next.js repositories disguised as legitimate projects and technical assessments deliver in-memory malware
- **Supply Chain Poisoning**: Malicious NuGet packages impersonating legitimate libraries to steal API tokens and credentials
- **USB-Based Air-Gap Bridging**: ScarCruft uses USB malware combined with Zoho WorkDrive for command and control to breach isolated networks
- **Trojanized Gaming Tools**: Java-based RATs distributed through gaming utilities via browsers and chat platforms
- **AI-Powered Document Forgery**: OnlyFake platform generated over 10,000 fake identification documents using AI technology

## Threat Actor Activities

- **ScarCruft (North Korean)**: Deploying advanced toolset including Zoho WorkDrive backdoors and USB malware to breach air-gapped networks
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors since December 2025 using Dohdoor backdoor
- **Unknown Sophisticated Actor**: Exploiting Cisco SD-WAN zero-day CVE-2026-20127 for three years with minimal forensic footprint
- **Developer-Targeting Campaign**: Coordinated effort using fake Next.js repositories and job assessments to compromise developer environments
- **Chinese Influence Operations**: Using ChatGPT and other AI tools for politically motivated influence campaigns and disinformation
- **Ransomware Ecosystem**: Despite payment rates dropping to 28%, attack volumes continue to surge with groups adapting tactics