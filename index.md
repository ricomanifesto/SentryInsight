# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities across enterprise infrastructure. The most severe include a maximum-severity Cisco SD-WAN zero-day (CVE-2026-20127) that has been actively exploited for three years, an Ivanti Connect vulnerability (CVE-2025-0282) with persistent RESURGE malware implants, and over 900 compromised Sangoma FreePBX instances affected by command injection attacks. Additionally, advanced persistent threat groups including APT37 and ScarCruft are deploying sophisticated tools to breach air-gapped networks, while new attack vectors are emerging through Google Cloud API key abuse and blockchain-based command-and-control infrastructure.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been under active exploitation by an unknown sophisticated threat actor
- **Impact**: Full system compromise with the ability for attackers to maintain persistent access while leaving minimal forensic evidence
- **Status**: Currently being exploited in the wild for approximately three years before detection
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Vulnerability with RESURGE Malware
- **Description**: Zero-day vulnerability in Ivanti Connect systems being exploited to deploy the RESURGE malicious implant
- **Impact**: Persistent backdoor access that can remain dormant on compromised devices, allowing for long-term unauthorized access
- **Status**: Active exploitation with CISA warning about dormant malware persistence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Full system compromise with over 900 instances currently infected and compromised
- **Status**: Ongoing attacks since December with hundreds of systems remaining compromised

### Trend Micro Apex One Critical Vulnerabilities
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software allowing remote code execution
- **Impact**: Attackers can achieve remote code execution on vulnerable Windows systems running the security software
- **Status**: Critical vulnerabilities patched by Trend Micro, exploitation status unclear

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved network operating system on PTX Series routers
- **Impact**: Unauthenticated attackers can execute code remotely with root privileges, allowing full router takeover
- **Status**: Critical severity flaw requiring immediate patching

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Network infrastructure components running SD-WAN software
- **Ivanti Connect Systems**: Enterprise connectivity and VPN solutions with persistent malware risk
- **Sangoma FreePBX Instances**: Over 900 compromised VoIP and communication systems worldwide
- **Trend Micro Apex One**: Enterprise security software on Windows systems
- **Juniper PTX Series Routers**: Network routing hardware running Junos OS Evolved
- **Google Cloud API Services**: API keys with unexpected Gemini AI access capabilities
- **Air-Gapped Networks**: Isolated systems being targeted through USB-based malware and specialized tools

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Long-term exploitation of previously unknown vulnerabilities with sophisticated evasion techniques
- **Web Shell Deployment**: Command injection leading to persistent web-based backdoor access
- **USB-Based Air-Gap Bridging**: Specialized malware designed to move data between isolated and internet-connected systems
- **API Key Abuse**: Exploitation of Google Cloud API keys to access private Gemini AI data and endpoints
- **Blockchain C2 Infrastructure**: Use of Polygon blockchain for resilient command-and-control communications (Aeternum C2 botnet)
- **Cloud Service Abuse**: Utilization of legitimate cloud services like Zoho WorkDrive for covert communications
- **Trojanized Software Distribution**: Gaming utilities and legitimate tools weaponized to deliver remote access trojans

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new malware tools specifically designed to breach air-gapped networks through removable drives and conduct covert surveillance operations
- **ScarCruft (North Korean)**: Using Zoho WorkDrive for command-and-control communications and deploying USB-based malware to compromise isolated network environments
- **UAT-10027**: Targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025, focusing on critical infrastructure
- **Unknown Sophisticated Actor**: Responsible for the three-year exploitation of Cisco SD-WAN systems, demonstrating advanced persistent capabilities with minimal detection footprint
- **Kimwolf Botmaster "Dort"**: Operating what is described as the world's largest and most disruptive botnet infrastructure
- **The Com Cybercrime Collective**: Online criminal group targeting children and teenagers, with 30 arrests made during Europol's "Project Compass" operation