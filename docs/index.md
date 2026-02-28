# Exploitation Report

The current threat landscape reveals several critical zero-day vulnerabilities under active exploitation, with attackers targeting enterprise infrastructure through sophisticated multi-vector campaigns. Most notably, a Cisco SD-WAN zero-day vulnerability has been exploited for three years by an unknown sophisticated threat actor, while Ivanti Connect systems face ongoing attacks through the RESURGE malware implant. North Korean APT groups, including APT37 and ScarCruft, continue deploying advanced tools to breach air-gapped networks using USB-based malware and cloud services for command-and-control operations. Additional exploitation activity includes ongoing web shell attacks against Sangoma FreePBX instances and critical vulnerabilities in enterprise security solutions from Trend Micro and Juniper Networks.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been actively exploited for approximately three years
- **Impact**: Allows sophisticated threat actors to gain unauthorized access to SD-WAN infrastructure with minimal forensic evidence
- **Status**: Under active exploitation by unknown sophisticated threat actors
- **CVE ID**: CVE-2026-20127

### Ivanti Connect RESURGE Malware
- **Description**: A malicious implant targeting Ivanti Connect systems through zero-day exploitation, capable of remaining dormant on infected devices
- **Impact**: Provides persistent access to corporate networks and can evade detection through dormancy capabilities
- **Status**: Active exploitation ongoing with CISA warnings about dormant infections
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Web Shell Attacks
- **Description**: Command injection vulnerability in Sangoma FreePBX systems being exploited to deploy web shells
- **Impact**: Over 900 instances remain compromised, allowing attackers persistent access to VoIP systems
- **Status**: Ongoing exploitation with hundreds of systems still infected since December attacks

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software allowing remote code execution
- **Impact**: Attackers can gain remote code execution on vulnerable Windows systems running the security software
- **Status**: Recently patched by Trend Micro

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved network operating system on PTX Series routers
- **Impact**: Allows unauthenticated attackers to execute code remotely with root privileges, enabling full router takeover
- **Status**: Critical vulnerability requiring immediate patching

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Enterprise SD-WAN deployments vulnerable to three-year exploitation campaign
- **Ivanti Connect Systems**: Corporate security appliances susceptible to RESURGE malware implants
- **Sangoma FreePBX Instances**: Over 900 VoIP systems compromised with persistent web shells
- **Trend Micro Apex One**: Enterprise endpoint security software on Windows systems
- **Juniper Networks PTX Routers**: Network infrastructure running Junos OS Evolved
- **Google API Keys**: Previously harmless API keys now exposing Gemini AI data access
- **Air-Gapped Networks**: Isolated systems targeted by North Korean APT groups using USB-based malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of unpatched Cisco SD-WAN vulnerability with sophisticated evasion techniques
- **Web Shell Deployment**: Command injection attacks against FreePBX systems for persistent access
- **USB-Based Air-Gap Bridging**: North Korean groups using removable drives to breach isolated networks
- **Cloud C2 Infrastructure**: APT37 and ScarCruft leveraging Zoho WorkDrive for command-and-control communications
- **Blockchain-Based Botnet**: Aeternum C2 botnet storing encrypted commands on Polygon blockchain to evade takedowns
- **Trojanized Gaming Tools**: Java-based RATs distributed through compromised gaming utilities via browsers and chat platforms
- **Malicious Go Modules**: Cryptocurrency-themed modules designed to harvest passwords and deploy Linux backdoors

## Threat Actor Activities

- **APT37 (North Korea)**: Deploying new malware tools to breach air-gapped networks using USB drives for data exfiltration and covert surveillance operations
- **ScarCruft (North Korea)**: Using Zoho WorkDrive for C2 communications and USB malware to target air-gapped environments with sophisticated backdoors
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with advanced evasion capabilities
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, disrupted by Europol operation resulting in 30 arrests
- **Ransomware Operations**: Continued attacks on healthcare systems with payment rates dropping to record low 28% despite surge in attacks