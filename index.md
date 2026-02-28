# Exploitation Report

Current threat landscape analysis reveals several critical active exploitation campaigns targeting enterprise infrastructure, network equipment, and air-gapped systems. The most significant ongoing activities include a three-year exploitation campaign against Cisco SD-WAN infrastructure, active web shell deployment against Sangoma FreePBX systems, and sophisticated North Korean operations targeting air-gapped networks. Additionally, critical vulnerabilities in Ivanti Connect devices are being exploited with dormant malware capabilities, while enterprise security solutions face remote code execution threats.

## Active Exploitation Details

### Cisco SD-WAN Zero-Day Vulnerability
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been under active exploitation by sophisticated threat actors
- **Impact**: Attackers can gain unauthorized access to SD-WAN infrastructure, potentially compromising network routing and security controls
- **Status**: Actively exploited for 3 years; sophisticated threat actor left minimal evidence
- **CVE ID**: CVE-2026-20127

### Ivanti Connect Zero-Day with RESURGE Malware
- **Description**: Zero-day vulnerability in Ivanti Connect devices being exploited to deploy RESURGE malware implants
- **Impact**: Allows attackers to establish persistent presence on corporate VPN infrastructure with dormant malware capabilities
- **Status**: Active exploitation with CISA warnings about dormant malware persistence
- **CVE ID**: CVE-2025-0282

### Sangoma FreePBX Command Injection
- **Description**: Command injection vulnerability in Sangoma FreePBX systems allowing web shell deployment
- **Impact**: Attackers gain persistent access to VoIP infrastructure, potentially intercepting communications and pivoting to internal networks
- **Status**: Over 900 instances remain infected with web shells despite ongoing attacks since December

### Trend Micro Apex One Remote Code Execution
- **Description**: Critical vulnerabilities in Trend Micro Apex One security platform allowing remote code execution
- **Impact**: Attackers can execute arbitrary code on Windows systems protected by the security solution
- **Status**: Recently patched but represents significant risk to enterprise endpoints

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved running on PTX Series routers
- **Impact**: Unauthenticated remote code execution with root privileges, allowing complete router takeover
- **Status**: Critical severity requiring immediate patching

## Affected Systems and Products

- **Cisco SD-WAN Infrastructure**: Network routing and security appliances across enterprise environments
- **Ivanti Connect**: Corporate VPN and remote access infrastructure
- **Sangoma FreePBX**: Voice over IP (VoIP) communication systems and telephony infrastructure
- **Trend Micro Apex One**: Enterprise endpoint protection platforms on Windows systems
- **Juniper PTX Series Routers**: Enterprise and service provider networking equipment
- **Google API Services**: Gemini AI data exposure through Maps API keys
- **Air-Gapped Networks**: Isolated systems targeted through USB-based malware propagation

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Sophisticated actors leveraging unknown vulnerabilities in network infrastructure
- **Web Shell Deployment**: Persistent backdoors installed on compromised FreePBX systems
- **USB-Based Air-Gap Bridging**: North Korean actors using removable media to breach isolated networks
- **Command Injection**: Direct system command execution through vulnerable web interfaces
- **Blockchain C2 Infrastructure**: Aeternum botnet using Polygon blockchain for resilient command channels
- **Cloud Service Abuse**: Zoho WorkDrive leveraged for covert command and control communications
- **Trojanized Gaming Tools**: Java-based RAT distribution through gaming utilities and chat platforms
- **API Key Abuse**: Google Maps API keys repurposed for Gemini AI data access

## Threat Actor Activities

- **APT37/ScarCruft (North Korean)**: Deploying new tools for air-gapped network infiltration using USB malware and Zoho WorkDrive for C2
- **UAT-10027**: Targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **Unknown Sophisticated Actor**: Three-year campaign against Cisco SD-WAN with advanced evasion techniques
- **The Com Collective**: Online cybercrime group targeting children and teenagers, disrupted by Europol operation
- **Ransomware Groups**: Continued hospital targeting despite decreasing payment rates (28% all-time low)
- **Cryptocurrency Scammers**: Pig butchering operations resulting in $61 million Tether seizure by DoJ