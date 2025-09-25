# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation, with Cisco firewall systems being targeted in the most urgent attacks. Two zero-day flaws in Cisco ASA and FTD firewalls are being actively exploited in the wild, prompting CISA to issue an emergency directive for federal agencies. Additional active exploitation includes an SNMP vulnerability in Cisco IOS software allowing remote code execution, and a GeoServer flaw that was exploited to breach a federal agency within two weeks of disclosure. Multiple APT groups are conducting sophisticated campaigns, including Chinese threat actors deploying BRICKSTORM backdoors on edge devices and North Korean groups targeting cryptocurrency developers with new malware variants.

## Active Exploitation Details

### **Cisco ASA and FTD Zero-Day Vulnerabilities**
- **Description**: Two zero-day vulnerabilities affecting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD)
- **Impact**: Attackers can compromise firewall systems and potentially gain network access
- **Status**: Actively being exploited in attacks; CISA has issued an emergency directive for federal agencies to patch immediately

### **Cisco IOS SNMP Vulnerability**
- **Description**: High-severity security flaw in IOS Software and IOS XE Software affecting SNMP functionality
- **Impact**: Remote attackers can execute arbitrary code or trigger denial-of-service conditions
- **Status**: Currently being exploited in attacks; security updates available

### **GeoServer Critical Vulnerability**
- **Description**: Critical flaw in GeoServer geospatial software
- **Impact**: Complete system compromise and unauthorized access to federal agency systems
- **Status**: Exploited within two weeks of disclosure to breach a large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### **Salesforce ForcedLeak AI Prompt Injection**
- **Description**: Critical vulnerability in Salesforce Agentforce platform allowing AI prompt injection attacks
- **Impact**: Potential exfiltration of CRM data through manipulation of AI agents
- **Status**: Recently patched by Salesforce

## Affected Systems and Products

- **Cisco ASA Software**: VPN web server components affected by zero-day vulnerabilities
- **Cisco FTD Software**: Firewall threat defense systems vulnerable to active exploits
- **Cisco IOS/IOS XE Software**: Network devices with SNMP functionality exposed to RCE attacks
- **GeoServer**: Geospatial server software used by federal agencies
- **Salesforce Agentforce**: AI agent platform vulnerable to data exfiltration
- **Supermicro BMC**: Baseboard Management Controller firmware allowing persistent backdoor creation
- **Edge Network Devices**: Various network appliances targeted by Chinese APT groups
- **Rust Crate Ecosystem**: Malicious packages targeting cryptocurrency wallet keys

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Cisco firewall systems
- **SNMP-Based RCE**: Remote code execution through Simple Network Management Protocol vulnerabilities
- **DLL Search Order Hijack**: BLACKWIDOW trojan uses DLL hijacking to maintain persistence
- **AI Prompt Injection**: Manipulation of AI agents to extract sensitive CRM data
- **Supply Chain Attacks**: Malicious Rust packages distributed through official repositories
- **ClickFix Social Engineering**: Fraudulent repair prompts to deploy ZAPCAT backdoors
- **BMC Firmware Manipulation**: Installation of malicious firmware images for persistent access
- **DNS Infrastructure Abuse**: Generation of massive DNS queries for malware and ad fraud operations

## Threat Actor Activities

- **UNC6258/UNC6259**: Multi-stage financially motivated campaign deploying ZAPCAT backdoor and providing ransomware affiliate access
- **UNC5221 (Chinese APT)**: Targeting U.S. legal and technology sectors with BRICKSTORM backdoors on edge devices
- **RedNovember (Chinese APT)**: Global government targeting using Pantegana malware and Cobalt Strike
- **North Korean APT**: Contagious Interview campaign targeting cryptocurrency developers with AkdoorTea backdoor
- **Scattered Spider**: Major financial losses reported including $107 million impact on Co-op Group; teen member recently surrendered
- **Vane Viper**: Operating massive malware and ad fraud network generating 1 trillion DNS queries
- **Russian State Actors**: Conducting disinformation campaigns targeting Moldovan elections