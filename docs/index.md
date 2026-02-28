# Exploitation Report

Critical exploitation activity continues to surge across multiple attack vectors, with several significant zero-day vulnerabilities and ongoing campaigns targeting enterprise infrastructure. The most concerning developments include a three-year exploitation campaign against Cisco SD-WAN systems through CVE-2026-20127, persistent infections of over 900 Sangoma FreePBX instances via web shell attacks, and sophisticated North Korean threat actors deploying new malware to breach air-gapped networks. Additional critical vulnerabilities have been identified in Trend Micro Apex One and Juniper Networks PTX routers, while threat actors continue leveraging novel techniques including blockchain-based command and control infrastructure and AI-powered fake document generation.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN systems that has been actively exploited by sophisticated threat actors
- **Impact**: Full compromise of SD-WAN infrastructure with potential for network-wide lateral movement
- **Status**: Under active exploitation for approximately three years; patches recently released
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure Zero-Day Exploitation
- **Description**: Zero-day vulnerability being exploited to deploy RESURGE malware implants on Ivanti devices
- **Impact**: Persistent backdoor access with dormant capabilities that can remain undetected
- **Status**: Active exploitation ongoing; CISA has issued warnings about dormant malware presence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection Vulnerability
- **Description**: Command injection flaw in FreePBX systems allowing web shell deployment
- **Impact**: Complete system compromise with persistent backdoor access via web shells
- **Status**: Over 900 instances remain compromised despite patches being available since December

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Apex One security software
- **Impact**: Full system compromise on Windows systems running vulnerable Apex One installations
- **Status**: Critical patches released; immediate patching required

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved running on PTX Series routers
- **Impact**: Unauthenticated remote code execution with root privileges, enabling full router takeover
- **Status**: Critical severity; patches available

## Affected Systems and Products

- **Cisco SD-WAN Systems**: All versions affected by three-year exploitation campaign
- **Sangoma FreePBX**: Over 900 instances currently infected with web shells
- **Ivanti Connect Secure**: Devices vulnerable to RESURGE malware implants
- **Trend Micro Apex One**: Windows systems running vulnerable versions
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved
- **Google API Services**: Previously harmless Maps API keys now expose Gemini AI data
- **Healthcare Systems**: Ransomware attacks targeting hospital infrastructure
- **Education Sector**: Targeted by UAT-10027 threat group with Dohdoor backdoor

## Attack Vectors and Techniques

- **Web Shell Deployment**: Persistent backdoor access through compromised FreePBX systems
- **USB-Based Air-Gap Bridging**: North Korean APT37 using removable drives to breach isolated networks
- **Zoho WorkDrive C2**: ScarCruft leveraging legitimate cloud services for command and control
- **Blockchain-Based C2**: Aeternum botnet storing encrypted commands on Polygon blockchain
- **Trojanized Gaming Tools**: Java-based RATs distributed via browsers and chat platforms
- **AI-Powered Fake Documents**: OnlyFake generating over 10,000 fraudulent identification documents
- **Malicious Go Modules**: Password harvesting and Rekoobe backdoor deployment
- **Social Engineering**: Deceptive celebrity-bait advertising scams across social platforms

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools to breach air-gapped networks using USB-based propagation and covert surveillance capabilities
- **ScarCruft (North Korean)**: Utilizing Zoho WorkDrive for C2 communications and developing sophisticated USB malware for air-gap bridging
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **The Com Cybercrime Collective**: Online group targeting children and teenagers; 30 arrests made in Europol-coordinated "Project Compass" operation
- **Sophisticated Unknown Actor**: Three-year exploitation campaign against Cisco SD-WAN systems with minimal forensic evidence
- **Multiple Ransomware Groups**: Continued targeting of healthcare systems with payment rates dropping to record low of 28%