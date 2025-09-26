# Exploitation Report

Critical zero-day vulnerabilities in Cisco firewall and IOS systems are being actively exploited in the wild, prompting emergency directives from CISA. The most concerning activity involves multiple Cisco ASA firewall zero-days that have been weaponized by nation-state actors, alongside SNMP vulnerabilities in IOS software enabling remote code execution. Additional threats include a federal agency breach through a GeoServer vulnerability, malicious supply chain attacks targeting developers through compromised packages, and sophisticated backdoor deployments by Chinese APT groups on edge devices.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software VPN web server
- **Impact**: Attackers can compromise firewall devices, potentially gaining network access and control
- **Status**: Actively exploited in attacks; CISA issued emergency directive ordering federal agencies to patch immediately

### Cisco SNMP Vulnerability in IOS Software
- **Description**: High-severity security flaw in Cisco IOS Software and IOS XE Software affecting SNMP functionality
- **Impact**: Remote attackers can execute arbitrary code or trigger denial-of-service conditions
- **Status**: Actively exploited; patches available

### GeoServer Critical Vulnerability
- **Description**: Critical flaw in GeoServer geospatial software
- **Impact**: Complete system compromise and unauthorized access to federal agency systems
- **Status**: Exploited within two weeks of disclosure to breach a large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce AI platform vulnerable to indirect prompt injection attacks
- **Impact**: Attackers can exfiltrate sensitive CRM data through malicious prompt injection
- **Status**: Recently patched after disclosure

## Affected Systems and Products

- **Cisco Secure Firewall ASA**: VPN web server components affected by zero-day exploits
- **Cisco Secure Firewall Threat Defense (FTD)**: Software vulnerable to active attacks
- **Cisco IOS Software and IOS XE Software**: SNMP functionality enabling RCE and DoS attacks
- **GeoServer**: Geospatial software used by federal agencies
- **Salesforce Agentforce**: AI agent platform vulnerable to data exfiltration
- **Supermicro BMC Systems**: Baseboard Management Controller firmware allowing persistent backdoors
- **macOS Xcode Development Environment**: Targeted by XCSSET malware variants
- **NPM and Rust Package Repositories**: Compromised with malicious packages stealing credentials

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Nation-state actors leveraging unpatched Cisco vulnerabilities for initial access
- **Supply Chain Attacks**: Malicious packages in NPM and Rust repositories stealing cryptocurrency wallet keys
- **Prompt Injection**: AI-based attacks against Salesforce agents to leak sensitive data
- **Backdoor Deployment**: Chinese APT groups installing persistent "Brickstorm" backdoors on edge devices
- **Firmware Manipulation**: Attackers creating persistent backdoors in Supermicro BMC systems
- **Social Engineering**: Scattered Spider group conducting sophisticated attacks resulting in $107 million losses

## Threat Actor Activities

- **Nation-State Actor (ArcaneDoor Campaign)**: Exploiting multiple Cisco zero-days, previously associated with advanced persistent threats targeting critical infrastructure
- **UNC5221 (Chinese APT)**: Compromising network appliances to deploy "Brickstorm" backdoor variants on edge devices that cannot run traditional EDR agents
- **Scattered Spider**: Conducting high-impact attacks against major organizations, with recent attacks causing $107 million in losses to The Co-operative Group
- **North Korean Hackers**: Using new "AkdoorTea" backdoor in Contagious Interview campaign targeting cryptocurrency developers globally
- **Vane Viper**: Operating malicious ad technology network generating over 1 trillion DNS queries to power malware distribution and ad fraud
- **Russian Disinformation Campaign**: Targeting Moldovan elections through coordinated information warfare operations