# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting enterprise infrastructure and air-gapped networks. Most concerning is the active exploitation of CVE-2025-0282 in Ivanti Connect Secure devices through the RESURGE malware, and CVE-2026-20127, a maximum-severity Cisco SD-WAN zero-day that has been exploited for three years by sophisticated threat actors. North Korean APT groups APT37 and ScarCruft are deploying new malware tools to breach air-gapped systems, while over 900 Sangoma FreePBX instances remain compromised through ongoing web shell attacks. The healthcare sector faces particular risk with ongoing ransomware campaigns, and new attack vectors include trojanized gaming utilities and blockchain-based command-and-control infrastructure.

## Active Exploitation Details

### Ivanti Connect Secure Zero-Day Exploitation
- **Description**: CISA has released details about RESURGE malware exploiting a zero-day vulnerability in Ivanti Connect Secure devices
- **Impact**: Allows attackers to deploy malicious implants that can remain dormant on compromised devices
- **Status**: Zero-day exploitation is ongoing; CISA has issued warnings about persistent threats
- **CVE ID**: CVE-2025-0282

### Cisco SD-WAN Critical Zero-Day
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure has been exploited for three years
- **Impact**: Enables sophisticated threat actors to gain unauthorized access to network infrastructure
- **Status**: Actively exploited by unknown sophisticated threat actors with minimal forensic evidence
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection
- **Description**: Web shell attacks exploiting a command injection vulnerability in FreePBX systems
- **Impact**: Over 900 instances remain compromised with persistent web shell access
- **Status**: Ongoing attacks with widespread compromise since December

### Trend Micro Apex One Critical Flaws
- **Description**: Two critical vulnerabilities in Trend Micro Apex One security software
- **Impact**: Remote code execution on vulnerable Windows systems
- **Status**: Recently patched but vulnerable systems remain at risk

### Juniper Networks PTX Router Vulnerability
- **Description**: Critical vulnerability in Junos OS Evolved running on PTX Series routers
- **Impact**: Unauthenticated remote code execution with root privileges, allowing full router takeover
- **Status**: Recently disclosed critical vulnerability requiring immediate patching

## Affected Systems and Products

- **Ivanti Connect Secure**: Zero-day exploitation with persistent RESURGE malware implants
- **Cisco SD-WAN Infrastructure**: Three-year exploitation campaign targeting network devices
- **Sangoma FreePBX**: Over 900 instances compromised with web shells
- **Trend Micro Apex One**: Windows security software with critical RCE vulnerabilities
- **Juniper Networks PTX Series**: Routers running Junos OS Evolved vulnerable to complete takeover
- **Google API Services**: Previously harmless API keys now expose Gemini AI data and private information
- **Healthcare Systems**: Multiple ransomware attacks targeting hospital infrastructure
- **Air-Gapped Networks**: North Korean APT groups targeting isolated systems via USB-based malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active targeting of unpatched vulnerabilities in enterprise security appliances
- **Web Shell Deployment**: Persistent compromise of FreePBX systems through command injection
- **USB-Based Malware**: APT37 and ScarCruft using removable drives to breach air-gapped networks
- **Blockchain C2 Infrastructure**: Aeternum C2 botnet storing encrypted commands on Polygon blockchain
- **Trojanized Gaming Tools**: Java-based RATs distributed through browsers and chat platforms
- **Cloud Service Abuse**: ScarCruft using Zoho WorkDrive for command-and-control communications
- **API Key Exploitation**: Google API keys being repurposed to access Gemini AI data
- **Social Engineering**: Gaming utilities and fake applications used as initial attack vectors

## Threat Actor Activities

- **APT37 (North Korea)**: Deploying new tools to move data between internet-connected and air-gapped systems through USB-based malware
- **ScarCruft (North Korea)**: Using Zoho WorkDrive and USB malware to breach air-gapped networks with custom backdoors
- **UAT-10027**: Previously undocumented threat cluster targeting U.S. education and healthcare sectors with Dohdoor backdoor since December 2025
- **Unknown Sophisticated Actor**: Three-year exploitation campaign against Cisco SD-WAN infrastructure with minimal forensic traces
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, with 30 arrests from Europol operation
- **Ransomware Groups**: Ongoing campaigns against healthcare systems despite declining payment rates