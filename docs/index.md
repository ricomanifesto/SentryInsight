# Exploitation Report

Critical exploitation activity is currently underway across multiple platforms, with attackers targeting AI development platforms, enterprise systems, and Windows infrastructure. The most severe threats include active exploitation of an unpatched path traversal vulnerability in Langflow (CVE-2026-5027), multiple Microsoft zero-day vulnerabilities being exploited for SYSTEM-level access, and widespread attacks against Oracle PeopleSoft servers by the ShinyHunters extortion gang. State-sponsored threat actors, particularly China-linked groups, are expanding their reconnaissance operations through botnets targeting U.S. military networks, while ransomware groups like The Gentlemen continue aggressive recruitment and targeting campaigns.

## Active Exploitation Details

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal vulnerability in the AI development platform Langflow that allows unauthenticated remote code execution
- **Impact**: Attackers can write arbitrary files on exposed servers and achieve complete system compromise
- **Status**: Currently unpatched and under active exploitation in the wild
- **CVE ID**: CVE-2026-5027

### Microsoft Exchange Server Zero-Day
- **Description**: Cross-site scripting (XSS) vulnerability in Exchange Server targeting Outlook Web Access
- **Impact**: Allows threat actors to execute arbitrary JavaScript code in victim browsers
- **Status**: Recently patched by Microsoft after active exploitation was detected

### Microsoft Defender Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in Microsoft Defender, including YellowKey, GreenPlasma, MiniPlasma, and RoguePlanet exploits
- **Impact**: Grant SYSTEM-level privileges on fully patched Windows systems and access to BitLocker-protected drives
- **Status**: YellowKey, GreenPlasma, and MiniPlasma have been patched; RoguePlanet remains unpatched

### ServiceNow Security Flaw
- **Description**: Security vulnerability allowing unauthorized access to customer instances
- **Impact**: Enables deeper unauthorized access to susceptible ServiceNow instances
- **Status**: Patched by ServiceNow on June 5, 2026, after exploitation was detected

### Oracle PeopleSoft Server Attacks
- **Description**: Ongoing data theft attacks targeting Oracle PeopleSoft servers
- **Impact**: Data theft from over 100 organizations
- **Status**: Active exploitation by ShinyHunters extortion gang

## Affected Systems and Products

- **Langflow AI Platform**: Open-source low-code AI development platform vulnerable to path traversal attacks
- **Microsoft Exchange Server**: Email servers vulnerable to XSS attacks through Outlook Web Access
- **Microsoft Defender**: Windows security software affected by multiple zero-day exploits
- **Oracle PeopleSoft**: Enterprise resource planning servers targeted for data theft
- **ServiceNow**: Cloud computing platform instances compromised through unauthorized access
- **Ivanti Sentry**: Secure mobile gateway solution with critical vulnerabilities allowing root code execution
- **Cisco, Chrome, and Arista Products**: Various products added to CISA's Known Exploited Vulnerabilities catalog
- **Fortinet and SAP Systems**: Multiple products patched for critical vulnerabilities
- **protobuf.js Libraries**: JavaScript and TypeScript Protocol Buffers implementation affecting Node.js applications

## Attack Vectors and Techniques

- **Path Traversal Attacks**: Exploiting directory traversal vulnerabilities to write arbitrary files and achieve remote code execution
- **Cross-Site Scripting (XSS)**: Injecting malicious JavaScript code through Exchange Server vulnerabilities
- **Privilege Escalation**: Using zero-day exploits to gain SYSTEM-level access on Windows systems
- **Supply Chain Attacks**: Targeting open-source ecosystems through credential-stealing frameworks like Miasma
- **Data Theft Operations**: Systematic attacks against enterprise servers for data exfiltration
- **Botnet Reconnaissance**: Using compromised SOHO devices for intelligence gathering and network mapping

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Conducting widespread data theft attacks against Oracle PeopleSoft servers, claiming compromise of over 100 organizations
- **China-Linked JDY Botnet**: Expanding network of over 1,500 compromised SOHO devices for cyber reconnaissance, specifically targeting U.S. military networks and critical infrastructure
- **Chinese and North Korean State Groups**: Building on Asia-Pacific success with continued targeting of business and financial firms, contributing to North Korea's GDP growth through cybercrime activities
- **The Gentlemen Ransomware Group**: Emerging as the second most active ransomware gang by victim count, implementing aggressive recruitment strategies to attract skilled hackers
- **Volt Typhoon-Associated Actors**: Utilizing JDY botnet infrastructure for intelligence gathering and maintaining persistent access to target networks
- **Nightmare-Eclipse/Chaotic Eclipse**: Disgruntled security researcher releasing multiple Microsoft Defender zero-day exploits, including the recent RoguePlanet proof-of-concept