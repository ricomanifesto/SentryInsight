# Exploitation Report

Critical zero-day exploitation activity has been identified with the most severe being CVE-2026-20127, a maximum-severity Cisco SD-WAN vulnerability that has been actively exploited since 2023 by sophisticated threat actors to gain administrative access. Multiple coordinated campaigns are targeting developers through malicious repositories and AI-powered coding tools, while Chinese espionage groups have successfully breached dozens of organizations across 42 countries. Additional critical vulnerabilities in Trend Micro Apex One and Juniper Networks PTX routers pose significant remote code execution risks to enterprise environments.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: Maximum-severity authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage)
- **Impact**: Allows unauthenticated remote attackers to gain administrative access and completely compromise SD-WAN infrastructure
- **Status**: Actively exploited in zero-day attacks since 2023; patch recently released
- **CVE ID**: CVE-2026-20127

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant
- **Impact**: Remote code execution and API key exfiltration on developer machines
- **Status**: Actively being exploited to compromise development environments and supply chains

### Google Gemini AI API Key Exposure
- **Description**: Previously harmless Google API keys for services like Maps can now be used to authenticate to Gemini AI assistant
- **Impact**: Access to private AI data and potential unauthorized AI service usage
- **Status**: Ongoing exposure affecting client-side embedded API keys

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controller**: All versions running vSmart controllers vulnerable to authentication bypass
- **Cisco Catalyst SD-WAN Manager**: All versions running vManage systems affected by zero-day exploitation
- **Trend Micro Apex One**: Windows systems running vulnerable versions susceptible to remote code execution
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved vulnerable to full system takeover
- **Anthropic Claude Code**: AI coding assistant platform with multiple RCE and data exfiltration vulnerabilities
- **Google API Services**: Maps and other API keys now expose Gemini AI access
- **Next.js Development Environment**: Targeted through malicious repositories in fake job interviews
- **NuGet Gallery**: Compromised with malicious StripeApi packages targeting financial services

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term stealth campaigns exploiting unpatched Cisco SD-WAN systems for administrative access
- **Supply Chain Poisoning**: Malicious NuGet packages impersonating legitimate Stripe libraries to steal API tokens
- **Social Engineering**: Fake job interviews using poisoned Next.js repositories to backdoor developer machines
- **AI Platform Abuse**: Exploiting Claude Code vulnerabilities for remote code execution and credential theft
- **SaaS API Hijacking**: Using legitimate SaaS API calls to hide malicious traffic and evade detection
- **Blockchain C2 Infrastructure**: Aeternum botnet storing encrypted commands on Polygon blockchain for resilience
- **Gaming Platform Distribution**: Trojanized gaming tools spreading Java-based RATs through browsers and chat platforms

## Threat Actor Activities

- **UNC2814 (China-nexus)**: Conducted GRIDTIDE espionage campaign breaching 53 organizations across 42 countries targeting telecommunications and government agencies
- **UAT-10027**: Previously undocumented cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **North Korean Groups**: Linked to fake job recruitment campaigns using malicious Next.js repositories to establish persistent access
- **Chinese State Actors**: Using ChatGPT and influence operations to conduct political smear campaigns against foreign officials
- **Sophisticated Unknown Actor**: Exploiting Cisco SD-WAN zero-day for three years while leaving minimal forensic evidence
- **Financial Threat Actors**: Targeting fintech companies through malicious package distribution and API token theft
- **Ransomware Operations**: Despite payment rates dropping to 28%, attack volumes continue to surge across multiple sectors