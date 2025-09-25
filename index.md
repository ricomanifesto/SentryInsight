# Exploitation Report

Critical zero-day vulnerabilities in Cisco networking infrastructure are being actively exploited by attackers, with CISA issuing emergency directives for federal agencies to patch affected systems. Multiple threat actors continue aggressive campaigns targeting organizations through fake update schemes, supply chain attacks, and social engineering tactics. Notable activities include North Korean hackers deploying new backdoors against cryptocurrency developers, Chinese espionage groups infiltrating government systems globally, and financially motivated actors leveraging sophisticated distribution channels to deploy malware payloads.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting Cisco ASA (Adaptive Security Appliance) firewall software that allow attackers to compromise network security infrastructure
- **Impact**: Complete compromise of firewall security controls, potential network infiltration and lateral movement
- **Status**: Actively exploited in the wild, patches available, CISA emergency directive issued for federal agencies

### Cisco IOS/IOS XE SNMP Vulnerability
- **Description**: High-severity security flaw in Cisco IOS Software and IOS XE Software affecting SNMP (Simple Network Management Protocol) implementation
- **Impact**: Remote code execution or denial-of-service conditions on network devices
- **Status**: Currently being exploited in attacks, security updates released

### GeoServer Critical Vulnerability
- **Description**: Critical flaw in GeoServer geospatial software that enables remote exploitation
- **Impact**: Complete system compromise and unauthorized access to federal agency networks
- **Status**: Exploited within two weeks of disclosure to breach a large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce ForcedLeak Vulnerability
- **Description**: Critical flaw in Salesforce Agentforce AI platform enabling data exfiltration through prompt injection attacks
- **Impact**: Exposure of sensitive CRM data through malicious AI prompt manipulation
- **Status**: Patched by Salesforce

### OnePlus OxygenOS SMS Access Vulnerability
- **Description**: Vulnerability in multiple OnePlus OxygenOS versions allowing unauthorized SMS access
- **Impact**: Any installed app can access SMS data and metadata without permissions or user interaction
- **Status**: Currently unpatched

## Affected Systems and Products

- **Cisco ASA Firewalls**: Multiple versions of Adaptive Security Appliance firewall software
- **Cisco IOS/IOS XE Devices**: Network routers and switches running affected software versions
- **GeoServer**: Geospatial data server software used by federal agencies
- **Salesforce Agentforce**: AI agent building platform
- **OnePlus Smartphones**: Multiple OxygenOS versions affected
- **Supermicro BMC**: Baseboard Management Controller firmware enabling persistent backdoors
- **Rust Crates Repository**: Malicious packages on Crates.io targeting cryptocurrency developers

## Attack Vectors and Techniques

- **Drive-By Downloads**: FAKEUPDATES campaigns using SEO poisoning and fake browser update notifications
- **Social Engineering**: Job posting spoofing and ClickFix techniques to deliver malicious payloads
- **Supply Chain Attacks**: Malicious packages in software repositories stealing cryptocurrency wallet keys
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in network infrastructure
- **AI Prompt Injection**: Manipulation of AI systems to extract sensitive data
- **Firmware Manipulation**: Creation of persistent backdoors through BMC vulnerabilities

## Threat Actor Activities

- **UNC2165**: Resumed operations using FAKEUPDATES distribution channels, deploying COLORFAKE.V2 dropper and MYTHIC payloads via UNC1543 infrastructure
- **UNC5518**: Evolved FAKETREFF JavaScript downloader campaigns with enhanced obfuscation and multi-stage deployment techniques
- **FIN6**: Ongoing campaign since December 2022 targeting corporate recruiters through spoofed job postings, distributing BULLZLINK and SQUIDSLEEP payloads
- **Scattered Spider**: Major ransomware operations resulting in $107 million losses for Co-operative Group UK, with recent arrests of teen members
- **North Korean APT**: Contagious Interview campaign deploying AkdoorTea backdoor alongside TsunamiKit against cryptocurrency developers
- **RedNovember (Chinese APT)**: Global espionage operations targeting governments across multiple continents using Pantegana and Cobalt Strike
- **UNC5221 (China-nexus)**: BRICKSTORM backdoor deployment against U.S. legal services, SaaS providers, and technology sectors