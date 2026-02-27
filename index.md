# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity across multiple critical infrastructure components. The most severe threat involves a maximum-severity Cisco SD-WAN vulnerability that has been actively exploited for over three years by sophisticated threat actors, enabling complete administrative access to network infrastructure. Concurrently, multiple threat actor groups are conducting coordinated campaigns targeting developers through sophisticated social engineering attacks, while critical vulnerabilities in enterprise security solutions and AI-powered development tools are creating new attack surfaces. Chinese state-sponsored groups continue aggressive espionage operations against telecommunications and government sectors globally, demonstrating the persistent nature of nation-state threats against critical infrastructure.

## Active Exploitation Details

### Cisco SD-WAN Authentication Bypass Vulnerability
- **Description**: A maximum-severity authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage) that allows complete circumvention of authentication mechanisms
- **Impact**: Remote attackers can gain full administrative access to SD-WAN infrastructure without authentication, enabling complete network compromise and control
- **Status**: Actively exploited in zero-day attacks since 2023, with sophisticated threat actors leaving minimal evidence of their activities
- **CVE ID**: CVE-2026-20127

### Claude Code AI Assistant Vulnerabilities
- **Description**: Multiple security flaws in Anthropic's Claude Code AI-powered coding assistant that enable remote code execution and credential theft
- **Impact**: Attackers can execute arbitrary code on developer machines and exfiltrate API keys and sensitive credentials from development environments
- **Status**: Recently disclosed vulnerabilities affecting developers using AI-integrated development workflows

### Google API Key Exposure
- **Description**: Previously harmless Google API keys embedded in client-side code can now be exploited to authenticate to Gemini AI services
- **Impact**: Unauthorized access to private AI data and conversations through misused API credentials
- **Status**: Ongoing exposure affecting applications with embedded Google service API keys

## Affected Systems and Products

- **Cisco Catalyst SD-WAN Controllers**: Complete administrative compromise possible on affected network infrastructure
- **Cisco Catalyst SD-WAN Managers**: Full management interface access for threat actors
- **Anthropic Claude Code**: AI development assistant vulnerable to remote code execution
- **Google Gemini AI Services**: Unauthorized access via misused API keys
- **Trend Micro Apex One**: Critical remote code execution vulnerabilities on Windows systems
- **Juniper Networks PTX Series Routers**: Root-level code execution via Junos OS Evolved vulnerability
- **Next.js Development Projects**: Malicious repositories targeting software developers
- **NuGet Package Gallery**: Supply chain attacks via fake Stripe library packages

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched Cisco SD-WAN infrastructure over multiple years
- **Social Engineering Campaigns**: Fake job interviews and technical assessments targeting developers
- **Supply Chain Attacks**: Malicious packages in software repositories mimicking legitimate libraries
- **API Key Abuse**: Exploitation of embedded client-side credentials for unauthorized service access
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command and control
- **SaaS API Evasion**: UNC2814 using legitimate SaaS API calls to hide malicious network traffic
- **Vishing Operations**: Scattered LAPSUS$ Hunters recruiting women for IT help desk social engineering attacks

## Threat Actor Activities

- **UNC2814 (Chinese APT)**: Conducted global espionage campaign breaching 53 organizations across 42 countries, targeting telecommunications and government sectors
- **UAT-10027**: Previously undocumented cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **North Korean Groups**: Linked to fake Next.js job recruitment campaigns establishing persistent access to developer machines
- **Scattered LAPSUS$ Hunters (SLH)**: Offering $500-$1,000 per call to recruit women for IT help desk vishing attacks
- **Sophisticated SD-WAN Actors**: Unknown but advanced threat group exploiting Cisco infrastructure while maintaining minimal forensic footprint
- **Aeternum C2 Operators**: Botnet operators using blockchain infrastructure to evade takedown efforts