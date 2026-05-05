# Exploitation Report

Critical vulnerabilities are being actively exploited across multiple platforms, with threat actors targeting everything from enterprise systems to railway infrastructure. The most severe incidents include active exploitation of CVE-2026-22679 in Weaver E-cology systems since March, CVE-2026-29014 in MetInfo CMS for remote code execution, and CVE-2026-23918 in Apache HTTP/2 servers. Supply chain attacks have compromised DAEMON Tools software distribution, while sophisticated phishing campaigns are leveraging legitimate services like Amazon SES and RMM tools to evade detection. Nation-state actors, including China-linked groups UAT-8302 and Silver Fox, are conducting targeted operations against government entities, while North Korean group ScarCruft has compromised gaming platforms to distribute malware across multiple platforms.

## Active Exploitation Details

### Weaver E-cology Remote Code Execution Vulnerability
- **Description**: Critical security flaw in Weaver E-cology enterprise office automation platform being exploited via debug API
- **Impact**: Attackers can execute arbitrary commands and gain unauthorized access to enterprise systems
- **Status**: Under active exploitation since mid-March 2026, with hackers running discovery commands
- **CVE ID**: CVE-2026-22679

### MetInfo CMS Remote Code Execution Vulnerability
- **Description**: Critical security flaw in the open-source MetInfo content management system
- **Impact**: Enables threat actors to achieve remote code execution on affected systems
- **Status**: Currently being actively exploited by threat actors
- **CVE ID**: CVE-2026-29014

### Apache HTTP/2 Critical Vulnerability
- **Description**: Severe vulnerability in Apache HTTP Server that affects HTTP/2 implementations
- **Impact**: Could lead to denial of service attacks and potentially remote code execution
- **Status**: Recently patched by Apache Software Foundation with security updates released
- **CVE ID**: CVE-2026-23918

### Taiwan High-Speed Rail TETRA Communication System
- **Description**: Security vulnerability in the TETRA communication system used by Taiwan's high-speed railway network
- **Impact**: Allows interference with railway operations, including triggering emergency brakes
- **Status**: Exploited by a 23-year-old university student who was subsequently arrested

### Microsoft Edge Password Storage Vulnerability
- **Description**: Security flaw where Microsoft Edge stores passwords in process memory
- **Impact**: Admin-privileged attackers can steal stored passwords for further malicious activity
- **Status**: Proof-of-concept exploit demonstrated, poses enterprise security risk

## Affected Systems and Products

- **Weaver E-cology**: Enterprise office automation and collaboration platform with critical RCE vulnerability
- **MetInfo CMS**: Open-source content management system vulnerable to remote code execution
- **Apache HTTP Server**: Web server software with HTTP/2 implementation flaws
- **DAEMON Tools**: Software distribution compromised in supply chain attack
- **Microsoft Edge**: Browser storing passwords insecurely in process memory
- **Taiwan High-Speed Rail**: TETRA communication systems vulnerable to interference
- **MOVEit Automation**: File transfer software with authentication bypass vulnerability
- **Gaming Platforms**: Compromised by ScarCruft for malware distribution
- **PyTorch Lightning**: Python package compromised with credential stealer
- **cPanel**: Web hosting control panel with critical authentication bypass flaw

## Attack Vectors and Techniques

- **Supply Chain Compromise**: DAEMON Tools installers compromised to deliver malicious payloads
- **Debug API Exploitation**: Weaver E-cology systems compromised through vulnerable debug interfaces
- **Phishing with Legitimate Services**: Amazon SES and RMM tools (SimpleHelp, ScreenConnect) abused to evade detection
- **OAuth Token Persistence**: Persistent OAuth tokens with no expiration used as backdoors
- **TETRA Communication Interference**: Direct manipulation of railway communication systems
- **Gaming Platform Compromise**: ScarCruft using compromised game platforms to distribute BirdCall malware
- **Package Repository Poisoning**: Malicious PyTorch Lightning package uploaded to PyPI
- **Microsoft Phone Link Abuse**: CloudZ malware hijacking Phone Link connections to steal SMS and OTPs

## Threat Actor Activities

- **UAT-8302 (China-linked)**: Targeting government entities in South America since late 2024 using shared APT malware across regions
- **ScarCruft/APT37 (North Korea)**: Compromising gaming platforms to deploy BirdCall malware on Android and Windows systems
- **Silver Fox (China-backed APT)**: Conducting tax-themed attacks against organizations in India and Russia with over 1,600 socially engineered messages
- **ShinyHunters**: Extortion gang responsible for Vimeo data breach affecting 119,000 people
- **Karakurt Ransomware Group**: Russian extortion gang with negotiator sentenced to 8.5 years in prison
- **Multiple Phishing Operators**: Large-scale credential theft campaign targeting 35,000 users across 26 countries using code of conduct-themed lures
- **RMM Tool Abusers**: Campaign targeting 80+ organizations using legitimate remote monitoring tools for persistent access