# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple sectors, with particularly concerning activity targeting infrastructure and enterprise systems. A Cisco SD-WAN zero-day vulnerability (CVE-2026-20127) has been under active exploitation for three years by sophisticated threat actors, while over 900 Sangoma FreePBX instances remain compromised through command injection attacks. North Korean threat groups APT37 and ScarCruft are deploying advanced tools to breach air-gapped networks, and CISA has warned about persistent RESURGE malware on Ivanti devices exploiting CVE-2025-0282. Additional critical vulnerabilities have been disclosed in Trend Micro Apex One and Juniper Networks PTX routers, requiring immediate attention.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been exploited for approximately three years
- **Impact**: Sophisticated threat actors can gain unauthorized access to network infrastructure with minimal forensic evidence
- **Status**: Recently disclosed after years of active exploitation
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Secure Zero-Day
- **Description**: A vulnerability in Ivanti Connect Secure systems being exploited through the RESURGE malware implant
- **Impact**: Attackers can establish persistent presence on affected systems, with malware potentially remaining dormant
- **Status**: Under active exploitation with CISA advisory issued
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: A command injection vulnerability in Sangoma FreePBX systems leading to web shell deployment
- **Impact**: Complete system compromise allowing persistent backdoor access
- **Status**: Over 900 instances remain compromised despite patching efforts

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One allowing remote code execution
- **Impact**: Attackers can achieve full system compromise on vulnerable Windows systems
- **Status**: Recently patched by Trend Micro

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical flaw in Junos OS Evolved running on PTX Series routers
- **Impact**: Unauthenticated attackers can execute code remotely with root privileges, achieving full router takeover
- **Status**: Recently disclosed, patches available

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Network devices and management systems across enterprise environments
- **Ivanti Connect Secure**: VPN and secure access solutions in enterprise networks
- **Sangoma FreePBX**: Open-source PBX telephony systems, over 900 confirmed compromised instances
- **Trend Micro Apex One**: Enterprise endpoint security solutions on Windows platforms
- **Juniper Networks PTX Routers**: High-performance routers running Junos OS Evolved
- **Google API Services**: Maps API keys potentially exposing Gemini AI data
- **Healthcare Systems**: Hospitals and healthcare providers targeted by ransomware campaigns

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of undisclosed vulnerabilities with sophisticated evasion techniques
- **Web Shell Deployment**: Command injection leading to persistent backdoor access via web shells
- **Air-Gapped Network Infiltration**: USB-based malware spreading between isolated and connected systems
- **Blockchain-Based C2**: Aeternum botnet using Polygon blockchain for command and control infrastructure
- **Social Engineering**: Trojanized gaming tools distributed through browsers and chat platforms
- **Remote Code Execution**: Direct system compromise through critical application vulnerabilities

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new tools for air-gapped network infiltration and covert surveillance operations
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for C2 communications and USB malware for air-gapped network breaches
- **UAT-10027**: Previously undocumented threat group targeting U.S. education and healthcare sectors with Dohdoor backdoor
- **Sophisticated Unknown Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with minimal forensic traces
- **The Com Cybercrime Collective**: Targeting children and teenagers, 30 arrests made in Europol-coordinated operation
- **Ransomware Groups**: Continued healthcare targeting despite declining payment rates, with attacks increasing overall