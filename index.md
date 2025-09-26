# Exploitation Report

Multiple critical zero-day vulnerabilities are currently under active exploitation, with Cisco firewall systems facing the most severe immediate threat. CISA has issued emergency directives regarding two zero-day flaws in Cisco ASA and FTD firewall products that are being actively exploited in the wild. Additionally, threat actors are exploiting a critical GeoServer vulnerability to breach federal agencies, while sophisticated supply chain attacks target developers through malicious packages in npm and Rust ecosystems. Chinese APT groups continue aggressive campaigns against global organizations using advanced backdoors on network edge devices, and North Korean hackers are deploying new malware to target cryptocurrency developers worldwide.

## Active Exploitation Details

### Cisco ASA and FTD Firewall Zero-Days
- **Description**: Two critical zero-day vulnerabilities affecting Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) VPN web servers
- **Impact**: Attackers can gain unauthorized access to firewall systems and potentially compromise entire network infrastructures
- **Status**: Actively exploited in the wild; CISA has issued emergency directive ordering federal agencies to patch immediately; patches available from Cisco

### Cisco IOS SNMP Vulnerability
- **Description**: High-severity flaw in Cisco IOS Software and IOS XE Software affecting SNMP functionality
- **Impact**: Remote code execution or denial-of-service conditions on network infrastructure devices
- **Status**: Actively exploited; patches available

### GeoServer Critical Flaw
- **Description**: Critical vulnerability in GeoServer geospatial software used by government agencies
- **Impact**: Complete system compromise and unauthorized access to sensitive government data
- **Status**: Exploited within two weeks of disclosure to breach a large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce AI Prompt Injection
- **Description**: Critical "ForcedLeak" vulnerability in Salesforce Agentforce AI platform allowing data exfiltration through prompt injection attacks
- **Impact**: Unauthorized access to sensitive CRM data through AI prompt manipulation
- **Status**: Patched by Salesforce; proof-of-concept demonstrated by security researchers

## Affected Systems and Products

- **Cisco ASA/FTD Firewalls**: VPN web servers in enterprise network security appliances
- **Cisco IOS/IOS XE**: Network infrastructure devices running affected software versions
- **GeoServer**: Geospatial data servers used by federal agencies and organizations
- **Salesforce Agentforce**: AI agent platform for customer relationship management
- **Supermicro BMC**: Baseboard Management Controller firmware in server hardware
- **npm Package Registry**: Malicious postmark-mcp package targeting email communications
- **Rust Crates.io**: Malicious packages fast_log and fats_log targeting cryptocurrency developers
- **Network Edge Devices**: Appliances targeted by Chinese APT groups that cannot run traditional EDR agents

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Immediate weaponization of unpatched vulnerabilities in critical infrastructure
- **Supply Chain Attacks**: Malicious packages in npm and Rust repositories targeting developers
- **AI Prompt Injection**: Manipulation of AI systems to extract sensitive data through crafted prompts
- **Network Device Compromise**: Targeting edge devices and BMC firmware for persistent access
- **Social Engineering**: North Korean actors using fake job interviews to deploy malware
- **DNS Manipulation**: Vane Viper generating over 1 trillion DNS queries for malware and ad fraud operations

## Threat Actor Activities

- **UNC5221 (Chinese APT)**: Deploying BRICKSTORM backdoors on network edge devices targeting U.S. legal, technology, and SaaS sectors
- **RedNovember (Chinese APT)**: Global espionage campaign using Pantegana and Cobalt Strike against government and private sector organizations across multiple continents
- **North Korean APT**: Contagious Interview campaign deploying AkdoorTea backdoor, TsunamiKit, and other tools to target cryptocurrency developers worldwide
- **Scattered Spider**: Despite claims of shutdown, the group caused $107 million in losses to UK Co-operative Group; teen member recently surrendered to authorities
- **Vane Viper**: Operating massive malware and ad fraud network through shell companies and generating enormous DNS query volumes
- **Unknown APT Groups**: Actively exploiting Cisco zero-days and GeoServer vulnerabilities for network infiltration and data theft