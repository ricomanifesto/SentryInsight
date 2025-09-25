# Exploitation Report

The cybersecurity landscape is currently facing several critical zero-day exploitations and active threat campaigns. Most notably, Cisco ASA firewalls are under active zero-day attack, prompting CISA to issue an emergency directive for federal agencies. Chinese APT groups are deploying sophisticated backdoors on edge devices, while North Korean hackers continue targeting cryptocurrency developers with new malware variants. Supply chain attacks are proliferating across package repositories, with malicious npm and Rust packages stealing sensitive data. Additionally, a federal agency breach through a GeoServer vulnerability highlights the ongoing exploitation of recently disclosed flaws.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) VPN web servers
- **Impact**: Attackers can exploit these flaws to compromise firewall systems and potentially gain network access
- **Status**: Actively exploited in the wild; CISA issued emergency directive for federal agencies to patch immediately

### Cisco IOS SNMP Vulnerability
- **Description**: High-severity security flaw in IOS Software and IOS XE Software related to SNMP functionality
- **Impact**: Remote attackers can execute arbitrary code or trigger denial-of-service conditions
- **Status**: Actively exploited; patches available

### GeoServer Critical Vulnerability
- **Description**: Critical vulnerability in GeoServer geospatial software
- **Impact**: Complete system compromise allowing unauthorized access to federal systems
- **Status**: Exploited less than two weeks after initial disclosure; used to breach large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce AI platform allowing prompt injection attacks
- **Impact**: Attackers can potentially exfiltrate CRM data through AI prompt manipulation
- **Status**: Recently patched by Salesforce

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two vulnerabilities in Supermicro Baseboard Management Controller (BMC) firmware
- **Impact**: Attackers can create persistent backdoors by updating systems with maliciously crafted firmware images
- **Status**: Recently disclosed; affects hardware-level security

### Wondershare RepairIt Critical Flaws
- **Description**: Two security flaws in Wondershare RepairIt software
- **Impact**: Exposure of private user data and potential AI model tampering
- **Status**: Recently disclosed vulnerabilities

## Affected Systems and Products

- **Cisco ASA Firewalls**: Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD)
- **Cisco Network Equipment**: IOS Software and IOS XE Software with SNMP functionality
- **GeoServer**: Geospatial software used by federal agencies
- **Salesforce Agentforce**: AI agent platform for CRM systems
- **Supermicro Hardware**: Systems with Baseboard Management Controller (BMC) firmware
- **Edge Devices**: Network appliances that cannot run traditional EDR agents
- **Package Repositories**: npm registry (postmark-mcp package) and Rust Crates.io (fast_log impersonation packages)
- **Wondershare RepairIt**: File repair software exposing user data and AI models

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Cisco ASA firewalls and IOS devices
- **Supply Chain Poisoning**: Malicious packages deployed to npm and Crates.io repositories with credential theft capabilities
- **AI Prompt Injection**: Manipulation of Salesforce AI agents through crafted prompts to extract CRM data
- **Firmware Backdoors**: Installation of persistent backdoors through malicious BMC firmware updates
- **Social Engineering**: North Korean hackers using fake job interviews to deploy AkdoorTea backdoor
- **Network Device Compromise**: Chinese APT groups targeting edge devices with BRICKSTORM backdoors
- **DNS Infrastructure Abuse**: Vane Viper generating 1 trillion DNS queries for malware distribution and ad fraud

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying BRICKSTORM backdoors on edge devices, targeting U.S. legal and technology sectors with focus on network appliances that cannot run traditional EDR
- **North Korean APT**: Using AkdoorTea backdoor in Contagious Interview campaigns targeting cryptocurrency developers globally, along with TsunamiKit tools
- **Chinese RedNovember Group**: Conducting cyber espionage against global governments using Pantegana and Cobalt Strike, targeting organizations across Africa, Asia, North America, South America, and Oceania
- **Scattered Spider**: Responsible for $107 million loss to Co-operative Group in the U.K.; recent claims of group shutdown following teen member surrender
- **Vane Viper**: Operating global malware and ad fraud network through shell companies, generating massive DNS query volumes for malicious infrastructure
- **Supply Chain Attackers**: Deploying malicious packages across multiple repositories (npm, Crates.io) to steal cryptocurrency wallet keys and email communications