# Exploitation Report

Critical exploitation activity is currently impacting multiple enterprise systems and platforms across various sectors. The most severe incidents include a zero-day vulnerability in Cisco SD-WAN systems that has been actively exploited for three years, ongoing web shell attacks compromising over 900 Sangoma FreePBX instances, and the deployment of RESURGE malware on Ivanti devices through zero-day exploitation. Additionally, threat actors are leveraging sophisticated supply chain attacks through malicious packages and repositories, while advanced persistent threat groups continue targeting critical infrastructure and air-gapped networks with novel techniques.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: Maximum-severity security flaw in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage)
- **Impact**: Allows sophisticated threat actors to gain administrative access to SD-WAN infrastructure
- **Status**: Actively exploited since 2023, recently disclosed with patches available
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Complete system compromise with persistent backdoor access
- **Status**: Over 900 instances remain infected despite patches being available
- **CVE ID**: Not specified in articles

### Ivanti Zero-Day with RESURGE Malware
- **Description**: Zero-day vulnerability in Ivanti Connect systems exploited to deploy RESURGE malicious implant
- **Impact**: Persistent backdoor access with potential for dormant long-term compromise
- **Status**: CISA has issued warnings about dormant malware remaining on systems
- **CVE ID**: CVE-2025-0282

### Trend Micro Apex One Remote Code Execution
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software
- **Impact**: Remote code execution on vulnerable Windows systems
- **Status**: Recently patched by Trend Micro
- **CVE ID**: Not specified in articles

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical flaw in Junos OS Evolved network operating system on PTX Series routers
- **Impact**: Unauthenticated remote code execution with root privileges, full router takeover
- **Status**: Patches available
- **CVE ID**: Not specified in articles

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Catalyst SD-WAN Controller and Manager systems globally affected
- **Sangoma FreePBX**: Over 900 VoIP systems compromised with web shells
- **Ivanti Connect**: Enterprise connectivity solutions vulnerable to RESURGE implant
- **Trend Micro Apex One**: Windows-based endpoint security platforms
- **Juniper PTX Series**: Network routers running Junos OS Evolved
- **Google API Services**: Previously harmless API keys now expose Gemini AI data
- **Developer Environments**: Next.js repositories and NuGet packages used in supply chain attacks

## Attack Vectors and Techniques

- **Web Shell Deployment**: Command injection vulnerabilities exploited to install persistent backdoors
- **Zero-Day Exploitation**: Long-term exploitation of unpatched vulnerabilities for administrative access
- **Supply Chain Attacks**: Malicious packages mimicking legitimate libraries (StripeApi NuGet, malicious Go modules)
- **Social Engineering**: Fake job repositories and technical assessments targeting developers
- **USB-Based Attacks**: Air-gapped network infiltration using removable media
- **Blockchain-Based C2**: Aeternum C2 botnet using Polygon blockchain for resilient command infrastructure
- **Cloud Service Abuse**: Zoho WorkDrive leveraged for command-and-control communications

## Threat Actor Activities

- **ScarCruft (North Korean APT)**: Targeting air-gapped networks using USB malware and cloud services for C2
- **UAT-10027**: Undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure
- **Supply Chain Attackers**: Coordinated campaigns targeting developers through malicious repositories and packages
- **Chinese State-Linked Operations**: Using AI tools like ChatGPT for political influence operations
- **Ransomware Groups**: Continued high-volume attacks despite record-low payment rates of 28%