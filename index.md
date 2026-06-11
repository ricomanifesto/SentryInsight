# Exploitation Report

Critical exploitation activity is currently targeting multiple high-impact vulnerabilities across enterprise infrastructure and AI development platforms. Attackers are actively exploiting a maximum-severity flaw in Ivanti Sentry that enables root-level code execution on Internet-exposed secure mobile gateways. Simultaneously, the AI development platform Langflow is under active attack through CVE-2026-5027, allowing unauthenticated remote code execution via path traversal. Microsoft has addressed multiple zero-day vulnerabilities including Exchange Server XSS flaws and Windows privilege escalation issues dubbed YellowKey, GreenPlasma, and MiniPlasma. Notable threat actor activity includes OceanLotus targeting Vietnamese entities with the SPECTRALVIPER backdoor, while the ShinyHunters extortion gang has compromised over 100 Oracle PeopleSoft servers for data theft operations.

## Active Exploitation Details

### Ivanti Sentry Maximum Severity Vulnerability
- **Description**: A critical flaw in Ivanti Sentry secure mobile gateways that has been recently patched but is now under active exploitation
- **Impact**: Allows attackers to execute arbitrary code with root privileges on Internet-exposed systems
- **Status**: Recently patched but actively exploited in the wild

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal flaw in the AI development platform Langflow enabling arbitrary file writes
- **Impact**: Unauthenticated remote code execution on exposed servers
- **Status**: Unpatched and actively exploited
- **CVE ID**: CVE-2026-5027

### Microsoft Exchange Server Zero-Day
- **Description**: Cross-site scripting vulnerability in Exchange Server targeting Outlook Web Access
- **Impact**: Arbitrary JavaScript code execution in XSS attacks
- **Status**: Patched by Microsoft after active exploitation

### Windows Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities affecting Windows systems, including privilege escalation flaws
- **Impact**: YellowKey and GreenPlasma allow attackers to gain SYSTEM privileges on fully patched Windows systems; MiniPlasma grants access to BitLocker-protected drives
- **Status**: Patched by Microsoft in latest security update

## Affected Systems and Products

- **Ivanti Sentry**: Internet-exposed secure mobile gateways vulnerable to root-level code execution
- **Langflow AI Platform**: Open-source low-code AI application development platform exposed to path traversal attacks
- **Microsoft Exchange Server**: Outlook Web Access components targeted by XSS attacks
- **Windows Systems**: All versions affected by privilege escalation and BitLocker bypass vulnerabilities
- **Oracle PeopleSoft**: Enterprise servers targeted by ShinyHunters for data theft
- **Cisco, Chrome, and Arista Systems**: Various products added to CISA KEV catalog due to active exploitation

## Attack Vectors and Techniques

- **Path Traversal Attacks**: Exploiting CVE-2026-5027 in Langflow to write arbitrary files and achieve remote code execution
- **Cross-Site Scripting**: Targeting Exchange Server to execute malicious JavaScript in user browsers
- **Privilege Escalation**: Using YellowKey and GreenPlasma zero-days to gain SYSTEM-level access on Windows
- **BitLocker Bypass**: Leveraging MiniPlasma vulnerability to access encrypted drives
- **Supply Chain Attacks**: Miasma worm targeting open-source ecosystems through compromised packages
- **Social Engineering**: ShinyHunters using various techniques to compromise PeopleSoft servers

## Threat Actor Activities

- **OceanLotus**: Vietnam-aligned APT conducting two distinct campaigns targeting domestic entities and stock investors using SPECTRALVIPER backdoor in "FireAnt Attack" operations
- **ShinyHunters**: Extortion gang claiming data theft from over 100 organizations through Oracle PeopleSoft server compromises
- **Chinese State-Sponsored Groups**: JDY botnet expansion to over 1,500 devices for cyber reconnaissance, targeting U.S. military networks and small office/home office devices
- **Nightmare-Eclipse**: Disgruntled researcher releasing proof-of-concept exploits including RoguePlanet for Windows Defender vulnerabilities
- **The Gentlemen**: Emerging ransomware group becoming the second most active by victim count through aggressive recruitment strategies
- **Volt Typhoon Associated Actors**: Linked to JDY botnet operations focusing on reconnaissance of critical infrastructure