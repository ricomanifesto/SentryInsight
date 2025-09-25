# Exploitation Report

Critical zero-day vulnerabilities in Cisco networking infrastructure are being actively exploited in the wild, prompting emergency directives from CISA to federal agencies. Simultaneously, multiple threat actors including North Korean groups, Chinese espionage clusters, and financially motivated cybercriminals are conducting sophisticated campaigns targeting organizations across various sectors. These activities span from supply chain attacks through malicious packages to social engineering campaigns using fake job postings and browser updates, while established groups like Scattered Spider continue to cause significant financial damage despite recent law enforcement actions.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting Cisco ASA (Adaptive Security Appliance) firewall software that are being actively exploited in attacks
- **Impact**: Attackers can exploit these flaws to compromise firewall security and potentially gain unauthorized access to protected networks
- **Status**: Active exploitation confirmed; CISA has issued emergency directive ordering federal agencies to patch immediately

### Cisco IOS/IOS XE SNMP Vulnerability  
- **Description**: High-severity security flaw in Cisco IOS Software and IOS XE Software affecting SNMP functionality
- **Impact**: Remote attackers can execute arbitrary code or trigger denial-of-service conditions
- **Status**: Currently being exploited in attacks; security updates released by Cisco

### Critical GeoServer Vulnerability
- **Description**: Critical vulnerability in GeoServer that was exploited by threat actors to breach a federal agency
- **Impact**: Complete compromise of affected systems and unauthorized access to sensitive government data
- **Status**: Exploited less than two weeks after initial disclosure to breach large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce ForcedLeak Bug
- **Description**: Critical flaw in Salesforce Agentforce platform that allows AI prompt injection attacks
- **Impact**: Attackers can potentially exfiltrate sensitive CRM data through manipulated AI agent interactions
- **Status**: Recently patched by Salesforce following security researcher disclosure

## Affected Systems and Products

- **Cisco ASA Firewalls**: Multiple versions affected by zero-day vulnerabilities requiring immediate patching
- **Cisco IOS/IOS XE Software**: SNMP functionality compromised across affected versions
- **GeoServer**: Geospatial server software used by federal agencies
- **Salesforce Agentforce**: AI agent building platform vulnerable to prompt injection
- **Supermicro BMC Firmware**: Baseboard Management Controller vulnerabilities allowing persistent backdoors
- **OnePlus OxygenOS**: Multiple versions allowing unauthorized SMS access
- **Rust Crate Repository**: Malicious packages targeting cryptocurrency developers
- **Windows Systems**: Targeted by various malware campaigns and social engineering attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in critical infrastructure
- **Supply Chain Attacks**: Malicious packages in legitimate software repositories (Rust crates)
- **Social Engineering**: Fake browser updates, job posting lures, and ClickFix techniques
- **AI Prompt Injection**: Manipulation of AI systems to extract sensitive data
- **Drive-By Downloads**: FAKEUPDATES campaigns delivering multiple malware payloads
- **Firmware Manipulation**: BMC vulnerabilities enabling persistent backdoor installation
- **SNMP-Based Attacks**: Remote code execution through network management protocols

## Threat Actor Activities

- **UNC2165**: Resumed operations after dormancy, leveraging SEO poisoning and FAKEUPDATES to deliver COLORFAKE.V2 and MYTHIC payloads
- **UNC5518**: Distributing FAKETREFF JavaScript downloader using fake error messages and ClickFix social engineering since April 2024
- **FIN6**: Ongoing campaign since December 2022 targeting corporate recruiters through spoofed job postings to distribute BULLZLINK and SQUIDSLEEP payloads
- **Scattered Spider**: Caused $107 million in losses to Co-operative Group in recent attack; teen member recently surrendered to authorities
- **North Korean APT**: Contagious Interview campaign using new AkdoorTea backdoor, TsunamiKit, and other tools to target cryptocurrency developers globally
- **RedNovember (Chinese APT)**: Targeting global government and private sector organizations across multiple continents using Pantegana and Cobalt Strike
- **UNC5221 (Chinese APT)**: Using BRICKSTORM backdoor to infiltrate U.S. legal services, SaaS providers, and technology sectors
- **Russian Disinformation Groups**: Conducting information warfare campaigns targeting Moldovan elections