# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with attackers targeting AI development platforms, enterprise software, and Windows systems. The most concerning activities include ongoing exploitation of CVE-2026-5027 in Langflow AI platform for unauthenticated remote code execution, multiple zero-day vulnerabilities in Microsoft products including Exchange Server and Windows Defender, and widespread targeting of Oracle PeopleSoft servers by the ShinyHunters extortion gang. Chinese state-sponsored actors continue expanding their reconnaissance operations through the JDY botnet, while new zero-day exploits are being publicly released by security researchers, creating immediate risks for organizations.

## Active Exploitation Details

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal vulnerability in the open-source AI development platform Langflow
- **Impact**: Allows attackers to write arbitrary files on exposed servers and achieve unauthenticated remote code execution
- **Status**: Currently unpatched and under active exploitation
- **CVE ID**: CVE-2026-5027

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: Zero-day vulnerability in Exchange Server allowing execution of arbitrary JavaScript code
- **Impact**: Enables cross-site scripting (XSS) attacks targeting Outlook Web Access users
- **Status**: Recently patched by Microsoft after active exploitation
- **CVE ID**: Not specified

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in Windows Defender, including YellowKey, GreenPlasma, MiniPlasma, and RoguePlanet exploits
- **Impact**: Allows attackers to gain SYSTEM privileges on fully patched Windows systems and access to BitLocker-protected drives
- **Status**: Some patched in June 2026 Patch Tuesday, RoguePlanet remains unpatched with public PoC available
- **CVE ID**: Not specified

### ServiceNow Unauthorized Access Flaw
- **Description**: Security vulnerability allowing deeper unauthorized access to customer instances
- **Impact**: Enables threat actors to gain unauthorized access to ServiceNow customer environments
- **Status**: Security patch applied on June 5, 2026
- **CVE ID**: Not specified

### Cisco, Chrome, and Arista Vulnerabilities
- **Description**: Multiple vulnerabilities across Cisco, Chrome, and Arista products
- **Impact**: Various security impacts leading to system compromise
- **Status**: Added to CISA KEV catalog due to active exploitation
- **CVE ID**: Not specified

## Affected Systems and Products

- **Langflow AI Platform**: Open-source low-code AI application development platform
- **Microsoft Exchange Server**: Enterprise email and collaboration platform, specifically Outlook Web Access
- **Microsoft Windows**: Various Windows versions affected by Defender zero-days
- **Microsoft Defender**: Windows security solution across multiple Windows versions
- **Oracle PeopleSoft**: Enterprise resource planning software targeted in data theft attacks
- **ServiceNow**: Cloud computing platform and customer instances
- **Cisco Products**: Various Cisco networking and security products
- **Google Chrome**: Web browser with actively exploited vulnerabilities
- **Arista Networks**: Network infrastructure products
- **Ivanti Sentry**: Secure mobile gateway solution with critical vulnerabilities
- **protobuf.js**: JavaScript and TypeScript Protocol Buffers implementation

## Attack Vectors and Techniques

- **Path Traversal Exploitation**: Attackers exploiting CVE-2026-5027 to write arbitrary files on Langflow servers
- **Cross-Site Scripting (XSS)**: JavaScript code execution targeting Outlook Web Access users
- **Privilege Escalation**: Zero-day exploits granting SYSTEM-level access on Windows systems
- **Data Theft Campaigns**: ShinyHunters targeting Oracle PeopleSoft servers for data exfiltration
- **Supply Chain Attacks**: Miasma worm framework targeting open-source ecosystems
- **Botnet Reconnaissance**: JDY botnet conducting cyber reconnaissance activities
- **Remote Code Execution**: Various vulnerabilities allowing arbitrary code execution
- **Social Engineering**: Service desk targeting and MFA fatigue attacks

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Conducting ongoing data theft attacks against Oracle PeopleSoft servers, claiming to have stolen data from over 100 organizations
- **Chinese State-Sponsored Actors**: Operating the expanded JDY botnet with over 1,500 devices targeting U.S. military networks and conducting cyber reconnaissance
- **Volt Typhoon**: Associated with JDY botnet operations and infrastructure targeting
- **The Gentlemen Ransomware Group**: Emerged as second most active ransomware gang by victim count with aggressive recruitment strategies
- **Chaotic Eclipse (Nightmare-Eclipse)**: Security researcher releasing multiple Microsoft Defender zero-day exploits including RoguePlanet
- **North Korean Threat Groups**: Expanding activities in Asia-Pacific region with increased cybercrime operations contributing to national GDP growth
- **Unknown Threat Actors**: Exploiting ServiceNow vulnerabilities to gain unauthorized access to customer instances