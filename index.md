# Exploitation Report

Critical zero-day vulnerabilities are under active exploitation across multiple Cisco platforms, prompting CISA to issue emergency directives for federal agencies. Cisco ASA firewalls and IOS/IOS XE software are experiencing widespread attacks targeting VPN services and SNMP implementations. Meanwhile, sophisticated threat actors are deploying new backdoors including ZAPCAT, BRICKSTORM, and AkdoorTea to compromise network infrastructure and target cryptocurrency developers. Chinese APT groups are particularly active, compromising edge devices and government organizations globally, while a massive DNS-based malware campaign is generating over 1 trillion queries to support ad fraud operations.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two critical zero-day vulnerabilities affecting Cisco Secure Firewall ASA and FTD software VPN web servers
- **Impact**: Remote attackers can gain unauthorized access to firewall systems and potentially compromise network infrastructure
- **Status**: Active exploitation confirmed; patches released by Cisco, CISA emergency directive issued

### Cisco IOS/IOS XE SNMP Vulnerability  
- **Description**: High-severity vulnerability in SNMP implementation of Cisco IOS and IOS XE software
- **Impact**: Remote code execution or denial-of-service conditions on affected network devices
- **Status**: Active exploitation confirmed; security updates released

### GeoServer Critical Vulnerability
- **Description**: Critical flaw in GeoServer geospatial software used by federal agencies
- **Impact**: Complete system compromise and unauthorized access to sensitive geospatial data
- **Status**: Exploited within two weeks of disclosure; federal agency breached
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: AI prompt injection vulnerability in Salesforce Agentforce platform
- **Impact**: Potential exfiltration of sensitive CRM data through malicious AI prompt manipulation
- **Status**: Patched by Salesforce following responsible disclosure

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two vulnerabilities in Baseboard Management Controller firmware allowing malicious firmware updates
- **Impact**: Creation of persistent backdoors with hardware-level access
- **Status**: Recently disclosed; patches available

## Affected Systems and Products

- **Cisco ASA and FTD Software**: VPN web server components across all versions
- **Cisco IOS/IOS XE Software**: SNMP-enabled network devices and routers
- **GeoServer**: Geospatial data servers used by federal civilian executive branch agencies
- **Salesforce Agentforce**: AI agent platform for CRM data processing
- **Supermicro Hardware**: BMC firmware on server and infrastructure systems
- **Network Edge Devices**: Appliances without traditional EDR capabilities targeted by UNC5221
- **Cryptocurrency Development Platforms**: Systems targeted by North Korean AkdoorTea backdoor
- **Rust Development Environment**: Crates.io package repository with malicious packages

## Attack Vectors and Techniques

- **VPN Web Server Exploitation**: Direct attacks against Cisco firewall VPN services
- **SNMP Protocol Abuse**: Exploitation of network management protocol implementations
- **AI Prompt Injection**: Malicious prompts designed to extract sensitive data from AI systems
- **DLL Search Order Hijacking**: BLACKWIDOW trojan deployment technique used by UNC6258
- **ClickFix Social Engineering**: Lure campaigns leading to ZAPCAT backdoor deployment
- **Supply Chain Compromise**: Malicious packages in Rust crates repository targeting crypto wallets
- **Edge Device Infiltration**: BRICKSTORM backdoor deployment on network appliances
- **DNS Infrastructure Abuse**: Vane Viper generating 1 trillion DNS queries for malware distribution

## Threat Actor Activities

- **UNC6258**: Multi-stage campaign using ClickFix lures and BLACKWIDOW trojan for initial access
- **UNC6259**: Ransomware affiliate operations coordinating with UNC6258 for access provision
- **UNC5221**: China-linked APT deploying BRICKSTORM backdoors against US legal and technology sectors
- **North Korean APT**: Contagious Interview campaign using AkdoorTea backdoor to target crypto developers
- **RedNovember**: Chinese espionage group using Pantegana and Cobalt Strike against global governments
- **Vane Viper**: Massive-scale threat actor operating malicious ad technology and DNS infrastructure
- **Scattered Spider**: Financially motivated group responsible for $107 million Co-op losses; recent teen member surrender