# Exploitation Report

The cybersecurity landscape is witnessing unprecedented exploitation activity, with threat actors actively targeting critical vulnerabilities across multiple platforms. Most concerning is the active exploitation of CVE-2026-5027, a high-severity path traversal vulnerability in the AI development platform Langflow that allows attackers to achieve remote code execution on exposed servers. Microsoft has addressed three zero-day vulnerabilities during a record-breaking Patch Tuesday that fixed 206 security flaws, including exploited Exchange Server cross-site scripting vulnerabilities and Windows Defender privilege escalation flaws. Additionally, threat actors continue to exploit Oracle PeopleSoft servers in large-scale data theft campaigns, while Chinese-linked botnets expand their reconnaissance capabilities against U.S. military networks.

## Active Exploitation Details

### Langflow Path Traversal Vulnerability
- **Description**: A high-severity path traversal flaw in Langflow, an open-source low-code AI application development platform, that allows unauthenticated attackers to write arbitrary files to exposed servers
- **Impact**: Remote code execution on vulnerable Langflow installations, complete system compromise
- **Status**: Currently unpatched and under active exploitation in the wild
- **CVE ID**: CVE-2026-5027

### Microsoft Exchange Server Cross-Site Scripting Vulnerability
- **Description**: An actively exploited zero-day vulnerability in Exchange Server that enables arbitrary JavaScript code execution through cross-site scripting attacks
- **Impact**: JavaScript code execution targeting Outlook Web Access users, potential credential theft and session hijacking
- **Status**: Patched by Microsoft during June 2026 Patch Tuesday, but was actively exploited as a zero-day

### YellowKey Windows Privilege Escalation
- **Description**: A zero-day vulnerability that allows attackers to gain SYSTEM privileges on fully patched Windows systems
- **Impact**: Complete system takeover with highest privileges on Windows machines
- **Status**: Patched by Microsoft during June 2026 Patch Tuesday

### GreenPlasma Windows Privilege Escalation
- **Description**: A second zero-day vulnerability enabling privilege escalation to SYSTEM level on Windows systems
- **Impact**: Administrative access and complete control over affected Windows systems
- **Status**: Patched by Microsoft during June 2026 Patch Tuesday

### MiniPlasma BitLocker Bypass
- **Description**: A zero-day vulnerability that grants unauthorized access to BitLocker-protected drives
- **Impact**: Bypass of Windows disk encryption, access to encrypted data
- **Status**: Patched by Microsoft during June 2026 Patch Tuesday

### RoguePlanet Microsoft Defender Zero-Day
- **Description**: A newly disclosed zero-day vulnerability in Microsoft Defender that allows privilege escalation to SYSTEM level
- **Impact**: Complete system compromise on updated Windows systems running Defender
- **Status**: Unpatched, proof-of-concept exploit released by security researcher

### ServiceNow Unauthorized Access Vulnerability
- **Description**: A security flaw that allows threat actors to gain deeper unauthorized access to ServiceNow customer instances
- **Impact**: Unauthorized access to enterprise ServiceNow environments and sensitive business data
- **Status**: Patched by ServiceNow on June 5, 2026

## Affected Systems and Products

- **Langflow AI Platform**: Open-source low-code AI application development platform, all versions prior to patch
- **Microsoft Exchange Server**: Cross-site scripting vulnerability affecting Outlook Web Access functionality
- **Windows Operating Systems**: All supported versions affected by YellowKey, GreenPlasma, and MiniPlasma zero-days
- **Microsoft Defender**: Windows Defender installations vulnerable to RoguePlanet exploit
- **Oracle PeopleSoft**: Enterprise resource planning servers targeted in data theft campaigns
- **ServiceNow Instances**: Customer instances affected by unauthorized access vulnerability
- **Ivanti Sentry**: Secure mobile gateway solution with critical remote code execution flaws
- **protobuf.js Library**: JavaScript and TypeScript Protocol Buffers implementation in Node.js applications
- **Cisco Systems**: Products added to CISA KEV catalog due to active exploitation
- **Google Chrome**: Browser vulnerabilities under active exploitation
- **Arista Networks**: Network equipment vulnerabilities being actively exploited

## Attack Vectors and Techniques

- **Path Traversal Exploitation**: Attackers exploiting CVE-2026-5027 to write arbitrary files and achieve remote code execution on Langflow servers
- **Cross-Site Scripting**: JavaScript injection attacks targeting Exchange Server and Outlook Web Access users
- **Privilege Escalation**: Zero-day exploits targeting Windows systems to gain SYSTEM-level privileges
- **Data Theft Campaigns**: Large-scale attacks against Oracle PeopleSoft servers for data exfiltration
- **Supply Chain Attacks**: Miasma credential-stealing framework targeting open-source ecosystems
- **Botnet Operations**: Reconnaissance and intelligence gathering through compromised SOHO devices
- **Social Engineering**: Service desk targeting and MFA fatigue attacks bypassing authentication
- **Remote Code Execution**: Maximum-severity vulnerabilities allowing code execution with root privileges

## Threat Actor Activities

- **ShinyHunters Gang**: Conducting ongoing data theft attacks against Oracle PeopleSoft servers, claiming to have stolen data from over 100 organizations
- **Chinese State-Sponsored Groups**: Operating the JDY botnet with over 1,500 compromised SOHO devices for cyber reconnaissance against U.S. military networks
- **Volt Typhoon**: Associated with expanded JDY botnet operations targeting critical infrastructure
- **The Gentlemen Ransomware Group**: Emerged as the second most active ransomware gang by victim count with aggressive recruitment strategies
- **North Korean Groups**: Leveraging cybercrime gains to contribute to national GDP growth through targeting of business and financial firms
- **Chaotic Eclipse (Nightmare-Eclipse)**: Anonymous researcher releasing proof-of-concept exploits for Microsoft vulnerabilities, including RoguePlanet
- **Unknown Threat Actors**: Exploiting ServiceNow instances and actively targeting Langflow installations worldwide