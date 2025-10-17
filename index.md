# Exploitation Report

Critical exploitation activity is currently targeting multiple high-profile vulnerabilities across enterprise systems and popular software platforms. Threat actors are actively exploiting zero-day vulnerabilities in Gladinet's CentreStack file-sharing software and Adobe Experience Manager, both receiving maximum severity scores. Nation-state actors have compromised F5 Networks using zero-day exploits to steal BIG-IP source code, while the Clop ransomware group exploited Oracle zero-day vulnerabilities to breach Harvard University. Additionally, attackers are leveraging recently patched Cisco SNMP vulnerabilities to deploy Linux rootkits on networking infrastructure, and sophisticated phishing campaigns are targeting password manager users through social engineering tactics.

## Active Exploitation Details

### Gladinet CentreStack Local File Inclusion Vulnerability
- **Description**: A local file inclusion vulnerability in Gladinet's CentreStack business file-sharing solution that allows unauthorized file access
- **Impact**: Threat actors can access sensitive files and potentially escalate privileges within the system
- **Status**: Actively exploited as zero-day since late 2024, security updates have been released
- **CVE ID**: CVE-2025-11371

### Adobe Experience Manager Remote Code Execution
- **Description**: A maximum-severity vulnerability in Adobe Experience Manager that allows remote code execution
- **Impact**: Attackers can execute arbitrary code on unpatched systems, potentially leading to full system compromise
- **Status**: Actively exploited in attacks, added to CISA KEV catalog
- **CVE ID**: Perfect 10.0 CVSS score vulnerability

### Cisco SNMP Remote Code Execution Vulnerability
- **Description**: A recently patched remote code execution vulnerability in older Cisco IOS Software and IOS XE Software SNMP implementations
- **Impact**: Allows deployment of Linux rootkits and persistent access to network infrastructure
- **Status**: Actively exploited in "Zero Disco" campaign targeting unpatched systems
- **CVE ID**: CVE-2025-20352

### F5 BIG-IP Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in F5 BIG-IP systems exploited by nation-state actors
- **Impact**: Complete system compromise, source code theft, and access to customer information
- **Status**: Recently disclosed breach, vulnerabilities used to infiltrate F5's internal systems

### Oracle Zero-Day Vulnerabilities
- **Description**: Zero-day vulnerabilities in Oracle products targeted in widespread campaign
- **Impact**: Data theft and system compromise across multiple Oracle customers
- **Status**: Actively exploited by Clop ransomware group, affecting Harvard University and other organizations

## Affected Systems and Products

- **Gladinet CentreStack**: Business file-sharing and collaboration platform
- **Adobe Experience Manager**: Content management system used by enterprises
- **Cisco IOS Software and IOS XE Software**: Network operating systems on older, unpatched devices
- **F5 BIG-IP**: Application delivery controllers and load balancers
- **Oracle Products**: Various Oracle enterprise applications and databases
- **Password Managers**: LastPass and other major password management solutions
- **Microsoft VS Code Marketplace**: Development environment extensions containing exposed secrets
- **WordPress Sites**: Compromised websites used for malware distribution via blockchain contracts
- **Microsoft Teams**: Targeted by ransomware attacks using malicious installers

## Attack Vectors and Techniques

- **EtherHiding Technique**: North Korean hackers hide malware inside blockchain smart contracts for stealth distribution
- **Blockchain Malware Distribution**: UNC5142 threat actor uses infected WordPress sites and smart contracts to deliver information stealers
- **Linux Rootkit Deployment**: LinkPro rootkit uses eBPF technology and magic TCP packets for persistence and stealth
- **Social Engineering**: Sophisticated phishing campaigns targeting password manager users' trust and anxiety
- **Supply Chain Attacks**: Exploitation of VS Code marketplace vulnerabilities and malicious Teams installer certificates
- **Certificate Abuse**: Rhysida ransomware group used over 200 fraudulent certificates for malicious Teams installers
- **AI-Optimized Attack Chains**: Chinese threat actors testing artificial intelligence-enhanced attack methodologies

## Threat Actor Activities

- **North Korean APT Groups**: Leveraging EtherHiding for cryptocurrency theft and espionage operations with enhanced stealth capabilities
- **UNC5142**: Financially motivated group distributing Atomic (AMOS), Lumma, and other information stealers via blockchain contracts
- **Clop Ransomware Group**: Conducting widespread Oracle zero-day exploitation campaign, claiming responsibility for Harvard University breach
- **Nation-State Actors**: Sophisticated infiltration of F5 Networks using multiple zero-day vulnerabilities for source code theft
- **Jewelbug (Chinese APT)**: Five-month infiltration of Russian IT service provider, expanding operations beyond Southeast Asia
- **Chinese Threat Groups**: Testing AI-optimized attack chains in Taiwan operations with mixed effectiveness results
- **Rhysida Ransomware**: Microsoft-disrupted campaign targeting Teams users through certificate abuse and malicious installers
- **Mysterious Elephant**: Cyber-espionage group targeting South Asian government and diplomatic entities with custom sophisticated tools