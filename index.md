# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting enterprise infrastructure and air-gapped networks. The most severe ongoing exploitation involves CVE-2025-0282, a zero-day vulnerability in Ivanti Connect devices that has enabled attackers to deploy RESURGE malware with dormant capabilities. Additionally, CVE-2026-20127, a maximum-severity Cisco SD-WAN vulnerability, has been actively exploited for three years by sophisticated threat actors. North Korean groups APT37 and ScarCruft are conducting advanced operations targeting air-gapped networks through USB-based malware and cloud services abuse. Over 900 Sangoma FreePBX instances remain compromised with web shells, while threat actors continue exploiting Google Cloud API keys to access Gemini AI data and Trend Micro Apex One critical vulnerabilities for remote code execution.

## Active Exploitation Details

### RESURGE Malware on Ivanti Devices
- **Description**: A sophisticated malicious implant targeting Ivanti Connect devices through zero-day exploitation, with capabilities to remain dormant on compromised systems
- **Impact**: Enables persistent access and can remain undetected for extended periods on enterprise network infrastructure
- **Status**: Actively exploited in zero-day attacks, CISA has released new threat details
- **CVE ID**: CVE-2025-0282

### Cisco SD-WAN Zero-Day
- **Description**: A maximum-severity vulnerability in Cisco SD-WAN infrastructure that has been exploited for an extended period
- **Impact**: Allows sophisticated threat actors to compromise network infrastructure with minimal evidence
- **Status**: Exploited for 3 years by unknown but sophisticated threat actors
- **CVE ID**: CVE-2026-20127

### Sangoma FreePBX Command Injection
- **Description**: A command injection vulnerability in FreePBX systems enabling web shell deployment
- **Impact**: Remote code execution and persistent access to VoIP infrastructure
- **Status**: Over 900 instances still compromised with ongoing web shell attacks since December

### Trend Micro Apex One Vulnerabilities
- **Description**: Critical vulnerabilities in Trend Micro Apex One security software allowing remote code execution
- **Impact**: Attackers can gain remote code execution on vulnerable Windows systems running the security software
- **Status**: Recently patched but previously exploitable for RCE

### Juniper Networks PTX Router Flaw
- **Description**: Critical vulnerability in Junos OS Evolved network operating system on PTX Series routers
- **Impact**: Allows unauthenticated attackers to execute code remotely with root privileges, enabling full router takeover
- **Status**: Critical vulnerability requiring immediate patching

## Affected Systems and Products

- **Ivanti Connect Devices**: Network appliances vulnerable to RESURGE malware deployment through zero-day exploitation
- **Cisco SD-WAN Infrastructure**: Enterprise networking equipment compromised through long-term exploitation
- **Sangoma FreePBX Systems**: Over 900 VoIP systems infected with web shells following command injection attacks
- **Google Cloud API Keys**: Thousands of public API keys with unintended Gemini AI access capabilities
- **Trend Micro Apex One**: Windows security software with critical remote code execution vulnerabilities
- **Juniper PTX Series Routers**: Network infrastructure running Junos OS Evolved vulnerable to complete takeover
- **Air-Gapped Networks**: Isolated systems targeted through USB-based malware and removable drive attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in enterprise infrastructure like Ivanti and Cisco systems
- **USB-Based Attacks**: Deployment of malware through removable drives to breach air-gapped networks and facilitate data exfiltration
- **Web Shell Deployment**: Command injection attacks resulting in persistent backdoor access through web shells
- **Cloud Service Abuse**: Misuse of legitimate cloud services like Zoho WorkDrive for command-and-control communications
- **API Key Exploitation**: Abuse of exposed Google Cloud API keys to access sensitive Gemini AI endpoints and private data
- **Blockchain C2 Infrastructure**: Use of blockchain technology for resilient command-and-control operations to evade takedown efforts
- **Trojanized Software**: Distribution of malicious gaming utilities through browsers and chat platforms to deploy remote access trojans

## Threat Actor Activities

- **APT37 (North Korean)**: Deploying new tools to breach air-gapped networks using removable drives for covert surveillance and data movement
- **ScarCruft (North Korean)**: Using Zoho WorkDrive and USB malware for sophisticated air-gapped network infiltration campaigns
- **UAT-10027**: Targeting U.S. education and healthcare sectors with Dohdoor backdoor malware since December 2025
- **The Com Cybercrime Collective**: Online group targeting children and teenagers, resulting in 30 arrests through Europol's Project Compass operation
- **Kimwolf Botnet Operators**: Operating what is described as the world's largest and most disruptive botnet through disclosed vulnerabilities
- **Unknown Sophisticated Actors**: Exploiting Cisco SD-WAN infrastructure for three years while leaving minimal forensic evidence