# Exploitation Report

Critical zero-day and active exploitation activity continues to pose significant threats to enterprise networks and infrastructure. Most notably, a maximum-severity Cisco SD-WAN vulnerability CVE-2026-20127 has been exploited by sophisticated threat actors since 2023, allowing complete administrative access to network infrastructure. Additionally, multiple AI-powered platforms including Claude Code and Google's Gemini AI have been compromised through various attack vectors, while Chinese threat actors have conducted widespread espionage campaigns targeting telecommunications and government agencies across 42 countries.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: A critical authentication bypass flaw in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage) that allows remote attackers to gain complete administrative control
- **Impact**: Attackers can achieve full administrative access to SD-WAN infrastructure, potentially compromising entire network segments and gaining persistent access to organizational networks
- **Status**: Currently being exploited in zero-day attacks since 2023 by sophisticated threat actors who leave minimal evidence behind
- **CVE ID**: CVE-2026-20127

### Claude Code Security Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant that enable remote exploitation through malicious code generation
- **Impact**: Remote code execution on developer systems and exfiltration of sensitive API keys and credentials from development environments
- **Status**: Vulnerabilities disclosed and highlight risks of AI integration in development workflows

### Google Gemini AI Data Exposure
- **Description**: Previously harmless Google API keys for services like Maps can now be exploited to authenticate with Gemini AI assistant
- **Impact**: Unauthorized access to private AI conversation data and potential exposure of sensitive information processed through Gemini
- **Status**: Active vulnerability affecting client-side embedded API keys

## Affected Systems and Products

- **Cisco Catalyst SD-WAN**: Controller and Manager components vulnerable to authentication bypass
- **Anthropic Claude Code**: AI coding assistant with remote code execution vulnerabilities
- **Google Gemini AI**: Accessible through misused API keys from other Google services
- **Trend Micro Apex One**: Critical remote code execution vulnerabilities in Windows systems
- **Juniper Networks PTX Series**: Critical router takeover vulnerability in Junos OS Evolved
- **Next.js Development Environments**: Targeted through malicious repositories and fake job assessments
- **NuGet Package Manager**: Compromised through malicious StripeApi package mimicking official Stripe library

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of Cisco SD-WAN infrastructure since 2023 with minimal forensic evidence
- **Supply Chain Attacks**: Malicious NuGet packages impersonating legitimate libraries to steal API tokens
- **Social Engineering**: Fake Next.js job interviews and technical assessments to backdoor developer systems
- **API Key Abuse**: Leveraging existing Google API keys to access unauthorized AI services
- **Blockchain-Based C2**: Aeternum botnet using Polygon blockchain to store encrypted commands and evade takedown
- **SaaS API Abuse**: Chinese threat actors using legitimate SaaS API calls to hide malicious traffic
- **Vishing Operations**: Scattered LAPSUS$ Hunters recruiting women for IT help desk social engineering attacks

## Threat Actor Activities

- **Unknown Sophisticated Actor**: Exploiting Cisco SD-WAN zero-day since 2023 with advanced evasion techniques and minimal attribution trails
- **UNC2814 (China-nexus)**: Conducted GRIDTIDE campaign breaching 53 organizations across 42 countries targeting telecommunications and government agencies
- **UAT-10027**: Targeting U.S. education and healthcare sectors since December 2025 using Dohdoor backdoor malware
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per successful call to recruit women for IT help desk vishing attacks
- **North Korean Groups**: Linked to malicious Next.js repository campaigns targeting developers through fake job recruitment operations
- **Chinese Police**: Using ChatGPT for politically motivated influence operations to smear Japanese political figures