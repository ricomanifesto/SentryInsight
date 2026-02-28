# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting enterprise networks, with the most concerning being a three-year-long exploitation of a maximum-severity Cisco SD-WAN zero-day vulnerability and ongoing attacks against Ivanti Connect Secure devices using the RESURGE malware implant. North Korean APT groups are actively deploying sophisticated tools to breach air-gapped networks, while threat actors continue to exploit command injection vulnerabilities in Sangoma FreePBX instances. Additionally, multiple critical vulnerabilities in enterprise security products including Trend Micro Apex One and Juniper Networks routers pose significant risks to organizational infrastructure.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been actively exploited for three years
- **Impact**: Complete network compromise with sophisticated threat actors leaving minimal evidence
- **Status**: Currently under active exploitation with patches available
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure RESURGE Malware
- **Description**: Malicious implant used in zero-day attacks targeting Ivanti Connect Secure devices
- **Impact**: Persistent backdoor access that can remain dormant on compromised devices
- **Status**: Active exploitation with CISA warnings issued
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: Command injection flaw in Sangoma FreePBX instances leading to web shell deployment
- **Impact**: Remote code execution and persistent access to VoIP systems
- **Status**: Over 900 instances remain compromised despite patches being available

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One allowing remote code execution
- **Impact**: Complete system compromise on vulnerable Windows systems
- **Status**: Patches available but systems remain at risk until updated

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved running on PTX Series routers
- **Impact**: Full router takeover with root-level code execution capabilities
- **Status**: Recently disclosed with patches required

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Network devices running vulnerable SD-WAN software
- **Ivanti Connect Secure**: VPN appliances vulnerable to RESURGE malware implantation
- **Sangoma FreePBX**: VoIP systems with over 900 instances currently compromised
- **Trend Micro Apex One**: Windows-based endpoint security platforms
- **Juniper Networks PTX Series**: Enterprise routers running Junos OS Evolved
- **Google API Services**: Gemini AI data exposure through misconfigured API keys
- **Air-Gapped Networks**: High-security isolated systems targeted by sophisticated malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched vulnerabilities in critical infrastructure
- **Web Shell Deployment**: Command injection leading to persistent backdoor installation
- **Air-Gap Bridging**: USB-based malware for transferring data between isolated and connected networks
- **Cloud Service Abuse**: Zoho WorkDrive used for command-and-control communications
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient communications
- **Social Engineering**: Fake job repositories and gaming tools targeting developers and users
- **Supply Chain Attacks**: Malicious Go modules delivering backdoors and credential stealers

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new tools for air-gapped network infiltration and covert surveillance
- **ScarCruft (North Korean)**: Using Zoho WorkDrive and USB malware for air-gapped network breaches
- **UAT-10027**: Targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **The Com Cybercrime Collective**: Online group targeting children and teenagers (30 arrests made)
- **Sophisticated Unknown Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure
- **Developer-Targeting Groups**: Coordinated campaigns using fake Next.js repositories to deliver in-memory malware
- **Gaming Community Threats**: Distribution of Java-based RATs through trojanized gaming utilities